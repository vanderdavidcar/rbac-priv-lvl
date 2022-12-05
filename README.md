# Restrict access for users with RBAC or low privilege level(ios, nxos, os10)

# auth_vars1.yml
Changes values for yours users and password to have a loop in jinja2 templates<br/>
On file create_scripts.py in line 11 change auth_vars.yml to auth_vars1.yml or rename file. 

# create_scripts.py
Using jinja2 templates which contains scripts to create RBAC on NXOS and Privilege Level 7 on IOS and OS 10 (Dell).<br/> 
Services users doesn't need full permissions to access device network

Note:
To fulfill oxidized needs I had to do a workround for task works properly. I had to create an alias "show-running-config" to collect backup correctly.

# send_config.py
I am using method send_config_from_file() to set RBAC and privilege level on devices, after configuration, I'm using method send_command() to check if users were created with the correct role and privilege level


