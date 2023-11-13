# import math
# import numpy as np

# numbers = []
# min = math.inf
# max = -math.inf
# sum = 0
# for i in range(5):
#     # int(input("Enter your "+ str(i+1)+" Number: "))
#     numbers.append(int(input(f"Enter your {i+1} number: ")))
#     sum = sum+numbers[-1]
#     if (numbers[-1]>max):
#         max = numbers[-1]
#     if (numbers[-1]<min):
#         min = numbers[-1]
# avg = sum/5

# sum = 0
# for number in numbers:
#     sum = sum+((number-avg)**2)
# var = sum/5

# print(f"Minimum number is : {min}")
# print(f"Maximum number is : {max}")
# print(f"Average of yours numbers is : {avg}")
# print(f"Variance of yours numbers is : {var}")
# print(numbers) 


# Min = np.amin(numbers)
# Max = np.amax(numbers)
# Avg = np.average(numbers)
# Var = np.var(numbers)


# print(f"Minimum number is : {Min}")
# print(f"Maximum number is : {Max}")
# print(f"Average of yours numbers is : {Avg}")
# print(f"Variance of yours numbers is : {Var}")


import min_max_avg_var as m

nums = [20, 15, 18, 12, 17, 20]

Max, Min = m.calmin_max(nums)
Avg, Var = m.calavg_var(nums)
print(f"Minimum number is : {Min}")
print(f"Maximum number is : {Max}")
print(f"Average of yours numbers is : {Avg}")
print(f"Variance of yours numbers is : {Var}")
