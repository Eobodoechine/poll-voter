import os
import csv


# Path to collect data from the Resources folder
bank_csv = os.path.join('/Users/eobodoechine/fake directory/python-challenge/PyBank', 'Resources', '03-Python_Homework_Instructions_PyBank_Resources_budget_data (2).csv')

#set total to 0
total = 0

#open file and set inital variables and lists to be used in analysis
with open(bank_csv) as csv_file:
    csvreader = csv.reader(csv_file, delimiter=",")
    header = next(csvreader)
    reader = list(csvreader)
    lines = len(reader)
    change = []
    yansh = []
    right = []
    zip_object = zip(change, yansh)
    sups = zip(reader, right)

#find total and create 2 lists with same values as 2nd column in reader list
    for row in reader:
        total += int(row[1])
        change.append(row[1])
        yansh.append(row[1])

#delete first value in list so previous value in yansh list can be subtracted by newer value in change list
change.pop(0)
for change_i, yansh_i in zip_object:
    right.append(int(change_i)-int(yansh_i))


#define average of set
def Average(right):
    return sum(right) / len(right)
average = Average(right)
#find max and min of right list
minset = min(right)
maxset = max (right)

#insert 0 to right so the number of values in right list match reader list
right.insert(0,0)
for reader_i, right_i in sups:
    if int(right_i) == minset:
        min_date = (str(reader_i[0]))

    if int(right_i) == maxset:
        max_date = (str(reader_i[0]))



print("Financial Analysis")
print("----------------------------")
#count lines to give total months
print("Total Months: " + str(lines))
#count total profit/losses
print("Total: $" + str(total))
#count average change in profit/losses
print("Average change: $" + str(round(average,2)))
print("Greatest Increase in Profits: " + str(max_date) + " ($" + str(maxset) + ")")
print("Greatest Decrease in Profits: " + str(min_date) + " ($" + str(minset) + ")")


#print results to txt file
import sys
f = open("/Users/eobodoechine/fake directory/python-challenge/PyBank/Analysis/Analyis.txt", 'w')
sys.stdout = f
print("Financial Analysis")
print("----------------------------")
#count lines to give total months
print("Total Months: " + str(lines))
#count total profit/losses
print("Total: $" + str(total))
#count average change in profit/losses
print("Average change: $" + str(round(average,2)))
print("Greatest Increase in Profits: " + str(max_date) + " ($" + str(maxset) + ")")
print("Greatest Decrease in Profits: " + str(min_date) + " ($" + str(minset) + ")")
f.close()

