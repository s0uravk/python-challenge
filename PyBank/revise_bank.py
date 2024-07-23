import csv

budget_data = r'python-challenge\PyBank\Resources\budget_data.csv'

with open(budget_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    number_of_months = 0
    total_profitloss = 0
    change = 0
    change_in_pl = []
    previous_month_pl = 0
    current_month_pl = 0
    month_ls = []
    for row in csvreader:

        number_of_months += 1

        total_profitloss += int(row[1])

        current_month_pl = int(row[1])

        if(number_of_months == 1):
            previous_month_pl = current_month_pl
        else :
            change = current_month_pl - previous_month_pl
            
            previous_month_pl = current_month_pl

            change_in_pl.append(change)

            month_ls.append(row[0])
        
    def avg(ls):
        sum = 0
        for i in ls :
            sum += i
        return sum/len(ls)
        
    greatest_increase_profit = max(change_in_pl)
    greatest_decrease_profit = min(change_in_pl)

    greatest_increase_profit_month = month_ls[change_in_pl.index(greatest_increase_profit)]
    greatest_decrease_profit_month = month_ls[change_in_pl.index(greatest_decrease_profit)]

    print('Finanical Analysis')
    print('-' * 45)
    print(f'Total Months :  {number_of_months}')
    print(f'Total : ${total_profitloss}')
    print(f'Average Change : ${avg(change_in_pl):.2f}')
    print(f'Greatest Increase in Profits : {greatest_increase_profit_month} (${greatest_increase_profit})')
    print(f'Greatest Decrease in Profits : {greatest_decrease_profit_month} (${greatest_decrease_profit})')
    
    output_path = r'python-challenge\PyBank\Output\analysis.txt'

    with open(output_path, 'w') as txtfile:
        writer = csv.writer(txtfile)

        writer.writerow(['Financial Analysis'])
        writer.writerow(['-' * 45])
        writer.writerow([f'Total Months :  {number_of_months}'])
        writer.writerow([f'Total : ${total_profitloss}'])
        writer.writerow([f'Average Change : ${avg(change_in_pl):.2f}'])
        writer.writerow([f'Greatest Increase in Profits : {greatest_increase_profit_month} (${greatest_increase_profit})'])
        writer.writerow([f'Greatest Decrease in Profits : {greatest_decrease_profit_month} (${greatest_decrease_profit})'])