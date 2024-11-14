d = float(input("What is the depth of the lawn in feet?"))   #user inputs the depth
w= float(input("What is the width of the lawn in feet?"))    #user inputs the width
a = d * w                                                    #the depth times the width gives the area
t = (a/2)/3600                                               #calculates the time
th = (a/2)/3600                                              #time in hours
th = int(th)                                                 #makes time in hours an integer
tm = (a/2)/60 % 60                                           #remaining time in minutes
tm = int(tm)                                                 #time in minutes as an integer
ts = (a/2)% 60                                               #remaining time in seconds
ts = int(ts)                                                 #time in seconds as an integer                                            
  
print("It will take you", th, "hours", tm, "minutes and", ts, "seconds to mow the lawn") #prints the time


m = t * 20                                                   #Calculates the money earnt
m = round(m, 2)                                              #rounds the money to two decimals
print("You will make", m, "dollars")                         #prints money earnt
