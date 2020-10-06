import os
import csv

budget_data = os.path.join("Resources", "budget_data.csv")

date=[]
profit_losses=[]

with open (budget_data) as pybank_file:
    budget_file = csv.reader(pybank_file, delimiter=",")

    next(budget_file)

    for line in budget_file:
        date.append(line[0])
        profit_losses.append(line[1])

#Total Months calculation
months_total=len(date)


#Total profit/losses calculation
profit_losses=[int(i) for i in profit_losses]

total_profit_losses=0
for i in range(len(profit_losses)):
    total_profit_losses+=profit_losses[i]

#Calculation of the average change of profit/losses

preaverage_profit_losses=0
monthly_change=[]

for i in range(len(profit_losses)-1):
    a=(profit_losses[i+1])-(profit_losses[i])
    monthly_change.append(a)
    preaverage_profit_losses+=a

average_profit_losses=preaverage_profit_losses/(len(profit_losses)-1)
average_profit_losses=round(average_profit_losses,2)

# Greatest Increase in Profits

mayor=monthly_change[0]

for i in range(len(monthly_change)):
    if monthly_change[i]>mayor:
        mayor=monthly_change[i]
        mayor_month=date[i+1]

# Greatest Decrease in Profits

menor=monthly_change[0]

for i in range(len(monthly_change)):
    if monthly_change[i]<menor:
        menor=monthly_change[i]
        menor_month=date[i+1]

result=(f"""
Financial Analysis
----------------------------
Total Months: {months_total}
Total: ${total_profit_losses}
Average  Change: ${average_profit_losses}
Greatest Increase in Profits: {mayor_month} (${mayor})
Greatest Decrease in Profits: {menor_month} (${menor})
```
""")

print(result)

# Export a text file with the results

writer =open('financial_analysis.txt', "w")
writer.write(result)
writer.close()
