import random
import matplotlib.pyplot as plt
import numpy as np
import math

# ---------- Objective Function ----------
def f(x):
    return 5 * (x ** 2) - 3

# ---------- Fitness Function ----------
def fitness_function(x):
    return 1 / (1 + abs(f(x)))

# ---------- Binary Conversion Utilities ----------
def float_to_8bit_binary(value):
    if value == 0:
        return '00000000'
    sign = 0
    if value < 0:
        sign = 1
        value = -value
    bias = 3
    exponent = int(math.floor(math.log(value, 2)))
    if exponent < -3:
        return '00000000'
    if exponent > 4:
        return f'{sign}1110000'
    mantissa = value / (2 ** exponent) - 1
    fraction = 0
    frac_val = mantissa
    for i in range(4):
        frac_val *= 2
        bit = 1 if frac_val >= 1 else 0
        fraction = (fraction << 1) | bit
        if bit == 1:
            frac_val -= 1
    exponent_bits = exponent + bias
    exponent_bits = max(0, min(exponent_bits, 7))
    binary_str = (sign << 7) | (exponent_bits << 4) | fraction
    return f'{binary_str:08b}'

def binary8_to_float(binary_str):
    if len(binary_str) != 8:
        raise ValueError("Binary string must be exactly 8 bits.")
    val = int(binary_str, 2)
    sign = (val >> 7) & 0x1
    exponent = (val >> 4) & 0x7
    fraction = val & 0xF
    bias = 3
    if exponent == 0 and fraction == 0:
        return 0.0
    mantissa = 1.0
    for i in range(4):
        if (fraction & (1 << (3 - i))) != 0:
            mantissa += 2 ** (-(i + 1))
    value = mantissa * (2 ** (exponent - bias))
    return -value if sign == 1 else value

# ---------- Selection ----------
def selection(fitness, population):
    sorted_fitness = sorted(enumerate(fitness), key=lambda x: x[1], reverse=False)
    indices = [i for i, val in sorted_fitness]
    values = [val for i, val in sorted_fitness]

    parents = []
    for _ in range(2):
        r = random.random()
        for i, val in enumerate(values):
            if r <= val:
                parents.append(population[indices[i]])
                break
        else:
            parents.append(population[indices[-1]])
    return parents

# ---------- Two-Point Crossover ----------
def crossover(parents):
    binaries = [float_to_8bit_binary(p) for p in parents]
    point1, point2 = sorted(random.sample(range(1, 7), 2))  # Ensure point1 < point2

    children = []
    for i in range(2):
        if i == 0:
            new_binary = binaries[0][:point1] + binaries[1][point1:point2] + binaries[0][point2:]
        else:
            new_binary = binaries[1][:point1] + binaries[0][point1:point2] + binaries[1][point2:]
        children.append(binary8_to_float(new_binary))
    return children

# ---------- Mutation ----------
def mutate(individual, mutation_rate=0.9):
    binary = float_to_8bit_binary(individual)
    mutated = ''.join(
        bit if random.random() > mutation_rate else str(1 - int(bit))
        for bit in binary
    )
    return binary8_to_float(mutated)

# ---------- GA Main Loop ----------
def genetic_algorithm(pop_size=10, generations=1000):
    population = [10 * (random.random() - 0.5) for _ in range(pop_size)]
    best_fitness_progress = []

    for gen in range(generations):
        fitness = [fitness_function(ind) for ind in population]

        new_population = []
        while len(new_population) < pop_size:
            parents = selection(fitness, population)
            children = crossover(parents)
            children = [mutate(child, mutation_rate=0.9) for child in children]
            new_population.extend(children)

        # Elitism: Combine old and new population and keep the best
        combined_population = population + new_population
        combined_fitness = [fitness_function(ind) for ind in combined_population]
        sorted_indices = sorted(range(len(combined_fitness)), key=lambda i: combined_fitness[i], reverse=True)

        population = [combined_population[i] for i in sorted_indices[:pop_size]]
        best_fitness_progress.append(combined_fitness[sorted_indices[0]])

    best_solution = population[0]
    best_fitness_value = fitness_function(best_solution)

    return best_solution, best_fitness_value, best_fitness_progress

# ---------- Run and Plot ----------
best_solution, best_fit, fit_progress = genetic_algorithm()

print("Best solution found:", best_solution)
print("Fitness of best solution:", best_fit)

plt.plot(fit_progress)
plt.title("Best Fitness Over Generations")
plt.xlabel("Generation")
plt.ylabel("Fitness")
plt.grid(True)
plt.show()
