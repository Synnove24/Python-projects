#defines a new function called swap
def swap(lst:list)->None:
    """Swaps the pairs of numbers"""
    for i in range(0, len(lst) - 1, 2):
        p = lst[i]
        q = lst[i + 1]
        lst[i] = q
        lst[i + 1] = p
#tests function        
my_list = [1,2,3,4,5,6,7]
swap(my_list)
print(my_list)

#defines a new function called add_to_evens
def add_to_evens(lst:list)->None:
    """ Adds 2 to evens"""
    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            lst[i] = lst[i] + 2
       
#tests function 
my_other_list = [1,2,3,4,5,6,7]
add_to_evens(my_other_list)
print(my_other_list)

#defines a new function called left_circular_shift
def left_circular_shift(lst:list)->None:
    """shifts every integer to the left"""
    l = lst[0]
    for i in range(len(lst) - 1):
        lst[i] = lst[i + 1]
    lst[-1] = l

#tests function                   
my_third_list = [1,2,3,4,5]
left_circular_shift(my_third_list)
print(my_third_list)

#defines a new function called encrypt
def encrypt(lst:list)->list:
    clone_list = lst[:]
    swap(clone_list)
    add_to_evens(clone_list)
    left_circular_shift(clone_list)
    swap(clone_list)
    return clone_list

#tests function 
fourth_list = [4,8,15,16,23,42]
encrypted_list = encrypt(fourth_list)
print(fourth_list)
print(encrypted_list)
