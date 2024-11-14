#!!!assumes today is 10/21/2022!!!
#names the function
def current_age():
    """calculates the user's age on 3/18/2022"""
    birthday = input("What is your birthday in the format mm/dd/yyyy?")
    birth = birthday.split("/")
    month = int(birth[0])  #changes string dates to integers
    day = int(birth[1])
    year = int(birth[2])
    if (month == 10)and(day==21):         #if statement to see if the birthday is 3/18
        age = 2022 - year + 1
        print("Happy birthday!")
    elif month < 10:        #calculates age
        age = 2022 - year
    elif month > 10:
        age = 2022 - year - 1
    else:
        if day < 21:
            age = 2022 - year
        else:
            age = 2022 - year - 1       
    return age             #returns age

print(current_age())       #prints the function output


