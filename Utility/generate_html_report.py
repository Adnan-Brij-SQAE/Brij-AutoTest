import os
from datetime import datetime
import subprocess

def generate_html_report():
    feature_path = "features"
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    report_file = f"Report/behave-report.html"

    os.makedirs("Report", exist_ok=True)

    command = f"behave {feature_path} -f html -o {report_file}"
    result = subprocess.run(command, shell=True)

    if result.returncode == 0:
        print(f" Test passed. Report: {report_file}")
    else:
        print(f" Test failed. Report: {report_file}")

    # Open the report (only works on Windows)
    if os.name == "nt" and os.path.exists(report_file):
        os.startfile(report_file)

if __name__ == "__main__":
    generate_html_report()
