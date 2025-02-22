Artificial Intelligence Assignment 3: Genetic Algorithm

Name: Cullen McCaleb
Date: 10/26

1. To define the problem as a genetic algorithm, a few things must be defined:
    - Structure of the chromosome: A list of 1s and 0s, where 1 represents the
        inclusion of the box a that index + 1, and 0 does not. For example, 
        [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0] would mean objects 1, 5, and 11
        are included in the knapsack.
    - Selection of an initial population: This is done by asking the user for a
        population size, and randomly creating hat number of chromosomes.
    - Fitness function: Total value of the chromosome, unless the total weight
        exceeds 250. In this case, the fitness is 0.
    - Selection process: Tournament selection, where 5 chromsomes are randomly 
        selected, and the chromosome with the best fitness is selected.
    - Genetic Operators: Both crossover and mutation will be used.

2. The genome for this problem is specified above, as the structure of the 
    chromosome.

3. The fringe operations, or genetic operators, are defined above.

4. The population is culled each generation, using the cull_population function

HOW TO RUN: Use the command 'python3 knapsack_problem.py' to run the main
            function of the program. It will ask for a population size and 
            number of generations, both of which should be integers.