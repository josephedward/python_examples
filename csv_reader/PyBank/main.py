import os
import csv
import numpy as np

csvpath = os.path.join('.', '', 'PyBank.csv')

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)


    row_count = 0
    new_total = 0
    changes = []
    p_l = []

    print(f"CSV Header: {csv_header}")
    for row in csvreader:
        p_l.append(row)
        if row_count == 0:
            changes.append(0)
        changes.append(int(row[1]) - (int(p_l[row_count-1][1])))
        row_count += 1
        new_total += int(row[1])

changes.pop(0)
changes.pop(0)

print("Financial Analysis")
print("----------------------------")
print(f'Total Months: {row_count}')
print(f'Net Total: ${new_total}')
# print(f'Changes: {changes}')
print(f'Avg Change: ${"{0:.2f}".format(np.mean(changes))}')
print(
    f'Greatest Increase in Profits: {p_l[changes.index(max(changes))][0]} (${max(changes)})')
print(
    f'Greatest Decrease in Profits: {p_l[changes.index(min(changes))][0]} (${min(changes)})')

open('MyFile.txt', 'w').close()
file1 = open("MyFile.txt", "a")
file1.write("Financial Analysis"+"\n")
file1.write("----------------------------"+"\n")
file1.write(f'Total Months: {row_count}'+"\n")
file1.write(f'Net Total: ${new_total}'+"\n")
# file1.write(f'Changes: {changes}')
file1.write(
    f'Avg Change: ${"{0:.2f}".format(np.mean(changes))}'+"\n")
file1.write(
    f'Greatest Increase in Profits: (${p_l[changes.index(max(changes))][0]}) {max(changes)}'+"\n")
file1.write(
    f'Greatest Decrease in Profits: (${p_l[changes.index(min(changes))][0]}) {min(changes)}'+"\n")
