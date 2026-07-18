$ErrorActionPreference = 'Stop'
$root = 'F:\CursorProject\excalibur-blog-cloud-public'
$env:GIT_AUTHOR_NAME = 'Horosheff'
$env:GIT_AUTHOR_EMAIL = 'horosheff@users.noreply.github.com'
$env:GIT_COMMITTER_NAME = 'Horosheff'
$env:GIT_COMMITTER_EMAIL = 'horosheff@users.noreply.github.com'

@(
  'memory\blog\articles\AS08-samye-komfortnye-avto-myagkaya-podveska-2026\AS08-samye-komfortnye-avto-myagkaya-podveska-2026',
  'memory\blog\articles\AS09-trust-encar-carhistory-proverka-do-depozita\AS09-trust-encar-carhistory-proverka-do-depozita',
  '.cursor\skills\cover-excalibur-blog\cover-excalibur-blog',
  '.cursor\skills\publish-excalibur-blog\publish-excalibur-blog',
  '.cursor\skills\writer-excalibur-blog\writer-excalibur-blog',
  'skills\cover-excalibur-blog\cover-excalibur-blog',
  'skills\publish-excalibur-blog\publish-excalibur-blog',
  'skills\writer-excalibur-blog\writer-excalibur-blog'
) | ForEach-Object {
  $p = Join-Path $root $_
  if (Test-Path $p) {
    Remove-Item -LiteralPath $p -Recurse -Force
    Write-Output "REMOVED $_"
  }
}

# Ensure flat skill SKILL.md present in .cursor
foreach ($s in @('cover-excalibur-blog','publish-excalibur-blog','writer-excalibur-blog')) {
  $src = Join-Path $root "skills\$s\SKILL.md"
  $dstDir = Join-Path $root ".cursor\skills\$s"
  if (-not (Test-Path $dstDir)) { New-Item -ItemType Directory -Force -Path $dstDir | Out-Null }
  Copy-Item $src (Join-Path $dstDir 'SKILL.md') -Force
}

Set-Location $root
git add -A
git commit -m 'chore: remove nested duplicate article and skill folders'
git push origin-new main
Write-Output 'CLEANUP_PUSH_OK'
git log -1 --oneline
