@echo off
cd /d %~dp0
$behave D:\Vqode\Brij-AutoTest\features\12Module_Custom.feature
python Utility\generate_html_report.py

