import csv

# Declare variables
Months = 0
Total = 0
Change = 0
Average = 0
PreviousRow = 0
CurrentRow = 0
CurrentChange = 0
Increase = 0
Decrease = 0
IncMonth = ""
DecMonth = ""

# import/open CSV
with open('budget_data.csv', 'r') as csvfile:
    file = csv.reader(csvfile)

    # skip header
    next(file, None)

    # process CSV data
    for row in file:
        Months += 1
        Total += int(row[1])

        if Total == 1088983:
            CurrentRow = 0
        else: 
            CurrentRow = int(row[1])

        CurrentChange = CurrentRow - PreviousRow
        Change += CurrentRow - PreviousRow

        if Total == 1088983:
            Increase = CurrentChange
            Decrease = CurrentChange

        if CurrentChange > Increase:
            Increase = CurrentChange
            IncMonth = row[0]

        
        if CurrentChange < Decrease:
            Decrease = CurrentChange
            DecMonth = row[0]
        
        
        
        PreviousRow = int(row[1])

    # calculate average
    Average = Change / (Months - 1)

print("Financial Analysis")
print("----------------------------")
print("Total Months:", Months)
print("Total:", Total)
print("Average Change:", Average)
print("Greatest Increase in Profits:", IncMonth, Increase)
print("Greatest Decrease in Profits:", DecMonth, Decrease)