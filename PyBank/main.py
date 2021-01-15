import os
import csv

row_count=0
total_sum=0
total_change=0
largest_increase=[" ", 0]
largest_decrease=[" ", 999999999]

budget_data = os.path.join( 'Resources', 'budget_data.csv')

#print(budget_data) # prints path

with open(budget_data, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile) 

    # print(csv_header) = prints headers "Date, Profit/Losses"

    first_row=next(csv_reader) # skips first row (headers)
    
    last_month_value=first_row[1] # second column [1] from row "first_row"
    row_count+=1 # same as : row_count = row_count + 1
    total_sum+=int(first_row[1]) 

    for row in csv_reader: 
        monthly_change=int(row[1])-int(last_month_value)
        total_change+=monthly_change
        if monthly_change > largest_increase[1]:
            largest_increase[1]=monthly_change
            largest_increase[0]=row[0]
        if monthly_change < largest_decrease[1]:
            largest_decrease[1]=monthly_change
            largest_decrease[0]=row[0]
        row_count+=1 
        total_sum+=int(row[1])
        last_month_value=int(row[1])

    print("Financial Analysis")
    print("----------------------------")    
    print(f"Total Months: {row_count}")
    print(f"Total: ${total_sum}")
    print(f"Average  Change: ${round(total_change/(row_count-1), 2)}")
    print(f"Greatest Increase in Profits: {largest_increase[0]} (${largest_increase[1]})")
    print(f"Greatest Decrease in Profits: {largest_decrease[0]} (${largest_decrease[1]})")

    Line1="Financial Analysis\n"
    Line2="----------------------------\n"    
    Line3=f"Total Months: {row_count}\n"
    Line4=f"Total: ${total_sum}\n"
    Line5=f"Average  Change: ${round(total_change/(row_count-1), 2)}\n"
    Line6=f"Greatest Increase in Profits: {largest_increase[0]} (${largest_increase[1]})\n"
    Line7=f"Greatest Decrease in Profits: {largest_decrease[0]} (${largest_decrease[1]})\n" 
    L = [Line1, Line2, Line3, Line4, Line5, Line6, Line7]

output_path = os.path.join('analysis', 'analysis_file.txt')

with open(output_path, 'w',  newline='') as textfile:
    textfile.writelines(L)
    textfile.close()

