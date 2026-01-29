$workers = Get-WmiObject Win32_Process | Where-Object { $_.CommandLine -like "*worker.main*" }
if ($workers) {
    Write-Host "Found $($workers.Count) worker process(es). Stopping..." -ForegroundColor Yellow
    $workers | ForEach-Object { 
        Stop-Process -Id $_.ProcessId -Force -ErrorAction SilentlyContinue 
        Write-Host "Stopped PID $($_.ProcessId)" -ForegroundColor Green
    }
}
else {
    Write-Host "No local worker process found." -ForegroundColor Gray
}
