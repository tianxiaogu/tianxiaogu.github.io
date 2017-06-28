title: SATA

# SATA: Steering Automated Testing for Android Applications

A replacement of Monkey.

Download our model-based automated testing tool [Ape](ape-bin.zip).

!!! note:
    Ape is the internal name used during developing SATA.

Files inside `ape-bin.zip`:

```
ape-bin/
ape-bin/7/
ape-bin/7/ape.jar  <--- For Android 7
ape-bin/ape.jar    <--- For Android 6
ape-bin/ape.py
ape-bin/README.md
```

## Install


    adb push ape.jar /sdcard/


!!! note:
    For Android 7, just use another jar.

        adb puosh 7/ape.jar /sdcard/



## Run

We provide a python script (i.e., `ape.py`) to facilitate running ape on Android platform.

The following command starts to run SATA to test the Calculator on a real device connected via `adb`.


    ./ape.py -p com.google.android.calculator --running-minutes 100 --ape sata

Check the `ape.py` if you want to run SATA with an emulator.
You should at least remove the `-d` options for `adb`.

Options:

* `-p`: specify the package name, the same as Monkey
* `--running-minutes`: the total testing time in minutes
    * This is the continuous mode, which means SATA does not stop when it triggers a crash.
* `--ape sata`: use the SATA exploration strategy described in the paper.
    * You can also try `orbit`, `wechat`, `random`, and reinforcement learning enhanced random (`satarl`)

You can also specify the total amount of Monkey events. In this mode, SATA will stop by default once there is a crash.


    ./ape.py -p com.google.android.calculator --ape sata 1000




## Visualization

We provide a tool to visualize the model.

1. SATA writes several js files into the output folder for visualization.
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


## Configuration

SATA is under developing now. There is no stable documentation right now.

Put the following content into `/sdcard/ape.properties` to configure SATA.

```
ape.WebViewActionThreshold = 30
ape.activityStableRestartThreshold = 200
ape.alwaysIgnoreWebViewAction = true
ape.avoidEditText = false
ape.checkHomogeneous = false
ape.checkUnsaturatedTrivialState = true
ape.defaultAlpha = 0.2
ape.defaultBeta = 0.8
ape.defaultEpsilon = 0.05
ape.defaultGUIThrottle = 200
ape.defaultGamma = 0.8
ape.defaultMaxDepthEarlyStage = 3
ape.defaultMaxLengthEarlyStage = 2
ape.extraBasePriority = 3
ape.fallbackToGraphTransition = true
ape.fillTransitionsByHistory = true
ape.flushImagesThreshold = 10
ape.generateRandomTextInput = true
ape.graphStableRestartThreshold = 100
ape.ignoreEmpty = true
ape.ignoreEmptyWebViewWidget = true
ape.ignoreEmptyWidget = false
ape.ignoreOutOfBounds = true
ape.ignoreOutOfBoundsWidget = true
ape.imageWriterCount = 3
ape.includeFocusable = true
ape.invalidBackCircleThreshold = 3
ape.maxAppendThrottle = 3000
ape.nopActionThrottle = 1000
ape.onlyAddedActions = true
ape.randomPickFromStringList = false
ape.simpleGreedyEarlyStage = false
ape.sizeOfGuiTreeBuffer = 5
ape.startActionThrottle = 0
ape.stateStableCheckWelcomeThreshold = 10
ape.stateStableRestartThreshold = 50
ape.stopWhenEqual = true
ape.takeScreenshot = true
ape.takeScreenshotForEveryStep = true
ape.takeScreenshotForNewState = true
ape.throttleForUnvisitedAction = 500
ape.throttlePerActivityTransition = 100
ape.throttlePerTrivialState = 1000
ape.throttlePerWeakEdge = 500
ape.trivialStateActionThreshold = 1
ape.trivialStateUnsaturationActionThreshold = 3
ape.trivialStateUnsaturationThreshold = 3
ape.trivialStateWidgetThreshold = 3
ape.useComplexSPathChildrenThreshold = 5
ape.useComplexSPathDescendantActionThreshold = 20
ape.useDynamicSPath = true
ape.useShortID = false
ape.useShortestPathForEarlyStage = false
ape.useSimpleSPath = false
ape.useSingleScroll = false
```



## Trap Detection

SATA will force the app to be restarted if it detects that it stays in a particular activity/state for a certain number of steps.
In addition, SATA will also restart the app if the graph is not updated for a specific steps.

Check the following options.

1. `ape.graphStableRestartThreshold`
2. `ape.stateStableRestartThreshold`
3. `ape.activityStableRestartThreshold`

## WebView

The `uiautomator dump` now support dumping contents into WebView.
But SATA ignores widgets inside a WebView by default.

Check the following options.

1. `ape.alwaysIgnoreWebViewAction = true`
    * This option will make SATA ignore any WebView.
2. `ape.WebViewActionThreshold = 30`
    * This option will make SATA to ignore any WebView that has more than 30 interactive widgets.

## XPathlet


SATA now supports configuring widgets-specified behaviors via XPath.

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

## Misc.


### Input Chinese

SATA can input Unicode text using the ADB Keyboard.

<https://github.com/senzhk/ADBKeyBoard>



