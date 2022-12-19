from netmiko import ConnectHandler
from getpass import getpass
import net_conn
from dotenv import load_dotenv
from datetime import datetime
load_dotenv()
import os

user_idc = os.getenv("USER_IDC")
pass_idc = os.getenv("PASS_IDC")

user_os10 = os.getenv("USER_OS10")
pass_os10 = os.getenv("PASS_OS10")

start_time = datetime.now()

#username = input('Enter your SSH username: ')
#password = getpass()

# Devices split to model due configuration files be different
with open("devices_nxos") as f_nxos:
    devices_nxos = f_nxos.read().splitlines()

with open("devices_ios") as f_ios:
    devices_ios = f_ios.read().splitlines()

with open("devices_dellos") as f_dellos10:
    devices_dell = f_dellos10.read().splitlines()

# NX-OS module 
def dev_conn_nxos(ips, model):
    for ips in devices_nxos:
        # call net_conn module there are all connection model (nxos, ios, dellos) 
        iosv = net_conn.netmiko_ios(ips)
        print(f"\n{'#'*79}\nConnecting to device model: {model.upper()}\nHostname: {ips}\n")
        net_connect = ConnectHandler(**iosv)
        command1 = net_connect.send_config_from_file(f'rbac_{model.lower()}.cfg')
        print(f"\n--------------- APPLIED CONFIG ---------------\n\n")
        print(command1)
        print("\n\n--------------- POST CONFIG ---------------\n")
        command2 = net_connect.send_command("show run | in username")
        print(command2)
        end_time = datetime.now()
        print("Total time: {}".format(end_time - start_time))

dev_conn_nxos(devices_nxos, "nxos")

# Dellos module
def dev_conn_dellos10(ips, model):
    for ips in devices_dell:
        iosv = net_conn.netmiko_dellos10(ips)
        print(f"\n{'#'*79}\nConnecting to device model: {model.upper()}\nHostname: {ips}\n")
        net_connect = ConnectHandler(**iosv)
        command1 = net_connect.send_config_from_file(f'rbac_{model.lower()}.cfg')
        print(f"\n--------------- APPLIED CONFIG ---------------\n\n")
        print(command1)
        
        print("\n\n--------------- POST CONFIG ---------------\n")
        command2 = net_connect.send_command(" show running-configuration | grep username")
        print(command2)
        end_time = datetime.now()
        print("Total time: {}".format(end_time - start_time))

dev_conn_dellos10(devices_dell, "dellos10")

# IOS module
def dev_conn_ios(ips, model):
    for ips in devices_ios:
        iosv = net_conn.netmiko_ios(ips)
        print(f"\n{'#'*79}\nConnecting to device model: {model.upper()}\nHostname: {ips}\n")
        net_connect = ConnectHandler(**iosv, default_enter="\r\n")
        command1 = net_connect.send_config_from_file(f'rbac_{model.lower()}.cfg')
        print(f"\n--------------- APPLIED CONFIG ---------------\n\n")
        print(command1)
        
        print("\n\n--------------- POST CONFIG ---------------\n")
        command2 = net_connect.send_command("show run | in username")
        print(command2)
        end_time = datetime.now()
        print("Total time: {}".format(end_time - start_time))

dev_conn_ios(devices_ios, "ios")
