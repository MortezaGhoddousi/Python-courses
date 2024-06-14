import RPi.GPIO as GPIO
from gpiozero import MotionSensor
import time

GPIO.setwarnings(False)

pir = MotionSensor(27)
led = 4

GPIO.setup(led, GPIO.OUT, initial=GPIO.LOW)

while True:
    pir.wait_for_motion()
    GPIO.output(led, GPIO.HIGH)
    print("led on")
    print('Motion detected!')
    pir.wait_for_no_motion()
    GPIO.output(led, GPIO.LOW)
    print('led off')
