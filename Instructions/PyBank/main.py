#import OS and CSV

import os
import csv
import statistics

#import the csv and show the csv

with open('Resources/budget_data.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
#    print(csvreader)
    csv_header = next(csvreader)
 #   print(f"pybank: {csv_header}")
  #  for row in csvreader:
 #       print(row)

#find the total number of months in the data set
    months= []
    profit= []
    change_in_profit= []
    numMonths=0;
    total= 0
    
    
    for row in csvreader:
        months.append(row[0])
        profit.append(int(row[1]))
        numMonths= numMonths+1
    
    
    for i in range(len(profit)-1):
        change_in_profit.append(profit[i+1] - profit[i])
        total = total + profit[i]
    
indexIncrease = profit.index(max(profit))
indexDecrease = profit.index(min(profit))

print (f"{numMonths}")
print (f"total: ${sum(profit)}")
print (f"average change:  $ {round(sum(profit)/len(profit),2)}")
print (f"greatest increase in profits:  {months[indexIncrease]} (${profit[indexIncrease]})")
print (f"Greatest decrease in Profits:  {months[indexDecrease]} (${profit[indexDecrease]})")
#print (round(statistics.mean(change_in_profit)))
#print (change_in_profit)
with open("output.txt", "w") as new:
    new.write("Total Months: " + str(numMonths))
    new.write("\n")
    new.write("Total: $" + str(sum(profit)))
    new.write("\n")
    new.write("Average Change: $" + str(round(sum(profit)/len(profit), 2)))
    new.write("\n")
    new.write("Greatest Increase in Profits: " + str(months[indexIncrease]) + " ($" + str(profit[indexIncrease]) + ")")
    new.write("\n")
    new.write("Greatest Decrease in Profits: " + str(months[indexDecrease]) + " ($" + str(profit[indexDecrease]) + ")")