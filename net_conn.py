"""
Function Netmiko Connection
"""

from netmiko import ConnectHandler
from dotenv import load_dotenv
load_dotenv()
import os
import paramiko

user_os10 = os.getenv("USER_OS10")
pass_os10 = os.getenv("PASS_OS10")

user_idc = os.getenv("USER_IDC")
pass_idc = os.getenv("PASS_IDC")

# Netmiko Dellos10 connection
def netmiko_dellos10(ip):
    return {
            'device_type': 'dell_os10',
            'ip': ip,
            'username': user_os10,
            'password': pass_os10,
             }

# Netmiko Connection (nxos, ios, iosxr)
def netmiko_ios(ip):
    return {
            'device_type': 'cisco_ios',
            'ip': ip,
            'username': user_idc,
            'password': pass_idc,
             }
