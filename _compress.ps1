Add-Type -AssemblyName System.Drawing
$hub = "C:\AndroidStudioProjects\batch20-hubs\fairgocasino"

function Compress-Jpg([string]$path, [int]$maxW = 1600, [int]$q = 78) {
  $img = [System.Drawing.Image]::FromFile($path)
  $w = $img.Width; $h = $img.Height
  if ($w -gt $maxW) { $h = [int]($h * $maxW / $w); $w = $maxW }
  $bmp = New-Object System.Drawing.Bitmap $w, $h
  $g = [System.Drawing.Graphics]::FromImage($bmp)
  $g.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
  $g.DrawImage($img, 0, 0, $w, $h)
  $img.Dispose(); $g.Dispose()
  $codec = [System.Drawing.Imaging.ImageCodecInfo]::GetImageEncoders() | Where-Object { $_.MimeType -eq "image/jpeg" }
  $ep = New-Object System.Drawing.Imaging.EncoderParameters 1
  $ep.Param[0] = New-Object System.Drawing.Imaging.EncoderParameter ([System.Drawing.Imaging.Encoder]::Quality, [long]$q)
  $tmp = $path + ".tmp.jpg"
  $bmp.Save($tmp, $codec, $ep)
  $bmp.Dispose()
  Move-Item -Force $tmp $path
}

Get-ChildItem -Recurse -Filter *.jpg $hub | ForEach-Object {
  Compress-Jpg $_.FullName
  Write-Host ("JPG {0} {1}" -f $_.Name, $_.Length)
}

# logo: already PNG; resize via GDI
$logo = Join-Path $hub "assets\brand\logo.png"
$src = [System.Drawing.Image]::FromFile($logo)
$side = 512
$bmp = New-Object System.Drawing.Bitmap $side, $side
$g = [System.Drawing.Graphics]::FromImage($bmp)
$g.Clear([System.Drawing.Color]::Transparent)
$g.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
$scale = [Math]::Min($side / $src.Width, $side / $src.Height)
$nw = [int]($src.Width * $scale); $nh = [int]($src.Height * $scale)
$g.DrawImage($src, [int](($side-$nw)/2), [int](($side-$nh)/2), $nw, $nh)
$src.Dispose(); $g.Dispose()
$tmp = $logo + ".tmp.png"
$bmp.Save($tmp, [System.Drawing.Imaging.ImageFormat]::Png)
$bmp.Dispose()
Move-Item -Force $tmp $logo
Write-Host ("LOGO {0}" -f (Get-Item $logo).Length)

function Make-Fav([int]$size, [string]$name, [bool]$bg) {
  $mark = [System.Drawing.Image]::FromFile($logo)
  $c = New-Object System.Drawing.Bitmap $size, $size
  $g = [System.Drawing.Graphics]::FromImage($c)
  if ($bg) { $g.Clear([System.Drawing.Color]::FromArgb(255,20,83,45)) } else { $g.Clear([System.Drawing.Color]::Transparent) }
  $g.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
  $pad = [Math]::Max(2, [int]($size/10))
  $box = $size - 2*$pad
  $g.DrawImage($mark, $pad, $pad, $box, $box)
  $mark.Dispose(); $g.Dispose()
  $out = Join-Path $hub $name
  $c.Save($out, [System.Drawing.Imaging.ImageFormat]::Png)
  $c.Dispose()
}
Make-Fav 32 "favicon-32x32.png" $true
Make-Fav 48 "favicon-48x48.png" $true
Make-Fav 96 "favicon-96x96.png" $true
Make-Fav 192 "favicon-192x192.png" $true
Make-Fav 180 "apple-touch-icon.png" $true
Copy-Item (Join-Path $hub "favicon-32x32.png") (Join-Path $hub "favicon.ico") -Force
Write-Host "favicons ok"
