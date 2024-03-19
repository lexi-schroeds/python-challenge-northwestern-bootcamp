import os
import csv

# Find path of file to analyze
csv_file = os.path.join('.', 'Resources', 'budget_data.csv')
txt_file = os.path.join('.', 'analysis', 'budget_analysis.txt')

# Initialize variables
total_months = 0
net_total = 0
previous_profit_loss = 0
monthly_changes = []
dates = []

# Read the CSV file
with open(csv_file) as csvfile:  
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    # Loop through rows in the CSV file
    for row in csvreader:
        # Extract date and profit & loss data
        date = row[0]
        profit_loss = int(row[1])

        # Calculate total number of months and net total amount of profits & losses
        total_months += 1
        net_total += profit_loss

        # Calculate change in profit/loss from previous month and store it
        if total_months > 1:
            monthly_change = profit_loss - previous_profit_loss
            monthly_changes.append(monthly_change)
            dates.append(date)

        # Store profit/loss for next iteration
        previous_profit_loss = profit_loss

# Calculate the average change in profit/loss
average_change = sum(monthly_changes) / len(monthly_changes)

# Find the greatest increase and decrease in profits
greatest_increase = max(monthly_changes)
greatest_decrease = min(monthly_changes)

# Find corresponding dates for greatest increase and decrease
increase_index = monthly_changes.index(greatest_increase)
decrease_index = monthly_changes.index(greatest_decrease)
increase_date = dates[increase_index]
decrease_date = dates[decrease_index]

#Print output of the analysis 
output = (
    f"Financial Analysis\n" 
    f"------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net_total}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {increase_date} (${greatest_increase})\n"
    f"Greatest Decrease in Profits: {decrease_date} (${greatest_decrease})\n"
    )
print(output)

with open(txt_file,"w") as txtfile:
    txtfile.write(output)