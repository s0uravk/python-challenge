import csv

election_data = r'python-challenge\PyPoll\Resources\election_data.csv'

with open(election_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    for row in csvreader:
        print(row)
        break