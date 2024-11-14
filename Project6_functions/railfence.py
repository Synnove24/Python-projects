#defines function called railfence
def railfence(word:str)->str:
    """Turns word into a railfence cypher"""
    length = len(word)
    #Empty lists for each section of the railfence
    top = []
    middle = []
    bottom = []
    #for loops to find each section of the railfence
    for i in range(0,length,4):
        top.append(word[i])

    for i in range(1,length,2):
        middle.append(word[i])

    for i in range(2,length,4):
        bottom.append(word[i])
    
    #Makes the list into a string
    result_list = top + middle + bottom
    result = "".join(result_list)

    #prints result
    return result

test = "Railfence Cypher"
print(railfence(test))

