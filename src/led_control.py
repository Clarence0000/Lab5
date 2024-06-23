from hal import hal_led as led
from threading import Thread
from time import sleep

from hal import hal_keypad as keypad

def led_thread():
    global delay

    while(True):
        if delay != 0:
            led.set_output(24,1)
            sleep(delay)
            led.set_output(24,0)
            sleep(delay)

def led_control_init(delay_input):
    global delay
    delay = delay_input
    led.init()
    t1 = Thread(target=led_thread)
    t1.start()

