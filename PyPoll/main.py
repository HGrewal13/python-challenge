# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os



# Files to load and output (update with correct file paths)
file_to_load = os.path.join("PyPoll", "Resources", "election_data.csv")
file_to_output = os.path.join("PyPoll", "analysis", "election_results.txt")

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

candidates_votes = {}

candidate_name = ""

# Winning Candidate and Winning Count Tracker


# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets)
        print(". ", end="")

        # Increment the total vote count for each row
        total_votes += 1

        candidate_name = row[2]

        # Add candidate to dictionary if they don't exist
        if candidate_name not in candidates_votes:
            candidates_votes[candidate_name] = 0
            
        # Increment vote count for the candidate
        candidates_votes[candidate_name] += 1
        
# Calculate the winner
winner = ""
winning_votes = 0

for candidate in candidates_votes:
    votes = candidates_votes[candidate]
    vote_percentage = (votes / total_votes) * 100
    
    if votes > winning_votes:
        winning_votes = votes
        winner = candidate

# Create output string
output = (
    f"Election Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"-------------------------\n"
)

# Add candidate results to output
for candidate in candidates_votes:
    votes = candidates_votes[candidate]
    vote_percentage = (votes / total_votes) * 100
    output += f"{candidate}: {vote_percentage:.3f}% ({votes})\n"

output += (
    f"-------------------------\n"
    f"Winner: {winner}\n"
    f"-------------------------\n"
)

# Print to terminal
print(output)



# Write to file
file_to_output = os.path.join("PyPoll", "analysis", "election_results.txt")
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
