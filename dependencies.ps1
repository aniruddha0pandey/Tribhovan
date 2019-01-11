$source = 'https://www.7-zip.org/a/7z1806-x64.exe'
$currentDir = (Get-Location).tostring()
curl $source -Outfile $currentDir + '\7z1806-x64.exe'
$source = @()
$source = 'https://github.com/mozilla/geckodriver/releases/download/v0.23.0/geckodriver-v0.23.0-win64.zip'
curl $source -Outfile $currentDir + '\geckodriver-v0.23.0-win64.zip'
start 7z1806-x64.exe
C:\Program` Files\7-Zip\7z x geckodriver-v0.23.0-win64.zip
echo "$env:Path += ';' + $currentDir" >> %UserProfile%\Documents\WindowsPowerShell\profile.ps1
