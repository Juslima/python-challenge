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
