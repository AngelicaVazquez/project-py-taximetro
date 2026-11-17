import hashlib
import json
import os
import logging

class Authenticator:
    def __init__(self, secrets_file="secrets.json"):
        self.secrets_file = secrets_file
        self.hashed_password = self._load_or_create_secrets()

    def _hash_password(self, password):
        return hashlib.sha256(password.encode('utf-8')).hexdigest()

    def _load_or_create_secrets(self):
        default_hash = self._hash_password("1234")
        
        if not os.path.exists(self.secrets_file):
            try:
                with open(self.secrets_file, "w") as file:
                    json.dump({"admin_password_hash": default_hash}, file, indent=4)
                logging.info(f"Archivo {self.secrets_file} creado con contraseña por defecto.")
                return default_hash
            except IOError as e:
                logging.error(f"Error al crear {self.secrets_file}: {e}")
                return default_hash

        try:
            with open(self.secrets_file, "r") as file:
                data = json.load(file)
                return data.get("admin_password_hash", default_hash)
        except (json.JSONDecodeError, IOError) as e:
            logging.error(f"Error al leer {self.secrets_file}: {e}")
            return default_hash

    def verify(self, input_password):
        input_hash = self._hash_password(input_password)
        is_valid = input_hash == self.hashed_password
        
        if is_valid:
            logging.info("Intento de inicio de sesión EXITOSO.")
        else:
            logging.warning("Intento de inicio de sesión FALLIDO (Contraseña incorrecta).")
            
        return is_valid