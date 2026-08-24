<#
STELLA V2-03 — MORNING PRE-MUTATION READ-ONLY REVERIFY R2
STATUS: PREPARED / READ-ONLY / VALIDATION-BRANCH DRAFT

Purpose:
Re-observe the exact local V2-02 baseline required before any V2-03A mutation.
This card emits evidence only. It does not authorize V2-03A and does not create,
edit, delete, copy, move, download, install, launch, stop, stage, commit, push,
fetch, change settings, or touch SCOS.

R2 corrections:
- exact known paths replace regex discovery for protected artifacts;
- no executable use of PowerShell's automatic regex-capture variable;
- expected size uses a plain Int64 sentinel;
- the entire observation is defined as one function before invocation so
  script-file, stdin, and interactive paste delivery share one execution scope.
#>

function Invoke-StellaV203MorningReverify {
    Set-StrictMode -Version Latest
    $ErrorActionPreference = 'Stop'

    $Holds = [System.Collections.Generic.List[string]]::new()

    function Add-Hold([string]$Reason) {
        if (-not $Holds.Contains($Reason)) { $Holds.Add($Reason) }
        Write-Host ('HOLD_OBSERVED=' + $Reason) -ForegroundColor Yellow
    }

    function Check-File(
        [string]$Label,
        [string]$Path,
        [string]$ExpectedHash,
        [long]$ExpectedSize = -1
    ) {
        try {
            if (-not (Test-Path -LiteralPath $Path -PathType Leaf -ErrorAction Stop)) {
                Write-Host ("{0}|EXISTS=NO|PATH={1}" -f $Label,$Path)
                Add-Hold ($Label + '_MISSING')
                return
            }

            $Item = Get-Item -LiteralPath $Path -ErrorAction Stop
            $Hash = (Get-FileHash -LiteralPath $Path -Algorithm SHA256 -ErrorAction Stop).Hash
            $HashOk = ($Hash -eq $ExpectedHash)
            $SizeOk = ($ExpectedSize -lt 0 -or $Item.Length -eq $ExpectedSize)

            Write-Host ("{0}|EXISTS=YES|SHA256={1}|EXPECTED_SHA256={2}|HASH_MATCH={3}|SIZE={4}|SIZE_MATCH={5}|PATH={6}" -f `
                $Label,$Hash,$ExpectedHash,$(if ($HashOk) {'YES'} else {'NO'}),$Item.Length,$(if ($SizeOk) {'YES'} else {'NO'}),$Item.FullName)

            if (-not $HashOk) { Add-Hold ($Label + '_HASH_DRIFT') }
            if (-not $SizeOk) { Add-Hold ($Label + '_SIZE_DRIFT') }
        }
        catch {
            Write-Host ("READ_ERROR|LABEL={0}|MESSAGE={1}|PATH={2}" -f $Label,$_.Exception.Message,$Path)
            Add-Hold ($Label + '_READ_ERROR')
        }
    }

    try {
        Write-Host ''
        Write-Host '=== 0. CARD BOUNDARY ===' -ForegroundColor Cyan
        Write-Host 'CARD_REVISION=R2_ATOMIC_PASTE_SAFE_EXACT_PATH'
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
        Write-Host 'EXPECTED_COMPUTER=SCOS-HOME'

        Write-Host ''
        Write-Host '=== 1. HOST / SESSION ===' -ForegroundColor Cyan
        Write-Host ("TIMESTAMP={0:o}" -f (Get-Date))
        Write-Host ("COMPUTER={0}" -f $env:COMPUTERNAME)
        Write-Host ("USER={0}" -f $env:USERNAME)
        Write-Host ("PS_VERSION={0}" -f $PSVersionTable.PSVersion)
        Write-Host ("OS_64BIT={0}" -f [Environment]::Is64BitOperatingSystem)
        $HostMatch = ($env:COMPUTERNAME -eq 'SCOS-HOME')
        Write-Host ("EXPECTED_COMPUTER_MATCH={0}" -f $(if ($HostMatch) {'YES'} else {'NO'}))
        if (-not $HostMatch) { Add-Hold 'UNEXPECTED_HOST' }

        $Desktop = Join-Path $env:USERPROFILE 'Desktop'
        $V01Root = Join-Path $Desktop 'STELLA_LUANTI_PLAYGROUND_V0_1'
        $V02Root = Join-Path $Desktop 'STELLA_LUANTI_PLAYGROUND_V0_2'
        $WKRoot  = Join-Path $Desktop 'STELLA_WORLD_KERNEL_V0_1'

        Write-Host ''
        Write-Host '=== 2. REQUIRED ROOTS ===' -ForegroundColor Cyan
        foreach ($Pair in @(
            @('V0_1_ROOT',$V01Root),
            @('V0_2_ROOT',$V02Root),
            @('WORLD_KERNEL_ROOT',$WKRoot)
        )) {
            $Exists = Test-Path -LiteralPath $Pair[1] -PathType Container -ErrorAction Stop
            Write-Host ("{0}|EXISTS={1}|PATH={2}" -f $Pair[0],$(if ($Exists) {'YES'} else {'NO'}),$Pair[1])
            if (-not $Exists) { Add-Hold ($Pair[0] + '_MISSING') }
        }

        Write-Host ''
        Write-Host '=== 3. WORLD KERNEL / A18 CURRENTNESS ===' -ForegroundColor Cyan
        if (Test-Path -LiteralPath $WKRoot -PathType Container -ErrorAction Stop) {
            $WKFiles = @(Get-ChildItem -LiteralPath $WKRoot -File -Recurse -Force -ErrorAction Stop)
            Write-Host ("WORLD_KERNEL_RECURSIVE_FILE_COUNT={0}" -f $WKFiles.Count)
            Write-Host 'WORLD_KERNEL_EXPECTED_FILE_COUNT=129'
            Write-Host ("WORLD_KERNEL_FILE_COUNT_MATCH={0}" -f $(if ($WKFiles.Count -eq 129) {'YES'} else {'NO'}))
            if ($WKFiles.Count -ne 129) { Add-Hold 'WORLD_KERNEL_FILE_COUNT_DRIFT' }

            Check-File 'A18' `
                (Join-Path $WKRoot 'DEVELOPMENT_MEMORY\STELLA_A18_SEMANTIC_RESOLUTION_SYNTHESIS_CHECKPOINT_V0_1.md') `
                '45C26E2626E1950F1ACF1FFB63B6B9993FBBDEEF53A6918C145E2E6BD42CCB7F' 16969
        }

        Write-Host ''
        Write-Host '=== 4. V0.1 PROTECTED BASELINE HASHES ===' -ForegroundColor Cyan
        Check-File 'V0_1_CONFIG_BASELINE' (Join-Path $V01Root 'Luanti\minetest.conf') '3533EEA4FA014548DE059CC7F018E3BD260293FCF0635E79B85979302D91A72E'
        Check-File 'V0_1_CORE_INIT_BASELINE' (Join-Path $V01Root 'Luanti\games\stella_playground\mods\stella_core\init.lua') '65D1140278CF7FC6A149C74C2AD5289628099FFCB8F598DD085B21A1FDD2B716'
        Check-File 'V0_1_RECEIPT_BASELINE' (Join-Path $V01Root 'STELLA_PLAYGROUND_DEPLOYMENT_RECEIPT_V0_1_R1.json') 'A80D124CD026ACCF8CA20E3C53F53AB4614CF15E884F0DCF33776DC1466CB346'

        Write-Host ''
        Write-Host '=== 5. LUANTI EXECUTABLE IDENTITY ===' -ForegroundColor Cyan
        $ExpectedLuantiHash = '7091913D6C7D1FACCF0F1895A9C009FC51C8F409DFFD577ABF17BAFC6AA1715F'
        Check-File 'LUANTI_V0_2_EXECUTABLE' (Join-Path $V02Root 'Luanti\bin\luanti.exe') $ExpectedLuantiHash
        Check-File 'LUANTI_V0_1_EXECUTABLE' (Join-Path $V01Root 'Luanti\bin\luanti.exe') $ExpectedLuantiHash

        Write-Host ''
        Write-Host '=== 6. PROCESS QUIESCENCE ===' -ForegroundColor Cyan
        $Running = @(Get-Process -ErrorAction Stop |
            Where-Object { $_.ProcessName -match '(?i)^(luanti|minetest|luantiserver|minetestserver)$' })
        Write-Host ("RELEVANT_LUANTI_PROCESS_COUNT={0}" -f $Running.Count)
        foreach ($P in $Running) {
            $PPath = ''
            try { $PPath = $P.Path } catch { $PPath = '' }
            Write-Host ("PROCESS|NAME={0}|PID={1}|PATH={2}" -f $P.ProcessName,$P.Id,$PPath)
        }
        if ($Running.Count -gt 0) { Add-Hold 'LUANTI_PROCESS_NOT_QUIESCENT' }

        Write-Host ''
        Write-Host '=== 7. V2-02 ACTIVE CODE / RECEIPTS ===' -ForegroundColor Cyan
        Check-File 'STELLA_DIALOGUE_INIT' (Join-Path $V02Root 'Luanti\games\stella_v0_2_shell\mods\stella_dialogue\init.lua') '6DC2E9A90CB7772C6C46B627F79D146E1C74397108C2E6AAF22EF37153A754EE'
        Check-File 'STELLA_INHABITANTS_INIT' (Join-Path $V02Root 'Luanti\games\stella_v0_2_shell\mods\stella_inhabitants\init.lua') 'FB36E8B3ECE92DA6C73C23BDA88C5C53F6A3A92BA402328735800536B1725519'
        Check-File 'V2_02A_BUILD_RECEIPT' (Join-Path $V02Root 'V2_02A_BUILD_RECEIPT.txt') 'B141B05A4FC9A40053CF354FA8FD072707AC1C8041C07D9825D98BD3654A15A0'
        Check-File 'V2_02R1A_R1_REPAIR_RECEIPT' (Join-Path $V02Root 'V2_02R1A_R1_VISUAL_REPAIR_RECEIPT.txt') '76C103F80CE75915B74108D8DCF56BABD9FC79EA4679F019116BE33E58803119'

        Write-Host ''
        Write-Host '=== 8. V0.2 WORLD IDENTITY ===' -ForegroundColor Cyan
        $WorldMt = Join-Path $V02Root 'Luanti\worlds\stella_v0_2_shell_world\world.mt'
        if (-not (Test-Path -LiteralPath $WorldMt -PathType Leaf -ErrorAction Stop)) {
            Write-Host ("WORLD_MT|EXISTS=NO|PATH={0}" -f $WorldMt)
            Add-Hold 'WORLD_MT_MISSING'
        } else {
            $WorldText = Get-Content -LiteralPath $WorldMt -Raw -ErrorAction Stop
            $WorldMatch = ($WorldText -match '(?m)^\s*gameid\s*=\s*stella_v0_2_shell\s*$')
            Write-Host ("WORLD_MT|EXISTS=YES|GAME_ID_MATCH={0}|PATH={1}" -f $(if ($WorldMatch) {'YES'} else {'NO'}),$WorldMt)
            if (-not $WorldMatch) { Add-Hold 'WORLD_MT_V0_2_IDENTITY_DRIFT' }
        }

        Write-Host ''
        Write-Host '=== 9. V2-02R1B RUNTIME EVIDENCE / OPEN OBSERVATIONS ===' -ForegroundColor Cyan
        $RuntimeLog = Join-Path $V02Root 'V2_02R1B_RUNTIME.log'
        Check-File 'V2_02R1B_RUNTIME_LOG' $RuntimeLog '68AF668526974D5B31385BF88EE8AB42DFE40426CF964FDE9D037197E8E44DF3'
        if (Test-Path -LiteralPath $RuntimeLog -PathType Leaf -ErrorAction Stop) {
            $Stone = @(Select-String -LiteralPath $RuntimeLog -Pattern "Mapgen alias 'mapgen_stone' is invalid" -SimpleMatch -ErrorAction Stop)
            $Water = @(Select-String -LiteralPath $RuntimeLog -Pattern "Mapgen alias 'mapgen_water_source' is invalid" -SimpleMatch -ErrorAction Stop)
            $ServerErrors = @(Select-String -LiteralPath $RuntimeLog -Pattern 'ERROR[ServerStart]' -SimpleMatch -ErrorAction Stop)
            Write-Host ("OPEN_01_MAPGEN_STONE_COUNT={0}" -f $Stone.Count)
            Write-Host ("OPEN_02_MAPGEN_WATER_COUNT={0}" -f $Water.Count)
            Write-Host ("SERVERSTART_ERROR_COUNT={0}" -f $ServerErrors.Count)
        }
        Write-Host 'OPEN_01_STATUS=CARRIED_FORWARD_UNRESOLVED_NONBLOCKING_FOR_STATE_FOUNDATION'
        Write-Host 'OPEN_02_STATUS=CARRIED_FORWARD_UNRESOLVED_NONBLOCKING_FOR_STATE_FOUNDATION'
        Write-Host 'OPEN_03_STATUS=HUMAN_OBSERVATION_REQUIRES_LATER_MOVEMENT_ORIENTATION_RETEST'
        Write-Host 'OPEN_04_STATUS=TEMPORARY_MARA_BODY_DEFERRED_TO_V2_05'
        Write-Host 'OPEN_05_STATUS=RUNTIME_HARNESS_MUST_DISTINGUISH_FATAL_ERROR_WARNING_KNOWN_NONBLOCKING'
        Write-Host 'OPEN_06_STATUS=ORCHESTRATION_DOCUMENT_CURRENTNESS_DRIFT_REQUIRES_DOC_RECONCILIATION_AFTER_LOCAL_REVERIFY'

        Write-Host ''
        Write-Host '=== 10. V2-03 TARGET FREEDOM ===' -ForegroundColor Cyan
        $StateTarget = Join-Path $V02Root 'Luanti\games\stella_v0_2_shell\mods\stella_state'
        $StateExists = Test-Path -LiteralPath $StateTarget -ErrorAction Stop
        Write-Host ("STELLA_STATE_TARGET_EXISTS={0}|PATH={1}" -f $(if ($StateExists) {'YES'} else {'NO'}),$StateTarget)
        if ($StateExists) { Add-Hold 'V2_03_STELLA_STATE_TARGET_NOT_FREE' }
    }
    catch {
        Write-Host ("UNHANDLED_OBSERVATION_ERROR={0}" -f $_.Exception.Message)
        Add-Hold 'UNHANDLED_OBSERVATION_ERROR'
    }

    Write-Host ''
    Write-Host '=== 11. REVERIFY RESULT — EVIDENCE ONLY ===' -ForegroundColor Cyan
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
}

Invoke-StellaV203MorningReverify
