from src.ad_script import *
from src.vsphere_script import *
import dotenv
import os
import getpass

def main():

    dotenv.load_dotenv(".env")

    username = input("Enter your username (name.surname@domain.it): ")
    password = getpass.getpass("Enter your password: ")

    tenant_username = os.getenv("AAD_TENANT_ID")
    client_id = os.getenv("AAD_CLIENT_ID")

    vcenter_host = os.getenv("VCENTER_HOST")
    vcenter_user = os.getenv("VCENTER_USER")
    vcenter_password = os.getenv("VCENTER_PASSWORD")

    excel_folder = os.getenv("EXCEL_FOLDER")

    if authenticate_user(username, password, tenant_username, client_id):
        name, surname = extract_name_surname(username)
        if name and surname:
            vm_name = get_vm_name(name, surname, excel_folder)
            if vm_name:
                print(f"VM name: {vm_name}")

                service_instance = connect_vsphere(vcenter_host, vcenter_user, vcenter_password)
                if service_instance:
                    vm = find_vm_by_name(service_instance, vm_name)
                    power_on_vm(vm)
            else:
                print("VM name not found.")
        else:
            print("Invalid username.")
