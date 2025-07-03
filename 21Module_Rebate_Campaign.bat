@echo off
cd /d %~dp0
behave D:\Vqode\Brij-AutoTest\features\20Module_Rebate_Campaign.feature -f allure_behave.formatter:AllureFormatter -o D:\Vqode\Brij-AutoTest\Report\allure_result
python Utility/generate_allure_report.py
