import csv
def vote_count():
    count = 0
    if((candidates[rows[1]][0]) in rows[2]):
        count += 1

        return count

#input file path
file_in = "PyPoll\Resources\election_data.csv"

#declaring a dictionary variable
candidates = {}
votes = []
count = 0
#open input file to be processed
with open(file_in, 'r') as input_data :
    read = csv.reader(input_data, delimiter = ",")
    header = next(read)
    
    for rows in read :
        if rows[1] in candidates.keys(): 
            if not rows[2] in candidates[rows[1]]:
                candidates[rows[1]].append(rows[2])
               
        else: 
            candidates[rows[1]] = [rows[2]]
        
        for people in candidates[rows[1]]:
            if((candidates[rows[1]][0]) in rows[2]):
                count += 1

    votes.append(count)
    print(votes)


            
                      
            
    print(candidates[rows[1]][2])   
    print(candidates)
   
    
    



