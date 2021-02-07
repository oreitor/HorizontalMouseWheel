# Contactless Horizontal Mouse Wheel Control

For this project, I made two version using Python and Arduino. If do you wanna use potantiometer and leds you can choose 'Pot Version' or another option is 'Ultrasonic Version' with using HR-SC4 ultrasonic sensor. I got help from [pyFirmata](https://pypi.org/project/pyFirmata/) module in Pot Version. However, in the Ultrasonic version, I preferred the [pyserial](https://pypi.org/project/pyserial/) module.

There is also a great package for mouse control, which is our main goal. The [PyAutoGUI](https://pypi.org/project/PyAutoGUI/) module provides cross-platform support for managing mouse and keyboard operations through code to enable automation of tasks. You can install this pip:

```python
pip install PyAutoGUI
```



Unlike the previous version, we will take the serial port data on the Arduino instead of controlling the Arduino. For this, selected pySerial module encapsulates the access for the serial port. This module automatically selects the matched serial from backend. So, we processed the selected data on the serial port with python.

Now, we have to write code related reading serial to Arduino. Actually, we dont have to write code too. Because, the related sketch is also available in the built-in examples of the Arduino IDE. To open it, access the File menu, then Examples, followed by 01.Basics, and finally AnalogReadSerial:

<p align="center">
  <img width="460" height="300" src="https://github.com/oreitor/contactless-horizontal-mouse-wheel-control/blob/master/HMW.gif">
</p>

When you upload the AnalogReadSerial sketch to Arduino, you can read serial port data on Arduino with Python. However, firstly you should install pySerial package, which you can install with pip:

```python
pip install pyserial
```

As with [Ultrasonic Version](https://github.com/oreitor/HorizontalMouseWheel/blob/master/UltrasonicVersion.py) in this project, you can read the serial port with this module and Python. 
