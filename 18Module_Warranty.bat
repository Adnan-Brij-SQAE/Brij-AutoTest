@echo off
cd /d %~dp0
behave D:\Vqode\Brij-AutoTest\features\23Module_Warranty.feature -f allure_behave.formatter:AllureFormatter -o D:\Vqode\Brij-AutoTest\Report\allure_result
python Utility/generate_allure_report.py
