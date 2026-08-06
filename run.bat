@echo off
title SensoPack Arduino Bridge
echo ===================================================
echo   SensoPack Cloud Bridge (Arduino -^> Firebase)
echo ===================================================
echo.

:: 1. Check for Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python is not installed or not in PATH!
    echo Please install Python 3 from python.org and try again.
    pause
    exit /b
)

:: 2. Check for Firebase Key
if not exist "serviceAccountKey.json" (
    echo [ERROR] serviceAccountKey.json is missing!
    echo Please download your private key from Firebase, rename it to serviceAccountKey.json, and place it in this folder.
    pause
    exit /b
)

:: 3. Install required Python packages
echo Checking dependencies (pyserial, firebase-admin)...
pip install -q pyserial firebase-admin

:: 4. Run the Python bridge
echo.
echo Starting the bridge...
echo.
python arduino_bridge.py

:: Pause if the script crashes so the user can read the error
pause
