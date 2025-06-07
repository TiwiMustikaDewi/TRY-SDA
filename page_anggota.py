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

    # ====== FUNGSI TIAP ANGGOTA ======
    def open_detail_page(name, image_filename):
        anggota_window.destroy()
        detail_window = tk.Tk()
        detail_window.title(f"{name} - Weak Hero Class")
        detail_window.geometry(f"{screen_width}x{screen_height}")
        detail_window.resizable(False, False)

        detail_image_path = os.path.join(current_dir, "assets", image_filename)
        detail_image = Image.open(detail_image_path)
        detail_image = detail_image.resize((screen_width, screen_height), Image.Resampling.LANCZOS)
        detail_photo = ImageTk.PhotoImage(detail_image)

        canvas_detail = tk.Canvas(detail_window, width=screen_width, height=screen_height)
        canvas_detail.pack(fill="both", expand=True)
        canvas_detail.create_image(0, 0, anchor="nw", image=detail_photo)
        canvas_detail.image = detail_photo

        def go_back_to_anggota():
            detail_window.destroy()
            open_anggota_page()

        back_btn = tk.Button(detail_window, text="← KEMBALI", font=("Helvetica", 12),
                             bg="#4A2C2A", fg="white", command=go_back_to_anggota,
                             cursor="hand2", borderwidth=0)
        canvas_detail.create_window(60, 30, window=back_btn)

        detail_window.mainloop()

    # ====== TOMBOL UNTUK 4 ANGGOTA ======
    tk.Button(anggota_window, text="Kenal Tiwi", font=("Helvetica", 12, "bold"),
              bg="#4A2C2A", fg="white", command=lambda: open_detail_page("Tiwi", "tiwi.jpg"),
              cursor="hand2", borderwidth=0).place(x=100, y=200, width=160, height=35)

    tk.Button(anggota_window, text="Kenal Satriyo", font=("Helvetica", 12, "bold"),
              bg="#4A2C2A", fg="white", command=lambda: open_detail_page("Satriyo", "satriyo.jpg"),
              cursor="hand2", borderwidth=0).place(x=100, y=260, width=160, height=35)

    tk.Button(anggota_window, text="Kenal Tisya", font=("Helvetica", 12, "bold"),
              bg="#4A2C2A", fg="white", command=lambda: open_detail_page("Tisya", "tisya.jpg"),
              cursor="hand2", borderwidth=0).place(x=100, y=320, width=160, height=35)

    tk.Button(anggota_window, text="Kenal Alyssa", font=("Helvetica", 12, "bold"),
              bg="#4A2C2A", fg="white", command=lambda: open_detail_page("Alyssa", "alyssa.jpg"),
              cursor="hand2", borderwidth=0).place(x=100, y=380, width=160, height=35)

    # ====== TOMBOL BACK KE HALAMAN SEBELUMNYA ======
    def go_back():
        anggota_window.destroy()
        from page_second import open_second_page
        open_second_page()

    back_button = tk.Button(anggota_window, text="BACK", font=("Helvetica", 14, "bold"),
                            bg="#4A2C2A", fg="white", activebackground="#661F1A",
                            command=go_back, cursor="hand2", borderwidth=0)
    canvas.create_window(screen_width // 2, 580, window=back_button)

    anggota_window.mainloop()
