title: SATA

# SATA: Steering Automated Testing for Android Applications

A replacement of Monkey.

Download our model-based automated testing tool [Ape](ape-bin.zip).

!!! note:
    The zip is for Android 6 only now. Click here to get the [ape.jar](ape.jar) for Android 7.

## Install


    adb push ape.jar /sdcard/


## Run

We provide a python script (i.e., `ape.py`) to facilitate running ape on Android platform.

The following command starts to run SATA to test the Calculator on a real device connected via `adb`.


    ./ape.py -p com.google.android.calculator --running-minutes 100 --ape sata


Check the `ape.py` if you want to run SATA with an emulator.
You should at least remove the `-d` options for `adb`.

Options:

* `-p`: specify the package name, the same as Monkey
* `--running-minutes`: the total testing time in minutes
* `--ape sata`: use the SATA exploration strategy described in the paper.
    * You can also try `orbit`, `wechat`, `random`, and reinforcement learning enhanced random (`satarl`)

## Visualization

We provide a tool to visualize the model.

1. SATA writes a js file into the output folder for visualization.
    *. Check the tail of the output to locate the output in the phone.
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
