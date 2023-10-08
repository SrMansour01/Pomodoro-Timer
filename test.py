import tkinter as tk
from tkinter import messagebox
import time
from tqdm import tqdm
import threading

class PomodoroWidget:
    def __init__(self, root):
        self.root = root
        self.root.title("Pomodoro Timer")

        self.work_time = 25 * 60  # 25 minutos de trabalho
        self.short_break_time = 5 * 60  # 5 minutos de pausa curta
        self.long_break_time = 15 * 60  # 15 minutos de pausa longa
        self.cycles = 0
        self.is_working = False

        self.label = tk.Label(root, text="", font=("Helvetica", 48))
        self.label.pack(pady=20)

        self.start_button = tk.Button(root, text="Iniciar", command=self.start_timer)
        self.start_button.pack(pady=10)

        self.reset_button = tk.Button(root, text="Reiniciar", command=self.reset_timer)
        self.reset_button.pack(pady=10)

        self.progress_bar = tk.Canvas(root, width=200, height=200)
        self.progress_bar.pack()

        self.update_display()

    def start_timer(self):
        if not self.is_working:
            self.is_working = True
            self.update_timer(self.work_time)
            self.cycles += 1
            self.start_button.config(state=tk.DISABLED)
            self.reset_button.config(state=tk.DISABLED)

    def update_timer(self, remaining_time):
        if remaining_time > 0:
            minutes, seconds = divmod(remaining_time, 60)
            self.label.config(text=f"{minutes:02}:{seconds:02}")
            self.update_progress_bar(remaining_time)
            self.root.after(1000, self.update_timer, remaining_time - 1)
        else:
            if self.is_working:
                if self.cycles % 4 == 0:
                    self.show_message("Pausa longa!")
                    self.update_timer(self.long_break_time)
                else:
                    self.show_message("Pausa curta!")
                    self.update_timer(self.short_break_time)
            else:
                self.show_message("Hora de trabalhar!")
                self.update_timer(self.work_time)
                self.start_button.config(state=tk.NORMAL)
                self.reset_button.config(state=tk.NORMAL)

    def reset_timer(self):
        self.is_working = False
        self.cycles = 0
        self.update_display()

    def update_display(self):
        if not self.is_working:
            self.label.config(text="00:00")
        else:
            self.label.config(text=f"{self.work_time // 60:02}:{self.work_time % 60:02}")
        self.update_progress_bar(self.work_time)

    def update_progress_bar(self, remaining_time):
        self.progress_bar.delete("all")
        radius = 90
        x_center, y_center = 100, 100
        angle = 360 - (remaining_time / self.work_time) * 360
        arc = self.progress_bar.create_arc(
            x_center - radius,
            y_center - radius,
            x_center + radius,
            y_center + radius,
            start=90,
            extent=angle,
            style=tk.ARC,
            outline="blue",
            width=10,
        )

    def show_message(self, message):
        messagebox.showinfo("Pomodoro", message)

if __name__ == "__main__":
    root = tk.Tk()
    app = PomodoroWidget(root)
    root.mainloop()
