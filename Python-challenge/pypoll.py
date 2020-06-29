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

#Count votes received by each candidate, save as variable
#Count votes received by Khan, save as variable
khanRows = poll[(poll.candidate == "Khan")]     
khanVotes = khanRows.voterID.count()
#print(khanVotes)

#Count votes received by Correy, save as variable
correyRows = poll[(poll.candidate == "Correy")]
correyVotes = correyRows.voterID.count()
#print(correyVotes)

#Count votes received by Li, save as variable
liRows = poll[(poll.candidate == "Li")]
liVotes = liRows.voterID.count()
#print(liVotes)

#Count votes received by O'Tooley, save as variable 
toolRows = poll[(poll.candidate == "O'Tooley")]
toolVotes = toolRows.voterID.count()
#print(toolVotes)
#Calculate percentage of votes each candidate received, save as variable
khanPercentage = (khanVotes/votesTotal)*100
#print(khanPercentage)
correyPercentage = (correyVotes/votesTotal)*100
#print(correyPercentage)
liPercentage = (liVotes/votesTotal)*100
#print(liPercentage)
toolPercentage = (toolVotes/votesTotal)*100
print(toolPercentage)