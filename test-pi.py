from gpiozero import Button, LED
import time
led1 = LED(2)
led1 = LED(3)
while True:
    led1.on()
    time.sleep(1)
    led1.off()
    time.sleep(1)
    led2.on()
    time.sleep(1)
    led2.off()
    time.sleep(1)