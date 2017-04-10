import os
import configparser
import json

def get_config(config_fn):
    config = configparser.ConfigParser()
    config._interpolation = configparser.ExtendedInterpolation()
    config.read(config_fn)
    return config

