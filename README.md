# Future You: A Financial Story

A simple interactive web simulation that teaches financial literacy and retirement planning.

This guide explains how to set up the environment and run the project locally (backend + frontend).

---

## ⚙️ Environment Setup

Follow these steps to get the project running locally.

### 1. Clone the repository

```bash
git clone https://github.com/NithilB/EdtechProject.git
cd EdtechProject/story-finance-game
```

### 2. Create a Python virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

On Windows (PowerShell):

```powershell
venv\Scripts\Activate.ps1
```

On Windows (cmd.exe):

```cmd
venv\Scripts\activate.bat
```

On macOS / Linux:

```bash
source venv/bin/activate
```

### 4. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the backend (Flask)

```bash
cd backend
python app.py
```

The backend will start at http://127.0.0.1:5000/ by default.