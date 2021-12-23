import yaml
import os


def read_yaml(path_to_file: str) -> dict:
    with open(path_to_file) as yaml_file:
        content=yaml.safe_load(yaml_file)
    return content

def create_directory(dir_list: list):
    for dirs in dir_list:
        os.makedirs(dirs, exist_ok=True)
        print(f"Directory created at {dirs}")

