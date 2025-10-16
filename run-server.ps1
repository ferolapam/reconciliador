# run-server.ps1
# Inicia o servidor em nova janela e salva PID em server.pid
$Root = $PSScriptRoot
if (-not $Root) { $Root = (Get-Location).Path }

Set-Location $Root

$python = Join-Path $Root ".venv\Scripts\python.exe"

if (-not (Test-Path $python)) {
  Write-Error "Python do venv não encontrado em $python. Crie o venv ou verifique o caminho."
  exit 1
}

# Start-Process em nova janela (vai mostrar logs do uvicorn)
$p = Start-Process -FilePath $python `
    -ArgumentList '-m','uvicorn','app.service:app','--host','127.0.0.1','--port','8000','--reload' `
    -WorkingDirectory $Root -PassThru

# salva PID para stop-server
$p.Id | Out-File -Encoding ascii -FilePath (Join-Path $Root "server.pid")

Write-Host "Server iniciado (PID $($p.Id)). Logs na nova janela. Para parar rode: .\stop-server.ps1"
