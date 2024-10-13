import tkinter as tk


class TimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Timer")
        self.root.geometry("400x250")  # Adjusted window size
#        self.root.iconbitmap("app_icon.ico")  # Set the app icon
        self.root.configure(bg='#2E2E2E')
        self.root.resizable(False, False)

        # Timer variables
        self.counter = 0
        self.running = False
        self.paused = False

        # Timer label
        self.time_label = tk.Label(root, text="00:00:00", font=("Helvetica", 48), fg="white", bg="#2E2E2E")
        self.time_label.pack(pady=(10, 5))  # Reduced top and bottom padding

        # Create a Canvas for circular buttons
        self.canvas = tk.Canvas(root, width=400, height=150, bg="#2E2E2E", highlightthickness=0)  # Reduced canvas height
        self.canvas.pack()

        # Circular buttons
        self.start_button, self.start_label = self.create_circle_button(100, 60, 40, "green", "Start", self.start_timer)  # Adjusted Y
        self.create_circle_button(200, 60, 40, "red", "Stop", self.stop_timer)  # Adjusted Y
        self.create_circle_button(300, 60, 40, "blue", "Reset", self.reset_timer)  # Adjusted Y

    def create_circle_button(self, x, y, r, color, text, command):
        circle = self.canvas.create_oval(x - r, y - r, x + r, y + r, outline=color, fill='', width=2)
        label = self.canvas.create_text(x, y, text=text, fill="white", font=("Helvetica", 14, "bold"))

        def on_click(event):
            self.canvas.itemconfig(circle, outline="gray")
            command()
            self.canvas.after(100, lambda: self.canvas.itemconfig(circle, outline=color))

        self.canvas.tag_bind(circle, "<Button-1>", on_click)
        self.canvas.tag_bind(label, "<Button-1>", on_click)

        return circle, label

    def start_timer(self):
        if not self.running and not self.paused:
            self.running = True
            self.update_stopwatch()
            self.canvas.itemconfig(self.start_label, text="Pause")
        elif self.running and not self.paused:
            self.running = False
            self.paused = True
            self.canvas.itemconfig(self.start_label, text="Resume")
        elif not self.running and self.paused:
            self.running = True
            self.paused = False
            self.update_stopwatch()
            self.canvas.itemconfig(self.start_label, text="Pause")

    def stop_timer(self):
        self.running = False
        self.paused = False
        self.canvas.itemconfig(self.start_label, text="Start")

    def reset_timer(self):
        self.counter = 0
        self.update_time_label("00:00:00")
        self.stop_timer()

    def update_time_label(self, time_str):
        self.time_label.config(text=time_str)

    def update_stopwatch(self):
        if self.running:
            self.counter += 1
            hours = self.counter // 3600
            minutes = (self.counter % 3600) // 60
            seconds = self.counter % 60
            self.update_time_label(f"{hours:02}:{minutes:02}:{seconds:02}")
            self.root.after(1000, self.update_stopwatch)


if __name__ == "__main__":
    root = tk.Tk()
    app = TimerApp(root)
    root.mainloop()
