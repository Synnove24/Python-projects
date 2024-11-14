#User inputs word and shift value
start = input("Enter your phrase in lowercase")
shift = input("What word do you want to use as a shifter in lowercase?")
#uppercase and lowercase alphabet
ll = "abcdefghijklmnopqrstuvwxyz"
ul = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


answer = ""  #Starts answer with nothing
for w in range(len(start)):   
    let = start[w]                          #changes letter into corresponding number
    num = ll.index(let)    
    shiftlet = shift[w % (len(shift))]      #changes shift word into corresponding numbers
    shiftnum = ll.index(shiftlet)
    print(shiftlet)
    newnum = (num + shiftnum) % 26          #finds new number
    uplet = ul[newnum]                      #changes number back to letter
    answer = answer + uplet                 #concatenates strings

#print answer
print(answer)  
