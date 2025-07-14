#!/bin/python3
import csv

new_rows = [
        ["14-07-2025", "Append1", "Appending the message1"],
        ["14-07-2025", "Append2", "Appending the message2"]
        ]
# Append to the existing CSV file
with open("logs.csv", mode="a", newline='') as file:
    writer = csv.writer(file)
    writer.writerows(new_rows)

print("Rows successfully appended")
