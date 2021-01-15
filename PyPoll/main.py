import os
import csv
from collections import Counter

row_count=0
candidate_list=[]


election_data = os.path.join( 'Resources', 'election_data.csv')

with open(election_data, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    vote_count=[]
    #print(csv_header)
    
    
    for row in csv_reader: 
        row_count+=1   # counts number of votes
        if row[2] not in candidate_list:  # Creates list with each candidate
            candidate_list.append(row[2])
        vote_count.append(row[2])

       
    #print(Counter(vote_count))
    counts = Counter(vote_count)
    #print(row_count)
    #print(candidate_list)
    
    
    counts_values= max(counts, key=counts.get)
    #print(counts[str(candidate_list[0])])
    

    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {row_count}")
    print("-------------------------")
    print(candidate_list[0] + ": " + '{:.3%}'.format(counts[str(candidate_list[0])]/row_count) + " (" + str(counts[str(candidate_list[0])]) + ")")
    print(candidate_list[1] + ": " + '{:.3%}'.format(counts[str(candidate_list[1])]/row_count) + " (" + str(counts[str(candidate_list[1])]) + ")")
    print(candidate_list[2] + ": " + '{:.3%}'.format(counts[str(candidate_list[2])]/row_count) + " (" + str(counts[str(candidate_list[2])]) + ")")
    print(candidate_list[3] + ": " + '{:.3%}'.format(counts[str(candidate_list[3])]/row_count) + " (" + str(counts[str(candidate_list[3])]) + ")")
    print("-------------------------")
    print(f"Winner: {counts_values}")
    print("-------------------------")




   


    
        
