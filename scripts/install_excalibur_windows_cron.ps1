# Install Excalibur BLOG cron into Windows Task Scheduler
# 4 times/day: 09:00, 13:00, 17:00, 21:00 (local PC time = Vladivostok UTC+10)

param(
  [string]$ProjectRoot = "F:\CursorProject\excalibur-blog-cloud-public",
  [switch]$Uninstall
)

$ErrorActionPreference = "Stop"
$prefix = "ExcaliburBlog"
$runScript = Join-Path $ProjectRoot "scripts\excalibur_blog_cron_run.ps1"
$times = @(
  @{ Name = "$prefix-0900"; Time = "09:00" },
  @{ Name = "$prefix-1300"; Time = "13:00" },
  @{ Name = "$prefix-1700"; Time = "17:00" },
  @{ Name = "$prefix-2100"; Time = "21:00" }
)

if (-not (Test-Path $runScript)) {
  throw "Run script not found: $runScript"
}

foreach ($t in $times) {
  schtasks /Delete /TN $t.Name /F 2>$null | Out-Null
}

if ($Uninstall) {
  Write-Output "UNINSTALLED all $prefix tasks"
  exit 0
}

$ps = Join-Path $env:SystemRoot "System32\WindowsPowerShell\v1.0\powershell.exe"

foreach ($t in $times) {
  $slot = $t.Time
  $tr = '"' + $ps + '" -NoProfile -ExecutionPolicy Bypass -File "' + $runScript + '" -ProjectRoot "' + $ProjectRoot + '" -Slot "' + $slot + '"'
  schtasks /Create /TN $t.Name /SC DAILY /ST $t.Time /RL LIMITED /F /TR $tr | Out-Null
  if ($LASTEXITCODE -ne 0) {
    throw "schtasks failed for $($t.Name) exit=$LASTEXITCODE"
  }
  Write-Output ("OK {0} @ {1} daily" -f $t.Name, $t.Time)
}

Write-Output ""
Write-Output "Schedule: 09:00 13:00 17:00 21:00 (local PC time)"
Write-Output "Window: 09:00-22:00, 4 runs/day"
Write-Output "Query: schtasks /Query /TN ExcaliburBlog-0900 /V /FO LIST"
Write-Output "Remove: .\scripts\install_excalibur_windows_cron.ps1 -Uninstall"
