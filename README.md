# ⚡️ Portable Ansible Environment

A self-contained Ansible workspace for MacOS, Linux and other posix compliant systems.

## Requirements

git, python3, pip3

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