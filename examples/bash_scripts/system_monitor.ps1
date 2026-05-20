<#
.SYNOPSIS
    Antigravity v2 - Windows PowerShell 系統資源安全監控腳本
.DESCRIPTION
    本腳本會定期檢測 Windows 系統的 CPU 與記憶體使用率，並在資源超標時發出警告並記錄至安全日誌。
    具備冪等性與結構化錯誤處理，符合 CWE 最佳安全實踐。
.PARAMETER Threshold
    警報臨界百分比 (預設 80)
.PARAMETER LogPath
    監控日誌儲存路徑
.EXAMPLE
    .\system_monitor.ps1 -Threshold 75 -LogPath "D:\Logs\monitor.log"
#>

[CmdletBinding()]
param (
    [ValidateRange(1, 100)]
    [int]$Threshold = 80,

    [string]$LogPath = "$PSScriptRoot\system_monitor.log"
)

# 1. 強制以 UTF-8 處理輸出編碼
$OutputEncoding = [System.Text.Encoding]::UTF8

Write-Host "==========================================" -ForegroundColor Cyan
Write-Host "⚡ Antigravity Windows 資源監控引擎" -ForegroundColor Cyan
Write-Host "==========================================" -ForegroundColor Cyan
Write-Host "警報門檻值: $Threshold %"
Write-Host "日誌檔案路徑: $LogPath"

try {
    # 2. 冪等性檢查：確認日誌儲存資料夾是否存在，不存在則建立
    $LogDir = Split-Path -Path $LogPath -Parent
    if (-not (Test-Path -Path $LogDir)) {
        Write-Host "[INFO] 建立日誌目錄: $LogDir" -ForegroundColor Yellow
        New-Item -ItemType Directory -Force -Path $LogDir | Out-Null
    }

    # 3. 取得系統 CPU 使用率
    # 透過 WMI/CIM 取得 CPU 負載
    Write-Host "[RUN] 正在計算 CPU 使用率..." -ForegroundColor Gray
    $CpuLoad = (Get-CimInstance Win32_Processor | Measure-Object -Property LoadPercentage -Average).Average
    $CpuFormatted = [Math]::Round($CpuLoad, 2)

    # 4. 取得系統記憶體使用率
    Write-Host "[RUN] 正在計算記憶體使用率..." -ForegroundColor Gray
    $OS = Get-CimInstance Win32_OperatingSystem
    $TotalVisibleMemory = $OS.TotalVisibleMemorySize
    $FreePhysicalMemory = $OS.FreePhysicalMemory
    $UsedMemoryPercent = (($TotalVisibleMemory - $FreePhysicalMemory) / $TotalVisibleMemory) * 100
    $MemFormatted = [Math]::Round($UsedMemoryPercent, 2)

    # 5. 彙整狀態
    $Timestamp = (Get-Date).ToString("yyyy-MM-dd HH:mm:ss")
    $Status = "CPU: $CpuFormatted% | MEMORY: $MemFormatted%"
    
    Write-Host "[INFO] 當前系統負載: $Status" -ForegroundColor White

    # 6. 超標防禦與報警機制
    if ($CpuLoad -gt $Threshold -or $UsedMemoryPercent -gt $Threshold) {
        $AlertMsg = "⚠️ [WARNING] 資源已超標！ $Timestamp - $Status"
        Write-Host $AlertMsg -ForegroundColor Red
        
        # 冪等性寫入：安全地附加日誌 (Out-File -Append)
        $AlertMsg | Out-File -FilePath $LogPath -Append -Encoding utf8
    } else {
        $NormalMsg = "🟢 [NORMAL] 資源在正常範圍內。 $Timestamp - $Status"
        Write-Host $NormalMsg -ForegroundColor Green
        
        $NormalMsg | Out-File -FilePath $LogPath -Append -Encoding utf8
    }

    Write-Host "✅ 資源監控檢測順利完成。" -ForegroundColor Green
    Write-Host "==========================================" -ForegroundColor Cyan

} catch {
    # 7. 結構化錯誤防禦 (Structured Exception Handling)
    Write-Error "❌ 監控腳本執行時發生未預期錯誤！"
    Write-Error $_.Exception.Message
    exit 1
}
