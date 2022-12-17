#0. Initiliaize Poll Data


#add dependencies
import csv
import os

#create variable to hold csv file
file_to_load = os.path.join("Election_Analysis", "resources", "election_results.csv")

#create file to write selected data to
file_to_save = os.path.join("Election_Analysis","analysis", "election_analysis.txt")

with open(file_to_load) as election_data:
    
    # read and analyze data
    file_reader = csv.reader(election_data)

    headers = next(file_reader)
    print(headers)


#TODO 1. Find total number of votes cast

#TODO 2. Make list of candidates whoe received votes

#TODO 3. Total votes each candidate receieved

#TODO 4. % votes each candidate won

#TODO 5. winner of election based on percentage of votes (popular vote)

