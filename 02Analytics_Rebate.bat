@echo off
cd /d %~dp0
behave D:\Vqode\Brij\features\02Analytics_rebate.feature -f allure_behave.formatter:AllureFormatter -o D:\Vqode\Brij\Report\allure_result
python Utility/generate_allure_report.py
