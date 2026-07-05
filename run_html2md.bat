@echo off
chcp 65001 >nul
cd /d "%~dp0"
py -3.12 html2md.py
echo.
pause
