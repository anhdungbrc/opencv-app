@echo off
REM 1-Click Launch Script for Windows Explorer double-click
chcp 65001 >nul
title OpenCV Studio Launcher
echo ==========================================================
echo    🚀 Khởi động OpenCV Studio (FastAPI + React)
echo ==========================================================

powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0start.ps1"
pause
