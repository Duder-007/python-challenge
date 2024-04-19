import os
import csv
from pathlib import Path
file_path = Path("C:/Repos/python-challenge/PyPoll/Resources") /'election_data.csv'

with open(file_path, newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    csv_header = next(reader)
    candidate_list = [candidate[2] for candidate in reader]
    
total_votes = len(candidate_list) #number of rows, total length

# number of votes matching the list
canditates_data = [[candidate,candidate_list.count(candidate)] for candidate in set(candidate_list)]

# Lambda magic monkey theorom
canditates_data = sorted(canditates_data, key=lambda x: x[1], reverse=True)
for candidate in canditates_data:
    percent_votes = (candidate[1] / total_votes) * 100
    print(f'{candidate[0]}: {percent_votes:6.3f}% ({candidate[1]})')

# Output
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
print("-------------------------")
print(f"Winner: {canditates_data[0][0]}")
print("-------------------------")

file_path = Path("C:/Repos/python-challenge/PyPoll/Resources") /'Results.txt'
with open(file_path, "w") as text_file:
    print("Election Results", file=text_file)
    print("-------------------------", file=text_file)
    print(f"Total Votes: {total_votes}", file=text_file)
    print("-------------------------", file=text_file)

    for candidate in canditates_data:
        percent_votes = (candidate[1] / total_votes) * 100
        print(f'{candidate[0]}: {percent_votes:6.3f}% ({candidate[1]})', file=text_file)

    for candidate in canditates_data:
        percent_votes = (candidate[1] / total_votes) * 100
        print(f'{candidate[0]}: {percent_votes:6.3f}% ({candidate[1]})', file=text_file)

    print("-------------------------", file=text_file)
    print(f"Winner: {canditates_data[0][0]}", file=text_file)
    print("-------------------------", file=text_file)