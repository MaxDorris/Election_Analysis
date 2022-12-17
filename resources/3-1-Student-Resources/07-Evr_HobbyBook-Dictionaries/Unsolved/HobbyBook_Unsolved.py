# @TODO: Your code here

dictionary = {
    "pet": "Fritz",    
    "pet_age": 3, 
    "hobbies": [
        'barking',
        'playing',
        'running',
        'eating',
        'sleeping'
        ],
    "wake_times": [
        '8:30',
        '9:00',
        '9:30',
        '10:00' 
    ]}

voting_data = []

voting_data.append({"county":"Arapahoe",
                    "registered_voters": 422829})
voting_data.append({"county":"Denver",
                    "registered_voters": 463353})
voting_data.append({"county":"Jefferson", 
                    "registered_voters": 432438})

voting_data.insert(1,{"County":"El Paso",
                    "registered voters":461149})

# voting_data.remove({"county":"Arapahoe",
#                     "registered_voters": 422829})  


#UPDATE LIST: for every index in voting_data, if county value does not equal Arapahoe, add it to the new voting_data list
voting_data[:] = [d for d in voting_data if d.get('county') != "Arapahoe"]  

voting_data[:] = [d for d in voting_data if d.get('county') != "Denver"]  

voting_data.append({"county":"Denver",
                    "registered voters": 463353})
voting_data.append({"county":"Arapahoe",
                    "registered_voters": 422829})

# How many votes did you get?
# my_votes = int(input("How many votes did you get in the election? "))
# #  Total votes in the election
# total_votes = int(input("What is the total votes in the election? "))
# # Calculate the percentage of votes you received.
# percentage_votes = (my_votes / total_votes) * 100
# print(f"I received {percentage_votes}% of the total votes.")


counties_tuple = ("Arapahoe","Denver","Jefferson")

for i in range(len(counties_tuple)) :
    print(counties_tuple[i])

for county in counties_tuple :
    print(county)