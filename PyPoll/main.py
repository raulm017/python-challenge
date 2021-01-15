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


    Line1="Election Results\n"
    Line2="-------------------------\n"
    Line3=f"Total Votes: {row_count}\n"
    Line4="-------------------------\n"
    Line5=candidate_list[0] + ": " + '{:.3%}'.format(counts[str(candidate_list[0])]/row_count) + " (" + str(counts[str(candidate_list[0])]) + ")\n"
    Line6=candidate_list[1] + ": " + '{:.3%}'.format(counts[str(candidate_list[1])]/row_count) + " (" + str(counts[str(candidate_list[1])]) + ")\n"
    Line7=candidate_list[2] + ": " + '{:.3%}'.format(counts[str(candidate_list[2])]/row_count) + " (" + str(counts[str(candidate_list[2])]) + ")\n"
    Line8=candidate_list[3] + ": " + '{:.3%}'.format(counts[str(candidate_list[3])]/row_count) + " (" + str(counts[str(candidate_list[3])]) + ")\n"
    Line9="-------------------------\n"
    Line10=f"Winner: {counts_values}\n"
    Line11="-------------------------\n"
 
    L = [Line1, Line2, Line3, Line4, Line5, Line6, Line7, Line8, Line9, Line10, Line11]

output_path = os.path.join('analysis', 'analysis_file.txt')

with open(output_path, 'w',  newline='') as textfile:
    textfile.writelines(L)
    textfile.close()


   


    
        
