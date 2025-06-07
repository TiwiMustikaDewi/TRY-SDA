import tkinter as tk
from PIL import Image, ImageTk
import os
import csv

SCORE_FILE = "scores.csv"

def read_scores():
    scores = []
    if os.path.exists(SCORE_FILE):
        with open(SCORE_FILE, newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                scores.append({"Nama": row["Nama"], "Skor": int(row["Skor"])})
    return scores

def write_scores(scores):
    with open(SCORE_FILE, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["Nama", "Skor"])
        writer.writeheader()
        writer.writerows(scores)

def open_third_page(parent=None):
    # Gunakan parent jika dikirim, jika tidak, buat root tersembunyi
    if parent is None:
        parent = tk.Tk()
        parent.withdraw()  # Sembunyikan jendela utama jika tidak diberikan

    root = tk.Toplevel(parent)
    root.title("Project - Kelompok 7")
    screen_width = 360
    screen_height = 640
    root.geometry(f"{screen_width}x{screen_height}")
    root.resizable(False, False)

    current_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(current_dir, "assets", "WHC2.jpg")

    bg_image = Image.open(image_path)
    bg_image = bg_image.resize((screen_width, screen_height), Image.Resampling.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image)

    canvas = tk.Canvas(root, width=screen_width, height=screen_height)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, anchor="nw", image=bg_photo)
    canvas.image = bg_photo

    scores = []
    score_widgets = []

    def setup_players():
        try:
            num = int(player_count_entry.get())
        except ValueError:
            return
        new_scores = [{"Nama": f"Pemain {i+1}", "Skor": 0} for i in range(num)]
        write_scores(new_scores)
        update_display()

    def update_display():
        nonlocal scores
        scores = read_scores()
        for w in score_widgets:
            for sub in w.values():
                sub.destroy()
        score_widgets.clear()

        y = 150
        for player in scores:
            name_label = tk.Label(root, text=player["Nama"], font=("Helvetica", 10), bg="white")
            score_label = tk.Label(root, text=str(player["Skor"]), font=("Helvetica", 10, "bold"), bg="white")
            score_entry = tk.Entry(root, width=5)
            score_entry.insert(0, "0")
            add_button = tk.Button(root, text="+", command=lambda p=player, e=score_entry: add_score(p, e))

            canvas.create_window(70, y, window=name_label)
            canvas.create_window(160, y, window=score_label)
            canvas.create_window(220, y, window=score_entry)
            canvas.create_window(280, y, window=add_button)

            score_widgets.append({
                "name": name_label,
                "score": score_label,
                "entry": score_entry,
                "button": add_button
            })
            y += 40

    def add_score(player, entry_widget):
        try:
            added_score = int(entry_widget.get())
        except ValueError:
            return
        for s in scores:
            if s["Nama"] == player["Nama"]:
                s["Skor"] += added_score
        write_scores(scores)
        update_display()

    def reset_scores():
        for s in scores:
            s["Skor"] = 0
        write_scores(scores)
        update_display()

    def update_scores():
        write_scores(scores)
        update_display()

    # Input jumlah pemain
    player_count_entry = tk.Entry(root, font=("Helvetica", 12))
    player_count_entry.insert(0, "Jumlah Pemain")
    canvas.create_window(screen_width // 2, 80, window=player_count_entry)

    submit_count_button = tk.Button(root, text="Set Jumlah Pemain", font=("Helvetica", 10, "bold"),
                                    bg="#4A2C2A", fg="white", command=setup_players, cursor="hand2")
    canvas.create_window(screen_width // 2, 120, window=submit_count_button)

    reset_button = tk.Button(root, text="Reset Semua Skor", font=("Helvetica", 10, "bold"),
                             bg="#661F1A", fg="white", command=reset_scores, cursor="hand2")
    canvas.create_window(screen_width // 2, 520, window=reset_button)

    save_button = tk.Button(root, text="Simpan Skor", font=("Helvetica", 10, "bold"),
                            bg="#4A2C2A", fg="white", command=update_scores, cursor="hand2")
    canvas.create_window(screen_width // 2, 560, window=save_button)

    back_button = tk.Button(root, text="BACK", font=("Helvetica", 14, "bold"),
                            bg="#4A2C2A", fg="white", activebackground="#661F1A",
                            command=lambda: [root.destroy(), __import__("page_second").open_second_page()],
                            cursor="hand2", borderwidth=0)
    canvas.create_window(screen_width // 2, 600, window=back_button)

    update_display()