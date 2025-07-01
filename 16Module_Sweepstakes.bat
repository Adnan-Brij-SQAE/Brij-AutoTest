@echo off
cd /d %~dp0
behave D:\playwright\Brij\features\16Module_Sweepstakes.feature
python Utility\generate_html_report.py