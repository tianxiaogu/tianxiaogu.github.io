title: Install MiniTracing

# Install MiniTracing in an Emulator



MiniTracing: Collect method/coverage without bytecode instrumentation.

* [Android 6 (binary for x86)](/art-mt-x86.zip): Android ART with method/instruction coverage support.
* [Android 4.4 (binary for x86)](/dalvikvm-mt-x86.zip): Android Dalvik VM with method/instruction coverage support.
* [android-mt-cmd](https://bitbucket.org/txgu/android-mt-cmd): Command line tools to collect coverage.
* [android-mt-parser](https://bitbucket.org/txgu/android-mt-parser): Parser for the coverage data.


## Usage

1. Create an AVD using the Android Nexus 5 API 23 x86 image. By default, the name of the AVD should be `Nexus 5 API 23`.

    !!! note
        Android studio has officially released three types of emulators for **Nexus 5 API 23 x86**, i.e., with Google Play Store, with Google API only and without any Google stuffs.
        Here you must select the one without any Google stuffs since we will install a full Google service framework manually.

2. Install Google Play (optional):
    1. Follow instructions in <https://medium.com/@dai_shi/installing-google-play-services-on-an-android-studio-emulator-fffceb2c28a1>
    2. By default, all permissions of Google Play Service have been disabled. You will encounter crashes as described in the previous link. To solve this issue, you must first enable location and then grant all permissions to Google Play Service.

3. Install MiniTracing
    1. Download [art-mt-x86.zip](/art-mt-x86.zip) for Android 6 and change directory to `art-mt-x86`.
    2. Run `install_libart.sh`. You need to provide the SERIAL of the Android Device. The default SERIAL for an emulator is `emulator-5554`:

            export SERIAL=emulator-5554 && bash install_libart.sh

    3. Wait for the restart of the emulator to be completed.
    4. Validate whether MiniTracing has been installed:

            adb -s emulator-5554 logcat | grep mini_trace

4. Download [android-mt-cmd](https://bitbucket.org/txgu/android-mt-cmd)
    1. Change directory to android-mt-cmd:

            cd android-mt-cmd

    2. Run `ant` to build the project

            ant

    3. Run `install.py` (necessary), and you also need to set the environment variable SERIAL.

            python2 install.py

4. Enable MiniTracing for a package

    1. Enable MiniTracing for a package before testing but must be done after the package has been installed.

            python2 minitrace.py enable <your-package-name>

        !!! note
            `minitrace.py` will generate config file based on the id of the installed package, which means you must reenable a package after reinstalling it.

    2. Harvest coverage data during the testing

            python2 minitrace.py harvest <your-package-name>

    3. Stop MiniTracing, data will be copied to `/sdcard/` in your emulator.

            python2 minitrace.py disable <your-package-name>


5. Parse coverage data

    1. Download [android-mt-parser](https://bitbucket.org/txgu/android-mt-parser). Use maven to build the project.

            mvn package

    2. Copy data from emulator via `adb pull`
    3. Run `android-mt-parser/run.py`

            python2 run.py -apk <path-to-your-apk> -cov <path-to-mini_trace_xxxxx_coverage.dat>
