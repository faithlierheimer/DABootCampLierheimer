import pandas as pd
#Import/read CSV for analysis
budget = pd.read_csv(r"C:\Users\flier\DABootCampLierheimer\Python-challenge\budget_data.csv")

#rename columns for ease of use
budget.columns = ['date', 'pandl']

#count number of months, save to variable
monthCount = budget.date.count()

#Sum total transactions, save to variable
totalTransactions = budget.pandl.sum()

#average total change over budget period, save to variable
averageChange = budget.pandl.mean()

#max increase over whole period, save to variable
maxChangeAmt = budget.pandl.max()

#use maxChangeAmt to find the month with the max change, save to variable
maxChangeMonth = budget[(budget.pandl == maxChangeAmt)]

#max decrease over whole period, save to variable
minChangeAmt = budget.pandl.min()

#useminChangeAmt to find month with min change, save to variable
minChangeMonth = budget[(budget.pandl == minChangeAmt)]

#Change minimum and maximum changes over period from DataFrames to strings
minChMonthStr = minChangeMonth.to_string()

maxChMonthStr = maxChangeMonth.to_string()

#Compile results of analysis into a list of strings called "contents" to later write to text file
contents = [f"Financial Report: \n The total number of months recorded was: {monthCount}."
f"\n The gross total of all the transactions was:$ {totalTransactions}"
f"\n The average change over the whole period of 86 months was: $ {averageChange} ."
f"\n The month with the greatest gain was: \n {maxChMonthStr} ."
f"\n The month with the greatest loss was: \n {minChMonthStr}"]

#Compile all metrics into one text file report
    #First, save path to file in "output" variable
output = r'C:\Users\flier\DABootCampLierheimer\Python-challenge\pybankoutput.txt'

#Writing file-open in read and write mode, write contents as a list of strings, then close it. 
write_output = open(output, "r+")
write_output.writelines(contents)
write_output.close()

#Analysis complete! Output is in file called "pybankoutput.txt"
