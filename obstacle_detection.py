import RPi.GPIO as GPIO
import time

VIBRATION_PIN = 22  # Vibration motor pin
OBSTACLE_SENSOR_PIN = 23  # Ultraviolet sensor pin

GPIO.setup(VIBRATION_PIN, GPIO.OUT)
GPIO.setup(OBSTACLE_SENSOR_PIN, GPIO.IN)

def start_obstacle_detection():
    while True:
        if GPIO.input(OBSTACLE_SENSOR_PIN) == GPIO.LOW:  # Obstacle detected
            print("Obstacle detected! Triggering vibration.")
            GPIO.output(VIBRATION_PIN, GPIO.HIGH)  # Turn on vibration motor
            time.sleep(1)  # Vibration duration
            GPIO.output(VIBRATION_PIN, GPIO.LOW)  # Turn off vibration motor
        time.sleep(0.1)  # Small delay to prevent CPU overload
