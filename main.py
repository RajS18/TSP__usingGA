import random
import math

# Define parameters
POPULATION_SIZE = 100
MUTATION_RATE = 0.01
NUM_GENERATIONS = 100
CITIES = [
    (60, 200), (80, 200), (80, 180), (140, 180), (20, 160),
    (100, 160), (200, 160), (140, 140), (40, 120), (100, 120),
    (180, 100), (60, 80), (120, 80), (180, 60), (20, 40),
    (100, 40), (200, 40), (20, 20), (60, 20), (160, 20)
]

# Define helper functions
def distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def fitness(individual):
    return sum(distance(individual[i], individual[i + 1]) for i in range(len(individual) - 1)) + distance(individual[-1], individual[0])

def random_individual():
    return random.sample(CITIES, len(CITIES))

def mutate(individual):
    if random.random() < MUTATION_RATE:
        idx1, idx2 = random.sample(range(len(individual)), 2)
        individual[idx1], individual[idx2] = individual[idx2], individual[idx1]
    return individual

# Create initial population
population = [random_individual() for _ in range(POPULATION_SIZE)]

# Evolve population
for generation in range(NUM_GENERATIONS):
    # Evaluate fitness of each individual in the population
    fitnesses = [fitness(individual) for individual in population]
    
    # Print current best individual
    best_individual = min(population, key=fitness)
    print(f"Generation {generation}: {best_individual} (fitness = {fitness(best_individual)})")
    
    # Select parents for next generation
    parents = random.choices(population, weights=[1 / f for f in fitnesses], k=2)
    
    # Create offspring by crossover and mutation
    offspring = []
    for i in range(POPULATION_SIZE):
        parent1, parent2 = random.choices(parents, k=2)
        child = [None] * len(CITIES)
        start, end = sorted(random.sample(range(len(CITIES)), 2))
        child[start:end+1] = parent1[start:end+1]
        for city in parent2:
            if city not in child:
                idx = child.index(None)
                child[idx] = city
        offspring.append(mutate(child))
    
    # Replace old population with new offspring
    population = offspring
