#! /usr/bin/python

import os, sys, traceback, re, subprocess


DEVNULL = open(os.devnull, 'w')

ANDROID_HOME=os.getenv('ANDROID_HOME')

SECURITY=set()

SERIAL=os.getenv('SERIAL')

if SERIAL:
    ADB_BASE = ['adb', '-s', SERIAL]
else:
    ADB_BASE = ['adb', '-d']


def get_broadcast_actions(base):
    sdk = get_sdk_version(base)
    data_dir = os.path.join(ANDROID_HOME, 'platforms', 'android-' + str(sdk), 'data')
    with open(os.path.join(data_dir, 'broadcast_actions.txt')) as f:
        return list([d.strip() for d in f.readlines()])

def get_service_actions(base):
    sdk = get_sdk_version(base)
    data_dir = os.path.join(ANDROID_HOME, 'platforms', 'android-' + str(sdk), 'data')
    with open(os.path.join(data_dir, 'service_actions.txt')) as f:
        return list([d.strip() for d in f.readlines()])



def get_activity_actions(base):
    sdk = get_sdk_version(base)
    data_dir = os.path.join(ANDROID_HOME, 'platforms', 'android-' + str(sdk), 'data')
    with open(os.path.join(data_dir, 'activity_actions.txt')) as f:
        return list([d.strip() for d in f.readlines()])



def get_sdk_version(base):
    output = call_output(base + 'shell getprop ro.build.version.sdk'.split(' '))
    return int(output.strip())

def install(base, apk):
    sdk = get_sdk_version(base)
    if sdk >= 23:
        call(base + ['install', '-r', '-g', apk])
    else:
        call(base + ['install', '-r', apk])


def uninstall(base, pkg):
    call(base + ['uninstall', pkg])


PACKAGE_PATTERN = re.compile('^( +)A: package="([^"]+)"')
COMP_PATTERN    = re.compile('^  E: (activity|receiver|service)')
NAME_PATTERN    = re.compile('^    A: android:name.+Raw: "([^"]+)".*')


def add_to_dict_list(d, key, val):
    if key in d:
        d[key].append(val)
    else:
        d[key] = [val]

def dump_apk(apk):
    cmd = ['aapt', 'd', 'xmltree', apk, 'AndroidManifest.xml']
    output = call_output(cmd)
    package = None
    package_indent = 0
    component = None

    components = dict()
    components['activity'] = []
    components['service'] = []
    components['receiver'] = []
    for line in output.splitlines():
        m = PACKAGE_PATTERN.search(line)
        if m:
            if package:
                raise RuntimeError('duplicated package name: {} vs {}'.format(package, m.group(1)))
            package_indent = len(m.group(1))
            package = m.group(2)
            continue

        line = line[package_indent:]
        m = COMP_PATTERN.search(line)
        if m:
            if component:
                raise RuntimeError('duplicated component {} v.s. {}'.format(component, m.group(1)))

            component = m.group(1)
            continue

        m = NAME_PATTERN.search(line)
        if m:
            if component:
                name = m.group(1)
                add_to_dict_list(components, component, name)
                component = None

    return package,components

def pre_fuzzing(base, pkg, component):
    call(base + ['shell', 'input', 'keyevent', '61']) # TAB
    call(base + ['shell', 'input', 'keyevent', '61']) # TAB
    call(base + ['shell', 'input', 'keyevent', '66']) # ENTER
    call(base + ['shell', 'am', 'force-stop', pkg])
    call(base + ['logcat', '-c'])
    #call(base + ['shell', 'monkey', '-p', pkg, '1'])


def app_switch(base):
    call(base + ['shell', 'input', 'keyevent', '187']) # APP_SWITCH
    call(base + ['shell', 'sleep', '2'])
    call(base + ['shell', 'input', 'keyevent', '4']) # HOME
    call(base + ['shell', 'sleep', '2'])

def home(base):
    call(base + ['shell', 'input', 'keyevent', '3']) # HOME
    call(base + ['shell', 'sleep', '2'])




def start_component(base, pkg, component_type, component_name, extra_options = []):
    if component_type == 'activity':
        o = call_output(base + ['shell', 'am', 'start'] + extra_options + ['-n', pkg + '/' + component_name])
    elif component_type == 'receiver':
        o = call_output(base + ['shell', 'am', 'broadcast'] + extra_options +  ['-n', pkg + '/' + component_name])
    elif component_type == 'service':
        o = call_output(base + ['shell', 'am', 'startservice'] + extra_options + ['-n', pkg + '/' + component_name])
    else:
        raise RuntimeError('Unsupported component type: ' + component_type)
    print(o)
    return o


def stop_service(base, pkg, component_name):
    call(base + ['shell', 'am', 'stopservice', '-n', pkg + '/' + component_name])

def post_fuzzing(base, pkg, component):
    # call(base + ['logcat', '-d', '-f', '/sdcard/logcat.txt', '"AndroidRuntime:I"', '"*:S"'])
    # call(base + ['pull', '/sdcard/logcat.txt', output])
    # call(base + ['shell', 'rm', '/sdcard/logcat.txt'])
    call(base + ['shell', 'input', 'keyevent', '61']) # TAB
    call(base + ['shell', 'input', 'keyevent', '61']) # TAB
    call(base + ['shell', 'input', 'keyevent', '66']) # ENTER
    call(base + ['shell', 'am', 'force-stop', pkg])
    #output = call_output(base + ['logcat', '-d', '"AndroidRuntime:I"', 'dalvikvm:I', 'art:I', '"*:S"'])
    output = call_output(base + ['logcat', '-d'])
    # print(output)
    return output


def fuzz_activity(adb_base, pkg, activity):
    pre_fuzzing(adb_base, pkg, activity)
    o = start_component(adb_base, pkg, 'activity', activity)
    if 'Permission Denial' in o:
        SECURITY.add(activity)
        return o
    return post_fuzzing(adb_base, pkg, activity)

def fuzz_activity_app_switch(adb_base, pkg, activity):
    pre_fuzzing(adb_base, pkg, activity)
    o = start_component(adb_base, pkg, 'activity', activity)
    app_switch(adb_base)
    if 'Permission Denial' in o:
        SECURITY.add(activity)
        return o
    return post_fuzzing(adb_base, pkg, activity)


def fuzz_activity_home(adb_base, pkg, activity):
    pre_fuzzing(adb_base, pkg, activity)
    o = start_component(adb_base, pkg, 'activity', activity)
    home(adb_base)
    if 'Permission Denial' in o:
        SECURITY.add(activity)
        return o
    return post_fuzzing(adb_base, pkg, activity)


def fuzz_service(adb_base, pkg, service):
    pre_fuzzing(adb_base, pkg, service)
    o = start_component(adb_base, pkg, 'service', service)
    if 'Permission Denial' in o:
        SECURITY.add(service)
        return o
    call(adb_base + ['shell', 'sleep', '2'])
    stop_service(adb_base, pkg, service)
    return post_fuzzing(adb_base, pkg, service)


def fuzz_receiver(adb_base, pkg, receiver):
    pre_fuzzing(adb_base, pkg, receiver)
    o = start_component(adb_base, pkg, 'receiver', receiver)
    if 'Permission Denial' in o:
        SECURITY.add(receiver)
        return o
    return post_fuzzing(adb_base, pkg, receiver)

def fuzz_apks(adb_base, apks):
    for apk in apks:
        fuzz_apk(adb_base, apk)

def fuzz_apk(adb_base, apk):
    pkg, components = dump_apk(apk)
    install(adb_base, apk)
    results = []
    for activity in components['activity']:
        output = fuzz_activity(adb_base, pkg, activity)
        results.append(output)
        output = fuzz_activity_app_switch(adb_base, pkg, activity)
        results.append(output)
        output = fuzz_activity_home(adb_base, pkg, activity)
        results.append(output)

    for service in components['service']:
        output = fuzz_service(adb_base, pkg, service)
        results.append(output)


    for receiver in components['receiver']:
        output = fuzz_receiver(adb_base, pkg, receiver)
        results.append(output)

    uninstall(adb_base, pkg)

    output_dir = makedir_if_not_exists('_'.join(adb_base))

    for index, o in enumerate(results):
        with open(os.path.join(output_dir, '{}-{}'.format(pkg, index)), 'w') as f:
            f.write(o)

    print(SECURITY)


def makedir_if_not_exists(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)
    return folder

def call(cmd):
    print(' '.join(cmd))
    subprocess.check_call(cmd, stdout=DEVNULL, stderr=subprocess.STDOUT)

def call_output(cmd):
    print(' '.join(cmd))
    return subprocess.check_output(cmd,stderr=subprocess.STDOUT)



if __name__ == '__main__':
    try:
        fuzz_apks(ADB_BASE, sys.argv[1:])
    except:
        traceback.print_exc()
