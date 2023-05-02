# python-challenge-PyBank
import csv

# Open and read the CSV file
with open('budget_data.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip the header row
    next(csvreader)

    # Initialize variables
    total_months = 0
    total_profit = 0
    previous_profit = 0
    profit_changes = []
    greatest_increase = ['', 0]
    greatest_decrease = ['', 0]

    # Loop through each row of the CSV
    for row in csvreader:
        # Increment the month counter
        total_months += 1

        # Calculate the total profit
        total_profit += int(row[1])

        # Calculate the profit change and add it to the list
        current_profit = int(row[1])
        if previous_profit != 0:
            profit_change = current_profit - previous_profit
            profit_changes.append(profit_change)

            # Check if this is the greatest increase or decrease in profit
            if profit_change > greatest_increase[1]:
                greatest_increase[0] = row[0]
                greatest_increase[1] = profit_change
            elif profit_change < greatest_decrease[1]:
                greatest_decrease[0] = row[0]
                greatest_decrease[1] = profit_change

        # Update the previous profit variable for the next loop iteration
        previous_profit = current_profit

# Calculate the average change in profit
average_change = sum(profit_changes) / len(profit_changes)

# Print the results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit}")
print(f"Average Change: ${round(average_change, 2)}")
print(
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")
#-----------------------------------------------------
# python-challenge-PyPoll
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
