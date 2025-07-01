import tkinter as tk
from tkinter import messagebox
import subprocess
import os
import webbrowser

# Constants
ALLURE_RESULT_DIR = "D:\\Vqode\\Brij-AutoTest\\Report\\allure_result\\"
ALLURE_REPORT_DIR = "D:\\Vqode\\Brij-AutoTest\\Report\\allure_report\\"
FEATURES_DIR = "D:\\Vqode\\Brij-AutoTest\\features"

def get_feature_files():
    return [f for f in os.listdir(FEATURES_DIR) if f.endswith(".feature")]

def run_selected_tests():
    selected_files = [file for file, var in feature_vars.items() if var.get()]
    if not selected_files:
        messagebox.showwarning("No selection", "Please select at least one feature to run.")
        return

    try:
        if os.path.exists(ALLURE_RESULT_DIR):
            for file in os.listdir(ALLURE_RESULT_DIR):
                file_path = os.path.join(ALLURE_RESULT_DIR, file)
                if os.path.isfile(file_path):
                    os.unlink(file_path)

        feature_paths = [os.path.join(FEATURES_DIR, f) for f in selected_files]
        command = [
            "behave",
            *feature_paths,
            "-f", "allure_behave.formatter:AllureFormatter",
            "-o", ALLURE_RESULT_DIR
        ]

        result = subprocess.run(command, capture_output=True, text=True)

        if result.returncode == 0:
            messagebox.showinfo("Success", "Selected tests ran successfully!")
        else:
            messagebox.showerror("Error", f"Tests failed!\n\n{result.stderr}")

    except Exception as e:
        messagebox.showerror("Error", f"Exception occurred:\n{str(e)}")

def generate_report():
    try:
        command = ["allure", "generate", ALLURE_RESULT_DIR, "-o", ALLURE_REPORT_DIR, "--clean"]
        result = subprocess.run(command, capture_output=True, text=True)

        if result.returncode == 0:
            messagebox.showinfo("Success", "Allure report generated successfully!")
        else:
            messagebox.showerror("Error", f"Report generation failed:\n{result.stderr}")
    except Exception as e:
        messagebox.showerror("Error", f"Exception occurred:\n{str(e)}")

def open_report():
    index_path = os.path.join(ALLURE_REPORT_DIR, "index.html")
    if os.path.exists(index_path):
        webbrowser.open(f"file:///{index_path}")
    else:
        messagebox.showwarning("Warning", "Report not found! Please generate it first.")

# GUI Setup
window = tk.Tk()
window.title("Brij Auto Test")
window.geometry("500x500")

# Title
tk.Label(window, text="Select Tests to Run", font=("Arial", 14, "bold")).pack(pady=10)

# Scrollable frame for checkboxes
frame_container = tk.Frame(window)
frame_container.pack(fill="both", expand=True, padx=10)

canvas = tk.Canvas(frame_container)
scrollbar = tk.Scrollbar(frame_container, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Checkbox creation
feature_vars = {}
for feature in get_feature_files():
    var = tk.BooleanVar()
    chk = tk.Checkbutton(scrollable_frame, text=feature, variable=var, anchor="w", padx=5)
    chk.pack(fill="x", anchor="w")
    feature_vars[feature] = var

# Action buttons
btn_frame = tk.Frame(window)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Run Selected Tests", command=run_selected_tests, width=20).grid(row=0, column=0, padx=5, pady=5)
tk.Button(btn_frame, text="Generate Report", command=generate_report, width=20).grid(row=0, column=1, padx=5, pady=5)
tk.Button(btn_frame, text="Open Report", command=open_report, width=20).grid(row=1, column=0, columnspan=2, pady=5)

window.mainloop()
