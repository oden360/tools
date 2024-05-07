
# Usage
from dataclasses import dataclass, field

default_config_path = 'config.yaml'
user_config_path = 'user_config.yaml'

with open(default_config_path, 'r') as file:
    default_config = yaml.safe_load(file)

with open(user_config_path, 'r') as file:
    user_config = yaml.safe_load(file)

config_data = {**default_config, **user_config}