import csv

budget_data = r'python-challenge\PyBank\Resources\budget_data.csv'

with open(budget_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    for row in csvreader:
        print(row)
        break