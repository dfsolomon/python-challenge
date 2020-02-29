#import OS and CSV

import os
import csv

#import the csv and show the csv

with open('PyBank/Resources/budget_data.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    for row in csvreader:
        print(row)

#create space to save unique months in

unique_months = []
x=0

 for row in csvreader:
        if row[0] == video:




