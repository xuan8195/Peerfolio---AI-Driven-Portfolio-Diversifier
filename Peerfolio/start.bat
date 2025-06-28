@echo off
echo Starting Peerfolio - AI Wealth Management Platform
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Python is not installed or not in PATH
    echo Please install Python 3.8 or later
    pause
    exit /b 1
)

echo Installing dependencies...
pip install -r requirements.txt

if errorlevel 1 (
    echo Failed to install dependencies
    pause
    exit /b 1
)

echo.
echo Starting Streamlit application...
echo Opening in browser at http://localhost:8501
echo.
echo Press Ctrl+C to stop the application
echo.

streamlit run app.py

pause
