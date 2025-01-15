# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join(".\PyBank\Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join(".\PyBank\Analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
# Add more variables to track other necessary financial data

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)
    csvreader = csv.reader(financial_data, delimiter=',')

    # Skip the header row
    header = next(reader)
    
    # Extract first row to avoid appending to net_change_list
    # row1 = next(reader)
    months = []
    totalProfit = []
    netChangeList = []
    totalProfitValue = 0
    
    # Store full data into seperate arrays. 1 For months and 1 for Total Profit recorded per month
    # Total Profit variable in incremented per integer value of monthly profit
    for r in csvreader:
        months.append(r[0])
        totalProfit.append(int(r[1]))
        totalProfitValue += int(r[1])
    
    # Store length of months array 
    totalMonths = len(months)
    # Store monthly net change. -1 because we are calculating change from month to month
    for m in range(len(totalProfit) - 1):
        netChangeList.append(totalProfit[m+1]-totalProfit[m])
    
    # Store total net change so we can make average calculation
    totalNetChange = 0
    for i in range(len(netChangeList)):
        totalNetChange += netChangeList[i]
    averageNetChange = round(totalNetChange/len(netChangeList), 2)
    
    # Calculate greatest increase/decrease and store their index in the array so we can iterate through months with the same index value
    greatestIncrease = max(netChangeList)
    greatestDecrease = min(netChangeList)
    greatestIncreaseIndex = 0
    greatestDecreaseIndex = 0
    for index in range(len(netChangeList)):
        if(netChangeList[index] == greatestIncrease):
            greatestIncreaseIndex = index
        elif(netChangeList[index] == greatestDecrease):
            greatestDecreaseIndex = index

    # greatestIncreaseIndex + 1 to account for netChange calculation starting at Feb-10 instead of Jan-10
    greatestIncreaseMonth = months[greatestIncreaseIndex+1]
    greatestDecreaseMonth = months[greatestDecreaseIndex+1]

# Write the results to a text file
with open(file_to_output, "w") as output:
    output.write("Financial Analysis\n")
    output.write("--------------------------------\n")
    output.write(f"Total Months: {totalMonths}\n")
    output.write(f"Total: ${totalProfitValue}\n")
    output.write(f"Average Change: ${averageNetChange}\n")
    output.write(f"Greatest Increase In Profits: {greatestIncreaseMonth} (${greatestIncrease})\n")
    output.write(f"Greatest Decrease In Profits: {greatestDecreaseMonth} (${greatestDecrease})\n")
