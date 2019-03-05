title: Ape

# Ape: Automated Testing of Android Applications with Abstraction Refinement


[Download (ape-bin.zip)](/ape-bin.zip)

## Publication

Ape applies a CEGAR style technique to refine and coarsen the model abstraction.
A paper about Ape's main idea has been accepted to ICSE 2019.

~~~{.bibtexhtml}
@inproceedings{gu_practical_2019,
  author    = {Tianxiao Gu and Chengnian Sun and Xiaoxing Ma and Chun Cao and Chang Xu and Yuan Yao and Qirun Zhang and Jian Lu and Zhendong Su},
  title     = {Practical GUI Testing of Android Applications via Model Abstraction and Refinement},
  pages     = {to appear},
  year      = {2019},
  booktitle = {Proceedings of the 41st ACM/IEEE International Conference on Software Engineering (ICSE 2019)},
  pdf       = {/static/ape-icse-2019.pdf},
}
~~~

### Evaluation

* Crashes detected by Ape.
    * [list1](https://ape-report.github.io/)
    * [list2](https://ape-report.github.io/ape-report-1)
* [Reported bugs](./reported-bugs)

In the ICSE paper, we evaluated Ape in two experiments.

* The first part of the evaluation was conducted on x86 emulators.
    * [Install the Google Play Store in an Emulator](./install-google-play-store-in-an-emulator).
        * We need to download x86 compatible apps.
    * Install [Mini Tracing](#minitracing).
        * This step can be omitted if you do not want to collect method and instruction coverage.
    * Login with a test google account.
        * This step can be omitted if you do not want to test the Google Drive app.
    * Install and test the following packages for one hour.
        * [`com.citymapper.app.release`](https://play.google.com/store/apps/details?id=com.citymapper.app.release)
        * [`com.duolingo`](https://play.google.com/store/apps/details?id=com.duolingo)
        * [`com.enzuredigital.weatherbomb`](https://play.google.com/store/apps/details?id=com.enzuredigital.weatherbomb)
        * [`com.google.android.apps.docs`](https://play.google.com/store/apps/details?id=com.google.android.apps.docs)
        * [`com.google.android.apps.translate`](https://play.google.com/store/apps/details?id=com.google.android.apps.translate)
        * [`com.nuzzel.android`](https://play.google.com/store/apps/details?id=com.nuzzel.android)
        * [`com.popularapp.thirtydayfitnesschallenge`](https://play.google.com/store/apps/details?id=com.popularapp.thirtydayfitnesschallenge)
        * [`com.zillow.android.zillowmap`](https://play.google.com/store/apps/details?id=com.zillow.android.zillowmap)
        * [`flipboard.app`](https://play.google.com/store/apps/details?id=flipboard.app)
        * [`org.videolan.vlc`](https://play.google.com/store/apps/details?id=org.videolan.vlc)
        * [`tunein.player`](https://play.google.com/store/apps/details?id=tunein.player)
        * [`com.amaze.filemanager`](https://play.google.com/store/apps/details?id=com.amaze.filemanager)
        * [`com.eleybourn.bookcatalogue`](https://play.google.com/store/apps/details?id=com.eleybourn.bookcatalogue)
        * [`org.liberty.android.fantastischmemo`](https://play.google.com/store/apps/details?id=org.liberty.android.fantastischmemo)
        * [`org.totschnig.myexpenses`](https://play.google.com/store/apps/details?id=org.totschnig.myexpenses)
* The second part of the evaluation requires a huge amount of time. We release all stack traces instead.
    * [Stack traces (537 in total)](./trace.zip)
* We have implemented a [Null Intent Fuzzer](./null-intent-fuzzer.py) using Python to filter out trivial crashes.
    * Remember to set environment variable `SERIAL` and `ANDROID_HOME`.

<a name="minitracing"></a>
### Mini Tracing

We provided a `libart.so` for x86 emulators to collect coverage without instrumentation.
That means, you can use this tool to collect coverage for apps such as Google Doc to evaluate your tools.

* MiniTracing: Collect method/coverage without bytecode instrumentation.
    * [Android 6 (binary for x86)](/art-mt-x86.zip): Android ART with method/instruction coverage support.
    * [Android 4.4 (binary for x86)](/dalvikvm-mt-x86.zip): Android Dalvik VM with method/instruction coverage support.
    * [android-mt-cmd](https://bitbucket.org/txgu/android-mt-cmd): Command line tools to collect coverage.
    * [android-mt-parser](https://bitbucket.org/txgu/android-mt-parser): Parser for the coverage data.




## Install

Files inside `ape-bin.zip`:

```
ape-bin/
ape-bin/ape
ape-bin/ape.jar
ape-bin/ape.py
ape-bin/install.py
ape-bin/README.md
```

Copy Just copy the `ape.jar` to the phone.

    adb push ape.jar /data/local/tmp/

and run

    adb shell CLASSPATH=/data/local/tmp/ape.jar /system/bin/app_process /data/local/tmp/ com.android.commands.monkey.Monkey


More details can be found in `README.md`.

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
