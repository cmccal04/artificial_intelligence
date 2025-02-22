import random

# Define knapsack parameters
MAX_WEIGHT = 250
NUM_BOXES = 12
POPULATION_SIZE = 80
TOURNAMENT_SIZE = 5
MUTATION_RATE = 0.05

# Box weights and values
weights = [20, 30, 60, 90, 50, 70, 30, 30, 70, 20, 20, 60]
values = [6, 5, 8, 7, 6, 9, 4, 5, 4, 9, 2, 1]

# initialize the population with random chromosomes
def init_population(size):
    population = []
    for i in range(size):
        chromosome = []
        for j in range(NUM_BOXES):
            chromosome.append(random.randint(0, 1))
        population.append(chromosome)
    return population

# fitness function, finds the total value of a chromosome, returns this value 
# if the total weight is under 250
def fitness(chromosome):
    total_weight = 0
    total_value = 0
    for i in range(NUM_BOXES):
        total_weight += (weights[i] * chromosome[i])
        total_value += (values[i] * chromosome[i])
    if total_weight > MAX_WEIGHT:
        return 0
    else:
        return total_value

# implementation of tournament selection to choose a parent
def tournament_selection(population):
    tournament = random.sample(population, TOURNAMENT_SIZE)
    return max(tournament, key=fitness)

# implementation of the 1 point crossover genetic operator
def crossover(parent1, parent2):
    point = random.randint(0, NUM_BOXES-1)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2

# implementation of the mutate genetic operator
def mutate(chromosome):
    for i in range(NUM_BOXES):
        if random.random() < MUTATION_RATE:
            chromosome[i] = 1 - chromosome[i]  # Flip the bit
    return chromosome

# culls the population by 50%
def cull_population(population, pop_size):
    new_pop = sorted(population, reverse=True, key=fitness)
    new_pop = new_pop[:pop_size // 2]
    return new_pop

# implementation of the genetic algorithm
def genetic_algorithm(population, num_generations, population_size):
    for generation in range(num_generations):

        # cull the populaion by 50%
        new_population = cull_population(population, population_size)

        #replenish the population using crossover and mutation
        while len(new_population) < population_size:
            parent1 = tournament_selection(population)
            parent2 = tournament_selection(population)
            child1, child2 = crossover(parent1, parent2)
            new_population.append(mutate(child1))
            if len(new_population) < population_size:
                new_population.append(mutate(child2))
        
        population = new_population

        # determine the fittest individual
        fittest_individual = max(population, key=fitness)
        best_fitness = fitness(fittest_individual)

        print("Generation ", generation+1, ", Best Fitness = ", best_fitness)
    
    return fittest_individual

def main():
    # ask user for desired number of generations and population size
    num_generations = int(input("How many generations would you like to generate: "))
    population_size = int(input("Enter a population size: "))
    population = init_population(population_size)

    # launch the genetic algorithm, find the optimal solution
    winner = genetic_algorithm(population, num_generations, population_size)
    print("Optimals solution is the chromosome: ", winner)

if __name__ == "__main__":
    main()




