import os
import csv


# Path to collect data from the Resources folder
poll_csv = os.path.join('/Users/eobodoechine/fake directory/python-challenge/PyPoll', 'Resources', '03-Python_Homework_Instructions_PyPoll_Resources_election_data.csv')


#set total to 0
total = 0


#open file and set inital variables and lists to be used in analysis
with open(poll_csv) as csv_file:
    csvreader = csv.reader(csv_file, delimiter=",")
    header = next(csvreader)
    reader = list(csvreader)
    change = []
    



#find total and create 2 lists with same values as 2nd column in reader list
    for row in reader:
        total += 1
        change.append(row[2])

correy_count = 0
li_count = 0
tooley_count = 0
khan_count = 0

# find individual names and counts
names = list(set(change))
for row in change:
    if row == 'Correy':
        correy_count += 1
    elif row == 'Khan':
        khan_count += 1
    elif row == 'Li':
        li_count += 1
    elif row == "O'Tooley":
        tooley_count += 1
    

#create coount list and add values to it
count = []
count.append(correy_count)
count.append(khan_count)
count.append(li_count)
count.append(tooley_count)


#create percentage list, calculate percentages and update list
percentages = []
correy_perc = correy_count/total
correy_percentage = "{:.3%}".format(correy_perc)
percentages.append(correy_percentage)
khan_perc = khan_count/total
khan_percentage = "{:.3%}".format(khan_perc)
percentages.append(khan_percentage)
li_perc = li_count/total
li_percentage = "{:.3%}".format(li_perc)
percentages.append(li_percentage)
tooley_perc = tooley_count/total
tooley_percentage = "{:.3%}".format(tooley_perc)
percentages.append(tooley_percentage)

#Find max percentage, combine lists
maxp = max(percentages)
n = sorted(names)
zipped = zip(n, percentages)

#find winner
for n_i, percentages_i in zipped:
    if percentages_i == maxp:
        winner = (str(n_i))
        

print("Election Results")
print("----------------------------")
#count lines to give total months
#print("Total Months: " + str(lines))
#count total profit/losses
print("Total Votes: " + str(total))
print("----------------------------")
print(n[0] + ": " + str(percentages[0]) + " (" + str(count[0]) + ")")
print(n[1] + ": " + str(percentages[1]) + " (" + str(count[1]) + ")")
print(n[2] + ": " + str(percentages[2]) + " (" + str(count[2]) + ")")
print(n[3] + ": " + str(percentages[3]) + " (" + str(count[3]) + ")")
print("----------------------------")
print("Winner: " + winner)
print("----------------------------")



#print results to txt file
import sys
f = open("/Users/eobodoechine/fake directory/python-challenge/PyPoll/Analysis/Analyis.txt", 'w')
sys.stdout = f
print("Election Results")
print("----------------------------")
#count lines to give total months
#print("Total Months: " + str(lines))
#count total profit/losses
print("Total Votes: " + str(total))
print("----------------------------")
print(n[0] + ": " + str(percentages[0]) + " (" + str(count[0]) + ")")
print(n[1] + ": " + str(percentages[1]) + " (" + str(count[1]) + ")")
print(n[2] + ": " + str(percentages[2]) + " (" + str(count[2]) + ")")
print(n[3] + ": " + str(percentages[3]) + " (" + str(count[3]) + ")")
print("----------------------------")
print("Winner: " + winner)
print("----------------------------")
f.close()
