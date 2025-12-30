param(
  [string]$ApiHost = "127.0.0.1",
  [int]$ApiPort = 8000,
  [int]$SimIntervalSeconds = 8,
  [double]$SimCreateProb = 0.70,
  [int]$RunnerIntervalSeconds = 10,
  [int]$EscalateAfterMinutes = 30
)

$ErrorActionPreference = "Stop"

# Go to project root (one level above scripts/)
$ProjectRoot = Resolve-Path (Join-Path $PSScriptRoot "..")
Set-Location $ProjectRoot

$VenvActivate = Join-Path $ProjectRoot ".venv\Scripts\Activate.ps1"
if (-not (Test-Path $VenvActivate)) {
  Write-Host "ERROR: Virtual env not found at .venv. Create it first: python -m venv .venv" -ForegroundColor Red
  exit 1
}

$BaseUrl = "http://$ApiHost`:$ApiPort"

function Start-NewPSWindow {
  param(
    [string]$Title,
    [string]$Command
  )

  # Open a new PowerShell window and run the command
  Start-Process -FilePath "powershell.exe" -ArgumentList @(
    "-NoExit",
    "-ExecutionPolicy", "Bypass",
    "-Command", "cd '$ProjectRoot'; `$host.ui.RawUI.WindowTitle='$Title'; $Command"
  )
}

Write-Host "Starting 3 processes in separate windows..." -ForegroundColor Cyan
Write-Host "API:        $BaseUrl" -ForegroundColor Cyan
Write-Host "Simulator:  interval=$SimIntervalSeconds create_prob=$SimCreateProb" -ForegroundColor Cyan
Write-Host "Runner:     interval=$RunnerIntervalSeconds escalate_after_minutes=$EscalateAfterMinutes" -ForegroundColor Cyan

# 1) API
$ApiCmd = @"
& '$VenvActivate'
uvicorn app.main:app --reload --host $ApiHost --port $ApiPort
"@

Start-NewPSWindow -Title "ATMS - API" -Command $ApiCmd

Start-Sleep -Seconds 2

# 2) Simulator
$SimCmd = @"
& '$VenvActivate'
`$env:API_BASE_URL = '$BaseUrl'
`$env:SIM_INTERVAL_SECONDS = '$SimIntervalSeconds'
`$env:SIM_CREATE_PROB = '$SimCreateProb'
python -m integrations.ingest_simulator
"@

Start-NewPSWindow -Title "ATMS - Simulator" -Command $SimCmd

Start-Sleep -Seconds 1

# 3) Runner
$RunnerCmd = @"
& '$VenvActivate'
`$env:API_BASE_URL = '$BaseUrl'
`$env:RUNNER_INTERVAL_SECONDS = '$RunnerIntervalSeconds'
`$env:ESCALATE_AFTER_MINUTES = '$EscalateAfterMinutes'
python -m automation.runner
"@

Start-NewPSWindow -Title "ATMS - Runner" -Command $RunnerCmd

Write-Host "`nDone. Open Swagger UI at: $BaseUrl/docs" -ForegroundColor Green
