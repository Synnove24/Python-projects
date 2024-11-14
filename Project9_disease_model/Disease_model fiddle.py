#imports random
import random
def infect(infect_chance:float)->bool:
    "Takes a probabilty and returns True or False"
    r = random.uniform(0,1)
    if r > infect_chance:
        return True
    else:
        return False

def death(death_chance:float)->bool:
    r = random.uniform(0,1)
    if r > death_chance:
        return True
    else:
        return False

def recover(recover_chance:float)->bool:
    "Takes a probabilty and returns True or False"
    r = random.uniform(0,1)
    if r < recover_chance:
        return True
    else:
        return False

def death(death_chance:float)->bool:
    r = random.uniform(0,1)
    if r < death_chance:
        return True
    else:
        return False

def contact_indices(pop_size:int,source:int,contact_range:int)->list:
    """Takes the population size, source location, and contact range and creates a list of everyone at risk."""
    rng = []
    for i in range(0,pop_size):
        rng.append(i)    
    lower = abs(source - contact_range)
    upper = (source + contact_range)
    #depending on where the source is within the range, it creates a list of everyone within the contact range
    if (source-contact_range) > 0:
        del rng[:lower]     
        del rng[(upper-lower+1):]
    else:
        del rng[upper+1:]
    return rng

            
def apply_recoveries(population:list, recover_chance:float)->list:
    """Takes the population and recover chance and applies the ercover chance to the population"""
    for i in range(len(population)):
        if population[i] == "I":
            if recover(recover_chance) == True:
                population[i] = "R"
            else:
                population[i] = "I"
    return population

def apply_deaths(population:list, death_chance:float)->list:
    for i in range(len(population)):
        if population[i] == "I":
            if death(death_chance) == True:
                population[i] = "D"
            else:
                population[i] = "I"
    return population                
                    

def contact(population:list,source:int,contact_range:int,infect_chance:float)->None:
    """Alters the population list to see who gets infected"""
    pop_size = len(population)
    risk = contact_indices(pop_size,source,contact_range)
    for i in risk:
        if population[i] == "S":
            if infect(infect_chance) == True:
                population[i] = "I"
                

def apply_contacts(population:list, contact_range:int, infect_chance:float)->None:
    """Alters the population by applying the contacts function"""
    infected = []
    for i in range(len(population)):
        if population[i] == "I":
            infected.append(i)
    for i in infected:        
        contact(population,i,contact_range,infect_chance)
        
def population_SIR_counts(population:list)->dict:
    """"Creates a dictionary of how many people are infected, susceptable, and recovered"""
    dict = {'infected':0,'susceptible':0,'recovered':0, 'dead':0}
    for i in population:
        if i == "R":
            dict["recovered"] += 1
        elif i == "I":
            dict["infected"] += 1
        elif i == "D":
            dict["dead"] += 1
        else:
            dict["susceptible"] += 1
    return dict        

def simulate_day(population:list,contact_range:int,infect_chance:float,recover_chance:float, death_chance:float)->list:
    """uses function apply_recoveries and apply_contacts"""
    apply_recoveries(population,recover_chance)
    apply_deaths(population,death_chance)
    apply_contacts(population,contact_range,infect_chance)

def initialize_population(pop_size:int) -> list:
    """Takes the population size and creates the population list with first person infected"""
    population = ['S'] * pop_size
    population[0] = 'I'
    return population

def simulate_disease(pop_size:int, contact_range:int, infect_chance:float, recover_chance:float, death_chance:float) -> list:
    """takes the population size, range, recovery chance, and infection chance and returns the counts of each person"""
    population = initialize_population(pop_size)
    counts = population_SIR_counts(population)
    all_counts = [counts]
    #If there is at least one person infected, it goes through another day
    while counts['infected'] > 0:
        simulate_day(population, contact_range, infect_chance, recover_chance, death_chance)
        counts = population_SIR_counts(population)
        all_counts.append(counts)
    return all_counts

def peak_infections(all_counts:list) -> int:
    """takes the counts and determines the maximum amount of infections"""
    max_infections = 0
    for day in all_counts:
        if day['infected'] > max_infections:
            max_infections = day['infected']
    return max_infections
        
def display_results(all_counts:list) -> None:
    """Takes the counts and prints the results"""
    num_days = len(all_counts)
    print("Day".rjust(12) + "Susceptible".rjust(12) + "Infected".rjust(12) + "Recovered".rjust(12) + "Dead".rjust(12))
    #line accumulates for each day
    for day in range(num_days):
        line = str(day).rjust(12)
        line += str(all_counts[day]["susceptible"]).rjust(12)
        line += str(all_counts[day]["infected"]).rjust(12)
        line += str(all_counts[day]["dead"]).rjust(12)
        line += str(all_counts[day]["recovered"]).rjust(12)
        print(line)
    print("\nPeak Infections: {}".format(peak_infections(all_counts)))    

#uses functions
counts = simulate_disease(5000,6,.75,.0036,.1)
display_results(counts)
