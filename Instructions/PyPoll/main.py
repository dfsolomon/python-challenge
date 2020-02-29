#import OS and CSV

import os
import csv
from collections import Counter

#import the csv and show the csv

with open('Resources/election_data.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #    print(csvreader)
    csv_header = next(csvreader)
    #    print(f"pybank: {csv_header}")
     #   for row in csvreader:
     #       print(row)
    #spaces for answers
        
    totalVotes=[]
    numvotes=0
    allCandidates=[]
    iVote=Counter()
    percent=[]
    winner=[]
    #Corry=0
   #Li=0
  #  Khan=0
  #  otooley=0
    
        
    for row in csvreader:
        allCandidates.append(row[2])
    numvotes = len(allCandidates)
    
    for name in allCandidates:
        iVote[name]+=1
        
victor= max(zip(iVote.values(), iVote.keys()))
candidates=tuple(iVote.keys())
votes=tuple(iVote.values())

for x in votes:
    percent.append((int(x)/numvotes)*100)

    
    
        
  
print (f"number of voters:{numvotes}")                
print ("names of the candidates: Corry, Li, Khan, O'Tooley ")        
for x in range(len(candidates)):
    print(candidates[x] + ":" + str(round(percent[x],1))+ "%" + str(votes[x]))
print(f"winner:" +victor[1])


with open("output.txt", "w") as new:
    new.write("names of the candidates: Corry, Li, Khan, O'Tooley ")
    new.write("\n")
    for x in range(len(candidates)):
        new.write(candidates[x] + ":" + str(round(percent[x],1))+ "%" + str(votes[x]))
    new.write("\n")
    new.write(f"winner:" +victor[1])
    
    
    
    