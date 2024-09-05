import subprocess
import sys

def install_and_import(package):
    try:
        __import__(package)
    except ImportError:
        print(f"{package} not found, installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    finally:
        globals()[package] = __import__(package)

# List of required packages
required_packages = ["pandas", "openpyxl"]

# Install and import each package
for package in required_packages:
    install_and_import(package)