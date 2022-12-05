#Imports from Jinja2
from jinja2 import Environment, FileSystemLoader

#Import YAML from PyYAML
import yaml

# List to do loop 
versions = ["nxos", "ios", "os10"]

#Load data from YAML file into Python dictionary
config = yaml.full_load(open('./auth_vars.yml'))

#Load Jinja2 template
env = Environment(loader = FileSystemLoader('./'), trim_blocks=True, lstrip_blocks=True)

for model in versions:
    template = env.get_template(f'rbac_{model}_template.j2')
    output = template.render(config)
    scriptFile = open(f'rbac_{model}.cfg', "w+")
    scriptFile.write(output)
    print(f'Created script FileName rbac_{model}.cfg') 


