import os
import csv

my_csv = os.path.join("Resources", "election_data.csv")

# Lists to store data
votes = []
candidate_list = []

# with open(udemy_csv, newline="", encoding='utf-8') as csvfile:
with open(my_csv, newline="", encoding='utf8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    for row in csvreader:
        
          # Add price
        candidate_list.append(row[2])
        
    #print(candidate_list)
    
    print("Election Results")
    print("--------------------")
    total_votes = len(candidate_list)
    print(f"Total Votes: {total_votes}")
    print("--------------------")
    khan_total = len([vote for vote in candidate_list if vote == "Khan"])
    khan_percent = round((khan_total/total_votes)*100,3)
    print (f"Khan: {khan_total} {khan_percent}%")

    correy_total = len([vote for vote in candidate_list if vote == "Correy"])
    correy_percent = round((correy_total/total_votes)*100,3)
    print (f"Correy: {correy_total} {correy_percent}%")

    li_total = len([vote for vote in candidate_list if vote == "Li"])
    li_percent = round((li_total/total_votes)*100,3)
    print (f"Li: {li_total} {li_percent}%")

    otooley_total = len([vote for vote in candidate_list if vote == "O'Tooley"])
    otooley_percent = round((otooley_total/total_votes)*100,3)
    print (f"O'Tooley: {otooley_total} {otooley_percent}%")

    print("--------------------")

    

