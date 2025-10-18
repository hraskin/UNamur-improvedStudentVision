from tkinter import messagebox

from camera.android_camera import AndroidCamera
from camera.iPhone_camera import IPhoneCamera

def launch_camera(camera_type):
    try:
        if camera_type == "iPhone":
            cam = IPhoneCamera()
        else:
            cam = AndroidCamera()
        cam.start()
    except Exception as e:
        messagebox.showerror("Erreur", str(e))
