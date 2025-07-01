import os
import json

# Define the Allure results directory (update the path as needed)
allure_results_dir = os.path.abspath("Report//allure_result")

# Ensure the directory exists
os.makedirs(allure_results_dir, exist_ok=True)

# Step 1: Update Title and Subtitle in executor.json
executor_data = {
    "name": "SQAE Department- Vqode",
    "type": "Brij & Vqode QA Department",
    "buildName": "Automation Test Run",
    "reportUrl": "http://your-report-url.com",  # Optional, change as needed
}

executor_file = os.path.join(allure_results_dir, "executor.json")
with open(executor_file, "w") as file:
    json.dump(executor_data, file, indent=4)

# Step 2: Add Chrome Browser to environment.properties
environment_data = """Browser=Chrome
OS=Windows
ExecutedBy=Brij & Vqode QA Team
"""

env_file = os.path.join(allure_results_dir, "environment.properties")
with open(env_file, "w") as file:
    file.write(environment_data)

print("Allure metadata updated successfully!")


def replace_trend_with_logo():
    allure_report_path = r"D:\Vqode\Brij-AutoTest\Report\allure_report"
    index_file = os.path.join(allure_report_path, "index.html")
    logo_filename = "brij.PNG"
    logo_path = os.path.join(allure_report_path, logo_filename)

    if not os.path.exists(index_file):
        print("Error: Allure report index.html not found!")
        return

    if not os.path.exists(logo_path):
        print("Error: Brij logo not found at", logo_path)
        return

    with open(index_file, "r", encoding="utf-8") as file:
        content = file.read()

    logo_html = f"""
    <div style="text-align:center; margin-top:20px;">
        <img src="{logo_filename}" alt="Brij Company Logo" style="max-width:300px;">
    </div>
    """

    updated_content = content.replace('<h2>TREND</h2>', logo_html)


    with open(index_file, "w", encoding="utf-8") as file:
        file.write(updated_content)

    print("Success: Allure report updated with Brij company logo!")


replace_trend_with_logo()


def generate_allure_report():
    """This method generates Allure report from the allure results"""
    os.chdir(os.path.abspath(__file__ + "/../../"))
    os.system(r'allure generate Report/allure_result -o Report/allure_report --clean')

generate_allure_report()
