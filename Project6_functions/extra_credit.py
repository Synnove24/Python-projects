#defined a new function called unswap
def unswap(lst:list)->None:
    """Unswaps the pairs of numbers"""
    for i in range(0, len(lst) - 1, 2):
        p = lst[i]
        q = lst[i + 1]
        lst[i] = q
        lst[i + 1] = p
        
#tests function        
my_list = [2,1,4,3,6,5,7]
unswap(my_list)
print(my_list)

#defines a new function called subtract_from_evens
def subtract_from_evens(lst:list)->None:
    """subtracts 2 from all the even numbers"""
    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            lst[i] = lst[i] - 2
       
#tests function 
my_other_list = [1,4,3,6,5,8,7]
subtract_from_evens(my_other_list)
print(my_other_list)
    
#defines a new function called right_circular_shift    
def right_circular_shift(lst:list)->None:
    """shifts every integer to the right"""
    l = lst[-1]
    for i in range(len(lst) - 1,0,-1):
        lst[i] = lst[i - 1]
    lst[0] = l

#tests function                   
my_third_list = [2,3,4,5,1]
right_circular_shift(my_third_list)
print(my_third_list)

#defines a function that is called decrypt
def decrypt(lst:list)->list:
    """decrypts the encrypted phrase"""
    decrypted_list = lst[:]
    unswap(decrypted_list)
    right_circular_shift(decrypted_list)
    subtract_from_evens(decrypted_list)
    unswap(decrypted_list)
    return decrypted_list

#tests function
encrypted_list = [18,6,44,15,10,23]
decrypted_list = decrypt(encrypted_list)
print(encrypted_list)
print(decrypted_list)
