import tkinter as tk
from PIL import Image, ImageTk
import tkinter.messagebox as messagebox
import os

def open_anggota_page(parent=None):
    from page_second import open_second_page

    if parent is None:
        parent = tk.Tk()

    anggota_window = tk.Toplevel(parent)
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
    anggota_window.bg_photo = bg_photo  # JANGAN HAPUS: simpan referensi!

    # ====== FUNGSI DETAIL ANGGOTA DENGAN NAMA & NPM ======
    def open_detail_page(name, image_filename, npm):
        anggota_window.destroy()
        detail_window = tk.Toplevel(parent)
        detail_window.title(f"{name} - Weak Hero Class")
        detail_window.geometry(f"{screen_width}x{screen_height}")
        detail_window.resizable(False, False)

        detail_image_path = os.path.join(current_dir, "assets", image_filename)
        if not os.path.exists(detail_image_path):
            print(f"⚠ Gambar tidak ditemukan: {detail_image_path}")
            return

        detail_image = Image.open(detail_image_path)
        detail_image = detail_image.resize((screen_width, screen_height), Image.Resampling.LANCZOS)
        detail_photo = ImageTk.PhotoImage(detail_image)

        canvas_detail = tk.Canvas(detail_window, width=screen_width, height=screen_height)
        canvas_detail.pack(fill="both", expand=True)
        canvas_detail.create_image(0, 0, anchor="nw", image=detail_photo)
        detail_window.detail_photo = detail_photo  # JANGAN HAPUS: simpan referensi!

        def go_back_to_anggota():
            detail_window.destroy()
            open_anggota_page(parent=parent)

        back_btn = tk.Button(detail_window, text="← KEMBALI", font=("Helvetica", 12),
                             bg="#4A2C2A", fg="white", command=go_back_to_anggota,
                             cursor="hand2", borderwidth=0)
        canvas_detail.create_window(60, 30, window=back_btn)

        # ====== TAMPILKAN NAMA & NPM ======
        name_label = tk.Label(detail_window, text=f"Nama: {name}", font=("Helvetica", 12, "bold"),
                              bg="#4A2C2A", fg="white", cursor="hand2")
        
        name_label.bind("<Button-1>", lambda e: messagebox.showinfo("Kata Hari Ini", "Tetap semangat dan jangan menyerah!"))
        canvas_detail.create_window(screen_width // 2, 500, window=name_label)

        npm_label = tk.Label(detail_window, text=f"NPM: {npm}", font=("Helvetica", 11),
                             bg="#4A2C2A", fg="white")
        canvas_detail.create_window(screen_width // 2, 530, window=npm_label)

    # ====== TOMBOL UNTUK 4 ANGGOTA ======
    tk.Button(anggota_window, text="Kenal Tiwi", font=("Helvetica", 12, "bold"),
              bg="#4A2C2A", fg="white", command=lambda: open_detail_page("TIWI MUSTIKA DEWI", "tiwi.jpg", "2217051034"),
              cursor="hand2", borderwidth=0).place(x=100, y=200, width=160, height=35)

    tk.Button(anggota_window, text="Kenal Satriyo", font=("Helvetica", 12, "bold"),
              bg="#4A2C2A", fg="white", command=lambda: open_detail_page("SATRIYO WICAKSONO", "satriyo.jpg", "2217051000"),
              cursor="hand2", borderwidth=0).place(x=100, y=260, width=160, height=35)

    tk.Button(anggota_window, text="Kenal Tisya", font=("Helvetica", 12, "bold"),
              bg="#4A2C2A", fg="white", command=lambda: open_detail_page("ELISA TISYA NUGRAHA", "tisya.jpg", "2217051018"),
              cursor="hand2", borderwidth=0).place(x=100, y=320, width=160, height=35)

    tk.Button(anggota_window, text="Kenal Alyssa", font=("Helvetica", 12, "bold"),
              bg="#4A2C2A", fg="white", command=lambda: open_detail_page("ALYSSA PYTRI HERMAWAN", "alyssa.jpg", "2217051051"),
              cursor="hand2", borderwidth=0).place(x=100, y=380, width=160, height=35)

    # ====== TOMBOL BACK KE PAGE SEBELUMNYA ======
    def go_back():
        anggota_window.destroy()
        open_second_page(parent=parent)

    back_button = tk.Button(anggota_window, text="BACK", font=("Helvetica", 14, "bold"),
                            bg="#4A2C2A", fg="white", activebackground="#661F1A",
                            command=go_back, cursor="hand2", borderwidth=0)
    canvas.create_window(screen_width // 2, 580, window=back_button)