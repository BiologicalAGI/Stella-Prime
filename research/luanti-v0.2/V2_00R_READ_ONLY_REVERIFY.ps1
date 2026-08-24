<#
STELLA V2-00R — FRESH LOCAL V0.1 CLOSURE / V0.2 READINESS REVERIFICATION
STATUS: PREPARED / READ-ONLY / NOT EXECUTED BY GITHUB

This script is intentionally observational. It does not create, edit, delete, copy,
move, download, install, start, stop, stage, commit, push, fetch, or change settings.
It writes results to the console only.

Running this script is a separate live action. The presence of this file is not authority.
#>

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

function Section([string]$Name) {
    Write-Host ''
    Write-Host ('=== ' + $Name + ' ===') -ForegroundColor Cyan
}

function Show-Path([string]$Label, [string]$Path) {
    $exists = Test-Path -LiteralPath $Path
    Write-Host ("{0}|EXISTS={1}|PATH={2}" -f $Label, ($(if ($exists) {'YES'} else {'NO'})), $Path)
    return $exists
}

function Show-Hash([string]$Label, [string]$Path) {
    if (Test-Path -LiteralPath $Path -PathType Leaf) {
        $item = Get-Item -LiteralPath $Path
        $hash = Get-FileHash -LiteralPath $Path -Algorithm SHA256
        Write-Host ("{0}|SHA256={1}|SIZE={2}|LASTWRITE={3:o}|PATH={4}" -f $Label, $hash.Hash, $item.Length, $item.LastWriteTime, $item.FullName)
    }
}

$VisibleDesktop = Join-Path $env:USERPROFILE 'OneDrive\Desktop'
$LocalDesktop   = Join-Path $env:USERPROFILE 'Desktop'
$V01Playground  = Join-Path $LocalDesktop 'STELLA_LUANTI_PLAYGROUND_V0_1'
$Shortcut       = Join-Path $VisibleDesktop 'PLAY STELLA PLAYGROUND.lnk'
$V02Candidate   = Join-Path $LocalDesktop 'STELLA_LUANTI_PLAYGROUND_V0_2'

$holds = [System.Collections.Generic.List[string]]::new()

Section '0. CARD BOUNDARY'
Write-Host 'MODE=READ_ONLY_LOCAL_REVERIFICATION'
Write-Host 'NETWORK_USE=NO'
Write-Host 'DOWNLOAD=NO'
Write-Host 'INSTALL=NO'
Write-Host 'FILE_MUTATION=NO'
Write-Host 'PROCESS_MUTATION=NO'
Write-Host 'GIT_MUTATION=NO'
Write-Host 'SCOS_MUTATION=NO'
Write-Host 'CANONICAL_PROMOTION=NO'

Section '1. HOST / SESSION'
Write-Host ("TIMESTAMP={0:o}" -f (Get-Date))
Write-Host ("COMPUTER={0}" -f $env:COMPUTERNAME)
Write-Host ("USER={0}" -f $env:USERNAME)
Write-Host ("PS_VERSION={0}" -f $PSVersionTable.PSVersion)
Write-Host ("OS_64BIT={0}" -f [Environment]::Is64BitOperatingSystem)

Section '2. EXPECTED DESKTOP / PLAYGROUND PATHS'
$visibleDesktopOk = Show-Path 'VISIBLE_DESKTOP' $VisibleDesktop
$localDesktopOk   = Show-Path 'LOCAL_DESKTOP' $LocalDesktop
$v01Ok            = Show-Path 'V0_1_PLAYGROUND' $V01Playground
$shortcutOk       = Show-Path 'VISIBLE_SHORTCUT' $Shortcut
$v02Exists        = Test-Path -LiteralPath $V02Candidate
Write-Host ("V0_2_CANDIDATE|FREE={0}|PATH={1}" -f ($(if ($v02Exists) {'NO'} else {'YES'})), $V02Candidate)

if (-not $v01Ok) { $holds.Add('V0_1_PLAYGROUND_NOT_FOUND_AT_EXPECTED_PATH') }
if (-not $shortcutOk) { $holds.Add('VISIBLE_SHORTCUT_NOT_FOUND') }
if ($v02Exists) { $holds.Add('V0_2_CANDIDATE_PATH_ALREADY_EXISTS') }

Section '3. SHORTCUT TARGET / ARGUMENTS / WORKING DIRECTORY'
$shortcutTarget = $null
if ($shortcutOk) {
    try {
        $shell = New-Object -ComObject WScript.Shell
        $sc = $shell.CreateShortcut($Shortcut)
        $shortcutTarget = $sc.TargetPath
        Write-Host ("SHORTCUT_TARGET={0}" -f $sc.TargetPath)
        Write-Host ("SHORTCUT_ARGUMENTS={0}" -f $sc.Arguments)
        Write-Host ("SHORTCUT_WORKING_DIRECTORY={0}" -f $sc.WorkingDirectory)
        if ($sc.TargetPath -and (Test-Path -LiteralPath $sc.TargetPath -PathType Leaf)) {
            Show-Hash 'SHORTCUT_TARGET_FILE' $sc.TargetPath
        }
    }
    catch {
        Write-Host ("SHORTCUT_RESOLVE_ERROR={0}" -f $_.Exception.Message)
        $holds.Add('SHORTCUT_TARGET_COULD_NOT_BE_RESOLVED')
    }
}

Section '4. LUANTI EXECUTABLE CANDIDATES'
$exeCandidates = [System.Collections.Generic.List[string]]::new()
if ($shortcutTarget -and $shortcutTarget -match '(?i)(luanti|minetest)\.exe$') {
    $exeCandidates.Add($shortcutTarget)
}

$boundedRoots = @(
    (Join-Path $env:LOCALAPPDATA 'Programs\Luanti'),
    (Join-Path $env:APPDATA 'Luanti'),
    'C:\Program Files\Luanti',
    'C:\Program Files (x86)\Luanti',
    $V01Playground
) | Select-Object -Unique

foreach ($root in $boundedRoots) {
    if (Test-Path -LiteralPath $root -PathType Container) {
        Get-ChildItem -LiteralPath $root -File -Recurse -ErrorAction SilentlyContinue |
            Where-Object { $_.Name -in @('luanti.exe','minetest.exe') } |
            ForEach-Object { if (-not $exeCandidates.Contains($_.FullName)) { $exeCandidates.Add($_.FullName) } }
    }
}

if ($exeCandidates.Count -eq 0) {
    Write-Host 'LUANTI_EXE_CANDIDATE_COUNT=0'
    $holds.Add('LUANTI_EXECUTABLE_NOT_RESOLVED')
}
else {
    Write-Host ("LUANTI_EXE_CANDIDATE_COUNT={0}" -f $exeCandidates.Count)
    foreach ($exe in $exeCandidates) {
        $item = Get-Item -LiteralPath $exe
        $version = $item.VersionInfo.ProductVersion
        if (-not $version) { $version = $item.VersionInfo.FileVersion }
        $hash = Get-FileHash -LiteralPath $exe -Algorithm SHA256
        Write-Host ("LUANTI_EXE|VERSION={0}|SHA256={1}|SIZE={2}|PATH={3}" -f $version, $hash.Hash, $item.Length, $item.FullName)
    }
}

Section '5. RELEVANT RUNNING PROCESSES'
$proc = Get-Process -ErrorAction SilentlyContinue |
    Where-Object { $_.ProcessName -match '(?i)^(luanti|minetest|luantiserver|minetestserver)$' }
if ($proc) {
    foreach ($p in $proc) {
        Write-Host ("PROCESS|NAME={0}|PID={1}|PATH={2}" -f $p.ProcessName, $p.Id, ($(try {$p.Path} catch {''})))
    }
    $holds.Add('RELEVANT_LUANTI_PROCESS_RUNNING')
}
else {
    Write-Host 'RELEVANT_LUANTI_PROCESS_COUNT=0'
}

Section '6. V0.1 EVIDENCE / RECEIPT / CHECKPOINT CANDIDATES'
if ($v01Ok) {
    $evidenceFiles = Get-ChildItem -LiteralPath $V01Playground -File -Recurse -ErrorAction SilentlyContinue |
        Where-Object { $_.Name -match '(?i)(receipt|checkpoint|evidence|manifest|hash|state|world\.mt|mod\.conf|init\.lua)' } |
        Sort-Object FullName

    Write-Host ("EVIDENCE_CANDIDATE_COUNT={0}" -f @($evidenceFiles).Count)
    foreach ($file in $evidenceFiles) {
        Show-Hash 'EVIDENCE_FILE' $file.FullName
    }
}

Section '7. TOP-LEVEL V0.1 INVENTORY'
if ($v01Ok) {
    Get-ChildItem -LiteralPath $V01Playground -Force -ErrorAction SilentlyContinue |
        Sort-Object Name |
        ForEach-Object {
            Write-Host ("V0_1_ENTRY|TYPE={0}|NAME={1}|LASTWRITE={2:o}|PATH={3}" -f ($(if ($_.PSIsContainer) {'DIR'} else {'FILE'})), $_.Name, $_.LastWriteTime, $_.FullName)
        }
}

Section '8. LOCAL GIT PRESENCE (OBSERVATION ONLY)'
if ($v01Ok) {
    $gitDir = Join-Path $V01Playground '.git'
    if (Test-Path -LiteralPath $gitDir) {
        Write-Host 'V0_1_LOCAL_GIT=YES'
        Write-Host 'NOTE=Git worktree status intentionally not invoked by this generic card; exact repo-aware check can be added after path confirmation.'
    }
    else {
        Write-Host 'V0_1_LOCAL_GIT=NO'
    }
}

Section '9. RESULT'
if ($holds.Count -eq 0) {
    Write-Host 'RESULT=PASS_V2_00R_FRESH_LOCAL_REVERIFY' -ForegroundColor Green
    Write-Host 'NEXT=V2_01_MAY_BE_PREPARED_AS_A_SEPARATELY_AUTHORIZED_ISOLATED_SHELL_ACTION'
}
else {
    Write-Host 'RESULT=HOLD_V2_00R_FRESH_LOCAL_REVERIFY' -ForegroundColor Yellow
    foreach ($h in $holds) { Write-Host ("HOLD={0}" -f $h) }
    Write-Host 'NEXT=RESOLVE_OR_EXPLAIN_HOLDS_BEFORE_ANY_V0_2_LOCAL_MUTATION'
}

Write-Host ''
Write-Host 'SAFE_TO_CLEAR_TERMINAL=YES'
