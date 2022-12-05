from netmiko import ConnectHandler
from getpass import getpass
import net_conn
from dotenv import load_dotenv
from datetime import datetime
load_dotenv()
import os

username = os.getenv("USER_IDC")
password = os.getenv("PASS_IDC")
start_time = datetime.now()
# username = input('Enter your SSH username: ')
# password = getpass()

with open("devices") as f:
    devices_list = f.read().splitlines()

for devices in devices_list:
    print()
    print("#" * 79)
    iosv = net_conn.netmiko_ios(devices)
    print('Connecting to device:  ' + devices)

    net_connect = ConnectHandler(**iosv)
    print()
    #command1 = net_connect.send_config_set('no role name backup.oxidized')
    command1 = net_connect.send_config_from_file('rbac_nxos.cfg')
    print("--------------- APPLIED CONFIG ---------------")
    print(command1)
    print("")
    print("--------------- POST CONFIG ---------------")
    command2 = net_connect.send_command("show run | in username")
    
    print(command2)
    print("")
    end_time = datetime.now()
    print("Total time: {}".format(end_time - start_time))
