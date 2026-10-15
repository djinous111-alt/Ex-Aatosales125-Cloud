# Excalibur BLOG — cron trigger (вызывается Планировщиком Windows)

param(
  [string]$ProjectRoot = "F:\CursorProject\excalibur-blog-cloud-public",
  [string]$Slot = ""
)

$ErrorActionPreference = "Stop"
$tz = [TimeZoneInfo]::FindSystemTimeZoneById("Russia Time Zone 10") # Vladivostok UTC+10
$nowLocal = [TimeZoneInfo]::ConvertTime([DateTime]::UtcNow, $tz)
$stamp = $nowLocal.ToString("yyyy-MM-dd HH:mm:ss")

$logDir = Join-Path $ProjectRoot "memory\cron"
New-Item -ItemType Directory -Force -Path $logDir | Out-Null
$logFile = Join-Path $logDir "cron-run-log.md"
$queueFile = Join-Path $logDir "pending-run.json"

$payload = @{
  requested_at = $stamp
  timezone     = "Asia/Vladivostok"
  slot         = $Slot
  action       = "excalibur_blog_pipeline"
  publish      = "yes"
  prompt       = @"
Запусти полный пайплайн Excalibur BLOG (Директор + Task субагенты) для Авто-Сейлс.
publish: yes
1) today.py + выбор следующей P0 темы по Метрике/пробелам блога (не дублировать published)
2) research_start → research → writer → geo-qa → cover||schema → indexer → publish
3) Без Wordstat/Метрики в тексте и на картинках; угол обложки avto-sales125.ru; одежда героя под погоду и тему.
Финальный ответ: permalink или блокер.
"@
} | ConvertTo-Json -Depth 4

[System.IO.File]::WriteAllText($queueFile, $payload, [System.Text.UTF8Encoding]::new($false))

$line = "- [$stamp] slot=$Slot queued → pending-run.json"
Add-Content -Path $logFile -Value $line -Encoding UTF8

Write-Output "EXCALIBUR_CRON_QUEUED $stamp slot=$Slot"
Write-Output "queue=$queueFile"
Write-Output "Open Cursor Agents and run the queued Excalibur pipeline (or Automation will pick this up)."

# Неблокирующий пинг: открыть handoff-флаг для оператора
$flag = Join-Path $ProjectRoot ".cursor\excalibur-cron-wake.md"
@"
# Excalibur cron wake

**queued_at:** $stamp (Asia/Vladivostok)
**slot:** $Slot
**action:** full pipeline + publish

Прочитай `memory/cron/pending-run.json` и запусти пайплайн как Директор.
"@ | Set-Content -Path $flag -Encoding UTF8
