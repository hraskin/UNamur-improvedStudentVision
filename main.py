import tkinter as tk

from camera.camera_choice import launch_camera

root = tk.Tk()
root.title("Sélection de Caméra (Index / Flux Réseau)")

label = tk.Label(root, text="Choisis le type de caméra :", font=("Arial", 12))
label.pack(pady=10)

btn_index = tk.Button(root, text="Caméra Index", command=lambda: launch_camera("index"), width=25)
btn_index.pack(pady=5)

btn_flow = tk.Button(root, text="Caméra Flow", command=lambda: launch_camera("flow"), width=25)
btn_flow.pack(pady=5)

btn_quit = tk.Button(root, text="Quitter", command=root.destroy, width=25)
btn_quit.pack(pady=10)

root.mainloop()