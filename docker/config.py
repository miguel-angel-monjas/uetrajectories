#!/usr/bin/env python
# coding: utf-8

import logging
import os
import sys

import yaml

# logging and debug settings
if 'LOGGER_ACTIVE' in os.environ and os.getenv('LOGGER_ACTIVE').lower() == 'false':
    logger_active = False
else:
    logger_active = True

if 'LOGGING_LEVEL' in os.environ and (os.getenv('LOGGING_LEVEL') in logging._nameToLevel):
    logging_level = logging.getLevelName(os.getenv('LOGGING_LEVEL'))
else:
    logging_level = logging.INFO

if logger_active:
    logging.basicConfig(
        level=logging_level,
        format='[%(asctime)s] {%(name)s:%(lineno)d} %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S')

log = logging.getLogger('config')


def get_configuration(config_folder='config', config_file_name='config.yaml'):
    current_folder = os.getcwd()
    config_file_path = os.path.join(current_folder, config_folder, config_file_name)
    log.info(f"Reading from configuration file in {config_file_path}.")
    if not os.path.exists(config_file_path):
        log.info(f"Configuration file {config_file_path} does not exist.")
    else:
        with open(config_file_path, 'r') as f:
            try:
                config = yaml.safe_load(f)
                #log.info(config)
                config_content = yaml.dump(config, default_flow_style=False)
                config_content = config_content.replace('\n- ', '\n\n- ')
                log.info("Configuration file contents:")
                for line in config_content.strip().split('\n'):
                    log.info(f"+ {line}")
                return config
            except yaml.YAMLError as error:
                log.error(f"{error}")
                log.error(f"Configuration file {config_file_path} exists but contains errors. Exiting")
                sys.exit(-1)
