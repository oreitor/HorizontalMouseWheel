# Horizontal Mouse Wheel with Contactless Control

Implementation that acts as a Horizontal Mouse Wheel with contactless control. For this implementation, we need just two electronics component and simple code written with Python. 

<p align="center">
  <img width="600" src="https://github.com/oreitor/contactless-horizontal-mouse-wheel-control/blob/master/HMW.gif">
</p>

First things first, lets built up electronics side. Arduino is our microcontroller. Also, I used HC-SR04 ultrasonic sensor for detect distance. When the ended up connecttions about Arduino and HC-SR04 required install [this](https://github.com/oreitor/contactless-horizontal-mouse-wheel-control/blob/master/arduino.ino) code which about distance detection to Arduino.

Lets move on to the fun part now. Two packages need to be installed before writing code with Python.

```python
pip install pyserial
pip install PyAutoGUI
```

We have to complete serial communications between Python and Arduino. [pyserial](https://pypi.org/project/pyserial/) package provides that. Distance results created by sensor send to Python with serial comm. Other package [pyAutoGUI](https://pypi.org/project/PyAutoGUI/), allows us to switch between Python and computer GUI platform. Thus, desired commands can be assigned for mouse or keyboard.

Lastly, run [this](https://github.com/oreitor/contactless-horizontal-mouse-wheel-control/blob/master/python.py) Python code. Everything is ready!
