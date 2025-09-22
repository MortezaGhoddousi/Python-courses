# def f(a, b, c):
#     delta = b**2 - 4*(a*c)
#     if delta > 0:
#         x1 = (-b+(delta**0.5))/(2*a)
#         x2 = (-b-(delta**0.5))/(2*a)
#         return [x1, x2]
#     elif delta == 0:
#         x1 = (-b)/(2*a)
#         return [x1]
#     else:
#         x1 = "No root"
#         return [x1]

# print (f(1, 5, 2))


# f(x) = sin(x)

# f(x) = 4*x+2

def f(x):
    return 4*x+2

initial_population = [5, 1, 7, -0.5, 2, 0, 8, 0.75, 1, 1.5]
fitness = []

for i in initial_population:
    fitness_value = 1 / (1 + abs(f(i)))
    fitness.append(fitness_value)

fitness.sort(reverse=True) 
print(fitness)
print('end')





