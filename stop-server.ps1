# stop-server.ps1 - versão corrigida (usa $serverPid em vez de $pid)
$Root = $PSScriptRoot
if (-not $Root) { $Root = (Get-Location).Path }

$pidFile = Join-Path $Root "server.pid"

if (-not (Test-Path $pidFile)) {
  Write-Host "Arquivo server.pid não encontrado. Use netstat -ano para localizar PID da porta 8000."
  exit 1
}

$serverPid = (Get-Content $pidFile | Select-Object -First 1).Trim()
if ($serverPid -and (Get-Process -Id $serverPid -ErrorAction SilentlyContinue)) {
  Stop-Process -Id $serverPid -Force
  Remove-Item $pidFile -ErrorAction SilentlyContinue
  Write-Host "Processo $serverPid parado."
} else {
  Write-Host "PID $serverPid não existe mais. Removendo server.pid (se existir)."
  Remove-Item $pidFile -ErrorAction SilentlyContinue
}
