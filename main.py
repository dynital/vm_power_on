from src.ad_script import *
from src.vsphere_script import *
from config import *
import getpass

def main():

    username = input("Enter your username (name.surname@domain.it): ")
    password = getpass.getpass("Enter your password: ")

    tenant_username = input("Enter your tenant username: ", default=AAD_TENANT_ID)
    client_id = input("Enter your client ID: ", default=AAD_CLIENT_ID)

    vcenter_host = input("Enter the vCenter host: ", default=VCENTER_HOST)
    vcenter_user = input("Enter the vCenter username: ", default=VCENTER_USER)
    vcenter_password = getpass.getpass("Enter the vCenter password: ")

    excel_folder = EXCEL_FOLDER

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