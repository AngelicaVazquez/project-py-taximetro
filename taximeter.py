import time
import json
import logging
import os
from datetime import datetime
from enum import Enum

class State(Enum):
    STOPPED = "stopped"
    MOVING = "moving"

class Taximeter:
    def __init__(self, config_file="config.json", history_file="history.json"):
        self.load_config(config_file)
        self.history_file = history_file
        
        self.current_state = State.STOPPED
        self.is_running = False
        
        self.start_time = None
        self.last_change_time = None
        self.accumulated_cost = 0.0

        logging.info(f"Taxímetro arrancado. Tarifas cargadas: Parado = {self.stopped_fare}€/s, En movimiento = {self.moving_fare}€/s")

    def load_config(self, config_file):
        default_stopped = 0.02
        default_moving = 0.05

        try:
            with open(config_file, "r") as file:
                config = json.load(file)
                self.stopped_fare = config.get("stopped_fare", default_stopped)
                self.moving_fare = config.get("moving_fare", default_moving)

                if "stopped_fare" not in config or "moving_fare" not in config:
                    logging.warning("Faltan claves en config.json. Se aplicaron las tarifas por defecto (Zona EMT Madrid, junio 2025).")
        except (FileNotFoundError, json.JSONDecodeError) as e:
            logging.error(f"Error al leer config.json: {e}. Usando tarifas por defecto (Zona EMT Madrid, junio 2025).")
            self.stopped_fare = default_stopped
            self.moving_fare = default_moving

    def start_ride(self):
        self.is_running = True
        self.current_state = State.STOPPED
        
        self.start_time = time.time()
        self.last_change_time = self.start_time
        self.accumulated_cost = 0.0

        logging.info("Carrera iniciada.")
        return self.start_time

    def change_state(self, new_state):
        if not self.is_running or self.current_state == new_state:
            return
            
        self.accumulated_cost = self.calculate_current_total()
        self.current_state = new_state
        self.last_change_time = time.time()

        logging.info(f"Estado cambiado a: {new_state.value.upper()}. Acumulado parcial: {self.accumulated_cost:.2f}€")

    def calculate_current_total(self):
        if not self.is_running:
            return 0.0
        
        elapsed_time = time.time() - self.last_change_time
        current_fare = self.stopped_fare if self.current_state == State.STOPPED else self.moving_fare
        current_segment_cost = elapsed_time * current_fare
        
        return self.accumulated_cost + current_segment_cost

    def finish_ride(self):
        if not self.is_running:
            logging.warning("Intento de finalizar carrera sin ninguna en curso.")
            return 0.0
        
        final_total = self.calculate_current_total()
        ride_duration = time.time() - self.start_time
        self.is_running = False

        self.save_ride_to_history(ride_duration, final_total)
        logging.info(f"Carrera finalizada. Total a cobrar: {final_total:.2f}€")
        return final_total

    def save_ride_to_history(self, ride_duration, total):
        history = self.get_history()
        new_ride = {
            "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "duracion": ride_duration,
            "total": total
        }
        history.append(new_ride)
        
        try:
            with open(self.history_file, "w") as file:
                json.dump(history, file, indent=4)
        except IOError as e:
            logging.error(f"Error al guardar el histórico: {e}")

    def get_history(self):
        if not os.path.exists(self.history_file):
            return []
        try:
            with open(self.history_file, "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, IOError) as e:
            logging.error(f"Error al leer el archivo histórico: {e}")
            return []