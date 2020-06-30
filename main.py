import os
import csv

filename = "/Users/kiranrangaraj/Desktop/Classwork/Homework/python_challenge/PyPoll"
PyPoll_csv = os.path.join(filename, "Resources", "02-Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv")

exportfile = "/Users/kiranrangaraj/Desktop/Classwork/Homework/python_challenge/PyPoll"
PyPoll_export = os.path.join(exportfile, "Analysis", "Analysis.txt")

total_votes = 0
candidates = []
candidate_votes = {}

winning_candidate = ""
winning_count = 0

with open(PyPoll_csv) as election_data:
    reader = csv.reader(election_data)

    header = next(reader)

    for row in reader:

        print("", end=""),
        total_votes = total_votes + 1

        candidate_name = row[2]

        if candidate_name not in candidates:
            candidates.append(candidate_name)
            candidate_votes[candidate_name] = 0
            
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

with open(PyPoll_export, "w") as txt_file:
    election_results = (
        f"Election Results\n"
        f"--------------------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"--------------------------------------\n")
    print(election_results,end="")
    
    txt_file.write(election_results)

    for candidate in candidate_votes:

        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes) * 100

        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate

        voter_output = f"{candidate}: {vote_percentage}% ({votes})\n"
        print(voter_output, end="")

        txt_file.write(voter_output)


    winning_candidate_summary = (
        f"--------------------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"--------------------------------------\n")
    print(winning_candidate_summary)

    txt_file.write(winning_candidate_summary)

