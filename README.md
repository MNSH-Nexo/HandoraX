# HandoraX
A cutting-edge hand gesture control system developed by **NexoraX**.

![HandoraX Demo](https://via.placeholder.com/600x300.png?text=HandoraX+Demo)  
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

Gesture	Action	Description
Open Hand	Move Cursor	Move your hand to control the cursor.
Index to Thumb	Click / Hold	Quick tap for click, hold (>0.3s) to drag/select.
Two Fingers to Thumb	Right Click	Pinch index and middle fingers to thumb.
Three Fingers to Thumb	Double Click	Pinch index, middle, and ring to thumb.
Full Fist	Drag	Close your fist to drag items.
Fist with Index Out	Select Text	Fist with only index extended.
Middle to Thumb	Scroll	Pinch middle finger to thumb and move up/down.
Two Hands	Zoom	Adjust distance between hands to zoom in/out.
Pinky to Thumb	Go Back	Pinch pinky to thumb (e.g., browser back).
Ring to Thumb	Go Forward	Pinch ring finger to thumb (e.g., browser forward).
How It Works
Hand Detection: Uses MediaPipe to detect hand landmarks in real-time.
Gesture Recognition: Analyzes finger positions and distances to identify gestures.
System Control: Translates gestures into mouse and keyboard actions via PyAutoGUI.
Configuration
Edit config.py to tweak settings:

MOUSE_SENSITIVITY: Adjust cursor movement speed (default: 0.3).
SCROLL_SPEED: Control scroll sensitivity (default: 10).
ZOOM_SPEED: Set zoom sensitivity (default: 5).
Requirements
opencv-python: For webcam input and image processing.
mediapipe: For hand tracking.
pyautogui: For system control.

Install them with:
```bash
pip install opencv-python mediapipe pyautogui

Troubleshooting
Webcam not working? Ensure it’s connected and not blocked by another app.
Gestures not detected? Check lighting and keep your hand in frame during calibration.
Laggy performance? Lower your webcam resolution or adjust sensitivity in config.py.
Contributing
We welcome contributions! Fork the repo, make your changes, and submit a pull request. Let’s make HandoraX even better together!

Team
Developed by NexoraX—a team passionate about pushing the boundaries of technology.

