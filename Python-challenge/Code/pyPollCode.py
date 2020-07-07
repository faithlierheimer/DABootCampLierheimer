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
    
    #Calculate percentage of votes each candidate received, save as variable, round each
    khanPercent = round(((khanVoteCount/votecount)*100), 2)
    correyPercent = round(((correyVoteCount/votecount)*100), 2)
    liPercent = round(((liVoteCount/votecount)*100), 2)
    toolPercent = round(((toolVoteCount/votecount)*100), 2)
    
    #Compile all vote counts into a list and select max 
    #Make list of candidates in same order as vote counts list to access winner
    contenders = ['Khan', 'Correy', 'Li', 'OTooley']
    voteTotals = [khanVoteCount, correyVoteCount, liVoteCount, toolVoteCount]
    #Find max number of votes in vote totals list 
    winner = max(voteTotals)
    #Find index of winner in list to cross ref to contenders list
    winnerIndex = voteTotals.index(winner)
    #Find winner name in contenders list 
    winnerName = contenders[winnerIndex]
    #Compile all results into text file

    #Save path to text output file as variable
    pollResults = r"C:\Users\flier\DABootCampLierheimer\Python-challenge\Analysis\pyPollAnalysis.txt"

    #Save/format results in 'text' variable
    text = [f"Election Results:" 
    f"\n Total votes cast: {votecount} " 
    f"\n Khan: {khanPercent} %  ({khanVoteCount}) "
    f"\n Correy: {correyPercent} %  ({correyVoteCount}) "
    f"\n Li: {liPercent} %  ({liVoteCount})"
    f"\n O'Tooley: {toolPercent} %  ({toolVoteCount}) "
    f"\n Winner: {winnerName}"]

    #Write contents of poll results file
    write_output = open(pollResults, "r+")
    write_output.writelines(text)
    write_output.close()