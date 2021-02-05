import serial
import pyautogui as pag

reading = serial.Serial('COM3', 9600)
i, x, y = 0, [], []

while True:

    value = reading.readline()
    value = int(value)
    print(f"Distance: {value} cm")
    result = (value - 20) / 3

    if 20 > value > 1:

        if i % 2 == 0:
            pag.press("right", abs(round(result)))
            x.append('0')
        else:
            pag.press("left", abs(round(result)))
            y.append('0')

    if len(y) > 0 and (value > 20 or value == 0):
        y.clear()
        i = 2
    elif len(x) > 0 and (value > 20 or value == 0):
        x.clear()
        i = 1
