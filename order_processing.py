import RPi.GPIO as GPIO
import time


class Pump:
    def __init__(self, pin):
        GPIO.setmode(GPIO.BCM)
        self.pin = pin

    def pour(self, time_delay):  # Время в секундах
        GPIO.output(self.pin, GPIO.HIGH)
        time.sleep(time_delay)
        GPIO.output(self.pin, GPIO.LOW)


class Motor:
    def __init__(self, pin):
        GPIO.setmode(GPIO.BCM)
        self.pin = pin

    def rotate(self, time_delay, reverse=False):  # Время в секундах
        GPIO.output(self.pin, GPIO.HIGH)
        time.sleep(time_delay)
        GPIO.output(self.pin, GPIO.LOW)


juice = Pump(11)
water = Pump(13)
mint = Pump(15)
motor = Motor(14)


recipes = {  # (water_units, juice_units, mint_units)
    "": (0, 0, 0),
    "Газированная вода": (5, 0, 0),
    "Мятный сироп": (0, 0, 1),
    "Апельсиновый сок": (0, 4, 0),
    "Лимонад “Мятный”": (8, 0, 2),
    "Лимонад “Заводной апельсин”": (3, 5, 0),
    "Лимонад ‘Тройной”": (3.5, 4.5, 1)
}

initial_time_rotate = 1  # Время для оборота первого стакана на выдачу
time_per_cup = 1  # Время для поворота на одного стакана.
time_per_10ml = 1


def process_the_order(slots):
    motor.rotate(initial_time_rotate)
    for i in range(len(slots)):
        motor.rotate(time_per_cup)
        water_time, juice_time, mint_time = recipes[slots[i]]
        water.pour(time_per_10ml * water_time)
        juice.pour(time_per_10ml * juice_time)
        mint.pour(time_per_10ml * mint_time)
    motor.rotate(len(slots) * time_per_cup + initial_time_rotate, reverse=True)

