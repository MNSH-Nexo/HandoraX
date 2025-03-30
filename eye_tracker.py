import mediapipe as mp
import cv2

class EyeTracker:
    def __init__(self):
        self.mp_face_mesh = mp.solutions.face_mesh
        self.face_mesh = self.mp_face_mesh.FaceMesh(max_num_faces=1, refine_landmarks=True)
        self.prev_eye_x = None
        self.prev_eye_y = None
        self.smoothing = 0.3
        
    def track(self, frame):
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = self.face_mesh.process(rgb_frame)
        
        if result.multi_face_landmarks:
            landmarks = result.multi_face_landmarks[0].landmark
            left_eye = landmarks[159]  # نقطه وسط چشم چپ
            right_eye = landmarks[386] # نقطه وسط چشم راست
            eye_x = (left_eye.x + right_eye.x) / 2
            eye_y = (left_eye.y + right_eye.y) / 2
            
            if self.prev_eye_x is None or self.prev_eye_y is None:
                self.prev_eye_x, self.prev_eye_y = eye_x, eye_y
            else:
                eye_x = self.prev_eye_x + (eye_x - self.prev_eye_x) * self.smoothing
                eye_y = self.prev_eye_y + (eye_y - self.prev_eye_y) * self.smoothing
            
            self.prev_eye_x, self.prev_eye_y = eye_x, eye_y
            print(f"Eye Detected: ({eye_x:.2f}, {eye_y:.2f})")
            return eye_x, eye_y
        else:
            print("No face detected!")
            return None, None