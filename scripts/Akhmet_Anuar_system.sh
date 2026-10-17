#!/bin/bash

PROJECT_DIR="$(cd "$(dirname "$0")/.." && pwd)"

echo "================================"
echo "STUDENT INFORMATION"
echo "================================"

if [ -f "$PROJECT_DIR/Akhmet_Anuar_info.txt" ]; then
    cat "$PROJECT_DIR/Akhmet_Anuar_info.txt"
    echo "Student information file exists."
else
    echo "Student information file does not exist."
fi

echo ""
echo "================================"
echo "SYSTEM INFORMATION"
echo "================================"

echo "Username: $(whoami)"
echo "Hostname: $(hostname)"
echo "Current Date: $(date)"
echo "Operating System: $(uname -s)"

echo ""
echo "Disk Usage:"
df -h /

echo ""
echo "Memory Usage:"
free -h
