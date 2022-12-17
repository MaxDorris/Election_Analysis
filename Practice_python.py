counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county in counties_dict:
    print(f'{county} county has {counties_dict[county]:,} registered voters.')

voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]

for dictionary in voting_data:
    print (f'{dictionary["county"]} county has {dictionary["registered_voters"]:,} registered voters.')
