import os
import csv
# Set path for file, process 2 works best.
#filepath = os.path.join('C:', 'Users', 'Jeremiah', 'Desktop', 'repos', 'python-challenge', 'PyBank', 'Resources', 'budget_data.csv')
from pathlib import Path
file_path = Path("C:/Repos/python-challenge/PyBank/Resources") /'budget_data.csv'
# Creating list to storing variables for manipulation
budget_data = []

# Opening the CSV
with open(file_path) as csvfile:
    reader = csv.DictReader(csvfile)

    # Create data dictionary, loop with calc profit divided by loss
    for row in reader:
        budget_data.append({"month": row["Date"], "amount": int(row["Profit/Losses"]),"change": 0})

# Calculating the total months by using total number of rows
total_months = len(budget_data)

# Looping through the dictionary in order to calculate changes between months
previous_amount = budget_data[0]['amount']
for i in range(total_months):
    budget_data[i]['change'] = budget_data[i]['amount'] - previous_amount
    prev_amount = budget_data[i]['amount']

# Calculating the total amount
total_amount = sum(row['amount'] for row in budget_data) 

# Calculating the average of amount changes
total_change = sum(row['change'] for row in budget_data)
average = round(total_change / (total_months-1), 2)

# Getting the  Greatest Increase and Decrease from the changes
get_increase = max(budget_data, key=lambda x:x['change'])
get_decrease = min(budget_data, key=lambda x:x['change'])


# End product displayed
print('Financial Analysis')
print('----------------------------')
print(f'Total Months: {total_months}')
print(f'Total: ${total_amount}')
print(f'Average Change: ${average}')
print(f'Greatest Increase in Profits: {get_increase["month"]} (${get_increase["change"]})')
print(f'Greatest Decrease in Profits: {get_decrease["month"]} (${get_decrease["change"]})')


# Printing  the analysis and exporting to a text file 
# Set path for file
file_path = Path("C:/Repos/python-challenge/PyBank/Resources") /'analysis.txt'
with open(file_path, "w") as text_file:
    print('Financial Analysis', file=text_file)
    print('----------------------------', file=text_file)
    print(f'Total Months: {total_months}', file=text_file)
    print(f'Total: ${total_amount}', file=text_file)
    print(f'Average Change: ${average}', file=text_file)
    print(f'Greatest Increase in Profits: {get_increase["month"]} (${get_increase["change"]})', file=text_file)
    print(f'Greatest Decrease in Profits: {get_decrease["month"]} (${get_decrease["change"]})', file=text_file)


# In[ ]:
