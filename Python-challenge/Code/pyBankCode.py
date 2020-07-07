#Import dependencies 
import os
import csv
#Empty lists 
months = []
moneyGross = []
profitMonth = []
#Set path to CSV 
csvpath = os.path.join(r"C:\Users\flier\DABootCampLierheimer\Python-challenge\Resources\budget_data.csv")
#Open CSV
with open(csvpath) as csvfile: 
    csvreader = csv.reader(csvfile, delimiter = ",")
    header = next(csvfile)
    for row in csvreader:
        month = row[0]
        months.append(month)
        #Count number of months in report, add to txt later
        monthcount = len(months)
        #Add up gross $$$$
        money = row[1]
        moneyGross.append(money)
    #Change moneyGross to integers and calculate sum
    moneyGross = [int(i) for i in moneyGross]
    #Final variable to print in CSV 
    moneyGrossSum = sum(moneyGross)
    #Calculate average change over total budget period
    AverageMoney = moneyGrossSum/len(moneyGross)
    AverageMoney = round(AverageMoney, 2)
    #Find max change in profit
    ##Calculate changes in profit first
    for i in range(0, len(moneyGross)-1):
        profitMonth.append(moneyGross[i + 1] - moneyGross[i])
    #Find max profit change
    profitMax = max(profitMonth)
    #Find index of max profit change to find month
    maxIndex = profitMonth.index(profitMax)
    #Use index of max profit change to find month (adding one to compensate for offset indices in for loop line 31)
    maxMonth = months[maxIndex + 1]
    #Find min profit change
    profitMin = min(profitMonth)
    #Find index of max profit change to find month 
    minIndex = profitMonth.index(profitMin)
    #Use index of min profit change to find month (adding one to compensate for offset indices in for loop line 31)
    minMonth = months[minIndex + 1]
    #Begin to write text file 
    contents = [f"Financial Report: \n The total number of months recorded was: {monthcount}."
    f"\n The gross total of all the transactions was:$ {moneyGrossSum}"
    f"\n The average change over the whole period of 86 months was: $ {AverageMoney} ."
    f"\n The month with the greatest gain was: \n {maxMonth} at ${profitMax} ."
    f"\n The month with the greatest loss was: \n {minMonth} at ${profitMin}"]

    #Define output file path
    output = r'C:\Users\flier\DABootCampLierheimer\Python-challenge\Analysis\pyBankAnalysis.txt'
    #Write file-open in read and write mode
    write_output = open(output, "r+")
    write_output.writelines(contents)
    write_output.close()

        
        

