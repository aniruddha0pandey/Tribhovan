# Tribhovan
A Multi-valued Functional Decomposition Analysis for SDP microprocessors.

```powershell
> wget 'https://www.7-zip.org/a/7z1806-x64.exe' 'https://github.com/mozilla/geckodriver/releases/download/v0.23.0/geckodriver-v0.23.0-win64.zip'
> C:\Program` Files\7-Zip\7z x geckodriver-v0.23.0-win64.zip
> echo "$env:Path += ';' + (Get-Location).tostring()" >> %UserProfile%\Documents\WindowsPowerShell\profile.ps1
> 
> wget 'https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe'
> start /wait "" Miniconda4-latest-Windows-x86_64.exe /InstallationType=JustMe /AddToPath=0 /RegisterPython=0 /S /D=%UserProfile%\Miniconda3
> conda update conda
> conda create --name tribhovan python=3
> activate tribhovan
> python -m pip install --upgrade pip
> pip install qiskit selenium
> python get_token.py main.py
```
