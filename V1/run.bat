@echo off
title SensoPack v2.0
color 0B

echo.
echo  ========================================
echo    SensoPack v2.0 - Smart Freshness Scanner
echo  ========================================
echo.

cd /d "%~dp0"

:: Check Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo  [ERROR] Python not found! Install Python 3.8+ and add to PATH.
    pause
    exit /b 1
)

:: Check required packages
echo  Checking dependencies...
python -c "import fastapi, uvicorn, joblib, sklearn, numpy" >nul 2>&1
if errorlevel 1 (
    echo  Installing missing packages...
    pip install fastapi uvicorn joblib scikit-learn numpy
    echo.
)

:: Check model file exists
if not exist "shrimp_spoilage_model.joblib" (
    echo  [ERROR] Model file not found: shrimp_spoilage_model.joblib
    echo  Run the training script first.
    pause
    exit /b 1
)

echo  Starting server on port 8000...
start "" python -m uvicorn server:app --host 127.0.0.1 --port 8000

timeout /t 3 /nobreak >nul

echo  Opening dashboard...
start http://127.0.0.1:8000/app

echo.
echo  ----------------------------------------
echo   Dashboard  : http://127.0.0.1:8000/app
echo   QR Generator: http://127.0.0.1:8000/app/qr-generator.html
echo   API Docs   : http://127.0.0.1:8000/docs
echo  ----------------------------------------
echo.
echo  Arduino sketches: PJSketch\
echo    - PJSketch.ino           (real sensors)
echo    - PJSketch_Simulator.ino (no sensors, for testing)
echo.
echo  Press any key to stop the server...
echo.
pause >nul

:: Kill the server
taskkill /f /im python.exe >nul 2>&1
echo  Server stopped.
