#!/bin/bash
cd "$(dirname "$0")/backend"
echo "========================================"
echo "  BabyMomo System Starting..."
echo "========================================"

if ! command -v python3 &>/dev/null; then
  echo "[ERROR] python3 not found. Please install Python 3"
  exit 1
fi

if [ ! -d venv ]; then
  echo "[1/3] Creating virtual environment..."
  python3 -m venv venv
fi

echo "[2/3] Installing packages..."
source venv/bin/activate
pip install -r requirements.txt -q

echo "[3/3] Starting server..."
echo ""
echo "Open browser: http://localhost:8000"
echo "Username: bonnie        / Password: Aa960723"
echo "Username: chrisavicii   / Password: Aa0965652118"
echo "Press Ctrl+C to stop"
echo ""
uvicorn main:app --host 0.0.0.0 --port 8000
