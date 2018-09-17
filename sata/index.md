title: Ape

# Ape: Automated Testing of Android Applications with Abstraction Refinement

* Please send me an email if you are interested in the tool.


## Install

Files inside `ape-bin.zip`:

```
ape-bin/
ape-bin/ape.jar
ape-bin/ape.py
ape-bin/install.py
ape-bin/README.md
```

Just copy the `ape.jar` to the phone.

    adb push ape.jar /data/local/tmp/


## Evaluation


* Crashes detected by Ape using only 15 minutes.
    * [list1](https://ape-report.github.io/)
    * [list2](https://ape-report.github.io/ape-report-1)
* [Reported bugs](./reported-bugs)

## Mini Tracing

We provided a `libart.so` for x86 emulators to collect coverage without instrumentation.
That means, you can use this tool to collect coverage for apps such as Google Doc to evaluate your tools.

* MiniTracing: Collect method/coverage without bytecode instrumentation.
    * [Android 6 (binary for x86)](/art-mt-x86.zip): Android ART with method/instruction coverage support.
    * [Android 4.4 (binary for x86)](/dalvikvm-mt-x86.zip): Android Dalvik VM with method/instruction coverage support.
    * [android-mt-cmd](https://bitbucket.org/txgu/android-mt-cmd): Command line tools to collect coverage.
    * [android-mt-parser](https://bitbucket.org/txgu/android-mt-parser): Parser for the coverage data.

## Run

We provide a python script (i.e., `ape.py`) to facilitate running ape on Android platform.

The following command starts to run Ape to test the Calculator on a real device connected via `adb`.


    ./ape.py -p com.google.android.calculator --running-minutes 100 --ape sata

Check the `ape.py` if you want to run Ape with an emulator.
You should at least remove the `-d` options for `adb`.

Options:

* `-p`: specify the package name, the same as Monkey
* `--running-minutes`: the total testing time in minutes
    * This is the continuous mode, which means Ape does not stop when it triggers a crash.
* `--ape sata`: use the default exploration strategy described in the paper.
    * <del>You can also try `orbit`, `wechat`, `random`, and reinforcement learning enhanced random (`satarl`)</del>
    * Only `random` and `ape` are supported now.

You can also specify the total amount of Monkey events. In this mode, Ape will stop by default once there is a crash.


    ./ape.py -p com.google.android.calculator --ape sata 1000



## Visualization


!!! note
    Screenshot is disabled by default to save space.



We provide a tool to visualize the model.

1. Ape writes several js files into the output folder for visualization.
    * Check the tail of the output message to locate the output folder in the phone.
2. `adb pull /sdcard/your-output-folder` to your local directory.
3. Copy the following files into the local output directory
    * [vis.html](./demo/vis.html) (Right click and choose 'save as')
    * [vis.min.css](./demo/vis.min.css)
    * [vis.min.js](./demo/vis.min.js)
4. Open the copied `vis.html` in your browser.
    * You may need to wait for a certain amount of time to let the browser render the model.

Examples:

* [Calculator](./demo/vis.html)
* [Meitu](./demo-mtxx/vis.html) (1 min).


Now we can check the timeline.

* [Google Keep](./demo-keep-timeline/vis.html)
    * [Timeline](./demo-keep-timeline/vis-timeline.html)
    * Copy [vis-timeline.html](./demo-keep-timeline/vis-timeline.html) to your local output directory.
    * Open the copied `vis-timeline.html` in your browser.

## Acknowledgments

We thank the following experts for their insightful comments on Ape.

* [Ting Su](https://tingsu.github.io/)
* Zhao Zhang 张钊
