# run_dev.ps1
Write-Host "[INIT] Resetting Environment..." -ForegroundColor Gray
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process

$ProjectRoot = "f:\My profession\web apps\Code Canyon\CANYONINTEL"
$PythonExe = "$ProjectRoot\venv\Scripts\python.exe"
$OutLog = "$ProjectRoot\api_out.log"
$ErrLog = "$ProjectRoot\api_err.log"

if (Test-Path $OutLog) { Remove-Item $OutLog }
if (Test-Path $ErrLog) { Remove-Item $ErrLog }

# 1. Launch FastAPI (Vercel Simulation) in background
Write-Host "[API] Starting at http://localhost:8000..." -ForegroundColor Cyan
Start-Process -FilePath $PythonExe -ArgumentList "-m", "uvicorn", "api.index:app", "--reload", "--port", "8000" -WorkingDirectory $ProjectRoot -NoNewWindow -RedirectStandardOutput $OutLog -RedirectStandardError $ErrLog

# 2. Wait a bit for the server to initialize
Start-Sleep -Seconds 5

# 3. Launch Local Worker in foreground
# Write-Host "[WORKER] Launching Local Harvester Worker..." -ForegroundColor Green
# $env:PYTHONPATH = $ProjectRoot
# & $PythonExe -m worker.main
Write-Host "[INFO] Worker should be running via Docker." -ForegroundColor Yellow
