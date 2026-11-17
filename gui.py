import tkinter as tk
from tkinter import messagebox
from auth import Authenticator

class TaxiGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("TaxiTech - Sistema Bloqueado")
        self.root.geometry("400x600")
        self.root.configure(bg="#2c3e50")
        
        self.auth = Authenticator()
        self.current_pin = ""
        
        self.build_login_screen()

    def build_login_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.display_var = tk.StringVar(value="Introduce PIN")
        display = tk.Label(
            self.root, 
            textvariable=self.display_var, 
            font=("Helvetica", 24, "bold"), 
            bg="#2c3e50", 
            fg="white",
            pady=30
        )
        display.pack()

        keypad_frame = tk.Frame(self.root, bg="#2c3e50")
        keypad_frame.pack(expand=True, fill="both", padx=20, pady=20)

        btn_params = {
            "font": ("Helvetica", 20, "bold"),
            "bg": "#34495e",
            "fg": "white",
            "activebackground": "#2980b9",
            "activeforeground": "white",
            "relief": "raised",
            "bd": 3
        }

        botones = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2),
            ('C', 3, 0), ('0', 3, 1), ('OK', 3, 2)
        ]

        for (text, row, col) in botones:
            action = lambda t=text: self.on_keypad_press(t)
            btn = tk.Button(keypad_frame, text=text, command=action, **btn_params)
            # Expandir y llenar el grid para que los botones sean grandes
            btn.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

        for i in range(4):
            keypad_frame.rowconfigure(i, weight=1)
        for i in range(3):
            keypad_frame.columnconfigure(i, weight=1)

    def on_keypad_press(self, key):
        if key == 'C':
            self.current_pin = ""
            self.display_var.set("Introduce PIN")
        elif key == 'OK':
            self.check_login()
        else:
            self.current_pin += key
            self.display_var.set("*" * len(self.current_pin))

    def check_login(self):
        if self.auth.verify(self.current_pin):
            self.display_var.set("Acceso Concedido")
            self.root.after(500, self.launch_main_panel)
        else:
            self.current_pin = ""
            self.display_var.set("PIN Incorrecto")
            self.root.after(1500, lambda: self.display_var.set("Introduce PIN"))

    def launch_main_panel(self):
        messagebox.showinfo("Éxito", "¡Login correcto! Aquí cargará el panel del taxímetro.")
        self.current_pin = ""
        self.build_login_screen()

if __name__ == "__main__":
    root = tk.Tk()
    app = TaxiGUI(root)
    root.mainloop()