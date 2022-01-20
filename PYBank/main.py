import csv
import os

#path to collect data and export
#csvpath = os.path.join(r"Resources",r"budget_data.csv")
csvpath = r"C:\Users\brian\OneDrive\Documents\NU data camp\Homework\Python-Homework\PYBank\Resources\budget_data.csv"
csvpath_output = ("Analysis","budget_data.txt")
print(csvpath)
#open readable
with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    
    #initialize
    row = next(csvreader)
    previous_amount = int(row[1])
    month_count = 1
    month = row[0]
    total = int(row[1])

    #if I can add delta to list, then I can pull the max delta and the min delta with the associated dates?
    #finding sum of 
    for row in csvreader:
        month_count = month_count + 1
        month = row[0]
        current_amount = int(row[1])
        total = total + current_amount
        delta = current_amount - previous_amount
        
        print(month_count,month,previous_amount,current_amount,total,delta)
        #this months current amount is next months previous amount
        previous_amount = current_amount


avg_profit = sum(int(delta)) / len(month_count)
print(avg_profit)


# print(months)
# print(amounts)
# sum_months = (len(months))
# sum_profits = (sum(amounts))


# print(amounts[4])
# # for i in range(sum_months):
# #     print(f"{i}     {amounts[i]}")

# for i in range(1,sum_months):
#     delta = amounts[i]-amounts[i-1]
#     print(delta)


# # print("Financial Analysis")
# # print("-----------------------------------")
# # print("Total Months: " + str(sum_months))
# # print("Total : " + "$" + str(sum_profits))


# # # #variables needed to solve 
# # # sum_months = 0
# # # sum_profit = 0
# # # #current_rev = # current - last = difference
# # # #last_rev =  #needs to be stored using len to itirate?





# # #     #sums months (rows)
# # # print ("read" + str(len(date)) + "rows")
# # #     #sum profit
# # # sum_profit = 0
# # # for i in csvreader:
# # #     sum_profit = sum_profit + i
# # #     print (sum_profit)
    
    






# # Generate Output Summary
# #output = (
#    # f"Financial Analysis\n"
#     #f"----------------------------\n"
#     #f"Total Months: {total_months}\n"
#     #f"Total: ${total_net}\n"
#     #f"Average  Change: ${net_monthly_avg:.2f}\n"
#     #f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
#     #f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

# # Print the output (to terminal)
# #print(output)

# # Export the results to text file