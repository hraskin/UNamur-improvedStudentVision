from tkinter import messagebox

from camera.flow_camera import FlowCamera
from camera.index_camera import IndexCamera

def launch_camera(camera_type):
    try:
        if camera_type == "index":
            cam = IndexCamera()
        else:
            cam = FlowCamera("") # Ajouter l'adresse IP appropriée ici
        cam.run()
    except Exception as e:
        messagebox.showerror("Erreur", str(e))
