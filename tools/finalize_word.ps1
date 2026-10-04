# Refresh contents pages and fields in the Word files listed in .build/made.txt; with -Pdf, also export QA
# PDFs to .build/ (opt-in: the export often stalls right after an update, but works in a later run). Each job runs in its own PowerShell process with its own Word instance and a time limit: running several
# jobs in one process intermittently hung Word with no visible dialog. Progress goes to .build/finalize.log.
param([string]$Job, [string]$File, [switch]$Pdf)
$ErrorActionPreference = "Stop"
$build = Join-Path (Split-Path $PSScriptRoot -Parent) ".build"   # repo-root .build (this file is in tools/)
$log = Join-Path $build "finalize.log"

if ($Job) {
    $w = New-Object -ComObject Word.Application
    $w.Visible = $false
    $w.DisplayAlerts = 0
    try {
        if ($Job -eq "update") {
            $d = $w.Documents.Open($File, $false, $false)
            foreach ($toc in $d.TablesOfContents) { $toc.Update() }
            $d.Fields.Update() | Out-Null
            $d.ComputeStatistics(2)   # page count, read by the parent
            $d.Save()
        } else {
            $d = $w.Documents.Open($File, $false, $true)
            $d.ExportAsFixedFormat((Join-Path $build ([IO.Path]::GetFileNameWithoutExtension($File) + ".pdf")), 17)
        }
        $d.Close($false)
    } finally { $w.Quit() }
    exit 0
}

$files = Get-Content (Join-Path $build "made.txt")
$qa = @("participant-workbook.docx", "facilitator-guide.docx", "after-the-workshop.docx", "hr-policy-answer.SKILL.docx", "readiness-checklist.docx", "03-skills-catalog.docx", "09-plugins.docx")
"start $(Get-Date -f T)" | Set-Content $log

function Run-Job($job, $file, $seconds = 180) {
    $out = Join-Path $build "finalize-job.txt"
    $before = @(Get-Process WINWORD -ErrorAction SilentlyContinue | ForEach-Object Id)
    $p = Start-Process powershell -PassThru -NoNewWindow -RedirectStandardOutput $out `
        -ArgumentList "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", "`"$PSCommandPath`"", "-Job", $job, "-File", "`"$file`""
    if (-not $p.WaitForExit($seconds * 1000)) {
        $p.Kill()
        # Stop only the Word instance this job started (never the user's own Word windows).
        Get-Process WINWORD -ErrorAction SilentlyContinue | Where-Object { $before -notcontains $_.Id } | Stop-Process -Force
        Remove-Item (Join-Path (Split-Path $file) ("~$" + (Split-Path $file -Leaf).Substring(2))) -Force -ErrorAction SilentlyContinue
        "$job $file TIMED OUT" | Add-Content $log
        return $null
    }
    "$job $([IO.Path]::GetFileName($file)) ok" | Add-Content $log
    return (Get-Content $out -ErrorAction SilentlyContinue | Select-Object -Last 1)
}

foreach ($f in $files) {
    $name = [IO.Path]::GetFileName($f)
    $pages = Run-Job "update" $f
    $pdfNote = if ($Pdf -and $qa -contains $name) { if ($null -ne (Run-Job "pdf" $f)) { "pdf" } else { "PDF FAILED" } } else { "" }
    if ($null -eq $pages) { $pages = "FAILED" }
    "{0,-40} {1,6} pages  toc={2}  {3}" -f $name, $pages, $(if ($f -match 'workbook|facilitator|readiness|README') { 'yes' } else { '-' }), $pdfNote
}
"done $(Get-Date -f T)" | Add-Content $log
