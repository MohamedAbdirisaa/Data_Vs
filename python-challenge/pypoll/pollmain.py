import csv

#files
input_file = "raw_data/election_data.csv"
output_file = "output/election_data.txt"

# votes counters
tot_votes = 0


# track candidates and count 
win_candidate = ""
win_count = 0


# Candidate options and votes
cand_options = []
cand_votes = {}


# read and change to dic
with open(input_file) as election_data:
    reader = csv.DictReader(election_data)

 
    for row in reader:

        #total votes
        tot_votes = tot_votes + 1

        # get candidate name from each row 
        cand_name = row["Candidate"] 

        # If candidates names dont match 
        if cand_name not in cand_options:

            # add it to running candidates
            cand_options.append(cand_name)

            # tracking candidate vote count 
            cand_votes[cand_name] = 0

        # adding a vote 
        cand_votes[cand_name] = cand_votes[cand_name] + 1
# Print total votes to terminal
    election_results = (
        f"\n\nelection Results\n"
        f"-------------------------\n"
        f"Total Votes: {tot_votes}\n"
        f"-------------------------\n")
    print(election_results, end="") 


    #finding the winner
for candidate in cand_votes: 

        # voter count and %
        vote = cand_votes.get(candidate)
        percent_vote = float(vote) / float(tot_votes) *(100)

        # winning candidate and how many votes
        if (vote > win_count):
            win_count = vote
            win_candidate = candidate

        # Print 
        voter_results = f"{candidate}: {percent_vote:.3f}% ({vote})\n"
        print(voter_results, end="")

        

# Print 
winner_summary = (
    f"-------------------------\n"
    f"Winner: {win_candidate}\n"
    f"-------------------------\n")
print(winner_summary)

# write to output file
with open(output_file, "w") as txt_file:
    # save in a txt file
    txt_file.write(election_results)
    txt_file.write(voter_results)
    txt_file.write(winner_summary)
    
