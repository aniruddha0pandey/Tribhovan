# Tribhovan
A Multi-valued Functional Decomposition Analysis for SDP Microprocessors. This circuit simulator is part of my undergraduate thesis, SDP Microprocessor is curretly in R&D phase heavily inspired by RISC-V Architecture.  
These decomposition algorithms are simulated with [IBM Q 5 Tenerife (ibmqx4)](https://quantumexperience.ng.bluemix.net/qx/editor), 5-qubits supported.
  
**API_TOKEN** is fetched each session rather than saving credentials on disk for portability. Only Firefox is supported currently.
```powershell
> set-executionpolicy remotesigned
> PowerShell -File .\dependencies.ps1
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
