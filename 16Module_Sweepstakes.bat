@echo off
cd /d %~dp0
set FEATURE_FILE=D:\Vqode\Brij-AutoTest\features\16Module_Sweepstakes.feature
python Utility\generate_html_report.py "%FEATURE_FILE%"
