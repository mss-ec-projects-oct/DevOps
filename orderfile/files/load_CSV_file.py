#!/bin/python3
import csv

def loadCSVFile(path, file):
    file_path = f"{path}/{file}"
    with open(file_path, 'r') as file:
        csv_reader = csv.DictReader(file)
        print("Headers:", csv_reader.fieldnames)
        data = [row for row in csv_reader if row['use_yn'].strip() == 'Y']

    return data

#Example usecase:
path = '/home/manoj/pythonscripts/python_notes/orderfile/files/datacsv'
file = 'items.csv'

print(f"data of the {file} is \n: {loadCSVFile(path,file)}")
