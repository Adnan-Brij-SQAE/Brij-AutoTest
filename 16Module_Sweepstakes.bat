@echo off
cd /d %~dp0
behave D:\playwright\Brij\features\16Module_Sweepstakes.feature -f allure_behave.formatter:AllureFormatter -o D:\playwright\Brij\Report\allure_result
python Utility/generate_allure_report.py