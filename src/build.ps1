# Builds the static site in ..\site from templates\ and strings\.
# Run from anywhere:  powershell -ExecutionPolicy Bypass -File src\build.ps1
# Finnish pages go in site\, Swedish in site\sv\, English in site\en\.

$ErrorActionPreference = 'Stop'
$src   = $PSScriptRoot
$out   = Join-Path (Split-Path $src -Parent) 'site'
$utf8  = New-Object System.Text.UTF8Encoding($false)
$domain = 'https://jnwebdesign.com/'

$langs = @('fi', 'sv', 'en')
$pages = @('index', 'work', 'services', 'about', 'contact')

function Read-Text($path) { [IO.File]::ReadAllText($path, $utf8) }

$config = Read-Text (Join-Path $src 'config.json') | ConvertFrom-Json

$layout = Read-Text (Join-Path $src 'templates\_layout.html')
$cta    = Read-Text (Join-Path $src 'templates\_cta.html')

function Get-LangPath($lang) { if ($lang -eq 'fi') { '' } else { "$lang/" } }

$missing = @{}
foreach ($lang in $langs) {
  $json = Read-Text (Join-Path $src "strings\$lang.json") | ConvertFrom-Json
  $s = @{}
  $json.PSObject.Properties | ForEach-Object { $s[$_.Name] = $_.Value }
  $config.PSObject.Properties | ForEach-Object { $s[$_.Name] = $_.Value }

  $dir = Join-Path $out (Get-LangPath $lang)
  if (-not (Test-Path $dir)) { New-Item -ItemType Directory -Force $dir | Out-Null }
  $base = if ($lang -eq 'fi') { '' } else { '../' }

  foreach ($page in $pages) {
    $file = "$page.html"
    $body = (Read-Text (Join-Path $src "templates\$file")).Replace('{{cta_band}}', $cta.TrimEnd())
    $html = $layout.Replace('{{content}}', $body.TrimEnd())

    $v = @{} + $s
    $v['page']  = $page
    $v['base']  = $base
    $v['title'] = $s["t_$page"]
    $v['desc']  = $s["d_$page"]
    foreach ($p in 'work','services','about','contact') { $v["cur_$p"] = if ($p -eq $page) { ' aria-current="page"' } else { '' } }
    foreach ($l in $langs) {
      $v["href_$l"]    = $base + (Get-LangPath $l) + $file
      $v["abs_$l"]     = $domain + (Get-LangPath $l) + $(if ($page -eq 'index') { '' } else { $file })
      $v["curlang_$l"] = if ($l -eq $lang) { ' aria-current="true"' } else { '' }
    }
    $v['abs_self'] = $v["abs_$lang"]

    $html = [regex]::Replace($html, '\{\{([a-z0-9_]+)\}\}', {
      param($m)
      $k = $m.Groups[1].Value
      if ($v.ContainsKey($k)) { [string]$v[$k] } else { $missing["$lang/$file : $k"] = 1; $m.Value }
    })
    [IO.File]::WriteAllText((Join-Path $dir $file), $html.Replace("`r`n", "`n"), $utf8)
  }
  "built $lang"
}
if ($missing.Count) { "MISSING KEYS:"; $missing.Keys | Sort-Object; exit 1 }
