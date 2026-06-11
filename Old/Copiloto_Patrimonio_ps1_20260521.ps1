Set-Location "C:\SecondBrain\OneDrive - Jordi Molins Coronado\RAM_Jordi\Prevengen\Prototipos\Jordi_Agent"

$latestAgent = Get-ChildItem -Path . -Filter "Jordi_Agent_*.py" |
    Sort-Object LastWriteTime -Descending |
    Select-Object -First 1

if ($null -eq $latestAgent) {
    Write-Host "No Jordi_Agent_*.py file found."
    Read-Host "Press Enter to close"
    exit
}

Write-Host "Running agent file:" $latestAgent.Name

python $latestAgent.FullName

Read-Host "Agent stopped. Press Enter to close"
