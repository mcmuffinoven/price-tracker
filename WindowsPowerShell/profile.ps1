
#region conda initialize
# !! Contents within this block are managed by 'conda init' !!
(& "C:\ProgramData\Anaconda3\Scripts\conda.exe" "shell.powershell" "hook") | Out-String | Invoke-Expression
#endregion
oh-my-posh --init --shell pwsh --config ~/jandedobbeleer.omp.json | Invoke-Expression
