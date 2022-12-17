
# Election_Analysis

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

## Election Audit Results

### How many votes were cast in this congressional election?
After importing the correct modules(**csv** and **os**), I defined a variable **total_votes** that would increase by one with each iteration of a *for* loop that scrolled through each row of data in the .csv file. To access this data, I had to first open the file from its location using the **os** module, then open and read the file with the **csv** module. After I removed the column headers (non-relevant data), I began the for loop. This is shown below:
```
<span style="color:blue">
#0. Initiliaize Poll Data

#add dependencies
*import csv*
*import os*

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
</span>

```

### Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.

### Which county had the largest number of votes?

### Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.

### Which candidate won the election, what was their vote count, and what was their percentage of the total votes?

## Election Audit Summary
