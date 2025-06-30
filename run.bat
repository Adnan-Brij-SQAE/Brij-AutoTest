behave -f allure_behave.formatter:AllureFormatter -o Report\allure_result
python Utility/generate_allure_report.py
python Utility/send_email.py
