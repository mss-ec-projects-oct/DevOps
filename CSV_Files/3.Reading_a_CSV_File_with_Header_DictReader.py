#!/bin/python3
#Reading a CSV File with Header (DictReader)
import csv
with open("logs.csv",mode='r',newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)

#OUTPUT
#{'date': '09-07-25', 'log level': 'Info', 'Message': 'Script Started'}
#{'date': '09-07-25', 'log level': 'ERROR', 'Message': 'Something went wrong'}
