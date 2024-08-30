# Assistive Tool for Visually Impaired

## Overview

The Assistive Tool for Visually Impaired is a Raspberry Pi-based project designed to aid visually impaired individuals through three main functionalities:
1. **Obstacle Detection**: Continuous monitoring for obstacles using an ultraviolet sensor.
2. **Currency Detection**: Detecting currency notes and converting text to speech.
3. **Emergency SOS**: Sending an SOS alert when a button is pressed.

## Project Structure

### 1. Obstacle Detection (High Priority)

**File**: `obstacle_detection.py`

- **Description**: Continuously monitors the environment using an ultraviolet sensor to detect obstacles.
- **Functionality**:
  - Runs in a background thread to ensure it continuously checks for obstacles.
  - Triggers a vibration alert when an obstacle is detected.
  - Ensures that obstacle detection has the highest priority to assist users effectively in avoiding obstacles.
- **Usage**: Started as a daemon thread in `main.py` to operate independently of other tasks.

### 2. Emergency SOS (Medium Priority)

**File**: `send_sos.py`

- **Description**: Handles the sending of an emergency SOS alert when the SOS button is pressed.
- **Functionality**:
  - Activated by a double press of a single GPIO button.
  - Sends an SOS message via SMS or other communication methods as configured.
  - Ensures that emergency alerts are sent promptly in case of urgent situations.
- **Usage**: Triggered from `main.py` based on double button press detection.

### 3. Currency Detection (Lower Priority)

**File**: `currency_detection.py`

- **Description**: Detects and identifies currency notes using machine learning and provides text-to-speech output.
- **Functionality**:
  - Activated by a single press of a GPIO button.
  - Processes the detected currency note and converts the text to speech to inform the user.
  - Ensures that currency detection does not interfere with higher-priority tasks.
- **Usage**: Triggered from `main.py` based on single button press detection.

## Main Script

**File**: `main.py`

- **Description**: The central script that manages the execution of the other components.
- **Functionality**:
  - Sets up GPIO pins and button listeners.
  - Starts the obstacle detection in a separate thread.
  - Listens for button presses to activate currency detection or send an SOS alert based on the press pattern.
  - Handles GPIO cleanup on exit to ensure the system is properly shut down.

## Setup Instructions

1. **Install Dependencies**:
   - Ensure that Python 3 and necessary libraries (`RPi.GPIO`, etc.) are installed on your Raspberry Pi.
   - Install additional dependencies required by each script.

2. **Hardware Setup**:
   - Connect the ultraviolet sensor for obstacle detection.
   - Connect the button for currency detection and SOS.
   - Connect any other hardware components required for the project.

3. **Run the Project**:
   - Execute the `main.py` script on your Raspberry Pi:
     ```bash
     python3 main.py
     ```

## File Descriptions

- **`obstacle_detection.py`**: Contains the code for obstacle detection.
- **`currency_detection.py`**: Contains the code for currency detection and text-to-speech conversion.
- **`send_sos.py`**: Contains the code for sending the emergency SOS alert.
- **`main.py`**: The main script that ties all the functionalities together and manages the execution flow.

## Notes

- Ensure that all hardware connections are secure and correct.
- Adjust time thresholds and configurations as needed based on user feedback and performance testing.
- Regularly test the system to ensure all components work as expected and the system is responsive to user interactions.

## Contact

For any questions or issues, please contact [Nandan P Kashyap](mailto:nandanpk4@gmail.com).
