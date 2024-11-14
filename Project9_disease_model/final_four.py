#Note: you will not be able to call these functions until you have implemented the other functions for this project.

def initialize_population(pop_size:int) -> list:
    population = ['S'] * pop_size
    population[0] = 'I'
    return population

def simulate_disease(pop_size:int, contact_range:int, infect_chance:float, recover_chance:float) -> list:
    population = initialize_population(pop_size)
    counts = population_SIR_counts(population)
    all_counts = [counts]
    while counts['infected'] > 0:
        simulate_day(population, contact_range, infect_chance, recover_chance)
        counts = population_SIR_counts(population)
        all_counts.append(counts)
    return all_counts

def peak_infections(all_counts:list) -> int:
    max_infections = 0
    for day in all_counts:
        if day['infected'] > max_infections:
            max_infections = day['infected']
    return max_infections
        
def display_results(all_counts:list) -> None:
    num_days = len(all_counts)
    print("Day".rjust(12) + "Susceptible".rjust(12) + "Infected".rjust(12) + "Recovered".rjust(12))
    for day in range(num_days):
        line = str(day).rjust(12)
        line += str(all_counts[day]["susceptible"]).rjust(12)
        line += str(all_counts[day]["infected"]).rjust(12)
        line += str(all_counts[day]["recovered"]).rjust(12)
        print(line)
    print("\nPeak Infections: {}".format(peak_infections(all_counts)))

    


