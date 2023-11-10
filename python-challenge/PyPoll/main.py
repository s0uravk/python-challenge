import csv
def vote_count():
    count = 0
    if((candidates[rows[1]][0]) in rows[2]):
        count += 1

        return count

#input file path
file_in = "election_data.csv"


candidatesNvotes = {}  #declaring a dictionary variable
total_votes = 0        #to count total iterations hence total votes
candidates_list = []   # to store keys of dictionary in a list
votes_per_candidate = []   # to store values of dictionary in a list
vote_percent = []      #to store vote percent calculated

#open input file to be processed
with open(file_in, 'r') as input_data :
    read = csv.reader(input_data, delimiter = ",")
    header = next(read)
    
    #loopin through the data in csv file
    for row in read :
        total_votes += 1      #total votes count
        if not row[2] in candidatesNvotes.keys(): #checking for candidate's name not in dictionary 
            candidatesNvotes[row[2]] =1           #first iteration of a key is not present in the dictionary, hence it adds a key as candidates_
                                                  #name and assign value for that first iteration
            
        else:                                     #checking for candidate's name in dictionary 
            candidatesNvotes[row[2]] += 1         #if name is found, adds one to the value of that key
   
    candidates_list.append(list(candidatesNvotes.keys()))     #appends candidate names into a list
    votes_per_candidate.append(list(candidatesNvotes.values())) ##appends votes per candidate into a list
    
    #print results to the terminal
    print("Election Results : ")
    print("---------------------------------------------------------------------------------------------------")
    print(f"Total Votes : {total_votes}")
    print("---------------------------------------------------------------------------------------------------")
    for votes in candidatesNvotes.values() :                #to print the candidate name, percentage of votes and number of votes a candidate won for each candidate
    
        percent = votes/total_votes                  
        vote_percent.append(percent)
        candidate = candidates_list[0][vote_percent.index(percent)]
        votes_won = votes_per_candidate[0][vote_percent.index(percent)]
        
        print(f"{candidate} : {percent :.2%} ({votes_won})")
        
    win_votes = max(votes_per_candidate[0])
    winner = candidates_list[0][vote_percent.index(max(vote_percent))]
    print("---------------------------------------------------------------------------------------------------")
    print(f"Winner is {winner} : {vote_percent[0] :.2%} ")
    
#creating an output file path  
outFile = "results.txt"

#manipulation of result
with open(outFile,'w') as output_data :
    writer = csv.writer(output_data)
    writer.writerow(["Election Results : "])
    writer.writerow(["---------------------------------------------------------------------------------------------------"])
    writer.writerow([f"Total Votes : {total_votes}"])
    writer.writerow(["---------------------------------------------------------------------------------------------------"])
    for votes in candidatesNvotes.values() :
    
        percent = int(votes)/total_votes
        vote_percent.append(percent)
        candidate = candidates_list[0][vote_percent.index(percent)]
        votes_won = votes_per_candidate[0][vote_percent.index(percent)]
        
        writer.writerow([f"{candidate} : {percent :.2%} ({votes_won})"])
    
    writer.writerow(["---------------------------------------------------------------------------------------------------"])
    writer.writerow([f"Winner is {winner} : {vote_percent[0] :.2%} "])
    writer.writerow(["---------------------------------------------------------------------------------------------------"])
