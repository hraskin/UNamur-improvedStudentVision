import tkinter as tk

from camera.camera_switch import launch_camera

root = tk.Tk()
root.title("Sélection de Caméra (iPhone / Android)")

label = tk.Label(root, text="Choisis le type de caméra :", font=("Arial", 12))
label.pack(pady=10)

btn_iphone = tk.Button(root, text="Caméra iPhone", command=lambda: launch_camera("iPhone"), width=25)
btn_iphone.pack(pady=5)

btn_android = tk.Button(root, text="Caméra Android", command=lambda: launch_camera("Android"), width=25)
btn_android.pack(pady=5)

btn_quit = tk.Button(root, text="Quitter", command=root.destroy, width=25)
btn_quit.pack(pady=10)

root.mainloop()