import os
import csv
from collections import Counter

row_count=0
candidate_list=[]
Candidate_votes={}

election_data = os.path.join( 'Desktop', 'python-challenge', 'PyPoll' , 'Resources', 'election_data.csv')

with open(election_data, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

    #print(csv_header)
    
    
    for row in csv_reader: 
        row_count+=1
        if row[2] not in candidate_list:
            candidate_list.append(row[2])
        

    print(row_count)
    
    print(Counter(csv_header))

    print(candidate_list)

   


    
        
