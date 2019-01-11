# Tribhovan
A Multi-valued Functional Decomposition Analysis for SDP Microprocessors. As part of my major project, SDP Microprocessor is curretly in R&D phase heavily inspired by RISC-V Architecture.  
These decomposition algorithms are simulated with [IBM Q 5 Tenerife (ibmqx4)](https://quantumexperience.ng.bluemix.net/qx/editor), 5-qubits supported.
  
**API_TOKEN** is fetched each session rather than saving credentials on disk for portability. Only Firefox is supported currently.
```powershell
> # Drivers for Selenium
> $source = 'https://www.7-zip.org/a/7z1806-x64.exe'
> $currentDir = (Get-Location).tostring()
> curl $source -Outfile $currentDir + '\7z1806-x64.exe'
> $source = @()
> $source = 'https://github.com/mozilla/geckodriver/releases/download/v0.23.0/geckodriver-v0.23.0-win64.zip'
> curl $source -Outfile $currentDir + '\geckodriver-v0.23.0-win64.zip'
> start 7z1806-x64.exe
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
