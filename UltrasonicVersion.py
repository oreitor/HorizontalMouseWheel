import serial
import pyautogui as pag

reading = serial.Serial('COM4', 9600)
i = 0
x = []
y = []

while True:

    value = reading.readline()
    value = float(value)
    threshold = 10
    result = (value - threshold) / 5

    if 10 > value > 1:

        if i % 2 == 0:
            pag.press("right", abs(round(result)))
            x.append('0')
        else:
            pag.press("left", abs(round(result)))
            y.append('0')

    if len(y) > 0 and value > 10:
        y.clear()
        i = 2
    elif len(x) > 0 and value > 10:
        x.clear()
        i = 1
