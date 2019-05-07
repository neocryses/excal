"""
Module which holds configuration related functions.
"""

import os
import shutil
import sys

import yaml

ROOT_PATH = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
DEFAULT_CONFIG_PATH = os.path.join(ROOT_PATH, "etc", "calendar.yml")
CWD = os.getcwd()


def generate_config_file():
    """
    Generate configuration file by copying the default configuration.
    """
    dest_path = os.path.join(CWD, "calendar.yml")
    if not os.path.exists(dest_path):
        shutil.copyfile(DEFAULT_CONFIG_PATH, dest_path)
        sys.exit(0)
    else:
        raise FileExistsError('aborting since config file already exists.')


def load_config(config_path=None):
    """
    Resolve which configuration file to load, then
    load the configuration yaml file and return it as an object.
    """
    if not config_path:
        config_path = os.path.join(CWD, "calendar.yml")

    if os.path.exists(config_path):
        target_config_path = config_path
    else:
        target_config_path = DEFAULT_CONFIG_PATH

    with open(target_config_path, 'r') as config_file:
        return yaml.safe_load(config_file)
