import pandas as pd
budget = pd.read_csv(r"C:\Users\flier\DABootCampLierheimer\Python-challenge\budget_data.csv")
#rename columns
budget.columns = ['date', 'pandl']

#count number of months
monthCount = budget.date.count()
#Sum total transactions
totalTransactions = budget.pandl.sum()

#average total change over budget period
averageChange = budget.pandl.mean()

#max increase over whole period 
maxChange = budget.max()

#max decrease over whole period
minChange = budget.min()

contents = print("The total number of months recorded was: " + str(monthCount) + "\n The gross total of all the transactions was: " + str(totalTransactions)
+ "\n The average change over the whole period of 86 months was: " + str(averageChange) + "\n The month with the greatest gain was: " + str(maxChange) +
"\n The month with the greatest loss was: " + str(minChange))
#Compile all metrics into one text file report
output = r'C:\Users\flier\DABootCampLierheimer\Python-challenge\pybankoutput.txt'
str(contents)
with open(output, 'w') as text:
    print(text)
    text.write(contents)
    print(contents)
    text.close()

#Alright I think I wrote the file contents but it's saying write argument must be string but it is not a string, i think because of the max change objects. help! 

