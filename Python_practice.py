#counties = ["Arapahoe","Denver","Jefferson"]
#if "El Paso" not in counties or "Arapahoe" in counties:
    #print("Only El Paso is in the list of counties.")
#els#
    #print("El Paso is in the list of counties and Arapahoe is not in the list of counties.")

#for county in counties:
    #print(county)

#for num in range(5):
    #print(num)

#for i in range(len(counties)):
    #print(counties[i])

#counties_tuple = ("Arapahoe","Denver","Jefferson")
#for i in range(len(counties_tuple)):
    #print(counties_tuple[i])

#for county in counties_tuple:
    #print(county)

#counties_dict = {"Arapahoe":422829,"Denver":463353,"Jefferson":432438}
#for voters in counties_dict.values():
    #print(voters)
#for county in counties_dict:
    #print(counties_dict[county])
#for key,value in counties_dict.items():
    #print(key,value)

#voting_data = ({"county":"Arapahoe", "registered_voters":422829},
                #{"county":"Denver", "registered_voters":463353},
                #{"county":"Jefferson", "registered_voters":432438})
#for i in voting_data:
    #print(i)
#for i in range(len(voting_data)):
    #print(voting_data[i])
#for county_dict in voting_data:
    #for value in county_dict.values():
        #print(value)

#for county_dict in voting_data:
    #print(county_dict['registered_voters'])

candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

print(message_to_candidate)