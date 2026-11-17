<#
.SYNOPSIS
    1-Click Development Startup Script for OpenCV Studio.
.DESCRIPTION
    Launches FastAPI Backend (Port 8000) and React Vite Frontend (Port 5173) in separate
    windows, then opens the web application in your default browser.
#>

$ErrorActionPreference = "Stop"
$ProjectRoot = $PSScriptRoot

Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host "   🚀 Khởi động OpenCV Studio (Computer Vision Web App)" -ForegroundColor Green
Write-Host "==========================================================" -ForegroundColor Cyan

# 1. Check Python virtual environment
$PythonExe = Join-Path $ProjectRoot ".venv\Scripts\python.exe"
if (-not (Test-Path $PythonExe)) {
    Write-Host "[!] Không tìm thấy .venv\Scripts\python.exe. Đang kiểm tra python hệ thống..." -ForegroundColor Yellow
    $PythonExe = "python"
}

# 2. Check Frontend node_modules
$NodeModules = Join-Path $ProjectRoot "frontend\node_modules"
if (-not (Test-Path $NodeModules)) {
    Write-Host "[*] Đang cài đặt thư viện Frontend (npm install)..." -ForegroundColor Yellow
    Push-Location (Join-Path $ProjectRoot "frontend")
    npm install
    Pop-Location
}

# 3. Start Backend server in a new window
Write-Host "[1/2] Đang khởi chạy Backend FastAPI tại http://127.0.0.1:8000 ..." -ForegroundColor Cyan
$BackendCmd = "cd `"$ProjectRoot`"; & `"$PythonExe`" main.py"
Start-Process -FilePath "powershell.exe" -ArgumentList "-NoExit", "-Command", "`$Host.UI.RawUI.WindowTitle = 'OpenCV Studio - Backend (Port 8000)'; $BackendCmd"

# 4. Start Frontend server in a new window
Write-Host "[2/2] Đang khởi chạy Frontend React tại http://localhost:5173 ..." -ForegroundColor Cyan
$FrontendCmd = "cd `"$ProjectRoot\frontend`"; npm run dev"
Start-Process -FilePath "powershell.exe" -ArgumentList "-NoExit", "-Command", "`$Host.UI.RawUI.WindowTitle = 'OpenCV Studio - Frontend (Port 5173)'; $FrontendCmd"

# 5. Open browser after a brief delay
Start-Sleep -Seconds 2
Write-Host "`n[✓] Đang mở trình duyệt tới http://localhost:5173 ..." -ForegroundColor Green
Start-Process "http://localhost:5173"

Write-Host "`nĐã khởi chạy thành công cả 2 server trong các cửa sổ riêng biệt." -ForegroundColor Green
Write-Host "Để dừng hệ thống: Đóng 2 cửa sổ terminal Backend và Frontend vừa mở.`n" -ForegroundColor DarkGray
