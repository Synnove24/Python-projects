#user inputs code and how much the code has been shifted
start = input("Enter your phrase in uppercase")
shift = int(input("How many steps was your phrase shifted?"))
#upper and lowercase alphabet            
ll = "abcdefghijklmnopqrstuvwxyz"
ul = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#For loop to change letter to corresponding number, then subtracts shift,
#then change back to letter
answer = ""
for w in range(len(start)):
    let = start[w]
    num = ul.index(let)
    newnum = (num - shift) %26
    uplet = ll[newnum]
    answer = answer + uplet
    
#print answer
print(answer)            
            
