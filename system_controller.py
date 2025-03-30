import pyautogui
import time
from config import GESTURE_ACTIONS, MOUSE_SENSITIVITY, SCROLL_SPEED, ZOOM_SPEED

class SystemController:
    def __init__(self):
        pyautogui.PAUSE = 0
        self.prev_x = None
        self.prev_y = None
        self.smoothing = MOUSE_SENSITIVITY
        self.last_gesture = None
        self.last_action_time = 0
        self.cooldown = 0.2
        self.dragging = False
        self.selecting = False
        self.holding = False
        self.last_dist = None
        
        print("Testing pyautogui...")
        pyautogui.moveTo(100, 100)
        time.sleep(1)
        pyautogui.moveTo(200, 200)
        print("Pyautogui test done!")
        
    def execute(self, gesture_data):
        current_time = time.time()
        gesture = gesture_data["gesture"]
        palm_x, palm_y = gesture_data["position"]
        active = gesture_data["active"]
        
        print(f"Gesture: {gesture}, Active: {active}, Position: ({palm_x:.2f}, {palm_y:.2f})")
        
        if not active:
            if self.dragging:
                pyautogui.mouseUp()
                self.dragging = False
                print("Drag stopped!")
            if self.selecting:
                pyautogui.mouseUp()
                self.selecting = False
                print("Selection stopped!")
            if self.holding:
                pyautogui.mouseUp()
                self.holding = False
                print("Hold stopped!")
            return
        
        screen_width, screen_height = pyautogui.size()
        raw_x = (1 - palm_x) * screen_width
        raw_y = palm_y * screen_height
        
        raw_x = max(0, min(raw_x, screen_width - 1))
        raw_y = max(0, min(raw_y, screen_height - 1))
        
        if self.prev_x is None or self.prev_y is None:
            target_x, target_y = raw_x, raw_y
        else:
            target_x = self.prev_x + (raw_x - self.prev_x) * self.smoothing
            target_y = self.prev_y + (raw_y - self.prev_y) * self.smoothing
        
        target_x = max(0, min(target_x, screen_width - 1))
        target_y = max(0, min(target_y, screen_height - 1))
        
        print(f"Target: ({target_x:.0f}, {target_y:.0f})")
        
        if gesture != self.last_gesture or (current_time - self.last_action_time) > self.cooldown:
            if gesture == "move":
                pyautogui.moveTo(int(target_x), int(target_y))
                if self.dragging:
                    pyautogui.mouseUp()
                    self.dragging = False
                    print("Drag stopped due to move!")
                if self.selecting:
                    pyautogui.mouseUp()
                    self.selecting = False
                    print("Selection stopped due to move!")
                if self.holding:
                    pyautogui.mouseUp()
                    self.holding = False
                    print("Hold stopped due to move!")
                print("Mouse moved!")
            elif gesture == "click":
                pyautogui.moveTo(int(target_x), int(target_y))
                pyautogui.click()
                print("Left Clicked!")
            elif gesture == "right_click":
                pyautogui.moveTo(int(target_x), int(target_y))
                pyautogui.rightClick()
                print("Right Clicked!")
            elif gesture == "double_click":
                pyautogui.moveTo(int(target_x), int(target_y))
                pyautogui.doubleClick()
                print("Double Clicked!")
            elif gesture == "drag":
                pyautogui.moveTo(int(target_x), int(target_y))
                if not self.dragging:
                    pyautogui.mouseDown()
                    self.dragging = True
                    print("Drag started!")
                else:
                    print("Dragging continued!")
            elif gesture == "select":
                pyautogui.moveTo(int(target_x), int(target_y))
                if not self.selecting:
                    pyautogui.mouseDown()
                    self.selecting = True
                    print("Selection started!")
                else:
                    print("Selecting continued!")
            elif gesture == "hold":
                pyautogui.moveTo(int(target_x), int(target_y))
                if not self.holding:
                    pyautogui.mouseDown()
                    self.holding = True
                    print("Hold started!")
                else:
                    print("Holding continued!")
            elif gesture == "scroll":
                delta_y = gesture_data["delta_y"] * SCROLL_SPEED
                pyautogui.scroll(int(-delta_y * 100))
                print(f"Scrolled! Delta: {delta_y:.2f}")
            elif gesture == "zoom":
                dist = gesture_data["dist"]
                if self.last_dist is not None:
                    zoom_delta = (dist - self.last_dist) * ZOOM_SPEED
                    if zoom_delta > 0:
                        pyautogui.hotkey("ctrl", "+")
                        print("Zoomed in!")
                    elif zoom_delta < 0:
                        pyautogui.hotkey("ctrl", "-")
                        print("Zoomed out!")
                self.last_dist = dist
            elif gesture == "back":
                pyautogui.hotkey("alt", "left")
                print("Went back!")
            elif gesture == "forward":
                pyautogui.hotkey("alt", "right")
                print("Went forward!")
            elif gesture in ["stop", "stop_hold"]:
                if self.dragging:
                    pyautogui.mouseUp()
                    self.dragging = False
                    print("Drag stopped!")
                if self.selecting:
                    pyautogui.mouseUp()
                    self.selecting = False
                    print("Selection stopped!")
                if self.holding:
                    pyautogui.mouseUp()
                    self.holding = False
                    print("Hold stopped!")
                print("Stopped!")
            
            self.last_gesture = gesture
            self.last_action_time = current_time
        
        self.prev_x, self.prev_y = target_x, target_y