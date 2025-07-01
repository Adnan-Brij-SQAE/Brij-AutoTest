import tkinter as tk
from tkinter import messagebox
import subprocess
import os
import webbrowser
import threading

# Updated Constants
# ALLURE_REPORT_DIR = "D:\\Vqode\\Brij-AutoTest\\Report\\allure_report"
HTML_REPORT_DIR = r"D:\Vqode\Brij-AutoTest\Report"  # Directory containing report
HTML_REPORT_FILE = "behave-report.html"  # Common report filename (change if different)
TEST_DIR = r"D:\Vqode\Brij-AutoTest"  # Directory containing .bat files

def get_bat_files():
    return [f for f in os.listdir(TEST_DIR) if f.endswith(".bat")]

def log_message(message, clear=False):
    """Log messages to the output panel."""
    if clear:
        log_output.delete("1.0", tk.END)
    log_output.insert(tk.END, message + "\n")
    log_output.see(tk.END)  # Auto-scroll to bottom

def clear_log():
    """Clear the log output panel."""
    log_output.delete("1.0", tk.END)

def run_selected_bat_files():
    selected_files = [file for file, var in bat_vars.items() if var.get()]
    if not selected_files:
        messagebox.showwarning("No Selection", "Please select at least one test to run.")
        return

    thread = threading.Thread(target=execute_tests_thread, args=(selected_files,))
    thread.start()

def execute_tests_thread(selected_files):
    """Threaded execution of .bat files with real-time log updates."""
    log_message("=== Starting Test Execution ===", clear=True)

    try:
        for bat_file in selected_files:
            bat_path = os.path.join(TEST_DIR, bat_file)
            log_message(f"\n[Running] {bat_file}...")

            process = subprocess.Popen(
                bat_path,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True
            )

            for line in process.stdout:
                log_message(line.strip())

            process.wait()

            if process.returncode == 0:
                log_message(f"[Success] {bat_file} executed successfully.")
            else:
                log_message(f"[Error] {bat_file} failed with exit code {process.returncode}.")
                messagebox.showerror("Execution Failed", f"{bat_file} failed.\nCheck log output for details.")
                return

        log_message("\n=== All selected test scripts executed ===")
        messagebox.showinfo("Success", "Selected test scripts ran successfully.\nYou may now open the report.")

    except Exception as e:
        log_message(f"[Exception] {str(e)}")
        messagebox.showerror("Error", f"An exception occurred:\n{str(e)}")

def open_html_report():
    """Open the HTML_report from the specified directory"""
    report_path = os.path.join(HTML_REPORT_DIR, HTML_REPORT_FILE)
    if os.path.exists(report_path):
        # Convert Windows path to file:// URL format
        report_url = f"file:///{report_path.replace('\\', '/')}"
        webbrowser.open(report_url)
        log_message(f"[Opened] HTML_report at {report_path}")
    else:
        error_msg = f"Report not found at: {report_path}"
        messagebox.showwarning("Report Not Found",
                              "HTML_report not found! Please ensure:\n"
                              "1. Tests completed successfully\n"
                              "2. Report was generated in expected location\n"
                              f"3. Report filename is '{HTML_REPORT_FILE}'")
        log_message(f"[Error] {error_msg}")

# GUI Setup
window = tk.Tk()
window.title("Brij Auto Test Runner")
window.geometry("650x700")

# Title
tk.Label(window, text="Select Test Scripts to Run", font=("Arial", 14, "bold")).pack(pady=10)

# Scrollable checkbox area
frame_container = tk.Frame(window)
frame_container.pack(fill="both", expand=False, padx=10)

canvas = tk.Canvas(frame_container, height=200)
scrollbar = tk.Scrollbar(frame_container, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas)

scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Checkbox variables
bat_vars = {}
for bat_file in get_bat_files():
    var = tk.BooleanVar()
    chk = tk.Checkbutton(scrollable_frame, text=bat_file, variable=var, anchor="w", padx=5)
    chk.pack(fill="x", anchor="w")
    bat_vars[bat_file] = var

# Buttons
btn_frame = tk.Frame(window)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Run Selected Tests", command=run_selected_bat_files, width=25).grid(row=0, column=0, padx=10, pady=5)
tk.Button(btn_frame, text="Open Report", command=open_html_report, width=25).grid(row=0, column=1, padx=10, pady=5)
tk.Button(btn_frame, text="Clear Log", command=clear_log, width=53).grid(row=1, column=0, columnspan=2, pady=5)

# Log output panel
tk.Label(window, text="Execution Log", font=("Arial", 12, "bold")).pack(pady=(10, 0))
log_output = tk.Text(window, height=20, wrap="word", bg="#f0f0f0")
log_output.pack(fill="both", expand=True, padx=10, pady=(0, 10))

# Start the GUI
window.mainloop()