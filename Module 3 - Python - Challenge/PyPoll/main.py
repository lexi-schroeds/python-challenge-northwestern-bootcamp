import os
import csv

# Find path of file to analyze
csv_file = os.path.join('.', 'Resources', 'election_data.csv')
txt_file = os.path.join('.', 'analysis', 'election_analysis.txt')

# Initialize variables
total_votes = 0
percent_votes = 0

# Create dictionary to hold candidates names and using dictionary & list
candidates_dict = {}

# Read the CSV file
with open(csv_file) as csvfile:  
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    # Loop through rows in the CSV file
    for row in csvreader:
        total_votes = total_votes+1
        candidate_name = row[2]

        # Update candidate votes in the dictionary
        if candidate_name in candidates_dict:
            candidates_dict[candidate_name] += 1
        else:
            candidates_dict[candidate_name] = 1

    #Use list and dictionary 
        #List of candidates stored one time each
        #If the candidate is NOT in candidate list, add to list or append them to list AND add to dictionary with name as key and value as 0 votes
    
    #Whoever the candidate is, increment their dictionary count by 1
        
    #Use list to pull the vote count out, iterate (for loop), calculate % of votes --> needs to be inside output 
    
    #If statement to show if candidate votes > X than display name as winner and show number of their votes

#Print output of the analysis 
output = (
    f"Election Results\n" 
    f"------------------\n"
    f"Total Votes: {total_votes}\n"
    f"------------------\n"
)
#Add each candidate and votes on each line from the dictionary
for candidate, votes in candidates_dict.items():
    percent_votes = (votes / total_votes) * 100
    output += f"{candidate}: {percent_votes:.3f}% ({votes})\n"
    f"------------------\n"

# Determine the winner based on the candidate with the most votes
winner = max(candidates_dict, key=candidates_dict.get)

# Add the winner to the output
output += (
    f"------------------\n"
    f"Winner: {winner}\n"
    f"------------------\n"
)

print(output)

with open(txt_file,"w") as txtfile:
    txtfile.write(output)