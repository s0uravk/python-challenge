import csv
import os

filein = r"python-challenge\PyBank\Resources\budget_data.csv"

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

with open(filein, 'r') as input_data:
    read = csv.reader(input_data, delimiter= ',')
    header = next(read)
    
    for rows in read:
        months.append(rows[0])
     
        net_pNl += int(rows[1])
        
        counter_month  += 1  
        
        current_month_pNl = int(rows[1])
       
        if(counter_month == 1) :
            previous_month_pNl = current_month_pNl
            
        else :
            change = current_month_pNl - previous_month_pNl
            previous_month_pNl = current_month_pNl
            
            changes_pNl.append(change)
               
avg_change = round(sum(changes_pNl)/(counter_month-1),2)   
grt_profit = max(changes_pNl)
  
grt_profit_month = months[changes_pNl.index(grt_profit)+1]

grt_loss = min(changes_pNl)

grt_loss_month = months[changes_pNl.index(grt_loss)+1]
   
print("Financial Analysis")     
print("-------------------------------------------------------")      
print(f"Total Months : {counter_month}")
print (f"Total Profit : ${net_pNl}")
print(f"Average Change : {avg_change}")
print(f"Best Month : {grt_profit_month} (${grt_profit})")
print(f"Worst Month : {grt_loss_month} (${grt_loss})")

fileout = r"python-challenge\PyBank\Output\analysis.txt"

with open (fileout, 'w') as output_data :
    writer = csv.writer(output_data)
    
    writer.writerow (["Financial Analysis "])
    writer.writerow (["-------------------------------------------------------"])      
    writer.writerow ([f"Total Months : {counter_month}"])
    writer.writerow ([f"Total Profit : ${net_pNl}"])
    writer.writerow ([f"Average Change : {avg_change}"])
    writer.writerow ([f"Best Month : {grt_profit_month} (${grt_profit})"])
    writer.writerow ([f"Worst Month : {grt_loss_month} (${grt_loss})"])

    


