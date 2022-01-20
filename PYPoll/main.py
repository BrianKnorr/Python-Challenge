# math formulas
# Count voters
#     Create a loop that has a count ticker for every row not including header
# Count Khan
#     for every instance that khan is run into while looping through rows for voter count, stor khan
# Count Correy
#     for every instance that khan is run into while looping through rows for voter count, stor khan
# Count Li
#     for every instance that khan is run into while looping through rows for voter count, stor khan
# Count O'Tooley
#     for every instance that khan is run into while looping through rows for voter count, stor khan
# Percent Khan = (Count Khan/CountVoters)*100
# Percent Correy = (Count Correy/CountVoters)*100
# Percent Li = (Count Li/CountVoters)*100
# Percent O'Tooley = (Count O'Tooley/CountVoters)*100
#     Print all percents directly
# To find winner percents have to be stored and indexed



import csv
import os

csvpath = r"C:\Users\brian\OneDrive\Documents\NU data camp\Homework\Python-Homework\PYPoll\Resources\election_data.csv"    
csvpath_output = ("Analysis","election_data.txt")

print(csvpath)
#open readable
with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    #variabled
    row = next(csvreader)
    voter = [0]
    candidates = [2]
    county = [1]
    voter_count = 1

    for row in csvreader:
        voter_count = voter_count + 1
        voter = row[0]
        print(voter_count)





