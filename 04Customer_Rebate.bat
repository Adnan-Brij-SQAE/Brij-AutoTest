@echo off
cd /d %~dp0
behave D:\Vqode\Brij\features\04Customer_Rebate.feature -f allure_behave.formatter:AllureFormatter -o D:\Vqode\Brij\Report\allure_result
python Utility/generate_allure_report.py
python Utility/send_email.py