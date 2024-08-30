import RPi.GPIO as GPIO
import time
import threading
from obstacle_detection import start_obstacle_detection
from currency_detection import detect_currency
from send_sos import send_sos

# Setup GPIO pin
GPIO.setmode(GPIO.BCM)
BUTTON_PIN = 17
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Time thresholds (in seconds)
SINGLE_PRESS_THRESHOLD = 0.5  # Maximum time between presses for single press
DOUBLE_PRESS_THRESHOLD = 1.0  # Maximum time between presses for double press

def button_listener():
    last_press_time = 0
    press_count = 0

    while True:
        if GPIO.input(BUTTON_PIN) == GPIO.LOW:  # Button pressed
            press_time = time.time()
            if press_count == 0:
                # First press
                last_press_time = press_time
                press_count += 1
            elif press_count == 1 and (press_time - last_press_time) < DOUBLE_PRESS_THRESHOLD:
                # Second press within threshold for double press
                press_count = 0
                send_sos()
            else:
                # Handle single press if time exceeds threshold
                if (press_time - last_press_time) > SINGLE_PRESS_THRESHOLD:
                    press_count = 0
                    detect_currency()
            time.sleep(0.1)  # Debounce delay
        else:
            # Reset the press count if the button is not pressed
            press_count = 0

# Start obstacle detection in a separate thread (highest priority)
obstacle_thread = threading.Thread(target=start_obstacle_detection)
obstacle_thread.daemon = True  # Run as a background process
obstacle_thread.start()

# Start listening for button presses (lower priority)
button_listener()

# Clean up GPIO on exit
GPIO.cleanup()
