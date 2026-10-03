$ErrorActionPreference = "Stop"
$build = Join-Path (Split-Path $PSScriptRoot -Parent) ".build"   # repo-root .build (this file is in tools/)
$files = Get-Content (Join-Path $build "made.txt")
$qa = @("participant-workbook.docx", "facilitator-guide.docx", "after-the-workshop.docx", "hr-policy-answer.SKILL.docx", "readiness-checklist.docx", "03-skills-catalog.docx", "09-plugins.docx")
$w = New-Object -ComObject Word.Application
$w.Visible = $false
$w.DisplayAlerts = 0
try {
    foreach ($f in $files) {
        $d = $w.Documents.Open($f, $false, $false)
        foreach ($toc in $d.TablesOfContents) { $toc.Update() }
        $d.Fields.Update() | Out-Null
        $pages = $d.ComputeStatistics(2)
        $d.Save()
        $name = [IO.Path]::GetFileName($f)
        if ($qa -contains $name) {
            $d.ExportAsFixedFormat((Join-Path $build ([IO.Path]::GetFileNameWithoutExtension($f) + ".pdf")), 17)
        }
        $d.Close($false)
        "{0,-40} {1,3} pages  toc={2}" -f $name, $pages, $(if ($f -match 'workbook|facilitator|readiness|README') { 'yes' } else { '-' })
    }
} finally { $w.Quit() }
