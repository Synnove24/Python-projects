#opens file and reads file
data_file = open("fatal-police-shootings-data.csv", 'r')
data_lines = data_file.readlines()

#creates empty dictionary named database
database = {}

#for loop iterating through each row
for row in range(1,len(data_lines)):
    line = data_lines[row]
    entries = line.split(',')
    #creates new empty dictionary named db_entry
    db_entry = {}
    #creates keys and corresponding values in the dictionary
    db_entry["name"] = entries[1]
    db_entry["date"] = entries[2]
    db_entry["armed"] = entries[4]
    db_entry["age"] = entries[5]
    db_entry["gender"] = entries[6]
    db_entry["race"] = entries[7]
    db_entry["state"] = entries[9]
    #db_entry["city"] = entries[8]
    entry_id = int(entries[0])
    #creates a dictionary within a dictionary
    database[entry_id] = db_entry
   

#prints id number 1694    
print(database[1694])

#prints all fatal shootings in Minnesota
for i in database:
    if "MN" in database[i]["state"]:
        print(database[i]["name"])

#creates dictionary of how many shootings correspond to each race
race_counts   = {}   
for i in database:
    race = database[i]["race"]
    if race in race_counts:
        race_counts[race] = race_counts[race] + 1
    else:
        race_counts[race] = 1
print(race_counts)

#calculates the percentage of people in fatal police shootings that were black
percent_B = race_counts["B"]/(race_counts["A"]+race_counts["W"]+race_counts["H"]+race_counts["O"]+race_counts[""]+race_counts["N"])
print(percent_B)

#creates new dictionary that only contains unarmed shootings
unarmed_selection = {}
for i in database:
    if database[i]["armed"] == "unarmed":
        unarmed_selection[i] = database[i]       
print(unarmed_selection)

#creates dictionary of how many unarmed fatal police shootings correspond to each race
unarmed_race_counts   = {}   
for i in unarmed_selection:
    race = unarmed_selection[i]["race"]
    if race in unarmed_race_counts:
        unarmed_race_counts[race] = unarmed_race_counts[race] + 1
    else:
        unarmed_race_counts[race] = 1
print(unarmed_race_counts)

#calculates the percentage of people were black in unarmed fatal police shootings
percent_B_unarmed = unarmed_race_counts["B"]/(unarmed_race_counts["A"]+unarmed_race_counts["W"]+unarmed_race_counts["H"]+unarmed_race_counts["O"]+unarmed_race_counts[""]+unarmed_race_counts["N"])
print(percent_B_unarmed)
