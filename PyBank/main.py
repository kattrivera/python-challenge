# import os and csv module
import os
import csv

# map csv file path in and txt file path out
budget_dataPath = os.path.join("Resources", "budget_data.csv")
budget_dataOut = os.path.join("Analysis","budget_data_summary.txt")

# read csv file
with open(budget_dataPath) as budget_dataFile:
    budget_dataReader = csv.reader(budget_dataFile, delimiter=",")
    
# ignore headers
    header = next(budget_dataReader)

# set variables and lists
    total_months = 0
    total_PL = 0
    curMonthly_PL = 0
    preMonthly_PL = 867884
    monthly_ChangeList = []
    avg_Change = 0
    date = []
    gi_Profits = 0
    gd_Losses = 0

# start looping by rows in reader    
    for row in budget_dataReader:

# month count by counting rows incrementally        
        total_months += 1

# PL total by adding row values incrementally        
        total_PL += int(row[1])

# set variables to calculate monthly change and add to list to hold values        
        curMonthly_PL = row[1] 
        monthly_Change = float(curMonthly_PL) - float(preMonthly_PL)
        preMonthly_PL = row[1]
        monthly_ChangeList.append(monthly_Change)

# find max value of monthly change by using max and index function to grab date and value        
        date.append(row[0])
        gi_Profits = max(monthly_ChangeList)
        max_DateIndex = monthly_ChangeList.index(gi_Profits)
        max_Date = date[max_DateIndex]

# find min value of monthly change by using min and index function to grab date and value       
        gd_Losses = min(monthly_ChangeList)
        min_DateIndex = monthly_ChangeList.index(gd_Losses)
        min_Date = date[min_DateIndex]

# calculate average monthly change        
    avg_Change = sum(monthly_ChangeList)/(total_months-1)

# print to Git Bash    
print("------------------------------------")
print("Financial Analysis")
print("------------------------------------")
print(f"Total Months: {total_months}") 
print(f"Total PL: {total_PL}")
print(f"Average Change: {avg_Change}")
print(f"Greatest Increase Profits: {max_Date} (${gi_Profits})")
print(f"Greatest Decrease Losses: {min_Date} (${gd_Losses})")
print("-------------------------------------") 

# print to txt file
with open(budget_dataOut, "w") as txtFile:  
    print("------------------------------------", file=txtFile)
    print("Financial Analysis", file=txtFile)
    print("------------------------------------", file=txtFile)
    print(f"Total Months: {total_months}", file=txtFile) 
    print(f"Total PL: {total_PL}", file=txtFile)
    print(f"Average Change: {avg_Change}", file=txtFile)
    print(f"Greatest Increase Profits: {max_Date} (${gi_Profits})", file=txtFile)
    print(f"Greatest Decrease Losses: {min_Date} (${gd_Losses})", file=txtFile)
    print("-------------------------------------", file=txtFile)
        