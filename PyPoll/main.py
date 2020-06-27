
import os
import csv


election_csv = os.path.join("Resources","election_data.csv")


total_votes = 0
candidate_list = []
unique_candidate = []
count_vote = []
vote_in_percentage = []

# Open CSV file

with open(election_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
 
    for row in csvreader:
        # Count the total votes
        total_votes = total_votes + 1
        # add candidates' names to candidate_list
        candidate_list.append(row[2])
        # count unique candidate
    for x in set(candidate_list):
        unique_candidate.append(x)
        y = candidate_list.count(x)
        count_vote.append(y)
        #  calculate percentage 
        b = round((y/total_votes)*100)
        vote_in_percentage.append(b)
        
    winner_total_vote = max(count_vote)
    winner = unique_candidate[count_vote.index( winner_total_vote)]

 
print("-------------------------")
print("Election Analysis")   
print("-------------------------")
print("Total Votes :" + str(total_votes))    
print("-------------------------")
for i in range(len(unique_candidate)):
            print(unique_candidate[i] + ": " + str(vote_in_percentage[i]) +"% (" + str(count_vote[i])+ ")")
print("-------------------------")
print("The winner is: " + winner)
print("-------------------------")

# Print to a text file: election_results.txt

with open('election_result.txt', 'w') as text:
    text.write("Election result\n")
    text.write("---------------------------------------\n")
    text.write("Total Vote: " + str(total_votes) + "\n")
    text.write("---------------------------------------\n")
    for i in range(len(set(unique_candidate))):
        text.write(unique_candidate[i] + ": " + str(vote_in_percentage[i]) +"% (" + str(count_vote[i]) + ")\n")
    text.write("---------------------------------------\n")
    text.write("The winner is: " + winner + "\n")

    text.write("---------------------------------------\n")
