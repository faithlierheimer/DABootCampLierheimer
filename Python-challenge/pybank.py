
import pandas as pd

#Import CSV into Jupyter Notebook
budget = pd.read_csv('budget_data.csv')

#Print first 5 rows of data to see what it looks like
print(budget.head())
#Rename columns for ease of use
budget.columns = ['date', 'pandl']
print(budget.head())
outfile = r'C:\Users\flier\DABootCampLierheimer\Python-challenge\pybankoutput.txt'
#Print total number of months included in the dataset, w/labels
print("Total Months: " + str(budget.date.count()), file = open(outfile, 'a'))

#Print net total amount of profits and losses in entire period
#Column name for Profits/Losses abbreviated to "pandl"
print("Net total over entire period: $" + str(budget.pandl.sum()),
     file = open(outfile, "a"))

#Print average of changes in "Profit/Losses over entire period"
print("Average Change : $" + str(budget.pandl.mean()),
     file = open(outfile, "a"))

#Print greatest increase in profits (date and amount) over entire period
maxDate = budget.max()
print("The greatest increase in profits was: ", 
     file = open(outfile, "a"))
print(maxDate, file = open(outfile, "a"))

#Print greatest decrease in losses (date and amount) over the entire period
minDate = budget.min()
print("The greatest decrease in profits was: ", file = outfile, "r")
print(minDate, file = outfile, "r")

#Export all print statements to a .txt file
