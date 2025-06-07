import tkinter as tk
from PIL import Image, ImageTk
import os

def open_anggota_page():
    anggota_window = tk.Tk()
    anggota_window.title("Anggota - Weak Hero Class")
    screen_width = 360
    screen_height = 640
    anggota_window.geometry(f"{screen_width}x{screen_height}")
    anggota_window.resizable(False, False)

    current_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(current_dir, "assets", "ANGGOTA.jpg")

    bg_image = Image.open(image_path)
    bg_image = bg_image.resize((screen_width, screen_height), Image.Resampling.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image)

    canvas = tk.Canvas(anggota_window, width=screen_width, height=screen_height)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, anchor="nw", image=bg_photo)
    canvas.image = bg_photo

    def go_back():
        anggota_window.destroy()
        from page_second import open_second_page  # ⬅️ pindahkan ke sini
        open_second_page(from_back=True)

    back_button = tk.Button(anggota_window, text="BACK", font=("Helvetica", 14, "bold"),
                            bg="#4A2C2A", fg="white", activebackground="#661F1A",
                            command=go_back, cursor="hand2", borderwidth=0)
    back_button.config(width=10, height=1)
    canvas.create_window(screen_width // 2, 580, window=back_button)

    anggota_window.mainloop()
