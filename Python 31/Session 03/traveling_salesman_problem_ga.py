import random
import matplotlib.pyplot as plt
import numpy as np

# ---------- Problem Setup ----------
NUM_CITIES = 20
POP_SIZE = 100
GENERATIONS = 500
TOURNAMENT_SIZE = 5
MUTATION_RATE = 0.2

# Generate random cities (2D coordinates)
cities = np.random.rand(NUM_CITIES, 2)

# ---------- Distance Matrix ----------
dist_matrix = np.zeros((NUM_CITIES, NUM_CITIES))
for i in range(NUM_CITIES):
    for j in range(NUM_CITIES):
        dist_matrix[i][j] = np.linalg.norm(cities[i] - cities[j])

# ---------- Fitness Function ----------
def total_distance(tour):
    """Calculate total length of the tour (cycle)."""
    dist = 0
    for i in range(len(tour)):
        dist += dist_matrix[tour[i]][tour[(i+1) % len(tour)]]
    return dist

def fitness_function(tour):
    """Fitness is inverse of total distance (minimize distance)."""
    dist = total_distance(tour)
    return 1 / dist if dist > 0 else float('inf')

# ---------- Population Initialization ----------
def create_population(pop_size):
    population = []
    base = list(range(NUM_CITIES))
    for _ in range(pop_size):
        individual = base[:]
        random.shuffle(individual)
        population.append(individual)
    return population

# ---------- Selection (Tournament) ----------
def tournament_selection(population, fitnesses):
    selected = []
    for _ in range(2):
        tournament = random.sample(list(zip(population, fitnesses)), TOURNAMENT_SIZE)
        winner = max(tournament, key=lambda x: x[1])[0]
        selected.append(winner)
    return selected

# ---------- Order Crossover (OX) ----------
def order_crossover(parent1, parent2):
    size = len(parent1)
    child1 = [-1]*size
    child2 = [-1]*size

    # Random crossover points
    start, end = sorted(random.sample(range(size), 2))

    # Copy slice from first parent
    child1[start:end+1] = parent1[start:end+1]
    child2[start:end+1] = parent2[start:end+1]

    # Fill remaining positions from other parent in order
    def fill_child(child, parent_other):
        current_pos = (end + 1) % size
        for city in parent_other:
            if city not in child:
                child[current_pos] = city
                current_pos = (current_pos + 1) % size
        return child

    child1 = fill_child(child1, parent2)
    child2 = fill_child(child2, parent1)

    return child1, child2

# ---------- Mutation (Swap Mutation) ----------
def mutate(tour, mutation_rate):
    if random.random() < mutation_rate:
        i, j = random.sample(range(len(tour)), 2)
        tour[i], tour[j] = tour[j], tour[i]
    return tour

# ---------- Genetic Algorithm Main ----------
def genetic_algorithm():
    population = create_population(POP_SIZE)
    best_fitness_progress = []

    for gen in range(GENERATIONS):
        fitnesses = [fitness_function(ind) for ind in population]

        new_population = []

        # Elitism: keep the best individual
        best_idx = fitnesses.index(max(fitnesses))
        best_individual = population[best_idx]
        best_fitness_progress.append(fitnesses[best_idx])

        new_population.append(best_individual)

        # Generate rest of population
        while len(new_population) < POP_SIZE:
            parents = tournament_selection(population, fitnesses)
            offspring1, offspring2 = order_crossover(parents[0], parents[1])
            offspring1 = mutate(offspring1, MUTATION_RATE)
            offspring2 = mutate(offspring2, MUTATION_RATE)
            new_population.extend([offspring1, offspring2])

        population = new_population[:POP_SIZE]

        # Optional: print progress every 50 generations
        if (gen + 1) % 50 == 0:
            print(f"Generation {gen+1}, Best fitness: {best_fitness_progress[-1]:.5f}, Distance: {1/best_fitness_progress[-1]:.4f}")

    # Final best solution
    best_idx = fitnesses.index(max(fitnesses))
    return population[best_idx], 1 / fitnesses[best_idx], best_fitness_progress

# ---------- Visualization ----------
def plot_tour(tour):
    tour_cities = cities[tour + [tour[0]]]  # Close the loop
    plt.figure(figsize=(8,6))
    plt.plot(tour_cities[:,0], tour_cities[:,1], 'o-', color='blue')
    plt.title("Best TSP Tour")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.show()

# ---------- Run ----------
best_tour, best_dist, fitness_progress = genetic_algorithm()

print(f"Best tour found has distance: {best_dist:.4f}")
print(f"Tour: {best_tour}")

plt.plot(fitness_progress)
plt.title("Best Fitness Over Generations")
plt.xlabel("Generation")
plt.ylabel("Fitness (1 / Distance)")
plt.grid(True)
plt.show()

plot_tour(best_tour)
