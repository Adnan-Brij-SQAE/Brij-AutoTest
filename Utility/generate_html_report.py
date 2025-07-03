import os
import sys
from datetime import datetime
import subprocess

def generate_html_report(target):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    report_file = "/Report/behave-report.html"

    os.makedirs("Report", exist_ok=True)

    command = f'behave "{target}" -f html -o {report_file}'
    print(f" Running: {command}")
    result = subprocess.run(command, shell=True)

    if result.returncode == 0:
        print(f" Test passed. Report: {report_file}")
    else:
        print(f" Test failed. Report: {report_file}")

    if os.name == "nt" and os.path.exists(report_file):
        os.startfile(report_file)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        target = sys.argv[1]
        generate_html_report(target)
    else:
        print(" No feature file or target passed.")
