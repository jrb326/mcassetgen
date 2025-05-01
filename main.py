import os
import subprocess
import sys

def setup_environment():
    # Clone the sd-scripts repository
    if not os.path.exists("sd-scripts"):
        subprocess.run(["git", "clone", "https://github.com/your-repo/sd-scripts.git"], check=True)

    # Navigate to the sd-scripts directory
    os.chdir("sd-scripts")

    # Set up virtual environment
    if not os.path.exists("venv"):
        subprocess.run([sys.executable, "-m", "venv", "venv"], check=True)

    # Activate virtual environment
    activate_script = "venv/bin/activate" if os.name != "nt" else "venv\\Scripts\\activate"
    activate_command = f"source {activate_script}" if os.name != "nt" else activate_script
    subprocess.run(activate_command, shell=True, check=True)

    # Install requirements
    subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", "pip"], check=True)
    subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], check=True)

    # Install torch and torchvision with wheel cu121
    subprocess.run([sys.executable, "-m", "pip", "install", "torch==2.0.1+cu121", "torchvision==0.15.2+cu121", "-f", "https://download.pytorch.org/whl/torch_stable.html"], check=True)



if __name__ == "__main__":
    try:
        setup_environment()
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
