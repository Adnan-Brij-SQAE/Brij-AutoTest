@echo off
cd /d %~dp0

:: Run Behave tests
echo Running Behave tests...
behave features\13Module_Document.feature -f allure_behave.formatter:AllureFormatter -o Report\allure_result

:: Generate Allure report
echo Generating Allure report...
python Utility\generate_allure_report.py

:: Wait a moment before serving
timeout /t 2 >nul

:: Serve the report via localhost
cd Report\allure_report
start http://localhost:8888
python -m http.server 8888
exit
