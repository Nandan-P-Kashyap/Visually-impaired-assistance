import RPi.GPIO as GPIO
import time
from twilio.rest import Client
import signal
import sys

# Setup for GPIO
button_pin = 2
GPIO.setmode(GPIO.BCM)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Twilio setup
sid = 'xxxxxx50xxxxxxxxxxxxxxxxxxxxxc81555'
authToken = '382fbbd3f9xxxxxxxxxxxxxx5'
twilio_number = '+130000000'
emergency_contact = '+917000000000'
client = Client(sid, authToken)

# Signal handler for graceful exit
def signal_handler(sig, frame):
    print('Exiting gracefully')
    GPIO.cleanup()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

def send_sos():
    print("Sending emergency SOS message...")
    try:
        message = client.messages.create(
            to=emergency_contact,
            from_=twilio_number,
            body="SOS worked!!"
        )
        print("Message sent")
    except Exception as e:
        print(f"Failed to send message: {e}")

# Send the SOS message immediately
send_sos()

# Cleanup GPIO
GPIO.cleanup()
