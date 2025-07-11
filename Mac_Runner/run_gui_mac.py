import tkinter as tk
from tkinter import messagebox
import subprocess
import os
import webbrowser
import threading
from http.server import HTTPServer, SimpleHTTPRequestHandler

# Adjust paths below for your Mac environment
HTML_REPORT_DIR = "Report/allure_report"
HTML_REPORT_FILE = "index.html"
TEST_DIR = "."
HTTP_PORT = 8888

def get_sh_files():
    return [f for f in os.listdir(TEST_DIR) if f.endswith(".sh")]

def log_message(message, clear=False):
    if clear:
        log_output.delete("1.0", tk.END)
    log_output.insert(tk.END, message + "\n")
    log_output.see(tk.END)

def clear_log():
    log_output.delete("1.0", tk.END)

def run_selected_sh_files():
    selected_files = [file for file, var in sh_vars.items() if var.get()]
    if not selected_files:
        messagebox.showwarning("No Selection", "Please select at least one test to run.")
        return
    thread = threading.Thread(target=execute_tests_thread, args=(selected_files,))
    thread.start()

def execute_tests_thread(selected_files):
    log_message("=== Starting Test Execution ===", clear=True)
    try:
        for sh_file in selected_files:
            script_path = os.path.join(TEST_DIR, sh_file)
            log_message(f"\n[Running] {sh_file}...")
            process = subprocess.Popen(
                ['bash', script_path],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True
            )
            for line in process.stdout:
                log_message(line.strip())
            process.wait()
            if process.returncode == 0:
                log_message(f"[Success] {sh_file} executed successfully.")
            else:
                log_message(f"[Error] {sh_file} failed with exit code {process.returncode}.")
                messagebox.showerror("Execution Failed", f"{sh_file} failed.\nCheck log output for details.")
                return
        log_message("\n=== All selected test scripts executed ===")
        messagebox.showinfo("Success", "Selected test scripts ran successfully.\nYou may now open the report.")
    except Exception as e:
        log_message(f"[Exception] {str(e)}")
        messagebox.showerror("Error", f"An exception occurred:\n{str(e)}")

def start_http_server():
    os.chdir(HTML_REPORT_DIR)
    server = HTTPServer(("localhost", HTTP_PORT), SimpleHTTPRequestHandler)
    threading.Thread(target=server.serve_forever, daemon=True).start()

def open_html_report():
    report_path = os.path.join(HTML_REPORT_DIR, HTML_REPORT_FILE)
    if os.path.exists(report_path):
        start_http_server()
        webbrowser.open_new_tab(f"http://localhost:{HTTP_PORT}")
        log_message(f"[Opened] http://localhost:{HTTP_PORT}")
    else:
        messagebox.showwarning("Report Not Found",
                               "HTML report not found! Please ensure:\n"
                               "1. Tests completed successfully\n"
                               "2. Report was generated in expected location\n"
                               f"3. Report filename is '{HTML_REPORT_FILE}'")
        log_message(f"[Error] Report not found at: {report_path}")

# GUI Setup
window = tk.Tk()
window.title("Brij Auto Test Runner (macOS)")
window.geometry("650x700")

tk.Label(window, text="Select Test Scripts to Run", font=("Arial", 14, "bold")).pack(pady=10)

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

sh_vars = {}
for sh_file in get_sh_files():
    var = tk.BooleanVar()
    chk = tk.Checkbutton(scrollable_frame, text=sh_file, variable=var, anchor="w", padx=5)
    chk.pack(fill="x", anchor="w")
    sh_vars[sh_file] = var

btn_frame = tk.Frame(window)
btn_frame.pack(pady=10)
tk.Button(btn_frame, text="Run Selected Tests", command=run_selected_sh_files, width=25).grid(row=0, column=0, padx=10, pady=5)
tk.Button(btn_frame, text="Open Report", command=open_html_report, width=25).grid(row=0, column=1, padx=10, pady=5)
tk.Button(btn_frame, text="Clear Log", command=clear_log, width=53).grid(row=1, column=0, columnspan=2, pady=5)

tk.Label(window, text="Execution Log", font=("Arial", 12, "bold")).pack(pady=(10, 0))
log_output = tk.Text(window, height=20, wrap="word", bg="#f0f0f0")
log_output.pack(fill="both", expand=True, padx=10, pady=(0, 10))

window.mainloop()
