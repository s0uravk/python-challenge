import csv

#input file path
election_data_csv = r'python-challenge\PyPoll\Resources\election_data.csv'
# declaring dictionary to store values for candidates and there total votes
candidatesNvotes= {}
#variable to store value of percentagae calculated
vote_percent=0
#stores the value for maximum votes that is later converted into percentage in output
win_votes= 0

#open the csv file
with open(election_data_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #skip the header
    csvheader = next(csvreader)
    
    #loop through the csv data
    for row in csvreader:
        
        if not row[2] in candidatesNvotes.keys(): #checking for candidate's name not in dictionary 
            candidatesNvotes[row[2]] = 1          #first iteration of a key is not present in the dictionary, hence it adds a key as candidates_
                                                 #name and assign value for that first iteration
                                                              
        else:                                     #checking for candidate's name in dictionary 
            candidatesNvotes[row[2]] += 1         #if name is found, adds one to the value of that key

    #output data to terminal        
    print("Election Results : ")
    print("---------------------------------------------------------------------------------------------------")
    print(f"Total Votes : {sum(candidatesNvotes.values())}") #sum function to add the votes per candidate
    print("---------------------------------------------------------------------------------------------------")
    
    #loop through the dictionary created earlier and ouput the data to terminal
    for candidate in candidatesNvotes :

        #calulate percentage of votes by accessing the values using keys(candidate)
        vote_percent = candidatesNvotes[candidate]/sum(candidatesNvotes.values())
        print(f"{candidate} : {vote_percent:.3%} ({candidatesNvotes[candidate]})")

    
    win_votes = max(candidatesNvotes.values())/sum(candidatesNvotes.values())
    winner = [i for i in candidatesNvotes if candidatesNvotes[i] == max(candidatesNvotes.values())]
  
    print("---------------------------------------------------------------------------------------------------")
    print(f"Winner : {winner[0]} ({win_votes :.2%}) ")
    
#creating an output file path  
outFile = r'python-challenge\PyPoll\Output\result.txt'

#manipulation of result
with open(outFile,'w') as output_data :
    writer = csv.writer(output_data)
    writer.writerow(["Election Results : "])
    writer.writerow(["---------------------------------------------------------------------------------------------------"])
    writer.writerow([f"Total Votes : {sum(candidatesNvotes.values())}"])
    writer.writerow(["---------------------------------------------------------------------------------------------------"])
    for candidate in candidatesNvotes :
        vote_percent = candidatesNvotes[candidate]/sum(candidatesNvotes.values())
        writer.writerow([f"{candidate} : {vote_percent :3%} ({candidatesNvotes[candidate]})"])
    
    writer.writerow(["---------------------------------------------------------------------------------------------------"])
    writer.writerow([f"Winner : {winner[0]} : ({win_votes :.2%}) "])
    writer.writerow(["---------------------------------------------------------------------------------------------------"])


