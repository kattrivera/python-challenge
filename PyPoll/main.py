# import os and csv module
import os
import csv

# map csv file path in and txt file path out
election_dataPath = os.path.join("Resources", "election_data.csv")
election_dataOut = os.path.join("Analysis","election_data_summary.txt")

# read csv file
with open(election_dataPath) as election_dataFile:
    election_dataReader = csv.reader(election_dataFile, delimiter=",")
    
# ignore headers   
    header = next(election_dataReader)

# set variables and lists
    totalVotes = 0
    candidateList = []
    Khan = 0
    perKhan = 0
    Correy = 0
    perCorrey = 0
    Li = 0
    perLi = 0
    OTooley = 0
    perOTooley = 0
    
# start looping by rows in reader      
    for row in election_dataReader:

# vote count by counting rows incrementally           
        totalVotes += 1      

# create candidate list to print set() to remove duplicates and retrieve candidate names    
        candidateList.append(row[2])

# set conditions for counting votes per candidate, percentage won        
        if row[2] == "Khan":
            Khan += 1
            perKhan = round(Khan/totalVotes * 100)
        elif row[2] == "Correy":
            Correy += 1
            perCorrey= round(Correy/totalVotes * 100)
        elif row[2] == "Li":
            Li += 1
            perLi = round(Li/totalVotes * 100)
        elif row[2] == "O'Tooley":
            OTooley += 1
            perOTooley = round(OTooley/totalVotes * 100)

# use above condition to give us the overall winner            
            if Khan > Correy: Winner = "Khan"
            elif Correy > Winner: Winner = "Correy"
            elif Li > Winner: Winner = "Li"
            elif OTooley > Winner: Winner = "OTooley"

# print to Git Bash    
print("Election Results")
print("---------------------------------")
print(f"Total Votes: {totalVotes}")
print("------------------------------")
# print(set(candidateList))
print(f"Khan: {perKhan}% ({Khan})")
print(f"Correy: {perCorrey}% ({Correy})")
print(f"Li: {perLi}% ({Li})")
print(f"O'Tooley: {perOTooley}% ({OTooley})")
print("------------------------------")
print(f"Winner: {Winner}")
print("------------------------------")

# print to txt file
with open(election_dataOut, "w") as txtFile:     
    print("Election Results", file=txtFile)
    print("---------------------------------", file=txtFile)
    print(f"Total Votes: {totalVotes}", file=txtFile)
    print("------------------------------", file=txtFile)
    # print(set(candidateList), file=txtFile)
    print(f"Khan: {perKhan}% ({Khan})", file=txtFile)
    print(f"Correy: {perCorrey}% ({Correy})", file=txtFile)
    print(f"Li: {perLi}% ({Li})", file=txtFile)
    print(f"O'Tooley: {perOTooley}% ({OTooley})", file=txtFile)
    print("------------------------------", file=txtFile)
    print(f"Winner: {Winner}", file=txtFile)
    print("------------------------------", file=txtFile)
