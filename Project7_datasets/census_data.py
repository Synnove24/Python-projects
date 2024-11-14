#creates a function that takes a file name and returns the information as a string
def get_data(filename:str)->str:
    """Returns data as a string"""
    file = open(filename,"r")
    lst = file.readlines()
    return lst

#creates a function that parses data by stripping the \n and splitting the commas
def parse_data(lst:list)->list:
    """Parses the data"""
    for i in range(len(lst)):
        lst[i] = lst[i].strip()
        lst[i] = lst[i].split(",")
    return lst

#creates a function that creates a list of the populations
def get_populations(lst:list)->list:
    """take a list and returns the populations"""
    pop = []
    for i in range(len(lst)):
        pop.append(lst[i][2])
    return pop 

#creates a function that prints the frequencies of each number
def leading_digits(pop:list)->None:
    """Returns frequencies of leading digits"""
    one = 0
    two = 0
    three = 0
    four = 0
    five = 0
    six = 0
    seven = 0
    eight = 0
    nine = 0
    #makes a list of all the first numbers
    first = []
    for i in range(len(pop)):
        first = first + list(pop[i][0:1])
    #decides what number it is and accumulates it    
    for i in range(len(first)):
        if first[i] == "1":
            one = one + 1
        elif first[i] == "2":
            two = two + 1
        elif first[i] == "3":
            three = three + 1
        elif first[i] == "4":
            four = four + 1
        elif first[i] == "5":
            five = five + 1
        elif first[i] == "6":
            six = six +1
        elif first[i] == "7":
            seven = seven + 1
        elif first[i] == "8":
            eight = eight + 1
        elif first[i] == "9":
            nine = nine + 1
    #calculates frequency        
    l = len(first)   
    onef = one/l
    twof = two/l
    threef = three/l
    fourf = four/l
    fivef = five/l
    sixf = six/l
    sevenf = seven/l
    eightf = eight/l
    ninef = nine/l
    #prints frequencies
    print("Frequency of 1: ", onef)
    print("Frequency of 2: ", twof)
    print("Frequency of 3: ", threef)
    print("Frequency of 4: ", fourf)
    print("Frequency of 5: ", fivef)
    print("Frequency of 6: ", sixf)
    print("Frequency of 7: ", sevenf)
    print("Frequency of 8: ", eightf)
    print("Frequency of 9: ", ninef)
     
        
                   
#functions used to find frequencies
file = "data1.csv"        
lst = get_data(file)
lst = parse_data(lst)
test = get_populations(lst)
leading_digits(test)

file = "data2.csv"        
lst = get_data(file)
lst = parse_data(lst)
test = get_populations(lst)
leading_digits(test)

file = "data3.csv"        
lst = get_data(file)
lst = parse_data(lst)
test = get_populations(lst)
leading_digits(test)

#define function plot_data  
def plot_data(lst:list)->None:
    """plots data from parse function"""
    #turns parse list into floats
    for row in range(len(lst)):
        for col in range(len(lst[row])):
            lst[row][col] = float(lst[row][col])
    #create a turtle and window
    import turtle
    wn = turtle.Screen()
    turtle.tracer(0,0)
    s = turtle.Turtle()
    turtle.setworldcoordinates(00,0,110,110)
    s.speed(10)
    #turtle goes to coordinates and creates a circle
    for i in range(len(lst)):
        r = ((lst[i][2])**(1/2))*.0008
        s.up()
        s.goto(170 - lst[i][1],lst[i][0])
        s.right(90)
        s.forward(r)
        s.left(90)
        s.fillcolor("black")
        s.begin_fill()
        s.circle(r)
        s.end_fill()
    turtle.update()    
    
plot_data(lst)





