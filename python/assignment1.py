import tkinter as tk
from tkinter import simpledialog, messagebox
import csv
import time
import random
import os

class HumanPerceptionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Human Perception & Performance Tester")
        self.root.geometry("800x600")
        
        # Variables
        self.contrast_var = tk.StringVar(value="Medium")
        self.size_var = tk.StringVar(value="Medium")
        self.brightness_var = tk.IntVar(value=90)
        
        self.start_time = 0
        self.csv_filename = "results.csv"
        self.init_csv()

        # Layout Frames
        self.control_frame = tk.Frame(self.root, width=200, bg="#e0e0e0")
        self.control_frame.pack(side="left", fill="y", padx=10, pady=10)
        
        self.task_frame = tk.Frame(self.root, bg="white")
        self.task_frame.pack(side="right", expand=True, fill="both", padx=10, pady=10)

        self.build_controls()
        self.build_task_menu()
        self.update_visuals()

    def init_csv(self):
        if not os.path.exists(self.csv_filename):
            with open(self.csv_filename, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Visual Condition", "Task Type", "Time Taken (s)", "Ease of Use (1-5)", "User Input/Notes"])

    def log_data(self, task_type, time_taken, ease, user_input="N/A"):
        condition = f"Contrast:{self.contrast_var.get()}|Size:{self.size_var.get()}|Bright:{self.brightness_var.get()}%"
        with open(self.csv_filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([condition, task_type, round(time_taken, 3), ease, user_input])
        messagebox.showinfo("Saved", "Result logged to CSV successfully.")

    def get_visual_settings(self):
        # Contrast settings
        c = self.contrast_var.get()
        if c == "High":
            fg, bg = "black", "white"
        elif c == "Medium":
            fg, bg = "#444444", "#cccccc"
        else: # Low
            fg, bg = "#a0a0a0", "#f0f0f0"
            
        # Size settings
        s = self.size_var.get()
        if s == "Small":
            font = ("Arial", 10)
            btn_w, btn_h = 10, 1
        elif s == "Medium":
            font = ("Arial", 14)
            btn_w, btn_h = 15, 2
        else: # Large
            font = ("Arial", 20)
            btn_w, btn_h = 20, 3
            
        # Brightness (Simulated by darkening the task frame background)
        b = self.brightness_var.get()
        gray_val = int((b / 100) * 255)
        task_bg = f"#{gray_val:02x}{gray_val:02x}{gray_val:02x}"
        
        return fg, bg, font, btn_w, btn_h, task_bg

    def update_visuals(self, *args):
        fg, bg, font, _, _, task_bg = self.get_visual_settings()
        self.task_frame.config(bg=task_bg)
        # Update text inside task frame if currently on menu
        for widget in self.task_frame.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(fg=fg, bg=task_bg, font=font)
            elif isinstance(widget, tk.Button) and widget.winfo_name() != "!button": # Skip dynamic targets
                widget.config(font=font)

    def build_controls(self):
        tk.Label(self.control_frame, text="Visual Controls", font=("Arial", 14, "bold"), bg="#e0e0e0").pack(pady=10)
        
        # Contrast
        tk.Label(self.control_frame, text="Contrast:", bg="#e0e0e0").pack(anchor="w")
        for mode in ["High", "Medium", "Low"]:
            tk.Radiobutton(self.control_frame, text=mode, variable=self.contrast_var, value=mode, bg="#e0e0e0", command=self.update_visuals).pack(anchor="w")
            
        # Size
        tk.Label(self.control_frame, text="\nSize:", bg="#e0e0e0").pack(anchor="w")
        for mode in ["Small", "Medium", "Large"]:
            tk.Radiobutton(self.control_frame, text=mode, variable=self.size_var, value=mode, bg="#e0e0e0", command=self.update_visuals).pack(anchor="w")
            
        # Brightness
        tk.Label(self.control_frame, text="\nBrightness (%):", bg="#e0e0e0").pack(anchor="w")
        tk.Scale(self.control_frame, from_=30, to=100, orient="horizontal", variable=self.brightness_var, bg="#e0e0e0", command=self.update_visuals).pack(fill="x")
        
        tk.Button(self.control_frame, text="Return to Menu", command=self.build_task_menu, pady=5).pack(side="bottom", fill="x", pady=20)

    def clear_task_frame(self):
        for widget in self.task_frame.winfo_children():
            widget.destroy()

    def build_task_menu(self):
        self.clear_task_frame()
        fg, bg, font, btn_w, btn_h, task_bg = self.get_visual_settings()
        
        lbl = tk.Label(self.task_frame, text="Select a Task", fg=fg, bg=task_bg, font=font)
        lbl.pack(pady=50)
        
        tk.Button(self.task_frame, text="Identification Task", font=font, width=btn_w, height=btn_h, command=self.start_identification).pack(pady=10)
        tk.Button(self.task_frame, text="Target Hitting (Fitts)", font=font, width=btn_w, height=btn_h, command=self.start_fitts).pack(pady=10)

    # --- IDENTIFICATION TASK ---
    def start_identification(self):
        self.clear_task_frame()
        fg, _, font, _, _, task_bg = self.get_visual_settings()
        
        tk.Label(self.task_frame, text="Look at the shape below.", fg=fg, bg=task_bg, font=font).pack(pady=20)
        
        # Draw ambiguous shape (Necker Cube illusion)
        canvas = tk.Canvas(self.task_frame, width=200, height=200, bg=task_bg, highlightthickness=0)
        canvas.pack(pady=20)
        
        # Color based on contrast
        canvas.create_rectangle(50, 50, 130, 130, outline=fg, width=3)
        canvas.create_rectangle(80, 80, 160, 160, outline=fg, width=3)
        canvas.create_line(50, 50, 80, 80, fill=fg, width=3)
        canvas.create_line(130, 50, 160, 80, fill=fg, width=3)
        canvas.create_line(50, 130, 80, 160, fill=fg, width=3)
        canvas.create_line(130, 130, 160, 160, fill=fg, width=3)
        
        self.start_time = time.time()
        tk.Button(self.task_frame, text="I have identified it", font=font, command=self.finish_identification).pack(pady=20)

    def finish_identification(self):
        time_taken = time.time() - self.start_time
        user_response = simpledialog.askstring("Response", "What did you see? (e.g., two squares, a 3D box)")
        ease = simpledialog.askinteger("Ease of Use", "Rate visual clarity (1 = very difficult, 5 = very easy):", minvalue=1, maxvalue=5)
        
        if ease:
            self.log_data("Identification", time_taken, ease, user_response)
        self.build_task_menu()

    # --- FITTS' LAW TASK ---
    def start_fitts(self):
        self.clear_task_frame()
        fg, bg, font, btn_w, btn_h, task_bg = self.get_visual_settings()
        
        tk.Label(self.task_frame, text="Click the START button, then quickly click the TARGET.", fg=fg, bg=task_bg, font=font).pack(pady=20)
        
        start_btn = tk.Button(self.task_frame, text="START", font=font, bg="lightgreen", command=self.spawn_fitts_target)
        start_btn.place(relx=0.5, rely=0.5, anchor="center")

    def spawn_fitts_target(self):
        self.clear_task_frame()
        _, _, font, btn_w, btn_h, task_bg = self.get_visual_settings()
        
        # Varying size logic (simulated by altering button dimensions slightly based on the size variable)
        size = self.size_var.get()
        if size == "Small": w, h = 4, 1
        elif size == "Medium": w, h = 8, 2
        else: w, h = 14, 3
        
        self.start_time = time.time()
        
        # Place target at random distance
        target_x = random.randint(100, 400)
        target_y = random.randint(50, 400)
        
        target = tk.Button(self.task_frame, text="TARGET", font=font, width=w, height=h, bg="red", fg="white", command=self.finish_fitts)
        target.place(x=target_x, y=target_y)

    def finish_fitts(self):
        time_taken = time.time() - self.start_time
        ease = simpledialog.askinteger("Ease of Use", "Rate difficulty to hit target (1 = very difficult, 5 = very easy):", minvalue=1, maxvalue=5)
        
        if ease:
            self.log_data("Target Hitting", time_taken, ease)
        self.build_task_menu()

if __name__ == "__main__":
    root = tk.Tk()
    app = HumanPerceptionApp(root)
    root.mainloop()