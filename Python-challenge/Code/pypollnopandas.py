#Import dependencies 
import os
import csv
#Empty lists 
votes = []
candidates = []
candidates_unique = []
khanVotes = []
correyVotes = []
liVotes = []
toolVotes = []
#Import/read CSV
csvpath = os.path.join(r"C:\Users\flier\DABootCampLierheimer\Python-challenge\Resources\election_data.csv")
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    header = next(csvfile)
    #For loop to count votes, make list of candidates, etc.
    for row in csvreader:
        #Count votes
        vote = row[0]
        votes.append(vote)
        #Make list of candidates
        candidate = row[2]
        candidates.append(candidate)
        #Count votes per candidates 
        if candidate == 'Khan':
            khanVotes.append(vote)
        elif candidate == 'Correy':
            correyVotes.append(vote)
        elif candidate == 'Li':
            liVotes.append(vote)
        else:
            toolVotes.append(vote)
    

    #Vote Count variable for printout
    votecount = len(votes)

    #Make list of unique candidates
    for i in candidates:
        if i not in candidates_unique:
            candidates_unique.append(i)
    #candidates_unique is list of unique candidates for printout

    #Tally votes for each candidate, store in variable
    khanVoteCount = len(khanVotes)
    correyVoteCount = len(correyVotes)
    liVoteCount = len(liVotes)
    toolVoteCount = len(toolVotes)
    
    #Calculate percentage of votes each candidate received, save as variable