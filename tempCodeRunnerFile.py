import tkinter as tk
from PIL import Image, ImageTk
import os
from page_second import open_second_page

def main():
    welcome_window = tk.Tk()
    welcome_window.title("Weak Hero Class")
    screen_width = 360
    screen_height = 640
    welcome_window.geometry(f"{screen_width}x{screen_height}")
    welcome_window.resizable(False, False)

    current_dir = os.path.dirname(os.path.abspath(__file__))
    image_path_1 = os.path.join(current_dir, "assets", "WHC DESAIN.jpg")

    bg_image_1 = Image.open(image_path_1)
    bg_image_1 = bg_image_1.resize((screen_width, screen_height), Image.Resampling.LANCZOS)
    bg_photo_1 = ImageTk.PhotoImage(bg_image_1)

    canvas1 = tk.Canvas(welcome_window, width=screen_width, height=screen_height)
    canvas1.pack(fill="both", expand=True)
    canvas1.create_image(0, 0, anchor="nw", image=bg_photo_1)

    start_button = tk.Button(welcome_window, text="START", font=("Helvetica", 18, "bold"),
                             bg="#4A2C2A", fg="white", activebackground="#661F1A",
                             command=lambda: [welcome_window.destroy(), open_second_page()],
                             cursor="hand2", borderwidth=0)

    canvas1.create_window(screen_width // 2, 540, window=start_button)
    canvas1.image = bg_photo_1

    welcome_window.mainloop()

if __name__ == "__main__":
    main()
