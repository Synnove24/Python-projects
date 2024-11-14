#user types in phrase and how much to shift
start = input("Enter your phrase in lowercase")
shift = int(input("How many steps do you want to shift foward?"))
#Upper and lowercase alphabet
ll = "abcdefghijklmnopqrstuvwxyz"
ul = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#For loop to do casear shift
answer = ""
for w in range(len(start)):         
    let = start[w]                  #Changes letter to corresponding number
    num = ll.index(let)
    newnum = (num + shift) % 26     #Adds shift to number
    uplet = ul[newnum]              #changes number back to coreesponding letter
    answer = answer + uplet

#prints answer
print(answer)  
