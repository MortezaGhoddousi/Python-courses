import random

def f(x):
    return 4*x+2

def selection (fitness, population):
    sorted_fitness = sorted(enumerate(fitness), key=lambda x: x[1], reverse=False)
    indices = [i for i, val in sorted_fitness]
    values = [val for i, val in sorted_fitness]

    parents = []
    
    for _ in range(2):
        r = random.random()
        # Find the first index where r <= cumulative probability
        for i, val in enumerate(values):
            if r <= val:
                parents.append(population[indices[i]])
                break
        else:
            # If not found due to rounding, pick last parent
            parents.append(population[indices[-1]])

    return parents



def float_to_8bit_binary(value):
    """Convert a float to a custom 8-bit float binary string."""
    import math
    
    if value == 0:
        return '00000000'  # zero special case
    
    sign = 0
    if value < 0:
        sign = 1
        value = -value
    
    bias = 3
    exponent = 0
    fraction = 0
    
    exponent = int(math.floor(math.log(value, 2)))
    if exponent < -3:
        # Underflow to zero (too small)
        return '00000000'
    if exponent > 4:
        # Overflow to infinity approximation
        return f'{sign}1110000'  # max exponent, zero fraction
    
    # Normalize mantissa between [1, 2)
    mantissa = value / (2 ** exponent) - 1  # fractional part
    
    # Fraction: 4 bits
    fraction = 0
    frac_val = mantissa
    for i in range(4):
        frac_val *= 2
        bit = 1 if frac_val >= 1 else 0
        fraction = (fraction << 1) | bit
        if bit == 1:
            frac_val -= 1
    
    exponent_bits = exponent + bias
    if exponent_bits < 0:
        exponent_bits = 0
    elif exponent_bits > 7:
        exponent_bits = 7
    
    binary_str = (sign << 7) | (exponent_bits << 4) | fraction
    return f'{binary_str:08b}'

def binary8_to_float(binary_str):
    """Convert an 8-bit custom float binary string to float."""
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
    if sign == 1:
        value = -value
    return value


def crossover(parents):
    # parents_binaries = []
    # for i in parents:
    #     parents_binaries.append(float_to_binary64(i))

    parents_binaries = [float_to_8bit_binary(i) for i in parents]

    one_point = 3

    children = []

    i = 0
    while i<2:
        j = 0
        temp1 = ''
        temp2 = ''
        while j<len(parents_binaries[i]):
            if j < one_point:
                temp1 = temp1+parents_binaries[i][j]
            else:
                if i==0:
                    temp2 = temp2+parents_binaries[1][j]
                else:
                    temp2 = temp2+parents_binaries[0][j]

            j = j+1
        children.append(binary8_to_float(temp1+temp2))
        i = i+1

    return children


# generate initial population
initial_population = [15, 11, 7, 5.5, 2, 0, 8, 0.75, 1, 1.5]
fitness = []

# calculate fitness for each person
for i in initial_population:
    fitness_value = 1 / (1 + abs(f(i)))
    fitness.append(fitness_value)

# selection operator
parents = selection (fitness, initial_population)

# crossover operator
new_population = []

for i in range(5):  
    children = crossover(parents)
    for child in children:
        new_population.append(child)

print(initial_population)
print(new_population)
print('end')



