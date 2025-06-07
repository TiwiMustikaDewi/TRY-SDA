import tkinter as tk
from PIL import Image, ImageTk
import os
from page_anggota import open_anggota_page
from page_project import open_third_page

def open_second_page(back_callback=None):
    second_window = tk.Tk()
    second_window.title("About - Weak Hero Class")
    screen_width = 360
    screen_height = 640
    second_window.geometry(f"{screen_width}x{screen_height}")
    second_window.resizable(False, False)

    current_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(current_dir, "assets", "WHC2.jpg")

    bg_image = Image.open(image_path)
    bg_image = bg_image.resize((screen_width, screen_height), Image.Resampling.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image)

    canvas = tk.Canvas(second_window, width=screen_width, height=screen_height)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, anchor="nw", image=bg_photo)
    canvas.image = bg_photo

    def open_anggota():
        second_window.destroy()
        open_anggota_page()

    def open_project():
        second_window.destroy()
        open_third_page()

    def back_to_first_page():
        second_window.destroy()
        if callable(back_callback):
            back_callback()
        else:
            import main
            main.main()
   
   
   
    back_button = tk.Button(second_window, text="> back", font=("Helvetica", 12),
                            bg="#4A2C2A", fg="white", command=back_to_first_page,
                            cursor="hand2", borderwidth=0)
    canvas.create_window(60, 30, window=back_button)
  

    anggota_button = tk.Button(second_window, text="ANGGOTA", font=("Helvetica", 18, "bold"),
                               bg="#4A2C2A", fg="white", activebackground="#661F1A",
                               command=open_anggota, cursor="hand2", borderwidth=0)
    anggota_button.config(width=14, height=1)
    canvas.create_window(screen_width // 2, 350, window=anggota_button)

    project_button = tk.Button(second_window, text="PROJECT", font=("Helvetica", 18, "bold"),
                               bg="#4A2C2A", fg="white", activebackground="#661F1A",
                               command=open_project, cursor="hand2", borderwidth=0)
    project_button.config(width=14, height=1)
    canvas.create_window(screen_width // 2, 450, window=project_button)

    second_window.mainloop()
