import csv

input_file = "raw-data/budget_data.csv"

output_file = "output/budget_data.txt"

#variables
tot_months = 0
p_revenue = 0
tot_revenue = 0
month_change = []
revenue_list_chan = []
greatest_decr = ['', 99999999999]
greatest_incr = ['', 0]

#read and change to dic
with open(input_file) as revenue_info:
    reader = csv.DictReader(revenue_info)

    for row in reader:

        #(Total) calclations 
        tot_revenue = tot_revenue + int(row["Profit/Losses"])
        tot_months = tot_months + 1
       

        # change in revenue
        revenue_change = int(row["Profit/Losses"]) - p_revenue
        p_revenue = int(row["Profit/Losses"])
        month_change = month_change + [row["Date"]]
        revenue_list_chan = revenue_list_chan + [revenue_change]
      
        # decrease calculations 
        if (revenue_change < greatest_decr[1]):
            greatest_decr[0] = row["Date"]
            greatest_decr[1] = revenue_change
       
	   
	   # increase calculations 
        if (revenue_change > greatest_incr[1]):
            greatest_incr[0] = row["Date"]
            greatest_incr[1] = revenue_change

 
# change in avg revenue 
average_rev = sum(revenue_list_chan) / len(revenue_list_chan)

# Output 
output = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {tot_months}\n"
    f"Total : ${tot_revenue}\n"
    f"Average Change: ${average_rev}\n"
    f"Greatest Increase in profit: {greatest_incr[0]} (${greatest_incr[1]})\n"
    f"Greatest Decrease in profit: {greatest_decr[0]} (${greatest_decr[1]})\n")

# Print the output (to terminal)
print(output)

# Export the output to a text file
with open(output_file, "w") as txt_file:
    txt_file.write(output)