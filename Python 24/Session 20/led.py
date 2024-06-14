import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

led = 4

GPIO.setup(led, GPIO.OUT, initial=GPIO.LOW)

for i in range(5):
    GPIO.output(led, GPIO.HIGH)
    print('led on')
    time.sleep(1)
    GPIO.output(led, GPIO.LOW)
    print('led off')
    time.sleep(1)