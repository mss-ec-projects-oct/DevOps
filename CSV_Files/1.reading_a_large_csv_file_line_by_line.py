#!/bin/python3
#Scenario: File too large to load into memory at once (e.g., 10GB logs file).
import csv
with open('text.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        #process each row
        print(row)
#OUTPUT
#['row1']
#['row2']
#['row3']
#['row4']
#['row5']
