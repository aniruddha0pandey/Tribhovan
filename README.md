# Tribhovan
A Multi-valued Functional Decomposition Analysis for SDP microprocessors.  
Simulated with [IBM Q 5 Tenerife (ibmqx4)](https://quantumexperience.ng.bluemix.net/qx/editor), 5-qubits supported.
  
**API_TOKEN** is fetched each session rather than saving credentials on disk for portability.
```powershell
> # Drivers for Selenium
> $source = 'https://www.7-zip.org/a/7z1806-x64.exe'
> $currentDir = (Get-Location).tostring()
> curl $source -Outfile $currentDir
> $source = @()
> $source = 'https://github.com/mozilla/geckodriver/releases/download/v0.23.0/geckodriver-v0.23.0-win64.zip'
> curl $source -Outfile $currentDir
> C:\Program` Files\7-Zip\7z x geckodriver-v0.23.0-win64.zip
> echo "$env:Path += ';' + $currentDir" >> %UserProfile%\Documents\WindowsPowerShell\profile.ps1
> # Virtuat-Envirnoment Setup
> wget 'https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe'
> start /wait "" Miniconda4-latest-Windows-x86_64.exe /InstallationType=JustMe /AddToPath=0 /RegisterPython=0 /S /D=%UserProfile%\Miniconda3
> conda update conda
> conda create --name tribhovan python=3
> activate tribhovan
> python -m pip install --upgrade pip
> pip install qiskit selenium clipboard
> python get_token.py main.py
```
