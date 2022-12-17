
# Election-Analysis

## Project Overview (Prompt)
A Colorado Board of  Elections employee has given you the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Create a list of all candidates who receieved votes.
3. Calculate the number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

## Resources
- Data Source: election_results.csv
- Software: Python 3.6.1, Visual Studio Code 1.38.1

## Summary
The analysis for the election show that:
- There were 369,711 total votes cast in this election.
- The candidates were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymond Anthony Doane
- The candidate results were:
    - Charles Casper Stockham received 23.0% of the vote with 85,213 votes.
    - Diana DeGetter received 73.8% of the vote with 272,892 votes.
    - Raymon Anthony Doane received 3.1% of the vote with 11,606 votes.
- The winner of the election was Diana DeGette, who received 73.8% of the vote and 272,892 votes.

## Overview of Election Audit

### Purpose
The purpose of this analysis was to take catagorized election data in a .csv file and transform it into a palatable summary comprised of total votes cast, counties where votes were cast, candidates for which votes were cast, number of (and percentage of total) votes cast in each represented county, number (and percentage of total) votes cast for each candidate, and the winner of the election based on percentage of votes cast in all counties.



### Finding Total Votes & Votes by County and Candidate
After importing the correct modules(**csv** and **os**), I defined a variable **total_votes** that would increase by one with each iteration of a *for* loop that scrolled through each row of data in the .csv file. To access this data, I had to first open the file from its location using the **os** module, then open and read the file with the **csv** module. After I removed the column headers (non-relevant data), I began the for loop. 

I created a list, **counties**, to store county names and a dictionary, **county_votes**, to store name-votes pairs (key, value) for each county to find the counties represented in the vote data, as well as how many votes each one accrued. After finding a unique county name with a membership if-statement, both **counties** and **county_votes** was updated with the name of the county. Then **county_votes** was initiliazed to hold 0 votes for the unique county. This integer value was updated for each county each time the second value in each row was equal to the county name. The same process was carries out for **candidate_names** and **candidate_votes**. This entire process is outlined in more detail below:
```
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

```
### Finding Largest Turnout, County Statistics, and Winning Candidate Statistics
I began this next section of code by creating a text file to store my findings. I then created a variable to store the name of the winning county, a variable to store the number of votes that were cast within this county, variable to store the calculation of the percentage of total votes by county, and one last variable to store these results as text. Within a for-loop iterating through each county in the **county_votes** dictionary, I calculated the percentage of the total votes and created an if-statement to find the winning county. This if-statement sifts through the **county_votes** values and only stores the county with the greatest number of votes in the variables listed above. These variable were then organized into a single variable and written to the text document.

The exact same process was repeated to find the winning candidate adn print out those parallel stats. The entire process can be seen below in more detail:
```
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

    #creates header for county section of output
    county_results = ('County Votes:\n')

    #loop through dictionary using county key
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

        #creates county data variable for .txt and print
        county_results = county_results + (f'{county}: {percentage:.1%} ({votes:,})\n')

    #adds section header info
    county_results = county_results + ('---------------------------\n'
    f'Largest County Turnout: {winning_county}\n'
    '---------------------------')

    #writes to text file
    txt_file.write(county_results)

    #prints to terminal
    print(county_results)


    #4. % votes each candidate won

    #create variable to hold name of winning candidate
    winner = ""

    #create variable to hold winning number of votes
    winning_votes = 0

    #create variable to hold the percentage of the total the candidate collected
    winning_percentage = 0

    #extract individual votes form candidate_votes dictionary
    candidate_results = ('\nCandidate Votes:')

    # loops through candidate_votes dictionary using candidate key
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

    winning_candidate_summary = ('\n---------------------------\n'
        f'Winner: {winner}\n'
        f'Winning Vote Count: {winning_votes:,}\n'
        f'Winning Percentage: {winning_percentage:.1%}\n'
            '---------------------------\n')
    txt_file.write(winning_candidate_summary)
    print(winning_candidate_summary)
```

## Election Audit Results
The result for the election audit are shown below in a screenshot of election_results.txt (included in analysis folder of this repository):

<p align="center">
  <img width=auto height="500" src=analysis/election_analysis.png>
  </p>

## Election Audit Summary
Using this script to package election results into a single text file would increase the speed of ballot counting by several orders of magnitude in comparison to hand-counting ballots. The script could quickly be adapted to any election data file categorizing votes by candidate and county by introducing a subroutine that finds the correct column ID for both candidate and county. It could then plug this value into any "row[x]" references (where x = column ID of either candidate or county). Additionally, the script could be adapted to suit tallying the popular vote of presidential elections by adding a subroutine that takes into account the state each county is in. This could utilize a pre-existing dictionary of all US counties organized by state, or a dictionary could be generated if the .csv file contains both state and county data for each row.
