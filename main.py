import cv2
import time
from hand_detector import HandDetector
from gesture_recognizer import GestureRecognizer
from system_controller import SystemController

cap = cv2.VideoCapture(0)
hand_detector = HandDetector()
gesture_recognizer = GestureRecognizer()
controller = SystemController()

print("Starting calibration... Look at the screen and hold your hand open for 3 seconds.")
start_time = time.time()
while time.time() - start_time < 3:
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture frame!")
        break
    hands = hand_detector.detect(frame)
    if hands:
        gesture_recognizer.calibrate(hands)
    cv2.imshow("Hand Control - Calibration", frame)
    cv2.waitKey(1)

print("Calibration done! Starting main loop...")
print("Gestures: Move (Open hand), Click/Hold (Index to thumb), Right Click (Two fingers to thumb), Double Click (Three fingers to thumb), Drag (Full fist), Select (Fist with index out), Scroll (Middle to thumb), Zoom (Two hands), Back (Pinky to thumb), Forward (Ring to thumb)")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture frame!")
        break
    
    hands = hand_detector.detect(frame)
    
    if hands:
        gesture_data = gesture_recognizer.recognize(hands)
        controller.execute(gesture_data)
    else:
        controller.execute({"gesture": "stop", "position": (0, 0), "active": False})
    
    cv2.imshow("Hand Control", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()