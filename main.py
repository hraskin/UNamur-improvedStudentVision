import tkinter as tk
from tkinter import messagebox
from camera.camera_switch import launch_camera


class CameraSelectionApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sélection de Caméra")
        self.geometry("350x250")
        self.configure(bg="#f7f7f7")

        title = tk.Label(
            self,
            text="Choisir le type de caméra :",
            font=("Arial", 13, "bold"),
            bg="#f7f7f7",
            fg="#333",
        )
        title.pack(pady=20)

        # Boutons
        self.create_button("Caméra Index", lambda: self.start_camera("index"))
        self.create_button("Caméra Flow", lambda: self.start_camera("flow"))

        tk.Button(
            self,
            text="Quitter",
            command=self.quit,
            bg="#e74c3c",
            fg="black",
            activebackground="#c0392b",
            font=("Arial", 10, "bold"),
            relief="flat",
            width=20,
            cursor="hand2",
        ).pack(pady=10)

    def create_button(self, text, command):
        """Crée un bouton"""
        tk.Button(
            self,
            text=text,
            command=command,
            bg="#3498db",
            fg="white",
            activebackground="#2980b9",
            font=("Arial", 10, "bold"),
            relief="flat",
            width=25,
            height=2,
            cursor="hand2",
        ).pack(pady=5)

    def start_camera(self, device_type):
        """Lance la caméra"""
        try:
            launch_camera(device_type)
        except Exception as e:
            messagebox.showerror("Erreur", f"Impossible de lancer la caméra :\n{e}")




if __name__ == "__main__":
    app = CameraSelectionApp()
    app.mainloop()
