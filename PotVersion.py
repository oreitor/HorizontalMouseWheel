import pyfirmata
import time
import pyautogui as pag

controller = pyfirmata.Arduino('COM4')
it = pyfirmata.util.Iterator(controller)
it.start()

pot = controller.get_pin("a:0:i")
left_led = controller.get_pin("d:11:p")
right_led = controller.get_pin("d:10:p")

while True:

    if pot.read() is None:
        pass
    else:
        reading = pot.read()
        threshold = 0.5
        value = reading - threshold

        if abs(round(value * 7)) < 1:
            left_led.write(0)
            right_led.write(0)
        else:

            if value > 0:
                left_led.write(1)
                pag.press("left", abs(round(value * 7)))
            else:
                right_led.write(1)
                pag.press("right", abs(round(value * 7)))

    time.sleep(0.1)
