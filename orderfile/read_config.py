#!/bin/python3
import configparser  #ConfigParser(), .sections(), .items(section), .get(section, key)

def read_config(config_file):
    config=configparser.ConfigParser()
    config.read(config_file)

    config_dic={}
    for section in config.sections():
        config_dic[section]={}
        for key,value in config.items(section):
            config_dic[section][key] = value
    #value=config.get('test1','hostname')
    #return value
    return config_dic


def load_config_values():
    config_path="config.ini"
    config_values=read_config(config_path)
    return config_values

test1_config = load_config_values().get('test1')
#print(test1_config.get('hostname'))
