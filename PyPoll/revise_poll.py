import csv

election_data = r'python-challenge\PyPoll\Resources\election_data.csv'

with open(election_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    candidates_votes = {}
    total_votes = 0

    for row in csvreader:
        total_votes += 1

        if(row[2] not in candidates_votes):
            candidates_votes[row[2]] = 1
        else:
            candidates_votes[row[2]] += 1

    print('Election Results')
    print('-' * 45)
    print(f'Total Votes : {total_votes}')
    print('-' * 45)
    for data in candidates_votes:
        votes_per_candidate = candidates_votes[data]
        percentage_votes = votes_per_candidate/total_votes
        print(f'{data}: {percentage_votes:.3%} ({votes_per_candidate})')
    print('-' * 45)
    print(f'Winner : {max(candidates_votes, key = lambda k: candidates_votes[k])} ({max(candidates_votes.values())})')
    print('-' * 45)

    output_file = r'python-challenge\PyPoll\Output\result.txt'

    with open(output_file, 'w') as txtfile:
        writer = csv.writer(txtfile)

        writer.writerow(['Election Results'])
        writer.writerow(['-' * 45])
        writer.writerow([f'Total Votes : {total_votes}'])
        writer.writerow(['-' * 45])
        for data in candidates_votes:
            votes_per_candidate = candidates_votes[data]
            percentage_votes = votes_per_candidate/total_votes
            writer.writerow([f'{data}: {percentage_votes:.3%} ({votes_per_candidate})'])
        writer.writerow(['-' * 45])
        writer.writerow([f'Winner : {max(candidates_votes, key = lambda k: candidates_votes[k])} ({max(candidates_votes.values())})'])
        writer.writerow(['-' * 45])