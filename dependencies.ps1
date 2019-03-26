$source = @()
$source += 'https://www.7-zip.org/a/7z1806-x64.exe'
$source += 'https://github.com/mozilla/geckodriver/releases/download/v0.23.0/geckodriver-v0.23.0-win64.zip'

ForEach ( $item in $source ) {
	$file = $currentDir + '\' + ($item).split('/')[-1]
	curl $item -Outfile $file
}

start 7z1806-x64.exe
C:\Program` Files\7-Zip\7z x geckodriver-v0.23.0-win64.zip
echo "$env:Path += ';' + $currentDir" >> %UserProfile%\Documents\WindowsPowerShell\profile.ps1 # Microsoft.PowerShell_profile.ps1
