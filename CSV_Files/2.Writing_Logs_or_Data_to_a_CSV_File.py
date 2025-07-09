#!/bin/python3
#Writing Logs or Data to a CSV File
import csv
data = [
        ["date", "log level", "Message"],
        ["09-07-25","Info","Script Started"],
        ["09-07-25","ERROR","Something went wrong"]
        ]

with open("logs.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)
print("data written to logs.csv")
