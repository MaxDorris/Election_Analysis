#0. Initiliaize Poll Data


#add dependencies
import csv
import os

#create variable to hold csv file
file_to_load = os.path.join("resources", "election_results.csv")

#create file to write selected data to
file_to_save = os.path.join("analysis", "election_analysis.txt")


#1. Find total number of votes cast

# create empty list to hold county names
counties = []

# votes by county (dictionary)
county_votes = {}

#initialize vote counter
total_votes = 0

#empty list for to hold candidate names
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
        
        #2. Make list of candidates whoe received votes

        # if first unique candidate mention in election_data
        if row[2] not in candidate_names:

            # add candidate name to list
            candidate_names.append(row[2])

            #3. Total votes each candidate receieved

            # start tracking votes for each candidate as an assigned dictionary value
            candidate_votes[row[2]] = 0
        
        if row[1] not in counties:
            # add candidate name to list
            counties.append(row[1])

            county_votes[row[1]] = 0

        # add vote for county
        county_votes[row[1]] += 1

        # add vote for the candidate
        candidate_votes[row[2]] += 1


with open(file_to_save,"w") as txt_file:

    #header
    election_results = (
        f"\nElection Results\n"
        f"---------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"---------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    #create variable to hold name of winning county
    winning_county = ""

    #create variable to hold winning number of county votes
    winning_county_votes = 0

    #create variable to hold winning percentage of total county votes
    winning_county_percentage = 0

    county_results = ('County Votes:\n')
    for county in county_votes:

        #pulls vote amount from each candidate
        votes = county_votes[county]

        #creates percentage of all votes submitted for each county
        percentage = county_votes[county]/total_votes

        #creates a one-directional update barrier, only the county with the highest percentage and vote count becomes the "winner" - also just updates from zero for first iteration of for loop
        if votes > winning_county_votes:

            # updates winning votes to highest values so far
            winning_county_votes = votes

            # "         county                               "
            winning_county = county

            # "         percentage                           "


        county_results = county_results + (f'{county}: {percentage:.1%} ({votes:,})\n')
    county_results = county_results + ('---------------------------\n'
    f'Largest County Turnout: {winning_county}\n'
    '---------------------------')
    txt_file.write(county_results)
    print(county_results)


    #4. % votes each candidate won

    #create variable to hold name of winning candidate
    winner = ""

    #create variable to hold winning number of votes
    winning_votes = 0

    #create variable to hold the percentage of the total the candidate collected
    winning_percentage = 0

    #extract individual votes form candidate_votes dictionary
    candidate_results = "Candidate Votes:"
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

        candidate_results = candidate_results + (f'\n{candidate}: {percentage:.1%} ({votes:,})')
    txt_file.write(candidate_results)
    print(candidate_results)



    #5. winner of election based on percentage of votes (popular vote)

    winning_candidate_summary = ('---------------------------\n'
        f'Winner: {winner}\n'
        f'Winning Vote Count: {winning_votes:,}\n'
        f'Winning Percentage: {winning_percentage:.1%}\n'
            '---------------------------\n')
    txt_file.write(winning_candidate_summary)
    print(winning_candidate_summary)


