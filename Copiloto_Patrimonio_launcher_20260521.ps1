Set-Location "C:\SecondBrain\OneDrive - Jordi Molins Coronado\RAM_Jordi\Prevengen\Prototipos\eCoach_Patrimonio"

$latestAgent = Get-ChildItem -Path . -Filter "eCoach_Patrimonio_*.py" |
    Sort-Object LastWriteTime -Descending |
    Select-Object -First 1

if ($null -eq $latestAgent) {
    Write-Host "No eCoach_Patrimonio_*.py file found."
    Read-Host "Press Enter to close"
    exit
}

Write-Host "Running Copiloto Patrimonio file:" $latestAgent.Name

python $latestAgent.FullName

Read-Host "Copiloto Patrimonio stopped. Press Enter to close"

