@echo off
cd /d "%~dp0backend"

echo ========================================
echo   BabyMomo System Starting...
echo ========================================
echo.

where python >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python not found!
    echo Please install Python from https://www.python.org/downloads/
    echo IMPORTANT: Check "Add Python to PATH" during install.
    echo.
    pause
    exit /b 1
)

echo [1/3] Creating virtual environment...
if not exist venv (
    python -m venv venv
    if errorlevel 1 (
        echo [ERROR] Failed to create venv
        pause
        exit /b 1
    )
)

echo [2/3] Installing packages (first time may take 1-2 min)...
call venv\Scripts\activate.bat
if errorlevel 1 (
    echo [ERROR] Failed to activate venv
    pause
    exit /b 1
)

pip install -r requirements.txt
if errorlevel 1 (
    echo [ERROR] pip install failed
    pause
    exit /b 1
)

echo.
echo [3/3] Starting server...
echo.
echo ----------------------------------------
echo   Open browser: http://localhost:8000
echo   Username: bonnie          / Password: Aa960723
echo   Username: chrisavicii     / Password: Aa0965652118
echo ----------------------------------------
echo   Press Ctrl+C to stop
echo ----------------------------------------
echo.

uvicorn main:app --host 0.0.0.0 --port 8000
echo.
pause
