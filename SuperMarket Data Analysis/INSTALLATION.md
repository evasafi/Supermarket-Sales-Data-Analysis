# Installation Guide

Complete step-by-step guide to install and set up the Supermarket Analytics project.

---

## 📋 System Requirements

- **Python:** 3.8 or higher
- **OS:** Windows, macOS, or Linux
- **RAM:** 2GB minimum (4GB recommended)
- **Disk Space:** 500MB free space
- **Internet:** Required for pip package installation

---

## 🚀 Quick Install (5 minutes)

### 1. Download Repository
```bash
git clone https://github.com/yourusername/supermarket-analytics.git
cd supermarket-analytics
```

### 2. Create Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate it
# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Launch Jupyter
```bash
jupyter lab
```

**Done!** ✅

---

## 📝 Step-by-Step Installation

### Step 1: Install Python

**Windows:**
1. Go to [python.org](https://www.python.org/downloads/)
2. Download Python 3.10+ installer
3. Run installer
4. ✅ Check "Add Python to PATH"
5. Click Install

**macOS:**
```bash
# Using Homebrew
brew install python3

# Or download from python.org
```

**Linux:**
```bash
sudo apt-get update
sudo apt-get install python3 python3-venv python3-pip
```

### Step 2: Clone Repository

```bash
# Using Git
git clone https://github.com/yourusername/supermarket-analytics.git

# Or download as ZIP from GitHub
# Then extract the folder
```

### Step 3: Navigate to Project
```bash
cd supermarket-analytics
```

### Step 4: Create Virtual Environment

A virtual environment isolates project dependencies.

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

You should see `(venv)` in your terminal prompt when activated.

### Step 5: Install Dependencies

```bash
# Upgrade pip first
pip install --upgrade pip

# Install requirements
pip install -r requirements.txt
```

### Step 6: Verify Installation

```bash
# Check Python version
python --version

# Check if pandas is installed
python -c "import pandas; print(f'Pandas {pandas.__version__}')"

# Check if matplotlib is installed
python -c "import matplotlib; print(f'Matplotlib {matplotlib.__version__}')"
```

All should print version numbers.

### Step 7: Launch Jupyter

```bash
jupyter lab
```

Jupyter Lab should open in your browser at `http://localhost:8888`

---

## 🛠️ Troubleshooting Installation

### ❌ "Python command not found"

**Solution:**
- **Windows:** Add Python to PATH
  1. Go to Settings → Environment Variables
  2. Add Python installation folder to PATH
  3. Restart terminal

- **macOS/Linux:** Use `python3` instead of `python`
  ```bash
  python3 --version
  ```

---

### ❌ "pip: command not found"

**Solution:**
```bash
# Use Python module instead
python -m pip install -r requirements.txt

# Or install pip
python -m ensurepip --upgrade
```

---

### ❌ "venv not recognized"

**Solution:**
```bash
# On Windows, try this path explicitly
python -m venv venv
venv\Scripts\activate

# If still fails, install venv
python -m pip install venv
```

---

### ❌ "Module not found" errors

**Solution:**
```bash
# Make sure virtual environment is activated
source venv/bin/activate  # macOS/Linux
# OR
venv\Scripts\activate     # Windows

# Then install again
pip install -r requirements.txt
```

---

### ❌ "Jupyter not launching"

**Solution:**
```bash
# Verify Jupyter is installed
python -m jupyter --version

# If not, install it
pip install jupyter jupyterlab

# Then launch
jupyter lab
```

---

### ❌ Port 8888 already in use

**Solution:**
```bash
# Use different port
jupyter lab --port 8889

# Or kill process using port 8888
# On Windows:
netstat -ano | findstr :8888
taskkill /PID <PID> /F

# On macOS/Linux:
lsof -i :8888
kill -9 <PID>
```

---

## 🔄 Updating Installation

### Update All Packages
```bash
pip install -r requirements.txt --upgrade
```

### Update Specific Package
```bash
pip install pandas --upgrade
```

### Check Installed Versions
```bash
pip list
```

---

## 🐍 Using Anaconda (Alternative)

If you prefer Anaconda distribution:

### 1. Install Anaconda
- Download from [anaconda.com](https://www.anaconda.com/download)
- Run installer

### 2. Create Environment
```bash
conda create -n supermarket python=3.10
conda activate supermarket
```

### 3. Install Dependencies
```bash
conda install -c conda-forge pandas numpy matplotlib seaborn jupyter jupyterlab
```

### 4. Launch Jupyter
```bash
jupyter lab
```

---

## 🐳 Docker Installation (Optional)

For consistent environments across machines:

### 1. Create Dockerfile
```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["jupyter", "lab", "--ip=0.0.0.0", "--allow-root"]
```

### 2. Build Image
```bash
docker build -t supermarket-analytics .
```

### 3. Run Container
```bash
docker run -p 8888:8888 -v $(pwd):/app supermarket-analytics
```

---

## ✅ Verify Complete Installation

Run this script to test everything:

```python
# test_installation.py
import sys

def test_installation():
    """Test if all required packages are installed."""
    
    packages = {
        'pandas': '✅ Pandas',
        'numpy': '✅ NumPy',
        'matplotlib': '✅ Matplotlib',
        'seaborn': '✅ Seaborn',
        'jupyter': '✅ Jupyter',
    }
    
    print("Testing Installation...")
    print("=" * 50)
    print(f"Python Version: {sys.version}")
    print("=" * 50)
    
    all_good = True
    for package, name in packages.items():
        try:
            __import__(package)
            print(f"{name}")
        except ImportError:
            print(f"❌ {name} - NOT INSTALLED")
            all_good = False
    
    print("=" * 50)
    if all_good:
        print("✅ Installation Complete!")
    else:
        print("❌ Some packages missing. Run: pip install -r requirements.txt")

if __name__ == '__main__':
    test_installation()
```

Run it:
```bash
python test_installation.py
```

---

## 📚 Next Steps

After successful installation:

1. **Read the README**
   ```bash
   cat README.md
   ```

2. **Launch Jupyter Lab**
   ```bash
   jupyter lab
   ```

3. **Open a notebook**
   - Create new notebook
   - Copy code from `implementation_guide.py`
   - Run analysis!

4. **Run the analysis**
   ```python
   exec(open('scripts/supermarket_advanced_analysis.py').read())
   ```

---

## 🆘 Getting Help

**If you're stuck:**

1. Check [Troubleshooting](#troubleshooting-installation) above
2. Read [requirements.txt](requirements.txt) comments
3. Check Python version: `python --version` (should be 3.8+)
4. Search [Issues](https://github.com/yourusername/supermarket-analytics/issues)
5. Open new [Issue](https://github.com/yourusername/supermarket-analytics/issues/new)

---

## 📦 Uninstalling

To remove the project:

```bash
# Deactivate virtual environment
deactivate

# Delete virtual environment folder
rm -rf venv  # macOS/Linux
rmdir /s venv  # Windows

# Delete project folder
cd ..
rm -rf supermarket-analytics  # macOS/Linux
rmdir /s supermarket-analytics  # Windows
```

---

## 🔐 Security Notes

- Never run with `sudo pip install`
- Always use virtual environments
- Keep dependencies updated: `pip list --outdated`
- Don't share `.env` files (if used)

---

## 💡 Pro Tips

### Speed Up Installation
```bash
# Use faster package resolver (pip 20.3+)
pip install --use-deprecated=legacy-resolver -r requirements.txt
```

### Reduce Disk Space
```bash
# Cache packages only
pip download -r requirements.txt -d ./packages
pip install --no-index --find-links ./packages -r requirements.txt
```

### Offline Installation
```bash
# On online machine
pip download -r requirements.txt -d ./packages

# Transfer to offline machine and run
pip install --no-index --find-links ./packages -r requirements.txt
```

---

## 📞 Support

- **Documentation:** See [README.md](README.md)
- **Issues:** [GitHub Issues](https://github.com/yourusername/supermarket-analytics/issues)
- **Discussions:** [GitHub Discussions](https://github.com/yourusername/supermarket-analytics/discussions)
- **Email:** your.email@example.com

---

**Last Updated:** January 2024
