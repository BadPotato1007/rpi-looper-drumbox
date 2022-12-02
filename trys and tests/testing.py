from pi74HC595 import pi74HC595
import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BCM)
shift_register = pi74HC595(16, 20, 21)


#data is 16
#latch is 20
#clock is 21

while True:
    shift_register.set_by_list([1, 0, 0, 0, 0, 0, 0, 0])
    time.sleep(0.5)
    shift_register.set_by_list([0, 1, 0, 0, 0, 0, 0, 0])
    time.sleep(0.5)
    shift_register.set_by_list([0, 0, 1, 0, 0, 0, 0, 0])
    time.sleep(0.5)
    shift_register.set_by_list([0, 0, 0, 1, 0, 0, 0, 0])
    time.sleep(0.5)
    shift_register.set_by_list([0, 0, 0, 0, 1, 0, 0, 0])
    time.sleep(0.5)
    shift_register.set_by_list([0, 0, 0, 0, 0, 1, 0, 0])
    time.sleep(0.5)
    shift_register.set_by_list([0, 0, 0, 0, 0, 0, 1, 0])
    time.sleep(0.5)
    shift_register.set_by_list([0, 0, 0, 0, 0, 0, 0, 1])
    time.sleep(0.5)
    