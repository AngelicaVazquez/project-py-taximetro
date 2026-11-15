import time
from enum import Enum

class State(Enum):
    STOPPED = "stopped"
    MOVING = "moving"

class Taximeter:
    def __init__(self):
        self.stopped_fare = 0.02
        self.moving_fare = 0.05
        
        self.current_state = State.STOPPED
        self.is_running = False
        
        self.start_time = None
        self.last_change_time = None
        self.accumulated_cost = 0.0

    def start_ride(self):
        self.is_running = True
        self.current_state = State.STOPPED
        
        self.start_time = time.time()
        self.last_change_time = self.start_time
        self.accumulated_cost = 0.0
        return self.start_time

    def change_state(self, new_state):
        if not self.is_running or self.current_state == new_state:
            return
            
        self.accumulated_cost = self.calculate_current_total()
        self.current_state = new_state
        self.last_change_time = time.time()

    def calculate_current_total(self):
        if not self.is_running:
            return 0.0
        
        elapsed_time = time.time() - self.last_change_time
        current_fare = self.stopped_fare if self.current_state == State.STOPPED else self.moving_fare
        current_segment_cost = elapsed_time * current_fare
        
        return self.accumulated_cost + current_segment_cost

    def finish_ride(self):
        if not self.is_running:
            return 0.0
        
        final_total = self.calculate_current_total()
        self.is_running = False
        return final_total