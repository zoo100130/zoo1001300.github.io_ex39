param(
    [Parameter(Mandatory = $true)]
    [string]$AppServiceName,

    [Parameter(Mandatory = $true)]
    [string]$ResourceGroupName,

    [string]$ZipPath = (Join-Path $PSScriptRoot "flask-exercises.zip")
)

$ErrorActionPreference = "Stop"

if (-not (Get-Command az -ErrorAction SilentlyContinue)) {
    throw "Azure CLI was not found. Install it with: winget install --exact --id Microsoft.AzureCLI"
}

Push-Location $PSScriptRoot
try {
    Compress-Archive `
        -Path "app.py", "double.py", "requirements.txt", "runtime.txt", "templates", "static" `
        -DestinationPath $ZipPath `
        -Force
}
finally {
    Pop-Location
}

az webapp config set `
    --name $AppServiceName `
    --resource-group $ResourceGroupName `
    --startup-file "gunicorn --bind=0.0.0.0 --timeout 600 app:app"

az webapp config appsettings set `
    --name $AppServiceName `
    --resource-group $ResourceGroupName `
    --settings SCM_DO_BUILD_DURING_DEPLOYMENT=true

az webapp deploy `
    --name $AppServiceName `
    --resource-group $ResourceGroupName `
    --src-path $ZipPath `
    --type zip

Write-Host "Deployed to: https://$AppServiceName.azurewebsites.net"
