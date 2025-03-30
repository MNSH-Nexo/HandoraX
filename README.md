# HandoraX
A cutting-edge hand gesture control system developed by **NexoraX**.


*Control your PC with the power of your hands!*

## Overview
HandoraX is an innovative application that transforms your webcam into a gesture-based controller. Say goodbye to traditional mouse and keyboard inputs—navigate, click, drag, scroll, and zoom using intuitive hand gestures. Built with Python, OpenCV, and MediaPipe, this project showcases the future of human-computer interaction.

## Features
- **Cursor Control**: Move your cursor with an open hand.
- **Click & Hold**: Tap or hold your index finger to your thumb for clicks or dragging.
- **Multi-Gesture Support**: From right-clicks to zooming, all with simple hand movements.
- **Customizable**: Adjust sensitivity and gesture mappings in `config.py`.
- **Real-Time**: Smooth and responsive tracking powered by MediaPipe.

## Installation
Follow these steps to get HandoraX running on your machine:

1. **Prerequisites**:
   - Python 3.12 or higher
   - A webcam

2. **Clone the Repository**:
   ```bash
   git clone https://github.com/MNSH-Nexo/HandoraX.git
   cd HandoraX

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
4. **Run the Program**:
   ```bash
   python main.py
On first run, hold your hand open for 3 seconds to calibrate.

Supported Gestures
HandoraX recognizes the following gestures:

## Supported Gestures
HandoraX recognizes the following gestures:
| Gesture                | Action                     | Description                              |
|------------------------|----------------------------|------------------------------------------|
| **Open Hand**          | Move Cursor               | Move your hand to control the cursor.    |
| **Index to Thumb**     | Click / Hold              | Quick tap for click, hold (>0.3s) to drag/select. |
| **Two Fingers to Thumb** | Right Click             | Pinch index and middle fingers to thumb. |
| **Three Fingers to Thumb** | Double Click          | Pinch index, middle, and ring to thumb.  |
| **Full Fist**          | Drag                      | Close your fist to drag items.           |
| **Fist with Index Out** | Select Text              | Fist with only index extended.           |
| **Middle to Thumb**    | Scroll                    | Pinch middle finger to thumb and move up/down. |
| **Two Hands**          | Zoom                      | Adjust distance between hands to zoom in/out. |
| **Pinky to Thumb**     | Go Back                   | Pinch pinky to thumb (e.g., browser back). |
| **Ring to Thumb**      | Go Forward                | Pinch ring finger to thumb (e.g., browser forward). |

## How It Works
HandoraX brings gesture control to life through a seamless three-step process:

- **Hand Detection**: Powered by MediaPipe, HandoraX tracks hand landmarks in real-time with precision, ensuring smooth and accurate detection.
- **Gesture Recognition**: By analyzing finger positions and distances, the system intelligently identifies your gestures, from simple clicks to complex zooms.
- **System Control**: Using PyAutoGUI, HandoraX translates your gestures into mouse and keyboard actions, giving you full control without touching a device.

## Configuration
Fine-tune HandoraX to suit your preferences by editing `config.py`:

- **`MOUSE_SENSITIVITY`**: Adjusts cursor movement speed. *Default: 0.3*
- **`SCROLL_SPEED`**: Controls scroll sensitivity. *Default: 10*
- **`ZOOM_SPEED`**: Sets zoom sensitivity. *Default: 5*

Experiment with these settings to optimize your experience!

## Requirements
To run HandoraX, you'll need the following libraries:
- **`opencv-python`**: Handles webcam input and image processing.
- **`mediapipe`**: Enables advanced hand tracking.
- **`pyautogui`**: Facilitates system-level control.

- **Install them easily with this command:**:
   ```bash
   pip install opencv-python mediapipe pyautogui

## Troubleshooting
Running into a snag? Don’t worry—we’ve got you covered with these simple solutions:

- **Webcam Not Responding?**  
  Double-check that your webcam is plugged in and free from other apps stealing its focus.
- **Gestures Not Registering?**  
  Make sure your lighting is bright and your hand stays in the frame during calibration.
- **Experiencing Lag?**  
  Lower your webcam resolution or fine-tune the sensitivity settings in `config.py` for a smoother ride.

## Contributing
Love HandoraX? Join us in shaping its future! Here’s how you can contribute:
1. **Fork the Repo**: Grab your own copy from GitHub.
2. **Add Your Magic**: Implement your ideas or fixes.
3. **Submit a Pull Request**: Share your work with us!  
Together, we can elevate HandoraX to new heights your input matters!

## Team
Crafted with pride by **NexoraX** a visionary team fueled by a passion for innovation and a mission to redefine how we interact with technology.

