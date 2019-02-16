import os

# Module for reading CSV files
import csv
month_list = []
profit_loss_list = []
csvpath = os.path.join('Resources', 'budget_data.csv')
    
with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    
    for row in csvreader:
       # print(row)
        
    #loop through and count/add the number of months
    
        month_list.append(row[0])
        profit_loss_list.append(int(row[1]))
        
#print(profit_loss)
month_total = len(month_list)
profit_loss_total = sum(profit_loss_list)
##profit_loss_mean = profit_loss_total/month_total

print("Financial Analysis")
print("---------------------")

#print(f"Total Months: {month_total}")
#print(f"Total: ${profit_loss_total}")

#averagech = profit_loss_total/month_total
##print(f"Average Change:{profit_loss_mean}")
#print(max(profit_loss_list))

change_list = []

for i in range(len(profit_loss_list)-1):
    change_list.append(profit_loss_list[i+1]-profit_loss_list[i])
average_change = round(sum(change_list)/len(change_list),2)

#totalmonth = ["Total Months:", "Total:"{month_total}")
total= print(f"Total: ${profit_loss_total}")
average = print(f"Average Change: ${average_change}")
maxy = print(f"Greatest Increase in Profits: {month_list[change_list.index(max(change_list))+1]} (${max(change_list)})")
minx = print(f"Greatest Decrease in Profits: {month_list[change_list.index(min(change_list))+1]} (${min(change_list)})")

#results = [totalmonth,total,average,maxy,minx]
#results = print(f"Total Months: $"{month_total}, "Average Change": round(average_change,2)}
#print(f"Total: ${profit_loss_total}")
#print(f"Average Change: ${round(average_change,2)}")
#print(f"Greatest Increase in Profits: {month_list[change_list.index(max(change_list))+1]} (${max(change_list)})")
#print(f"Greatest Decrease in Profits: {month_list[change_list.index(min(change_list))+1]} (${min(change_list)})")
# Zip lists together

#print(results)
#cleaned_csv = zip(title, price, subscribers, reviews, review_percent, length)

# Set variable for output file
output_file = os.path.join("Resources","Pybank_LSA.txt")

output_file.write("Financial Analysis")
output_file.write("---------------------") 

 
output_file.close() 
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerow(["Title", "Course Price", "Subscribers", "Reviews Left",
                     "Percent of Reviews", "Length of Course"])

    # Write in zipped rows
    writer.writerows(cleaned_csv)


#  Open the output file
#with open(output_file, "w", newline="") as datafile:
    #writer = csv.writer(datafile)

    # Write the header row
    #writer.writerows(results)
   # writer.writerows(print(f"Total Months: {month_total}"))
    #writer.writerows(print(f"Total: ${profit_loss_total}"))
    #writer.writerows(print(f"Average Change: ${round(average_change,2)}"))
    #writer.writerows(print(f"Greatest Increase in Profits: {month_list[change_list.index(max(change_list))+1]} (${max(change_list)})"))
    #writer.writerows(print(f"Greatest Decrease in Profits: {month_list[change_list.index(min(change_list))+1]} (${min(change_list)})"))

    # Write in zipped rows
   # writer.writerows(cleaned_csv)