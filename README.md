# ⚡️ Portable Ansible Environment

![Release](https://img.shields.io/badge/Release-v0.1.0-green)
![Language](https://img.shields.io/badge/Language-Python3-blue)
![Tags](https://img.shields.io/badge/Tags-Automation-lightgray)
![Tags](https://img.shields.io/badge/Tags-Productivity-lightgray)

A self-contained Ansible workspace for MacOS, Linux and other posix compliant systems.

## Requirements

git, python3, python3-pip, python3-venv

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/jamieahelmke/portable-ansible
   cd portable-ansible
   ```
2. Build the environment:
   ```bash
   python3 setup.py
   ```
3. Activate the environment:
   ```bash
   source ./start_venv.sh
   ```
4. Run the example playbook:
   ```bash
   ansible-playbook -i ansible/inventory/hosts.yml ansible/playbooks/example.yml
   ```
