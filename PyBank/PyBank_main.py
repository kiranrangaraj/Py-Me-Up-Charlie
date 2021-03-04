import os
import csv

filename = "/Users/kiranrangaraj/Desktop/Classwork/Homework/python_challenge/PyBank"
PyBank_csv = os.path.join(filename, "Resources", "budget_data.csv")

total_months = 0
net_total_amount = 0
month_of_change = []
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 0]

with open(PyBank_csv, 'r') as csvfile:
    reader = csv.reader(csvfile)
    
    header = next(reader)
    first_row = next(reader)
    total_months += 1
    net_total_amount += int(first_row[1])
    prev_net = int(first_row[1])

    for row in reader:
        total_months += 1
        
        net_total_amount += int(row[1])
        
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list += [net_change]
        month_of_change += [row[0]]

        avg_monthly_change = sum(net_change_list) / len(net_change_list)

        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change

        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row [0]
            greatest_decrease[1] = net_change

output = (
    f"Financial Analysis\n"
    f"--------------------------------------------------\n"
    f"Total Months: {total_months}\n"
    f"Net Total Amount: ${net_total_amount}\n"
    f"Average Change: ${avg_monthly_change}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]}, ${greatest_increase[1]}\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]}, ${greatest_decrease[1]}\n"
    )

print(output)

exportfile = "/Users/kiranrangaraj/Desktop/Classwork/Homework/python_challenge/PyBank"
PyBank_export = os.path.join(exportfile, "Analysis", "PyBank_Analysis.txt")

with open(PyBank_export, "w") as txt_file:
    txt_file.write(output)
