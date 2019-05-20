import RPi.GPIO as gpio
import time


PIN = 11

def callback_func(channel):
    print("We have a falling edge at " + str(channel))

gpio.setmode(gpio.BOARD)
gpio.setup(PIN, gpio.IN, pull_up_down=gpio.PUD_UP)

gpio.add_event_detect(PIN, gpio.FALLING, callback=callback_func, bouncetime=1000)

try:
    while True:
        print("Normal Routine")
        time.sleep(1)
        
except KeyboardInterrupt:
    gpio.cleanup()
gpio.cleanup()
