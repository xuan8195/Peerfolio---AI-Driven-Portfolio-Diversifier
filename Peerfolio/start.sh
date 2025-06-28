#!/bin/bash

echo "Starting Peerfolio - AI Wealth Management Platform"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Python 3 is not installed"
    echo "Please install Python 3.8 or later"
    exit 1
fi

echo "Installing dependencies..."
pip3 install -r requirements.txt

if [ $? -ne 0 ]; then
    echo "Failed to install dependencies"
    exit 1
fi

echo ""
echo "Starting Streamlit application..."
echo "Opening in browser at http://localhost:8501"
echo ""
echo "Press Ctrl+C to stop the application"
echo ""

streamlit run app.py
