title: Ape

# Ape: Automated Testing of Android Applications with Abstraction Refinement

Download our model-based automated testing tool [Ape](ape-bin.zip) (update: 2018-01-05).


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

    adb push ape.jar /sdcard/



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
    * You can also try `orbit`, `wechat`, `random`, and reinforcement learning enhanced random (`satarl`)

You can also specify the total amount of Monkey events. In this mode, Ape will stop by default once there is a crash.


    ./ape.py -p com.google.android.calculator --ape sata 1000


## Known Bugs

1. Memory Bloat:
    * Ape runs in the phone with limited memory for each process. Hence it may run out of memory as now we simply keep a large number of Strings and XML document objects in the memory.



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


## Configuration

Ape is under developing now. There is no stable documentation right now.
After the testing, ape will print a list of configurations.
To change an option,
you can put a Java properties file into `/sdcard/ape.properties`.

!!! note:
    The documentation below is out-of-date now. Updated documentation will come later.


## Model Evolution

Naming is a set of XPath based rules to specify how to abstract a GUI tree into a state representation.
The details of a naming is not covered in this document.


1. Disable abstraction refinement:
    * `ape.evolveModel = false`
    * `ape.baseNaming = stoat`
2. Enable abstraction refinement:
    * `ape.evolveModel = true` (default)
    * `ape.baseNaming = resourceid` (default)
3. User specified custom base naming is under working.

If you want to use ape as a stress testing tool, you need to disable abstraction refinement
and set a proper wait interval.

## Action Wait Interval


An action needs more throttle if it is

1. unvisited
    * `ape.throttleForUnvisitedAction = 500`
    * An unvisited action usually triggers resource loading and warm up.
2. an activity transition.
    * Rendering a new activity usually needs to wait for more time.
3. visited and non-deterministic (weak transition)
    * Non-deterministic actions usually are caused by canceling a long time GUI transition.

However, the previous rules are heuristic-based. There are a few actions that need a relative long wait interval.
Hence, we randomly append a `maxExtraThorttle` to an action.

Recommend configurations:

1. \#1: Use the recommended default throttle.
2. \#2: Smaller regular throttle and large probability to trigger the `maxExtraThrottle`:
    * `ape.throttleForUnvisitedAction = 100` (or smaller, e.g., 10)
    * `ape.throttlePerActivityTransition= 0`
    * `ape.throttlePerWeakStateTransition= 0`
    * `ape.throttlePerTrivialState = 0`
    * `ape.maxExtraThrottleProbability = 0.1` (default is 0.01)
3. Use XPathlet to specify a wait interval for particular actions.

Details of how ape calculates the wait interval for an action.

```java
    private static final int throttleForUnvisitedAction = Config.getInteger("ape.throttleForUnvisitedAction", 500); // set base throttle
    private static final int throttlePerActivityTransition = Config.getInteger("ape.throttlePerActivityTransition", 200); // set base throttle
    private static final int throttlePerWeakStateTransition =  Config.getInteger("ape.throttlePerWeakStateTransition", 500); // false;
    private static final int throttlePerTrivialState = Config.getInteger("ape.throttlePerTrivialState", 1000);
    private static final int maxExtraThrottle =  Config.getInteger("ape.maxExtraThrottle", 5000);
    private static final int maxThrottle =  Config.getInteger("ape.maxThrottle", 5000); // 5 000;

    private static final double maxExtraThrottleProbability = Config.getDouble("ape.maxExtraThrottleProbability", 0.01D);
    private static final double maxExtraThrottleProbabilityForActivityTransition = Config.getDouble("ape.maxExtraThrottleProbabilityForActivityTransition", 0.10D);

    protected int getThrottleForNewAction(State state, Action action) {
        int throttle = 0;
        Collection<StateTransition> edges = getGraph().getOutStateTransitions(action);
        boolean hasActivityTransition = false;
        boolean hasWeakStateTransition = false;
        boolean hasTrivialState = false;
        for (StateTransition edge : edges) {
            if (edge.action.isBack()) {
                continue;
            }
            if (!edge.isStrong()) {
                hasWeakStateTransition = true;
            } else if (edge.target.isTrivialState()) {
                hasTrivialState = true;
            }
            if (!edge.isSameActivity()) {
                hasActivityTransition = true;
            }
        }

        if (hasTrivialState && edges.size() == 0) {
            throttle += throttlePerTrivialState;
        } else {
            if (hasWeakStateTransition) {
                throttle += throttlePerWeakStateTransition; // only count one weak edge
            }
            if (hasActivityTransition) {
                throttle += throttlePerActivityTransition;
            }
        }
        if (action.isUnvisited()) {
            throttle += throttleForUnvisitedAction;
        }

        if (toss(maxExtraThrottleProbability)) {
            throttle = throttle + getRandom().nextInt(maxExtraThrottle);
        }
        if (hasActivityTransition && toss(maxExtraThrottleProbabilityForActivityTransition)) {
            throttle = throttle + getRandom().nextInt(maxExtraThrottle);
        }

        throttle =  throttle <= maxThrottle ? throttle : maxThrottle;

        GUITreeNode node = action.getResolvedNode();
        if (node != null) {
            throttle += node.getExtraThrottle(); // via XPath
        }

        if (throttle > 0) {
            Logger.dformat("Append a throttle %d for action %s", throttle, action);
        }
        return throttle;
    }


```


## Trap Detection

Ape will force the app to be restarted if it detects that it stays in a particular activity/state for a certain number of steps.
In addition, Ape will also restart the app if the graph is not updated for a specific steps.

Check the following options.

1. `ape.graphStableRestartThreshold`
2. `ape.stateStableRestartThreshold`
3. `ape.activityStableRestartThreshold`

## WebView

The `uiautomator dump` now support dumping contents into WebView.
But Ape ignores widgets inside a WebView by default.

Check the following options.

1. `ape.alwaysIgnoreWebViewAction = true`
    * This option will make Ape ignore any WebView.
2. `ape.WebViewActionThreshold = 30`
    * This option will make Ape to ignore any WebView that has more than 30 interactive widgets.

## XPathlet


Ape now supports configuring widgets-specified behaviors via XPath.

Put the following json into the file `/sdcard/ape.xpath`.
This will disable actions on any widget that has no text.

```
[{
    "xpath": "//*[@text='']",
    "actions": []
}]
```


!!! note:
    Use <https://jsonlint.com/> to validate your json first.

The field `actions` is an array of action names.

```
NOP
CLICK
LONG_CLICK
SCROLL_TOP_DOWN
SCROLL_BOTTOM_UP
SCROLL_LEFT_RIGHT
SCROLL_RIGHT_LEFT
```


## Screenshots

```
ape.takeScreenshot = true
ape.takeScreenshotForEveryStep = true
ape.takeScreenshotForNewState = true
ape.imageWriterCount = 3
```

## Input Text

Ape decides to do text input by checking the following three conditions.

1. Specified by XPath

        [{
            "xpath": "//*[@text='Title']",
            "text": "I am a Title"
        }]

    An example of testing the Google Keep app can be found here.

    * [vis-timeline.html](./xpath-input-example/vis-timeline.html)

    This feature depends on the [ADB Keyboard](https://github.com/senzhk/ADBKeyBoard). You must build and install a ADBKeyboard first.

    !!! warning:
        ADB Keyboard cannot properly handle `imeOptions`. To avoid unnecessary crashes, we now only do text input but disable IME actions.
        More information can be found at <https://developer.android.com/reference/android/view/inputmethod/EditorInfo.html>.

2. `ape.randomPickFromStringList = true`
    * Randomly pick a line from a text file located at `/sdcard/ape.strings`.
3. `ape.generateRandomTextInput = true`
    * Randomly generate a string by regex `[0-9a-z]{0,32}`.


!!! note:
    Only one type of input action can be triggered.

## Acknowledgments

We thank the following experts for their insightful comments on Ape.

* [Ting Su](https://tingsu.github.io/)
* Zhao Zhang 张钊
