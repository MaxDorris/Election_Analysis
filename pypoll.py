#0. Initiliaize Poll Data


#add dependencies
import csv
import os

#create variable to hold csv file
file_to_load = os.path.join("Election_Analysis", "resources", "election_results.csv")

#create file to write selected data to
file_to_save = os.path.join("Election_Analysis","analysis", "election_analysis.txt")


#TODO 1. Find total number of votes cast

#initialize vtoe counter
total_votes = 0

#candidate options
candidate_names = []

#votes by candidate (dictionary)
candidate_votes = {}

#

# open file and give it ID "election_data"
with open(file_to_load) as election_data:
    
    # read and analyze data
    file_reader = csv.reader(election_data)

# remove non-relevant headers (clean)
    headers = next(file_reader)

    # add 1 vote for every row to find total
    for row in file_reader:
        total_votes += 1
        
        #TODO   2. Make list of candidates whoe received votes

        # if first unique candidate mention in election_data
        if row[2] not in candidate_names:
            # add candidate name to list
            candidate_names.append(row[2])


            #TODO 3. Total votes each candidate receieved

            # start tracking votes for each candidate as an assigned dictionary value
            candidate_votes[row[2]] = 0

        # add vote for the candidate
        candidate_votes[row[2]] += 1


with open(file_to_save,"w") as txt_file:

    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)


    #TODO 4. % votes each candidate won

    #create variable to hold name of winning candidate
    winner = ""

    #create variable to hold winning number of votes
    winning_votes = 0

    #create variable to hold the percentage of the total the candidate collected
    winning_percentage = 0

    #extract individual votes form candidate_votes dictionary
    for candidate in candidate_votes:

        #pulls vote amount from each candidate
        votes = candidate_votes[candidate]

        #calulates percentage of total votes for each candidate
        percentage = candidate_votes[candidate]/total_votes

        #creates a one-directional update barrier, only the candidate with the highest percentage and vote count becomes the "winner" - also just updates from zero for first iteration of for loop
        if votes > winning_votes and percentage > winning_percentage:

            # updates winning votes to highest values so far
            winning_votes = votes

            # "         percentage                          "
            winning_percentage = percentage

            # "         candidate                           "
            winner = candidate

        candidate_results = (f'\n{candidate}: {percentage:.1f}% ({votes:,})\n')
        txt_file.write(candidate_results)
        print(candidate_results)



    #TODO 5. winner of election based on percentage of votes (popular vote)

    winning_candidate_summary = ('---------------------------\n\n'
        f'Winner: {winner}\n\n'
        f'Winning Vote Count: {winning_votes:,}\n\n'
        f'Winning Percentage: {winning_percentage:.1%}\n\n'
            '---------------------------\n')
    txt_file.write(winning_candidate_summary)
    print(winning_candidate_summary)


