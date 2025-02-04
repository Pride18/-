import RPi.GPIO as GPIO
import time


class Pump:
    def __init__(self, pin):
        GPIO.setmode(GPIO.BCM)
        self.pin = pin

    def pour(self, time_delay):  # Time in seconds
        GPIO.output(self.pin, GPIO.HIGH)
        time.sleep(time_delay)
        GPIO.output(self.pin, GPIO.LOW)


class Motor():
    def __init__(self, pin):
        GPIO.setmode(GPIO.BCM)
        self.pin = pin

    def rotate(self, time_delay):  # Time in seconds
        GPIO.output(self.pin, GPIO.HIGH)
        time.sleep(time_delay)
        GPIO.output(self.pin, GPIO.LOW)


juice = Pump(11)
water = Pump(13)
mint = Pump(15)
motor = Motor(14)


def process_the_order(slots):
    for i in range(len(slots)):
        pass