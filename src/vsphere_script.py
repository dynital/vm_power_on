import ssl
import atexit
from pyVim.connect import SmartConnect, Disconnect
from pyVmomi import vim

# Function to connect to the vCenter
def connect_vsphere(vcenter_host:str, vcenter_user:str, vcenter_password:str) -> vim.ServiceInstance:
    try:
        context = ssl.SSLContext(ssl.PROTOCOL_TLS)
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE

        service_instance = SmartConnect(host=vcenter_host, user=vcenter_user, pwd=vcenter_password, sslContext=context)

        atexit.register(Disconnect, service_instance)
        print("Connection successful.")
        return service_instance
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Function to find the VM in the vCenter
def find_vm_by_name(service_instance:vim.ServiceInstance, vm_name:str) -> None:
    content = service_instance.RetrieveContent()
    for datacenter in content.rootFolder.childEntity:
        if hasattr(datacenter, 'vmFolder'):
            vm_folder = datacenter.vmFolder
            vm_list = vm_folder.childEntity
            for vm in vm_list:
                if vm.name == vm_name:
                    return vm
    return None

# Function to power on the VM
def power_on_vm(service_instance:vim.ServiceInstance ,vm_name:str) -> None:
    vm = find_vm_by_name(service_instance, vm_name)
    if vm:
        if vm.runtime.powerState == vim.VirtualMachinePowerState.poweredOn:
            print(f"VM '{vm_name}' is already powered on.")
        else:
            task = vm.PowerOn()
            print(f"Powering on VM: {vm_name} ...")
            return task
    else:
        print(f"VM '{vm_name}' not found in vSphere.")
    return None
    