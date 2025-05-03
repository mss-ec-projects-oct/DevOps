#!/bin/python3
import read_config
import csv  # DictReader(file), .fieldnames
import datetime

def loadcsvfile(path,filename):
    filepath = f"{path}{filename}"
    try:
        with open(filepath, mode='r') as file:
            csv_reader = csv.DictReader(file)
            print("Headers: ", csv_reader.fieldnames)
            data = [row for row in csv_reader if row['use_yn'].strip() == 'Y']
    except FileNotFoundError:
        print(f"Error: The File {filepath} does not exit")
        data = []
    except Exception as e:
        print(f"An Error occured: {e}")
        data = []

    return data


def replace_file_content(filepath, data):
    with open(filepath, 'w') as file:
        file.write(data)
    print(f"{filepath} content is successfully replaced by {data}")


def copy_file(source_file, destination_file):
    with open(source_file, 'r') as source:
        with open(destination_file, 'w') as destination:
            destination.write(source.read())
    print(f"the content is copied from {source_file} to {destination_file} succesfully")


#Example Usage:
config=read_config.load_config_values().get('test1')

#1)
items=loadcsvfile(config.get('itemdirpath'),config.get('itemcsv'))
item_count=sum(1 for row in items)
print(item_count)


#3)
source = config.get('itemdirpath') + config.get('itemcsv')
destination= config.get('itemdirpath') + "destination.csv"
copy_file(source, destination)

#2)
data="sample text"
replace_file_content(destination,data)
