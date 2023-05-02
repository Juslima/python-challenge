import csv

# Set the path for the input file
file_path = "election_data.csv"

# Initialize variables
total_votes = 0
candidates = []
candidate_votes = {}

# Open the file and read in the data
with open(file_path, "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    next(csv_reader)  # Skip header row

    # Loop through each row in the file
    for row in csv_reader:
        # Count the total number of votes cast
        total_votes += 1

        # Add the candidate to the list of candidates if not already present
        candidate_name = row[2]
        if candidate_name not in candidates:
            candidates.append(candidate_name)
            candidate_votes[candidate_name] = 0

        # Count the votes for the candidate
        candidate_votes[candidate_name] += 1

# Calculate the percentage of votes each candidate won
percentages = {}
for candidate in candidates:
    vote_count = candidate_votes[candidate]
    percentage = (vote_count / total_votes) * 100
    percentages[candidate] = round(percentage, 3)

# Find the winner based on popular vote
winner = max(candidate_votes, key=candidate_votes.get)

# Print out the results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate in candidates:
    print(
        f"{candidate}: {percentages[candidate]}% ({candidate_votes[candidate]})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")
