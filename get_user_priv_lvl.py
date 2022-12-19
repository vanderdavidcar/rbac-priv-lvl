from netmiko import ConnectHandler
import net_conn
import re

with open("devices") as f:
    hosts = f.read().splitlines()

def get_user_priv_lvl(hosts):
    for devices in hosts:
        iosv = net_conn.netmiko_connection(devices)
        print(f"\n{'-'*78}\nConnecting to device model: {str(devices)}\n")
        # A variable "default_enter" has a press enter to confirm users delete
        net_connect = ConnectHandler(**iosv, default_enter="\r\n")
        
        # Show usernames on devices
        show_cmd = net_connect.send_command("sh run | in username")
        
        # Regex pattern to users
        users_pattern = re.compile(r"username (?P<username>\S+)")
        users_match = users_pattern.search(show_cmd)
        user_list = re.findall(users_pattern, show_cmd)

        # Regex pattern to users and priv_lvl
        users_priv_pattern = re.compile(r"username (?P<username>\w.+) privilege (?P<prv_lvl>\d{1,2})")
        users_match = users_priv_pattern.search(show_cmd)
        user_priv_list = re.findall(users_priv_pattern, show_cmd)

        for i in user_priv_list:
            print(f"Users and Priv-Level".ljust(18) + ": " + str(i))
        
get_user_priv_lvl(hosts)