import csv
import os

#input file path
filein = r"python-challenge-main\PyBank\Resources\budget_data.csv"

#declaring required variables
months = []
changes_pNl =[]
net_pNl = 0
avg_change = 0
counter_month = 0
grt_loss_month = 0
grt_profit_month = 0
current_month_pNl = 0
previous_month_pNl = 0
grt_loss = 0
grt_profit = 0

#open the csv file
with open(filein, 'r') as input_data:
    read = csv.reader(input_data, delimiter= ',')

    #skip the header
    header = next(read)
    
    #loop through the csv data
    for rows in read:
        months.append(rows[0])     #storing all the months in months list
     
        net_pNl += int(rows[1])    #calculate total of Profit/Loss
        
        counter_month  += 1        #count number of observation, in this case months
        
        current_month_pNl = int(rows[1])      #assigining value of profit/loss to the variable
       
        if(counter_month == 1) :
            previous_month_pNl = current_month_pNl       #for first month as there is no previous data to find the difference from, assigning value of first months profit/loss to previous month variable for nexr iteration
            
        else :                                           #for rest of months, data will be calculated in else block
            change = current_month_pNl - previous_month_pNl              #calculating change occured
            previous_month_pNl = current_month_pNl                       #assigning current months profit/loss to previous month variable for next iteration
            
            changes_pNl.append(change)                      #appending the calculation into a list
               
avg_change = round(sum(changes_pNl)/(counter_month-1),2)   #calculate average change, chnages occured 85 times hence subtracting one from total months
grt_profit = max(changes_pNl)                              #calculate greatest positive change
  
grt_profit_month = months[changes_pNl.index(grt_profit)+1]   #finding month for greatest positive change

grt_loss = min(changes_pNl)                               #calculate greatest negative change

grt_loss_month = months[changes_pNl.index(grt_loss)+1]        #calculate greatest negative chang

#output data to terminal  
print("Financial Analysis")     
print("-------------------------------------------------------")      
print(f"Total Months : {counter_month}")
print (f"Total Profit : ${net_pNl}")
print(f"Average Change : {avg_change}")
print(f"Best Month : {grt_profit_month} (${grt_profit})")
print(f"Worst Month : {grt_loss_month} (${grt_loss})")

#creating an output file path 
fileout = r"python-challenge-main\PyBank\Output\analysis.txt"

#manipulation of result
with open (fileout, 'w') as output_data :
    writer = csv.writer(output_data)
    
    writer.writerow (["Financial Analysis "])
    writer.writerow (["-------------------------------------------------------"])      
    writer.writerow ([f"Total Months : {counter_month}"])
    writer.writerow ([f"Total Profit : ${net_pNl}"])
    writer.writerow ([f"Average Change : {avg_change}"])
    writer.writerow ([f"Best Month : {grt_profit_month} (${grt_profit})"])
    writer.writerow ([f"Worst Month : {grt_loss_month} (${grt_loss})"])
