#!!!assumes today is 03/18/2022!!!
#names the function
def current_age():
    birthday = input("What is your birthday in the format mm/dd/yyyy?")
    birth = birthday.split("/")
    month = int(birth[0])  #changes string dates to integers
    day = int(birth[1])
    year = int(birth[2])
    if month == 3:         #if statement to see if the birthday is 3/18
        if day == 18:
            age = 2022 - year + 1
            print("Happy birthday!")
    elif month < 3:        #calculates age
        age = 2022 - year
    elif month > 3:
        age = 2022 - year - 1
    else:
        if day < 18:
            age = 2022 - year
        else:
            age = 2022 - year - 1       
    return age             #returns age

print(current_age())       #prints the function output
