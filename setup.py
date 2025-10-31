#!/usr/bin/env python3
import os
import platform
import subprocess
import sys
import time

# --- Config ---
REQUIRED_PATHS = [
    "ansible/ansible.cfg",
    "ansible/inventory/",
    "ansible/playbooks/",
    "requirements.txt",
    "start_venv.sh",
]
VENV_DIR = ".venv"
COLLECTIONS_DIR = "ansible/lib/collections"

# --- Helper functions ---
def print_step(step, message, end="\n"):
    sys.stdout.write(f"[{step}] {message}{end}")
    sys.stdout.flush()

def live_status(message):
    sys.stdout.write(f"\r{message}")
    sys.stdout.flush()

def verify_repo_structure():
    missing = [p for p in REQUIRED_PATHS if not os.path.exists(p)]
    if missing:
        print_step("2/5", "Checking repository structure...")
        print(f"ERROR: Missing required file or directory:\n  {missing[0]}")
        print("\nFix this by running:")
        print("  git fetch origin")
        print("  git reset --hard origin/main")
        sys.exit(1)
    print_step("2/5", "Checking repository structure... OK")

def create_local_dirs():
    print_step("3/5", "Creating local directories...")
    os.makedirs("env", exist_ok=True)
    os.makedirs(COLLECTIONS_DIR, exist_ok=True)
    for d in [
        "ansible/inventory",
        "ansible/playbooks",
        "ansible/roles",
        "ansible/group_vars",
        "ansible/host_vars",
    ]:
        os.makedirs(d, exist_ok=True)
    print("Local directories verified or created.")

def recreate_venv():
    print_step("4/5", "Creating and initializing Python virtual environment...")
    if os.path.exists(VENV_DIR):
        subprocess.run(["rm", "-rf", VENV_DIR], check=True)
    subprocess.run([sys.executable, "-m", "venv", VENV_DIR], check=True)

    pip_path = f"{VENV_DIR}/bin/pip"
    live_status("[4/5] Installing dependencies... 0%")
    result = subprocess.run([pip_path, "install", "-r", "requirements.txt"], capture_output=True, text=True)
    if result.returncode != 0:
        print("\nDependency installation failed:")
        print(result.stderr)
        sys.exit(1)
    live_status("[4/5] Installing dependencies... 100%\n")

def verify_ansible():
    print_step("5/5", "Final checks...")
    ansible_path = f"{VENV_DIR}/bin/ansible"
    result = subprocess.run([ansible_path, "--version"], capture_output=True, text=True)
    if result.returncode == 0:
        version_line = result.stdout.splitlines()[0]
        print(f"Ansible version: {version_line}")
        print("\nSetup complete.\n")
        print("Next steps:")
        print("1. Activate environment:   source ./start_venv.sh")
        print("2. Run playbook example:   ansible-playbook -i ansible/inventory/hosts.yml ansible/playbooks/example.yml")
        print("3. To rebuild:             python3 setup_env.py")
    else:
        print("Ansible verification failed. Check installation.")

# --- Main ---
def main():
    print_step("1/5", "Detecting operating system...")
    system = platform.system()
    print(f"Detected OS: {system}")
    if system not in ("Darwin", "Linux"):
        print("Unsupported OS. Use macOS or Linux.")
        sys.exit(1)

    verify_repo_structure()
    create_local_dirs()
    recreate_venv()
    verify_ansible()

if __name__ == "__main__":
    main()
