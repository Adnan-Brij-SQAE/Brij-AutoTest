@echo off
cd /d %~dp0
behave D:\playwright\Brij\features\12Module_Custom.feature -f allure_behave.formatter:AllureFormatter -o D:\playwright\Brij\Report\allure_result
python Utility/generate_allure_report.py
