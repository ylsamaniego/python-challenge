import csv

# Declare variables
Total = 0
Winner = ""
Candidate1 = "Charles Casper Stockham"
Candidate2 = "Diana DeGette"
Candidate3 = "Raymon Anthony Doane"
Vote1 = 0
Vote2 = 0
Vote3 = 0

# import/open CSV
with open('election_data.csv', 'r') as csvfile:
    file = csv.reader(csvfile)

    # skip header
    next(file, None)

    # process CSV data
    for row in file:
        Total += 1

        if row[2] == Candidate1:
            Vote1 += 1
        elif row[2] == Candidate2:
            Vote2 += 1
        elif row[2] == Candidate3:
            Vote3 += 1

# Determine Winner
if Vote1 > Vote2 and Vote1 > Vote3:
    Winner = Candidate1
elif Vote2 > Vote1 and Vote2 > Vote3:
    Winner = Candidate2
elif Vote3 > Vote1 and Vote3 > Vote2:
    Winner = Candidate3
    


print("Election Results")
print("-------------------------")
print("Total Votes", Total)
print("-------------------------")
print("Charles Casper Stockham:", f"{Vote1 / Total:.3%}", Vote1)
print("Diana DeGette:", f"{Vote2 / Total:.3%}", Vote2)
print("Raymon Anthony Doane:", f"{Vote3 / Total:.3%}", Vote3)
print("-------------------------")
print("Winner", Winner)
print("-------------------------")
