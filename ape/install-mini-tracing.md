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
            However, some tool may re-install the package, e..g, Sapienz. To use MiniTrace with these tools, you need to disable the reinstallation.

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

## Coverage Parser


The explanation of column heads:

1. Timestamp: The timestamp when the line of data is dumped.
2. PID: The PID of the process in which the line of data is dumped. A package may have multiple running processes at the same time.
3. Event: Two events: `Start` and `Dump`. MiniTracing will produce a Start event when a process is started. A `Dump` event is created when you run the harvest command.
4. \#Total Methods: The total number of methods defined in the APK. Methods in dynamically downloaded files are not included.
5. \#Total Concrete Methods: The total number of methods that have byte code instructions. Native and abstract methods are excluded. Even an empty method must  have a `return` instruction.
6. \#Total Covered Methods: The total number of methods that have non-zero instruction coverage.
7. \#Total Instructions: The total number of bytecode instructions.
8. \#Total Covered Instructions: The total number of covered bytecode instructions.
9. (\#Total Covered Methods)/(\#Total Methods): method coverage over all methods.
10. (\#Total Covered Methods)/(\#Total Concrete Methods): method coverage over concrete methods.
11. (\#Total Covered Instructions)/(\#Total Instructions): instruction coverage.

```
1512387	23197	Start	97613	90865	3794	1480064	45738	0.038868	0.041754	0.030903
1542162	23197	Dump	97613	90865	4561	1480064	53897	0.046725	0.050195	0.036415
1603555	23197	Dump	97613	90865	4566	1480064	53944	0.046777	0.050250	0.036447
1664963	23197	Dump	97613	90865	4567	1480064	53950	0.046787	0.050261	0.036451
1725368	23197	Dump	97613	90865	4567	1480064	53950	0.046787	0.050261	0.036451
1786763	23197	Dump	97613	90865	4567	1480064	53950	0.046787	0.050261	0.036451
1848153	23197	Dump	97613	90865	4567	1480064	53950	0.046787	0.050261	0.036451
1909538	23197	Dump	97613	90865	4567	1480064	53950	0.046787	0.050261	0.036451
1970931	23197	Dump	97613	90865	4567	1480064	53950	0.046787	0.050261	0.036451
2031324	23197	Dump	97613	90865	4567	1480064	53950	0.046787	0.050261	0.036451
2091716	23197	Dump	97613	90865	4567	1480064	53950	0.046787	0.050261	0.036451
2153127	23197	Dump	97613	90865	4567	1480064	53950	0.046787	0.050261	0.036451
2214560	23197	Dump	97613	90865	4567	1480064	53950	0.046787	0.050261	0.036451
2275947	23197	Dump	97613	90865	4567	1480064	53950	0.046787	0.050261	0.036451
2336355	23197	Dump	97613	90865	4567	1480064	53950	0.046787	0.050261	0.036451
2397752	23197	Dump	97613	90865	4567	1480064	53950	0.046787	0.050261	0.036451
2459154	23197	Dump	97613	90865	4567	1480064	53950	0.046787	0.050261	0.036451
2520555	23197	Dump	97613	90865	4567	1480064	53950	0.046787	0.050261	0.036451
2581952	23197	Dump	97613	90865	4567	1480064	53950	0.046787	0.050261	0.036451
2642357	23197	Dump	97613	90865	4567	1480064	53950	0.046787	0.050261	0.036451
2702746	23197	Dump	97613	90865	4567	1480064	53950	0.046787	0.050261	0.036451
2763152	23197	Dump	97613	90865	4567	1480064	53950	0.046787	0.050261	0.036451
2824665	23197	Dump	97613	90865	4567	1480064	53950	0.046787	0.050261	0.036451
2885128	23197	Dump	97613	90865	4567	1480064	53950	0.046787	0.050261	0.036451
2946530	23197	Dump	97613	90865	4567	1480064	53950	0.046787	0.050261	0.036451
3007984	23197	Dump	97613	90865	4567	1480064	53950	0.046787	0.050261	0.036451
3069390	23197	Dump	97613	90865	4567	1480064	53950	0.046787	0.050261	0.036451
3130784	23197	Dump	97613	90865	4567	1480064	53950	0.046787	0.050261	0.036451
3192180	23197	Dump	97613	90865	4567	1480064	53950	0.046787	0.050261	0.036451
3253618	23197	Dump	97613	90865	4567	1480064	53950	0.046787	0.050261	0.036451
3315183	23197	Dump	97613	90865	4567	1480064	53950	0.046787	0.050261	0.036451
```

The parser also produces a histogram of method coverage.
In the following histogram, the coverage of 86,309 methods are below 10% and 3,198 methods have full coverage.

```
  0% 86309
 10% 58
 20% 68
 30% 93
 40% 128
 50% 187
 60% 213
 70% 195
 80% 265
 90% 156
100% 3193
```
