# Horizontal Mouse Wheel

For this project, I made two version using Python and Arduino. If do you wanna use potantiometer and leds you can choose 'Pot Version' or another option is 'Ultrasonic Version' with using HR-SC4 ultrasonic sensor. I got help from [pyFirmata](https://pypi.org/project/pyFirmata/) module in Pot Version. However, in the Ultrasonic version, I preferred the [pyserial](https://pypi.org/project/pyserial/) module. Your choice. :)

There is also a great package for mouse control, which is our main goal. The [PyAutoGUI](https://pypi.org/project/PyAutoGUI/) module provides cross-platform support for managing mouse and keyboard operations through code to enable automation of tasks. You can install this pip:

```python
pip install PyAutoGUI
```

### Pot Version

First of all, to control Arduino from the PC, you’d have to design a protocol for the communication between the PC and Arduino. On the PC, you could write a program to control the Arduino through a serial connection, based on the protocol you’ve designed. Fortunately, there are standard protocols to do this. Firmata is one of them. This protocol establishes a serial communication format that allows you to read digital and analog inputs, as well as send information to digital and analog outputs.

Before you write your Python program to drive Arduino, you have to upload the Firmata sketch so that you can use that protocol to control the board. The sketch is available in the Arduino IDE’s built-in examples. To open it, access the File menu, then Examples, followed by Firmata, and finally StandardFirmata:

![alt text](https://github.com/oreitor/HorizontalMouseWheel/blob/master/StandartFirmata.png)

When you upload the Firmata sketch to Arduino, you don't notice any activity on the Arduino. To control it, you still need a program that can communicate with the board through the serial connection. To work with the Firmata protocol in Python, you’ll need the pyFirmata package, which you can install with pip:

```python
pip install pyFirmata
```
After the installation finishes, you can run an any application using Python and Firmata with Arduino. For my project, you can run [Pot Version](https://github.com/oreitor/HorizontalMouseWheel/blob/master/PotVersion.py).

## Ultrasonic Version

Unlike the previous version, we will take the serial port data on the Arduino instead of controlling the Arduino. For this, selected pySerial module encapsulates the access for the serial port. This module automatically selects the matched serial from backend. So, we processed the selected data on the serial port with python.
