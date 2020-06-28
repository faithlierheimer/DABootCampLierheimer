
import os
import csv
csvpath = os.path.join(r'C:\Users\flier\Desktop\du-den-data-pt-06-2020-u-c\Class_Materials\03-Python\Homework\Instructions\PyBank\Resources', 'budget_data.csv')

#Read csv
with open(csvpath) as bank:
    bank = csv.reader(bank, delimiter = ',')
    print(bank)
    bank_header = next(bank)
    print(f"Bank Header: {bank_header}")
    for row in bank:
        print(row)