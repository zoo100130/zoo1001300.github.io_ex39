# Flask Exercises 39-48

This project follows `42-Flask 01 (Exercises 39-48) (Azure_deploy).pdf`.

## Run Locally

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
flask --app app run
```

Open:

- `http://127.0.0.1:5000/`
- `http://127.0.0.1:5000/hello`
- `http://127.0.0.1:5000/user/John`
- `http://127.0.0.1:5000/post/5`
- `http://127.0.0.1:5000/path/class/flask/demo`
- `http://127.0.0.1:5000/apple`
- `http://127.0.0.1:5000/banana`
- `http://127.0.0.1:5000/orange`
- `http://127.0.0.1:5000/page/app`
- `http://127.0.0.1:5000/variables`
- `http://127.0.0.1:5000/double`

## Exercise 48 Only

```powershell
flask --app double run
```

Then open `http://127.0.0.1:5000/`.

## Azure App Service

The root project already contains `app.py`, `requirements.txt`, and `runtime.txt`.

Recommended startup command:

```bash
gunicorn --bind=0.0.0.0 --timeout 600 app:app
```

Zip the project files at the root of the archive, not inside an extra folder. For example:

```powershell
Compress-Archive -Path app.py,double.py,requirements.txt,runtime.txt,templates,static -DestinationPath flask-exercises.zip -Force
```

After creating the Azure Web App, deploy the ZIP through Deployment Center or Azure CLI.

PowerShell deploy helper:

```powershell
winget install --exact --id Microsoft.AzureCLI
az login
.\deploy-azure.ps1 -AppServiceName "<your-web-app-name>" -ResourceGroupName "<your-resource-group-name>"
```

The script recreates `flask-exercises.zip` with project files at the ZIP root, sets
`SCM_DO_BUILD_DURING_DEPLOYMENT=true`, and deploys it with `az webapp deploy`.

## Render

This project also works on Render.

Manual setup in the Render dashboard:

```text
Runtime: Python
Build Command: pip install -r requirements.txt
Start Command: gunicorn --bind 0.0.0.0:$PORT app:app
```

The repository also includes [render.yaml](./render.yaml) for Blueprint-based setup.

Typical steps:

1. Push this project to GitHub.
2. Sign in to [Render](https://render.com/).
3. Create a new Web Service from the GitHub repository, or use Blueprint with `render.yaml`.
4. Wait for the first deploy to finish.
5. Open the generated `.onrender.com` URL.
