import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

pir = 27
led = 4

GPIO.setup(led, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(pir, GPIO.IN)

while True:
    if GPIO.input(pir) == True:
        print("Motion detected!")
        GPIO.output(led, GPIO.HIGH)
        time.sleep(2)
    elif GPIO.input(pir) == False:
        GPIO.output(led, GPIO.LOW)
