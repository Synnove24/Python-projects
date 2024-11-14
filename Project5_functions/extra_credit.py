#defines function
def is_legal_birthday():
    """decides if the user inputed the age correctly"""
    #user inputs birthday and the slashes go away
    bbday = input("Input your birthday")
    bday = bbday.split("/")
    #checks length of list
    if len(bday) != 3:
        return 3==2
    #creates variables for month, day, and year
    month = bday[0]
    day = bday[1]
    year = bday[2]
    #checks to make sure there are only numbers
    if (month.isnumeric()==False)or(day.isnumeric()==False)or(year.isnumeric()==False):
        return 3==2
    #checks length of month, day, and year
    elif((len(day)==1)or(len(day)==2))and((len(month)==2)or(len(month)==1))and(len(year)==4):
        month = int(bday[0])
        day = int(bday[1])
        year = int(bday[2])
        #checks to see if its Feb 29 on a leap year
        if(month==2)and(day==29)and((year%4)==0):
            return 3==3
        #checks months with 31 days
        if(month==1)or(month==3)or(month==5)or(month==7)or(month==8)or(month==10)or(month==12):
            if(day<32)and(day>0):
                if(year<2023)and(year>0):
                    return 3==3
                else:
                    return 3==2
            else:
                return 3==2
        #checks months with 30 days
        elif(month==4)or(month==6)or(month==9)or(month==11):
            if(day<31)and(day>0):
                if(year<2023)and(year>0):
                    return 3==3
                else:
                    return 3==2
            else:
                return 3==2
        #checks February    
        elif(month==2):
            if(day<29)and(day>0):
                if(year<2023)and(year>0):
                    return 3==3
                else:
                    return 3==2
            else:
                return 3==2       
        else:
            return 3==2
    else:
        return 3==2
    
#starts function
print(is_legal_birthday())

























