#!/bin/python3
#Filtering Data Based on a Condition

import csv

with open("logs.csv",mode='r',newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row["log level"] == "ERROR":
            print(row)

#OUTPUT
#{'date': '09-07-25', 'log level': 'ERROR', 'Message': 'Something went wrong'}
