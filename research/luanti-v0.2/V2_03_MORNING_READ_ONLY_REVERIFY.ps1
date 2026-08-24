<#
STELLA V2-03 — MORNING PRE-MUTATION READ-ONLY REVERIFY
STATUS: PREPARED / READ-ONLY / VALIDATION-BRANCH DRAFT

Purpose:
Re-observe the exact local V2-02 baseline required before any V2-03A mutation.
This card emits evidence only. It does not authorize V2-03A and does not create,
edit, delete, copy, move, download, install, launch, stop, stage, commit, push,
fetch, change settings, or touch SCOS.
#>

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

function Section([string]$Name) {
    Write-Host ''
    Write-Host ('=== ' + $Name + ' ===') -ForegroundColor Cyan
}

$Holds = [System.Collections.Generic.List[string]]::new()

function Add-Hold([string]$Reason) {
    if (-not $Holds.Contains($Reason)) { $Holds.Add($Reason) }
    Write-Host ('HOLD_OBSERVED=' + $Reason) -ForegroundColor Yellow
}

function Check-ExactFileHash(
    [string]$Label,
    [string]$Path,
    [string]$ExpectedHash,
    [Nullable[long]]$ExpectedSize = $null
) {
    if (-not (Test-Path -LiteralPath $Path -PathType Leaf)) {
        Write-Host ("{0}|EXISTS=NO|PATH={1}" -f $Label, $Path)
        Add-Hold ($Label + '_MISSING')
        return
    }

    $Item = Get-Item -LiteralPath $Path
    $Hash = (Get-FileHash -LiteralPath $Path -Algorithm SHA256).Hash
    $HashOk = ($Hash -eq $ExpectedHash)
    $SizeOk = $true
    if ($null -ne $ExpectedSize) { $SizeOk = ($Item.Length -eq $ExpectedSize.Value) }

    Write-Host ("{0}|EXISTS=YES|SHA256={1}|EXPECTED_SHA256={2}|HASH_MATCH={3}|SIZE={4}|SIZE_MATCH={5}|PATH={6}" -f `
        $Label,$Hash,$ExpectedHash,$(if ($HashOk) {'YES'} else {'NO'}),$Item.Length,$(if ($SizeOk) {'YES'} else {'NO'}),$Item.FullName)

    if (-not $HashOk) { Add-Hold ($Label + '_HASH_DRIFT') }
    if (-not $SizeOk) { Add-Hold ($Label + '_SIZE_DRIFT') }
}

function Check-HashMatchInRoot(
    [string]$Label,
    [string]$Root,
    [string]$ExpectedHash,
    [string]$NameRegex
) {
    if (-not (Test-Path -LiteralPath $Root -PathType Container)) {
        Write-Host ("{0}|ROOT_MISSING=YES|ROOT={1}" -f $Label,$Root)
        Add-Hold ($Label + '_ROOT_MISSING')
        return
    }

    $Matches = @()
    $Candidates = @(Get-ChildItem -LiteralPath $Root -File -Recurse -ErrorAction SilentlyContinue |
        Where-Object { $_.Name -match $NameRegex })

    foreach ($File in $Candidates) {
        $Hash = (Get-FileHash -LiteralPath $File.FullName -Algorithm SHA256).Hash
        if ($Hash -eq $ExpectedHash) {
            $Matches += $File
            Write-Host ("{0}|MATCH=YES|SHA256={1}|SIZE={2}|PATH={3}" -f $Label,$Hash,$File.Length,$File.FullName)
        }
    }

    Write-Host ("{0}|EXPECTED_SHA256={1}|MATCH_COUNT={2}" -f $Label,$ExpectedHash,$Matches.Count)
    if ($Matches.Count -eq 0) { Add-Hold ($Label + '_EXPECTED_HASH_NOT_FOUND') }
}

Section '0. CARD BOUNDARY'
Write-Host 'MODE=READ_ONLY_V2_03_PRE_MUTATION_REVERIFY'
Write-Host 'NETWORK_USE=NO'
Write-Host 'DOWNLOAD=NO'
Write-Host 'INSTALL=NO'
Write-Host 'FILE_MUTATION=NO'
Write-Host 'PROCESS_MUTATION=NO'
Write-Host 'GIT_MUTATION=NO'
Write-Host 'SCOS_MUTATION=NO'
Write-Host 'CANONICAL_PROMOTION=NO'
Write-Host 'V2_03A_MUTATION_AUTHORIZED_BY_CARD=NO'

Section '1. HOST / SESSION'
Write-Host ("TIMESTAMP={0:o}" -f (Get-Date))
Write-Host ("COMPUTER={0}" -f $env:COMPUTERNAME)
Write-Host ("USER={0}" -f $env:USERNAME)
Write-Host ("PS_VERSION={0}" -f $PSVersionTable.PSVersion)
Write-Host ("OS_64BIT={0}" -f [Environment]::Is64BitOperatingSystem)

$Desktop = Join-Path $env:USERPROFILE 'Desktop'
$V01Root = Join-Path $Desktop 'STELLA_LUANTI_PLAYGROUND_V0_1'
$V02Root = Join-Path $Desktop 'STELLA_LUANTI_PLAYGROUND_V0_2'
$WKRoot  = Join-Path $Desktop 'STELLA_WORLD_KERNEL_V0_1'

Section '2. REQUIRED ROOTS'
foreach ($Pair in @(
    @('V0_1_ROOT',$V01Root),
    @('V0_2_ROOT',$V02Root),
    @('WORLD_KERNEL_ROOT',$WKRoot)
)) {
    $Exists = Test-Path -LiteralPath $Pair[1] -PathType Container
    Write-Host ("{0}|EXISTS={1}|PATH={2}" -f $Pair[0],$(if ($Exists) {'YES'} else {'NO'}),$Pair[1])
    if (-not $Exists) { Add-Hold ($Pair[0] + '_MISSING') }
}

Section '3. WORLD KERNEL / A18 CURRENTNESS'
if (Test-Path -LiteralPath $WKRoot -PathType Container) {
    $WKFiles = @(Get-ChildItem -LiteralPath $WKRoot -File -Recurse -Force -ErrorAction SilentlyContinue)
    Write-Host ("WORLD_KERNEL_RECURSIVE_FILE_COUNT={0}" -f $WKFiles.Count)
    Write-Host 'WORLD_KERNEL_EXPECTED_FILE_COUNT=129'
    Write-Host ("WORLD_KERNEL_FILE_COUNT_MATCH={0}" -f $(if ($WKFiles.Count -eq 129) {'YES'} else {'NO'}))
    if ($WKFiles.Count -ne 129) { Add-Hold 'WORLD_KERNEL_FILE_COUNT_DRIFT' }

    $A18 = Join-Path $WKRoot 'DEVELOPMENT_MEMORY\STELLA_A18_SEMANTIC_RESOLUTION_SYNTHESIS_CHECKPOINT_V0_1.md'
    Check-ExactFileHash 'A18' $A18 '45C26E2626E1950F1ACF1FFB63B6B9993FBBDEEF53A6918C145E2E6BD42CCB7F' 16969
}

Section '4. V0.1 PROTECTED BASELINE HASHES'
Check-HashMatchInRoot 'V0_1_CONFIG_BASELINE' $V01Root '3533EEA4FA014548DE059CC7F018E3BD260293FCF0635E79B85979302D91A72E' '^minetest\.conf$'
Check-HashMatchInRoot 'V0_1_CORE_INIT_BASELINE' $V01Root '65D1140278CF7FC6A149C74C2AD5289628099FFCB8F598DD085B21A1FDD2B716' '^init\.lua$'
Check-HashMatchInRoot 'V0_1_RECEIPT_BASELINE' $V01Root 'A80D124CD026ACCF8CA20E3C53F53AB4614CF15E884F0DCF33776DC1466CB346' '(?i)receipt'

Section '5. LUANTI EXECUTABLE IDENTITY'
$ExpectedLuantiHash = '7091913D6C7D1FACCF0F1895A9C009FC51C8F409DFFD577ABF17BAFC6AA1715F'
$ExeRoots = @(
    $V02Root,
    $V01Root,
    (Join-Path $env:LOCALAPPDATA 'Programs\Luanti'),
    'C:\Program Files\Luanti',
    'C:\Program Files (x86)\Luanti'
)
$LuantiMatches = @()
foreach ($Root in $ExeRoots) {
    if (Test-Path -LiteralPath $Root -PathType Container) {
        $Executables = @(Get-ChildItem -LiteralPath $Root -File -Recurse -ErrorAction SilentlyContinue |
            Where-Object { $_.Name -in @('luanti.exe','minetest.exe') })
        foreach ($Exe in $Executables) {
            $Hash = (Get-FileHash -LiteralPath $Exe.FullName -Algorithm SHA256).Hash
            if ($Hash -eq $ExpectedLuantiHash) {
                $LuantiMatches += $Exe
                Write-Host ("LUANTI_MATCH|SHA256={0}|PRODUCT_VERSION={1}|FILE_VERSION={2}|SIZE={3}|PATH={4}" -f `
                    $Hash,$Exe.VersionInfo.ProductVersion,$Exe.VersionInfo.FileVersion,$Exe.Length,$Exe.FullName)
            }
        }
    }
}
Write-Host ("LUANTI_EXPECTED_HASH_MATCH_COUNT={0}" -f $LuantiMatches.Count)
if ($LuantiMatches.Count -eq 0) { Add-Hold 'LUANTI_EXPECTED_EXECUTABLE_HASH_NOT_FOUND' }

Section '6. PROCESS QUIESCENCE'
$Running = @(Get-Process -ErrorAction SilentlyContinue |
    Where-Object { $_.ProcessName -match '(?i)^(luanti|minetest|luantiserver|minetestserver)$' })
Write-Host ("RELEVANT_LUANTI_PROCESS_COUNT={0}" -f $Running.Count)
foreach ($P in $Running) {
    $PPath = ''
    try { $PPath = $P.Path } catch { $PPath = '' }
    Write-Host ("PROCESS|NAME={0}|PID={1}|PATH={2}" -f $P.ProcessName,$P.Id,$PPath)
}
if ($Running.Count -gt 0) { Add-Hold 'LUANTI_PROCESS_NOT_QUIESCENT' }

Section '7. V2-02 ACTIVE CODE / RECEIPTS'
if (Test-Path -LiteralPath $V02Root -PathType Container) {
    $DialogueFiles = @(Get-ChildItem -LiteralPath $V02Root -File -Recurse -Filter 'init.lua' -ErrorAction SilentlyContinue |
        Where-Object { $_.FullName -match '[\\/]stella_dialogue[\\/]init\.lua$' })
    Write-Host ("DIALOGUE_INIT_CANDIDATE_COUNT={0}" -f $DialogueFiles.Count)
    if ($DialogueFiles.Count -eq 1) {
        Check-ExactFileHash 'STELLA_DIALOGUE_INIT' $DialogueFiles[0].FullName '6DC2E9A90CB7772C6C46B627F79D146E1C74397108C2E6AAF22EF37153A754EE'
    } else {
        Add-Hold 'STELLA_DIALOGUE_INIT_NOT_EXACTLY_ONE'
    }

    $InhabitantFiles = @(Get-ChildItem -LiteralPath $V02Root -File -Recurse -Filter 'init.lua' -ErrorAction SilentlyContinue |
        Where-Object { $_.FullName -match '[\\/]stella_inhabitants[\\/]init\.lua$' })
    Write-Host ("INHABITANTS_INIT_CANDIDATE_COUNT={0}" -f $InhabitantFiles.Count)
    if ($InhabitantFiles.Count -eq 1) {
        Check-ExactFileHash 'STELLA_INHABITANTS_INIT' $InhabitantFiles[0].FullName 'FB36E8B3ECE92DA6C73C23BDA88C5C53F6A3A92BA402328735800536B1725519'
    } else {
        Add-Hold 'STELLA_INHABITANTS_INIT_NOT_EXACTLY_ONE'
    }

    Check-HashMatchInRoot 'V2_02A_BUILD_RECEIPT' $V02Root 'B141B05A4FC9A40053CF354FA8FD072707AC1C8041C07D9825D98BD3654A15A0' '(?i)receipt'
    Check-HashMatchInRoot 'V2_02R1A_R1_REPAIR_RECEIPT' $V02Root '76C103F80CE75915B74108D8DCF56BABD9FC79EA4679F019116BE33E58803119' '(?i)receipt'
}

Section '8. V0.2 WORLD IDENTITY'
if (Test-Path -LiteralPath $V02Root -PathType Container) {
    $WorldFiles = @(Get-ChildItem -LiteralPath $V02Root -File -Recurse -Filter 'world.mt' -ErrorAction SilentlyContinue)
    Write-Host ("WORLD_MT_CANDIDATE_COUNT={0}" -f $WorldFiles.Count)
    $MatchingWorlds = @()
    foreach ($WorldFile in $WorldFiles) {
        $Text = Get-Content -LiteralPath $WorldFile.FullName -Raw
        $Match = ($Text -match '(?m)^\s*gameid\s*=\s*stella_v0_2_shell\s*$')
        Write-Host ("WORLD_MT|GAME_ID_MATCH={0}|PATH={1}" -f $(if ($Match) {'YES'} else {'NO'}),$WorldFile.FullName)
        if ($Match) { $MatchingWorlds += $WorldFile }
    }
    Write-Host ("WORLD_MT_V0_2_GAME_ID_MATCH_COUNT={0}" -f $MatchingWorlds.Count)
    if ($MatchingWorlds.Count -ne 1) { Add-Hold 'WORLD_MT_V0_2_IDENTITY_NOT_EXACTLY_ONE' }
}

Section '9. V2-02R1B RUNTIME EVIDENCE / OPEN OBSERVATIONS'
$RuntimeLog = Join-Path $V02Root 'V2_02R1B_RUNTIME.log'
if (Test-Path -LiteralPath $RuntimeLog -PathType Leaf) {
    Check-ExactFileHash 'V2_02R1B_RUNTIME_LOG' $RuntimeLog '68AF668526974D5B31385BF88EE8AB42DFE40426CF964FDE9D037197E8E44DF3'

    $Stone = @(Select-String -LiteralPath $RuntimeLog -Pattern "Mapgen alias 'mapgen_stone' is invalid" -SimpleMatch)
    $Water = @(Select-String -LiteralPath $RuntimeLog -Pattern "Mapgen alias 'mapgen_water_source' is invalid" -SimpleMatch)
    $ServerErrors = @(Select-String -LiteralPath $RuntimeLog -Pattern 'ERROR[ServerStart]' -SimpleMatch)
    Write-Host ("OPEN_01_MAPGEN_STONE_COUNT={0}" -f $Stone.Count)
    Write-Host ("OPEN_02_MAPGEN_WATER_COUNT={0}" -f $Water.Count)
    Write-Host ("SERVERSTART_ERROR_COUNT={0}" -f $ServerErrors.Count)
    Write-Host 'OPEN_01_STATUS=CARRIED_FORWARD_UNRESOLVED_NONBLOCKING_FOR_STATE_FOUNDATION'
    Write-Host 'OPEN_02_STATUS=CARRIED_FORWARD_UNRESOLVED_NONBLOCKING_FOR_STATE_FOUNDATION'
} else {
    Write-Host ("V2_02R1B_RUNTIME_LOG|EXISTS=NO|PATH={0}" -f $RuntimeLog)
    Add-Hold 'V2_02R1B_RUNTIME_LOG_MISSING'
}
Write-Host 'OPEN_03_STATUS=HUMAN_OBSERVATION_REQUIRES_LATER_MOVEMENT_ORIENTATION_RETEST'
Write-Host 'OPEN_04_STATUS=TEMPORARY_MARA_BODY_DEFERRED_TO_V2_05'
Write-Host 'OPEN_05_STATUS=RUNTIME_HARNESS_MUST_DISTINGUISH_FATAL_ERROR_WARNING_KNOWN_NONBLOCKING'
Write-Host 'OPEN_06_STATUS=ORCHESTRATION_DOCUMENT_CURRENTNESS_DRIFT_REQUIRES_DOC_RECONCILIATION_AFTER_LOCAL_REVERIFY'

Section '10. V2-03 TARGET FREEDOM'
if (Test-Path -LiteralPath $V02Root -PathType Container) {
    $StateDirs = @(Get-ChildItem -LiteralPath $V02Root -Directory -Recurse -Force -ErrorAction SilentlyContinue |
        Where-Object { $_.Name -eq 'stella_state' })
    Write-Host ("STELLA_STATE_TARGET_DIRECTORY_COUNT={0}" -f $StateDirs.Count)
    foreach ($Dir in $StateDirs) { Write-Host ("STELLA_STATE_TARGET_EXISTING_PATH={0}" -f $Dir.FullName) }
    if ($StateDirs.Count -ne 0) { Add-Hold 'V2_03_STELLA_STATE_TARGET_NOT_FREE' }
}

Section '11. REVERIFY RESULT — EVIDENCE ONLY'
if ($Holds.Count -eq 0) {
    Write-Host 'RESULT=PASS_V2_03_MORNING_REVERIFY_EVIDENCE_COLLECTION' -ForegroundColor Green
    Write-Host 'CURRENTNESS_EVIDENCE=SUFFICIENT_FOR_RECONCILIATION'
    Write-Host 'NEXT=RETURN_OUTPUT_FOR_ASSISTANT_RECONCILIATION_BEFORE_ANY_V2_03A_MUTATION'
} else {
    Write-Host 'RESULT=HOLD_V2_03_MORNING_REVERIFY_EVIDENCE_COLLECTION' -ForegroundColor Yellow
    foreach ($Reason in $Holds) { Write-Host ("HOLD={0}" -f $Reason) }
    Write-Host 'CURRENTNESS_EVIDENCE=HOLD'
    Write-Host 'NEXT=RETURN_OUTPUT; DO_NOT_BEGIN_V2_03A_MUTATION'
}

Write-Host 'V2_03A_MUTATION_AUTHORIZED_BY_CARD=NO'
Write-Host 'SAFE_TO_CLEAR_TERMINAL=YES'
