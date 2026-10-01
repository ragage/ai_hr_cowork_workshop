$ErrorActionPreference = "Stop"
$build = if ($env:KIT_BUILD) { $env:KIT_BUILD } else { Join-Path (Split-Path $PSScriptRoot -Parent) ".build" }
$files = Get-Content (Join-Path $build "made.txt")
$qa = @("participant-workbook.docx", "facilitator-guide.docx", "after-the-workshop.docx", "hr-policy-answer.SKILL.docx", "readiness-checklist.docx", "03-skills-catalog.docx", "09-plugins.docx")

function New-Word {
    $app = New-Object -ComObject Word.Application
    $app.Visible = $false
    $app.DisplayAlerts = 0
    return $app
}

$w = New-Word
try {
    foreach ($f in $files) {
        $d = $w.Documents.Open($f, $false, $false)
        foreach ($toc in $d.TablesOfContents) { $toc.Update() }
        $d.Fields.Update() | Out-Null
        $pages = $d.ComputeStatistics(2)
        $d.Save()
        $d.Close($false)
        "{0,-40} {1,3} pages  toc={2}" -f [IO.Path]::GetFileName($f), $pages, $(if ($f -match 'workbook|facilitator|readiness|README') { 'yes' } else { '-' })
    }
} finally { $w.Quit() }

# QA PDFs from read-only copies in a fresh Word instance: exporting in the instance that just
# edited and saved the documents can hang Word.
$w = New-Word
try {
    foreach ($f in $files | Where-Object { $qa -contains [IO.Path]::GetFileName($_) }) {
        $d = $w.Documents.Open($f, $false, $true)
        $d.ExportAsFixedFormat((Join-Path $build ([IO.Path]::GetFileNameWithoutExtension($f) + ".pdf")), 17)
        $d.Close($false)
        "QA PDF: " + [IO.Path]::GetFileNameWithoutExtension($f) + ".pdf"
    }
} finally { $w.Quit() }
