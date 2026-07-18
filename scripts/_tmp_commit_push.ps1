$ErrorActionPreference = 'Stop'
$env:GIT_AUTHOR_NAME = 'Horosheff'
$env:GIT_AUTHOR_EMAIL = 'horosheff@users.noreply.github.com'
$env:GIT_COMMITTER_NAME = 'Horosheff'
$env:GIT_COMMITTER_EMAIL = 'horosheff@users.noreply.github.com'

Set-Location 'F:\CursorProject\excalibur-blog-cloud-public'

# Do not commit secrets or temp scripts
git add -A
git reset HEAD -- scripts/_migrate_avtosales.ps1 2>$null
git reset HEAD -- scripts/_tmp_*.ps1 2>$null
git reset HEAD -- memory/site.env.local 2>$null
git reset HEAD -- .env 2>$null

git status -sb | Select-Object -First 50
git commit -m @"
feat: rebrand Ex-Aatosales125-Cloud for AVTO SALES

Apply Autо-Sales company brief, authors, cover prompts/assets, Metrika topics,
env templates, cloud Dockerfile env, and published AS08/AS09 continuity.
Remove Maya badge and example.com defaults.
"@

if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

git push -u origin-new main
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

Write-Output 'PUSH_OK'
git log -1 --oneline
git remote -v
