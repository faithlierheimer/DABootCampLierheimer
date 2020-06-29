import pandas as pd 

#Import and read CSV, inspect first 5 rows. 
poll = pd.read_csv(r'C:\Users\flier\DABootCampLierheimer\Python-challenge\election_data.csv')

#print(poll.head()) [Commenting out print rows after I use them for sake of code cleanliness]
#Change Column names for ease of use 
poll.columns = ['voterID', 'county', 'candidate']

#Count total number of votes cast, save as variable
votesTotal = poll.voterID.count()

#List of unique candidates that received votes, save as variable
candidates = poll.candidate.unique()
candidateList = candidates.tolist()
#print(candidateList)

#Calculate percentage of votes each candidate received, save as variable