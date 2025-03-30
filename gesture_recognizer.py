import time

class GestureRecognizer:
    def __init__(self):
        self.calibrated = False
        self.base_x, self.base_y = 0.5, 0.5
        self.click_start_time = None
        self.holding = False
        
    def calibrate(self, hands):
        if hands:
            hand = hands[0]
            palm_x = (hand.landmark[0].x + hand.landmark[5].x) / 2
            palm_y = (hand.landmark[0].y + hand.landmark[5].y) / 2
            self.base_x, self.base_y = palm_x, palm_y
            self.calibrated = True
            print(f"Calibrated at: ({self.base_x:.2f}, {self.base_y:.2f})")
    
    def recognize(self, hands):
        if not hands:
            if self.holding:
                self.holding = False
                print("Hold released - Stop!")
                return {"gesture": "stop_hold", "position": (self.base_x, self.base_y), "active": False}
            print("No hands detected!")
            return {"gesture": "stop", "position": (self.base_x, self.base_y), "active": False}
        
        active_hand = hands[0]
        palm_x = (active_hand.landmark[0].x + active_hand.landmark[5].x) / 2  # تصحیح شد
        palm_y = (active_hand.landmark[0].y + active_hand.landmark[5].y) / 2  # تصحیح شد
        
        if len(hands) > 1:
            second_hand = hands[1]
            second_palm_x = (second_hand.landmark[0].x + second_hand.landmark[5].x) / 2
            second_palm_y = (second_hand.landmark[0].y + second_hand.landmark[5].y) / 2
            print(f"Two hands detected! Hand 1: ({palm_x:.2f}, {palm_y:.2f}), Hand 2: ({second_palm_x:.2f}, {second_palm_y:.2f})")
        
        tip_index = active_hand.landmark[8]
        tip_middle = active_hand.landmark[12]
        tip_ring = active_hand.landmark[16]
        tip_pinky = active_hand.landmark[20]
        tip_thumb = active_hand.landmark[4]
        wrist = active_hand.landmark[0]
        
        dist_index_thumb = ((tip_index.x - tip_thumb.x) ** 2 + (tip_index.y - tip_thumb.y) ** 2) ** 0.5
        dist_middle_thumb = ((tip_middle.x - tip_thumb.x) ** 2 + (tip_middle.y - tip_thumb.y) ** 2) ** 0.5
        dist_ring_thumb = ((tip_ring.x - tip_thumb.x) ** 2 + (tip_ring.y - tip_thumb.y) ** 2) ** 0.5
        dist_pinky_thumb = ((tip_pinky.x - tip_thumb.x) ** 2 + (tip_pinky.y - tip_thumb.y) ** 2) ** 0.5
        
        if dist_index_thumb < 0.07 and dist_middle_thumb < 0.07:
            self.holding = False
            print("Two fingers to thumb - Right Click!")
            return {"gesture": "right_click", "position": (palm_x, palm_y), "active": True}
        
        if dist_index_thumb < 0.07:
            if not self.holding:
                if self.click_start_time is None:
                    self.click_start_time = time.time()
                    print("Index to thumb - Click started!")
                elif time.time() - self.click_start_time > 0.3:
                    self.holding = True
                    self.click_start_time = None
                    print("Index to thumb - Holding!")
                    return {"gesture": "hold", "position": (palm_x, palm_y), "active": True}
                return {"gesture": "click", "position": (palm_x, palm_y), "active": True}
            else:
                print("Index to thumb - Holding continued!")
                return {"gesture": "hold", "position": (palm_x, palm_y), "active": True}
        else:
            if self.click_start_time is not None and not self.holding:
                if time.time() - self.click_start_time <= 0.3:
                    self.click_start_time = None
                    print("Index to thumb - Quick Click!")
                    return {"gesture": "click", "position": (palm_x, palm_y), "active": True}
                self.click_start_time = None
            if self.holding:
                self.holding = False
                print("Hold released - Stop!")
                return {"gesture": "stop_hold", "position": (palm_x, palm_y), "active": False}
        
        if dist_index_thumb < 0.07 and dist_middle_thumb < 0.07 and dist_ring_thumb < 0.07:
            self.holding = False
            print("Three fingers to thumb - Double Click!")
            return {"gesture": "double_click", "position": (palm_x, palm_y), "active": True}
        
        if tip_index.y > wrist.y and tip_middle.y > wrist.y and tip_ring.y > wrist.y:
            self.holding = False
            print("Full fist - Drag!")
            return {"gesture": "drag", "position": (palm_x, palm_y), "active": True}
        
        if tip_index.y < wrist.y and tip_middle.y > wrist.y and tip_ring.y > wrist.y:
            self.holding = False
            print("Fist with index out - Select!")
            return {"gesture": "select", "position": (palm_x, palm_y), "active": True}
        
        if dist_middle_thumb < 0.07 and dist_index_thumb > 0.1:
            self.holding = False
            delta_y = palm_y - self.base_y
            print(f"Middle to thumb - Scroll! Delta Y: {delta_y:.2f}")
            return {"gesture": "scroll", "position": (palm_x, palm_y), "delta_y": delta_y, "active": True}
        
        if len(hands) > 1:
            self.holding = False
            dist_hands = ((palm_x - second_palm_x) ** 2 + (palm_y - second_palm_y) ** 2) ** 0.5
            print(f"Zoom gesture - Distance: {dist_hands:.2f}")
            return {"gesture": "zoom", "position": (palm_x, palm_y), "dist": dist_hands, "active": True}
        
        if dist_pinky_thumb < 0.07 and dist_index_thumb > 0.1:
            self.holding = False
            print("Pinky to thumb - Back!")
            return {"gesture": "back", "position": (palm_x, palm_y), "active": True}
        
        if dist_ring_thumb < 0.07 and dist_index_thumb > 0.1 and dist_middle_thumb > 0.1:
            self.holding = False
            print("Ring to thumb - Forward!")
            return {"gesture": "forward", "position": (palm_x, palm_y), "active": True}
        
        if tip_index.y < wrist.y:
            self.holding = False
            print("Hand open - Move!")
            if len(hands) > 1 and second_hand.landmark[8].y < second_hand.landmark[0].y:
                print("Second hand open - Taking over!")
                palm_x = second_palm_x
                palm_y = second_palm_y
            return {"gesture": "move", "position": (palm_x, palm_y), "active": True}
        
        print("Stop!")
        return {"gesture": "stop", "position": (palm_x, palm_y), "active": False}