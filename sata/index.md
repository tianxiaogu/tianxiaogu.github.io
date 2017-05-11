title: SATA

# SATA: Steering Automated Testing for Android Applications

A replacement of Monkey.

Download our model-based automated testing tool [Ape](ape-bin.zip).

!!! note:
    On Android 6 only now. If you need a version for Android 7, please contact me.

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

