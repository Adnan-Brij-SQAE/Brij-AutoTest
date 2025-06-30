@echo off
cd /d %~dp0
behave D:\Vqode\Brij\features\01Alalytics_general.feature -f allure_behave.formatter:AllureFormatter -o D:\Vqode\Brij\Report\allure_result
python D:\Vqode\Brij\Utility/generate_allure_report.py
