title: Ape

# Ape: Automated Testing of Android Applications with Abstraction Refinement

## Download

* Binary:
    * Please build from the source code for the latest binary.
* Source:
    * <https://github.com/tianxiaogu/ape>

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
    * Install [Mini Tracing](./install-mini-tracing).
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


!!! note
    To install and use MiniTracing, an emulator must be started with option `-writable-system`.
    No product build emulators such as those with builtin Google Play Store are supported.
    See [Install the Google Play Store in an Emulator](./install-google-play-store-in-an-emulator) manually.

* MiniTracing: Collect method/coverage without bytecode instrumentation.
    * [Android 9 API 28 (binary for x86)](/art-mt-x86-api28.zip): Android ART with method/instruction coverage support.
        * Currently does not support of the `x86_arm` emulator.
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
Make sure `adb` is available in your `PATH`.


    ./ape.py -p com.google.android.calculator --running-minutes 100 --ape sata


Check the `ape.py` if you want to run Ape with multiple devices via `adb -s`.

Options:

* `-p`: specify the package name, the same as Monkey
* `--running-minutes`: the total testing time in minutes
    * This is the continuous mode, which means Ape does not stop when it triggers a crash.
* `--ape sata`: use the default exploration strategy described in the paper.
    * Only `random` and `sata` are supported now, where `sata` is the default exploration strategy described in the paper.

You can also specify the total amount of Monkey events. In this mode, Ape will stop by default once there is a crash.


    ./ape.py -p com.google.android.calculator --ape sata 1000


## Output

Users should save everything that has been outputted into the console.
In addition to the standard output, Ape also records both high-level actions and low-level events and saves them into a folder under `/sdcard`,
e.g., `/sdcard/sata-com.amaze.filemanager-ape-sata-running-minutes-10`.

* `action-history.log`: The history of actions. We create a phantom action `PHANTOM_CRASH` to record crash information.
    An action may produce more than one events.
* `produce.log`: The history of events that are generated from actions.
* `consume.log`: The history of events that are actually injected but the injection may fail. For example, a click event may fail if the GUI changes after the event is created.
* `sataGraph.vis.js`: Model graph can be visualized using [vis](http://visjs.org/).
* `sataTimeline.vis.js`: Timeline can be visualized using [vis](http://visjs.org/).
* `sataModel.obj`: Model graph has been dumped using the [Java Serialization API](https://docs.oracle.com/javase/tutorial/jndi/objects/serial.html). This file could be used for off-line graph analysis of the model.
* `step-11-g5s8.txt`: The state at iteration 11.
* `step-1404.xml`: The GUI tree (in XML) at iteration 1404.
* `step-597.png`: The snapshot at step 597.

## Visualization

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

## Patching GUI Tree

Ape will read file `/sdcard/ape.xpath` to patch the GUI tree before applying the abstraction function to build the state.

The configuration file is a JSON file encoding a JSON array. Each element of the array is an object that has the following attributes.

1. `"xpath"`: the xpath to select elements in the XML tree
    * The XML that Ape used is different from that obtained via `uiautomator dump --compressed`. Please check the output directory to find some examples (e.g., `step-N.xml`)
    * The value of property `text` has been truncated to save memory. Try to avoid using property `text` or see `ape.truncateTextLength`. The default length of truncated text string is 8.
2. `"actions"` (optional): a set of supported model actions, i.e., `MODEL_CLICK`, `MODEL_`
    * click: `MODEL_CLICK`
    * long click: `MODEL_LONG_CLICK`
    * swipe vertically: `MODEL_SCROLL_TOP_DOWN` or `MODEL_SCROLL_BOTTOM_UP`
    * swipe horizontally: `MODEL_SCROLL_LEFT_RIGHT` or `MODEL_SCROLL_RIGHT_LEFT`
    * An empty array will clear the actions on the widget, i.e., the widget has been disabled.
3. `"text"` (optional):
    * If the selected widget is an `EditText`, the text will be used to generate input for the widget.
4. `"throttle"` (optional):
    * Throttle for the widget.

```
[{
    "xpath": "//*[@class='android.widget.EditText']",
    "actions": ["MODEL_CLICK"],
    "text": "San Francisco",
    "throttle": 500
},
{
    "xpath": "//*[@class='android.widget.ImageButton']",
    "actions": []
}]
```

The above example will do the following patch to every GUI tree.

1. Input `San Francisco` for every `EditText`.
2. Disable all `ImageButton` (no actions).


Ape will output the following messages if it can successfully parse file `ape.xpath`.

```
[APE] *** INFO *** Select 1 nodes by //*[@class='android.widget.EditText']
[APE] *** INFO *** Select 0 nodes by //*[@class='android.widget.ImageButton']
```



!!! note
    1. Make sure that `ape.xpath` is a valid JSON file and still available at `/sdcard/ape.xpath`.
    2. Make sure that your XPath expression works on the dumped `step-N.xml`.
    3. You could use a large throttle for debugging to easily test whether the XPath based patching takes effect.

## Acknowledgments

We thank the following experts for their insightful comments on Ape.

* [Ting Su](https://tingsu.github.io/)
* Zhao Zhang 张钊
