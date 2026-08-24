<#
STELLA V2-00R — FRESH LOCAL V0.1 CLOSURE / V0.2 READINESS OBSERVATION
STATUS: PREPARED / READ-ONLY / NOT EXECUTED BY GITHUB

This card COLLECTS fresh local evidence. It intentionally does not award the final
V2-00R PASS by itself, because current observations still require reconciliation
against prior receipts/baselines and the live authorization context.

It does not create, edit, delete, copy, move, download, install, start, stop,
stage, commit, push, fetch, or change settings. Console output only.

Running this script is a separate live action. The presence of this file is not authority.
#>

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

function Section([string]$Name) {
    Write-Host ''
    Write-Host ('=== ' + $Name + ' ===') -ForegroundColor Cyan
}

function Show-Path([string]$Label, [string]$Path) {
    $exists = $false
    if ($Path) { $exists = Test-Path -LiteralPath $Path }
    Write-Host ("{0}|EXISTS={1}|PATH={2}" -f $Label, ($(if ($exists) {'YES'} else {'NO'})), $Path)
    return $exists
}

function Show-Hash([string]$Label, [string]$Path) {
    if (Test-Path -LiteralPath $Path -PathType Leaf) {
        $item = Get-Item -LiteralPath $Path
        $hash = Get-FileHash -LiteralPath $Path -Algorithm SHA256
        Write-Host ("{0}|SHA256={1}|SIZE={2}|LASTWRITE={3:o}|PATH={4}" -f $Label, $hash.Hash, $item.Length, $item.LastWriteTime, $item.FullName)
        return $hash.Hash
    }
    return $null
}

function Expand-EnvironmentPath([string]$Path) {
    if (-not $Path) { return $null }
    return [Environment]::ExpandEnvironmentVariables($Path)
}

$holds = [System.Collections.Generic.List[string]]::new()

Section '0. CARD BOUNDARY'
Write-Host 'MODE=READ_ONLY_LOCAL_EVIDENCE_COLLECTION'
Write-Host 'NETWORK_USE=NO'
Write-Host 'DOWNLOAD=NO'
Write-Host 'INSTALL=NO'
Write-Host 'FILE_MUTATION=NO'
Write-Host 'PROCESS_MUTATION=NO'
Write-Host 'GIT_MUTATION=NO'
Write-Host 'SCOS_MUTATION=NO'
Write-Host 'CANONICAL_PROMOTION=NO'
Write-Host 'FINAL_V2_00R_PASS_SELF_AWARDED=NO'

Section '1. HOST / SESSION'
Write-Host ("TIMESTAMP={0:o}" -f (Get-Date))
Write-Host ("COMPUTER={0}" -f $env:COMPUTERNAME)
Write-Host ("USER={0}" -f $env:USERNAME)
Write-Host ("PS_VERSION={0}" -f $PSVersionTable.PSVersion)
Write-Host ("OS_64BIT={0}" -f [Environment]::Is64BitOperatingSystem)

Section '2. DESKTOP RESOLUTION — DISCOVER, DO NOT ASSUME'
$DesktopDotNet = [Environment]::GetFolderPath([Environment+SpecialFolder]::Desktop)
$DesktopRegistryRaw = $null
$DesktopRegistry = $null
try {
    $DesktopRegistryRaw = (Get-ItemProperty -LiteralPath 'HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders' -Name Desktop -ErrorAction Stop).Desktop
    $DesktopRegistry = Expand-EnvironmentPath $DesktopRegistryRaw
}
catch {
    Write-Host ("DESKTOP_REGISTRY_READ_ERROR={0}" -f $_.Exception.Message)
    $holds.Add('VISIBLE_DESKTOP_REGISTRY_COULD_NOT_BE_READ')
}

Write-Host ("DESKTOP_DOTNET={0}" -f $DesktopDotNet)
Write-Host ("DESKTOP_REGISTRY_RAW={0}" -f $DesktopRegistryRaw)
Write-Host ("DESKTOP_REGISTRY_EXPANDED={0}" -f $DesktopRegistry)

$VisibleDesktop = $DesktopDotNet
if ($DesktopRegistry) {
    if ($DesktopDotNet -and ([IO.Path]::GetFullPath($DesktopDotNet) -ne [IO.Path]::GetFullPath($DesktopRegistry))) {
        $holds.Add('VISIBLE_DESKTOP_RESOLVERS_DISAGREE')
    }
    $VisibleDesktop = $DesktopRegistry
}

$LocalDesktop = Join-Path $env:USERPROFILE 'Desktop'
$PriorVisibleCandidate = Join-Path $env:USERPROFILE 'OneDrive\Desktop'
Show-Path 'RESOLVED_VISIBLE_DESKTOP' $VisibleDesktop | Out-Null
Show-Path 'LOCAL_DESKTOP_CANDIDATE' $LocalDesktop | Out-Null
Show-Path 'PRIOR_ONEDRIVE_DESKTOP_CANDIDATE' $PriorVisibleCandidate | Out-Null

if (-not $VisibleDesktop -or -not (Test-Path -LiteralPath $VisibleDesktop -PathType Container)) {
    $holds.Add('RESOLVED_VISIBLE_DESKTOP_NOT_AVAILABLE')
}

Section '3. V0.1 PLAYGROUND / V0.2 TARGET RESOLUTION'
$V01Name = 'STELLA_LUANTI_PLAYGROUND_V0_1'
$V02Name = 'STELLA_LUANTI_PLAYGROUND_V0_2'
$V01Candidates = @(
    (Join-Path $LocalDesktop $V01Name),
    $(if ($VisibleDesktop) { Join-Path $VisibleDesktop $V01Name } else { $null }),
    (Join-Path $PriorVisibleCandidate $V01Name)
) | Where-Object { $_ } | Select-Object -Unique

$V01Existing = @($V01Candidates | Where-Object { Test-Path -LiteralPath $_ -PathType Container })
foreach ($candidate in $V01Candidates) { Show-Path 'V0_1_CANDIDATE' $candidate | Out-Null }

if ($V01Existing.Count -eq 0) {
    $V01Playground = Join-Path $LocalDesktop $V01Name
    $holds.Add('V0_1_PLAYGROUND_NOT_RESOLVED')
}
elseif ($V01Existing.Count -gt 1) {
    $V01Playground = $V01Existing[0]
    $holds.Add('MULTIPLE_V0_1_PLAYGROUND_CANDIDATES')
}
else {
    $V01Playground = $V01Existing[0]
}
Write-Host ("V0_1_SELECTED_PATH={0}" -f $V01Playground)

$V02Candidate = Join-Path $LocalDesktop $V02Name
$V02Exists = Test-Path -LiteralPath $V02Candidate
Write-Host ("V0_2_CANDIDATE|FREE={0}|PATH={1}" -f ($(if ($V02Exists) {'NO'} else {'YES'})), $V02Candidate)
if ($V02Exists) { $holds.Add('V0_2_CANDIDATE_PATH_ALREADY_EXISTS') }

Section '4. VISIBLE SHORTCUT / TARGET'
$Shortcut = if ($VisibleDesktop) { Join-Path $VisibleDesktop 'PLAY STELLA PLAYGROUND.lnk' } else { $null }
$ShortcutOk = $false
$ShortcutTarget = $null
$ShortcutArguments = $null
$ShortcutWorkingDirectory = $null
if ($Shortcut) { $ShortcutOk = Show-Path 'VISIBLE_SHORTCUT' $Shortcut }
if (-not $ShortcutOk) {
    $holds.Add('VISIBLE_SHORTCUT_NOT_RESOLVED')
}
else {
    try {
        $shell = New-Object -ComObject WScript.Shell
        $sc = $shell.CreateShortcut($Shortcut)
        $ShortcutTarget = $sc.TargetPath
        $ShortcutArguments = $sc.Arguments
        $ShortcutWorkingDirectory = $sc.WorkingDirectory
        Write-Host ("SHORTCUT_TARGET={0}" -f $ShortcutTarget)
        Write-Host ("SHORTCUT_ARGUMENTS={0}" -f $ShortcutArguments)
        Write-Host ("SHORTCUT_WORKING_DIRECTORY={0}" -f $ShortcutWorkingDirectory)
        if (-not $ShortcutTarget -or -not (Test-Path -LiteralPath $ShortcutTarget -PathType Leaf)) {
            $holds.Add('SHORTCUT_TARGET_NOT_RESOLVED_TO_FILE')
        }
        else {
            Show-Hash 'SHORTCUT_TARGET_FILE' $ShortcutTarget | Out-Null
        }
    }
    catch {
        Write-Host ("SHORTCUT_RESOLVE_ERROR={0}" -f $_.Exception.Message)
        $holds.Add('SHORTCUT_TARGET_COULD_NOT_BE_RESOLVED')
    }
}

Section '5. LUANTI EXECUTABLE / VERSION / HASH'
$ExeCandidates = [System.Collections.Generic.List[string]]::new()
if ($ShortcutTarget -and $ShortcutTarget -match '(?i)(luanti|minetest)\.exe$' -and (Test-Path -LiteralPath $ShortcutTarget -PathType Leaf)) {
    $ExeCandidates.Add((Get-Item -LiteralPath $ShortcutTarget).FullName)
}

$BoundedRoots = @(
    (Join-Path $env:LOCALAPPDATA 'Programs\Luanti'),
    (Join-Path $env:APPDATA 'Luanti'),
    'C:\Program Files\Luanti',
    'C:\Program Files (x86)\Luanti',
    $V01Playground
) | Where-Object { $_ } | Select-Object -Unique

foreach ($root in $BoundedRoots) {
    if (Test-Path -LiteralPath $root -PathType Container) {
        Get-ChildItem -LiteralPath $root -File -Recurse -ErrorAction SilentlyContinue |
            Where-Object { $_.Name -in @('luanti.exe','minetest.exe') } |
            ForEach-Object {
                if (-not $ExeCandidates.Contains($_.FullName)) { $ExeCandidates.Add($_.FullName) }
            }
    }
}

Write-Host ("LUANTI_EXE_CANDIDATE_COUNT={0}" -f $ExeCandidates.Count)
$ActiveExe = $null
if ($ShortcutTarget -and $ExeCandidates.Contains($ShortcutTarget)) {
    $ActiveExe = $ShortcutTarget
}
elseif ($ExeCandidates.Count -eq 1) {
    $ActiveExe = $ExeCandidates[0]
}
elseif ($ExeCandidates.Count -eq 0) {
    $holds.Add('LUANTI_EXECUTABLE_NOT_RESOLVED')
}
else {
    $holds.Add('ACTIVE_LUANTI_EXECUTABLE_AMBIGUOUS')
}

foreach ($exe in $ExeCandidates) {
    $item = Get-Item -LiteralPath $exe
    $versionText = $item.VersionInfo.ProductVersion
    if (-not $versionText) { $versionText = $item.VersionInfo.FileVersion }
    $hash = Get-FileHash -LiteralPath $exe -Algorithm SHA256
    Write-Host ("LUANTI_EXE|ACTIVE={0}|VERSION={1}|SHA256={2}|SIZE={3}|PATH={4}" -f ($(if ($ActiveExe -and $item.FullName -eq $ActiveExe) {'YES'} else {'NO'})), $versionText, $hash.Hash, $item.Length, $item.FullName)
}

if ($ActiveExe) {
    $activeItem = Get-Item -LiteralPath $ActiveExe
    $activeVersionText = $activeItem.VersionInfo.ProductVersion
    if (-not $activeVersionText) { $activeVersionText = $activeItem.VersionInfo.FileVersion }
    $parsed = $null
    if ($activeVersionText -match '(\d+\.\d+\.\d+)') {
        try { $parsed = [version]$Matches[1] } catch { $parsed = $null }
    }
    if (-not $parsed) {
        $holds.Add('ACTIVE_LUANTI_VERSION_NOT_PARSEABLE')
    }
    elseif ($parsed -lt [version]'5.17.0') {
        $holds.Add('ACTIVE_LUANTI_VERSION_BELOW_V0_2_RESEARCH_TARGET_5_17_0')
    }
}

Section '6. RELEVANT RUNNING PROCESSES'
$Proc = Get-Process -ErrorAction SilentlyContinue |
    Where-Object { $_.ProcessName -match '(?i)^(luanti|minetest|luantiserver|minetestserver)$' }
if ($Proc) {
    foreach ($p in $Proc) {
        Write-Host ("PROCESS|NAME={0}|PID={1}|PATH={2}" -f $p.ProcessName, $p.Id, ($(try {$p.Path} catch {''})))
    }
    $holds.Add('RELEVANT_LUANTI_PROCESS_RUNNING_REQUIRES_EXPLANATION')
}
else {
    Write-Host 'RELEVANT_LUANTI_PROCESS_COUNT=0'
}

Section '7. V0.1 EVIDENCE / RECEIPT / CHECKPOINT CANDIDATES'
$EvidenceFiles = @()
if (Test-Path -LiteralPath $V01Playground -PathType Container) {
    $EvidenceFiles = @(Get-ChildItem -LiteralPath $V01Playground -File -Recurse -ErrorAction SilentlyContinue |
        Where-Object { $_.Name -match '(?i)(receipt|checkpoint|evidence|manifest|hash|state|world\.mt|mod\.conf|init\.lua)' } |
        Sort-Object FullName)

    Write-Host ("EVIDENCE_CANDIDATE_COUNT={0}" -f $EvidenceFiles.Count)
    foreach ($file in $EvidenceFiles) {
        Show-Hash 'EVIDENCE_FILE' $file.FullName | Out-Null
    }
}
if ($EvidenceFiles.Count -eq 0) {
    $holds.Add('NO_V0_1_EVIDENCE_RECEIPT_CHECKPOINT_CANDIDATES_RESOLVED')
}

Section '8. TOP-LEVEL V0.1 INVENTORY'
if (Test-Path -LiteralPath $V01Playground -PathType Container) {
    Get-ChildItem -LiteralPath $V01Playground -Force -ErrorAction SilentlyContinue |
        Sort-Object Name |
        ForEach-Object {
            Write-Host ("V0_1_ENTRY|TYPE={0}|NAME={1}|LASTWRITE={2:o}|PATH={3}" -f ($(if ($_.PSIsContainer) {'DIR'} else {'FILE'})), $_.Name, $_.LastWriteTime, $_.FullName)
        }
}

Section '9. LOCAL GIT PRESENCE — OBSERVATION ONLY'
if (Test-Path -LiteralPath $V01Playground -PathType Container) {
    $GitDir = Join-Path $V01Playground '.git'
    if (Test-Path -LiteralPath $GitDir) {
        Write-Host 'V0_1_LOCAL_GIT=YES'
        Write-Host 'NOTE=Git status is not invoked by this generic evidence-collection card. If the local path is an active repo, perform a separately reviewed repo-aware read-only check after path confirmation.'
    }
    else {
        Write-Host 'V0_1_LOCAL_GIT=NO'
    }
}

Section '10. COLLECTION RESULT — NOT FINAL GATE CLASSIFICATION'
if ($holds.Count -eq 0) {
    Write-Host 'RESULT=PASS_V2_00R_EVIDENCE_COLLECTION_COMPLETE' -ForegroundColor Green
    Write-Host 'V2_00R_FINAL_CLASSIFICATION=PENDING_RECONCILIATION'
    Write-Host 'NEXT=RETURN_OUTPUT_FOR_RECONCILIATION_AGAINST_PRIOR_RECEIPTS_BASELINES_AND_CURRENT_AUTHORITY'
}
else {
    Write-Host 'RESULT=HOLD_V2_00R_EVIDENCE_COLLECTION' -ForegroundColor Yellow
    foreach ($h in $holds) { Write-Host ("HOLD={0}" -f $h) }
    Write-Host 'V2_00R_FINAL_CLASSIFICATION=HOLD_UNTIL_REVIEWED'
    Write-Host 'NEXT=RETURN_OUTPUT; DO_NOT_START_V0_2_LOCAL_MUTATION'
}

Write-Host ''
Write-Host 'SAFE_TO_CLEAR_TERMINAL=YES'
