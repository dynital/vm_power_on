# Powering on vCenter VMs

## 📌 Overview
This program is used to power on VMs, given a username and a password.

[This is a project for self-education]

## 📖 Table of Contents
1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Configuration](#configuration)
4. [Resources](#resources)

## 📝 Introduction
This script is written in Python 3.13 on Windows 11 and has not been tested in any other environments.

The program receives in input a user's name (name.surname@domain.it) and password.

The input will be processed, in case Azure Active Directory truncates the user name as it supports a max of 20 characters.

The credentials will then be sent to the Domain Controller to be checked and will return either a True (the credentials are valid) or a False (the credentials are not valid).

After the validation, the script will check the excel files for a match of the user's name and surname and retrieve their VM name.

Once the VM name is found, the program will get connection to the vCenter to find a match of the VM name within the list.

Finally, after a match is found, the user's VM will be turned on and the script will end.

## ⚙️ Installation
To set up your environment to use the program, run the following command in a terminal:

```sh
# On Windows
git clone https://github.com/dynital/vm_power_on.git
cd .\vm_power_on\
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

```sh
# On Linux
git clone https://github.com/dynital/vm_power_on.git
cd .\vm_power_on\
python3 -m venv .venv
source .venv\bin\activate
pip install -r requirements.txt
```

## 🔧 Configuration
The needed configurations on the program can be found and customized in config.py, which looks like this

```py
# Azure Active Directory (AAD) configuration
AAD_TENANT_ID = "your_tenant_id"
AAD_CLIENT_ID = "your_client_id"

# vCenter configuration
VCENTER_HOST = "your_vcenter_host"
VCENTER_USER = "your_vcenter_user"
VCENTER_PASSWORD = "your_vcenter_password" # HIGHLY RECOMMENDED NOT TO USE

# Excel folder path
EXCEL_FOLDER = "path_to_excel_folder"
```

## 📚 Resources
This is the documentations that was used to make this program.

- [vSphere Automation SDK for Python](https://vmware.github.io/vsphere-automation-sdk-python/vsphere/8.0.3.0/)
- [Microsoft Authentication Library for Python](https://msal-python.readthedocs.io/en/latest/)
- [pandas Documentation](https://pandas.pydata.org/docs/)
