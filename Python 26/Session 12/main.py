def calculator(number1, number2, operator):
    if operator == '+':
        return number1 + number2
    if operator == '-':
        return number1 - number2
    if operator == '*':
        return number1 * number2
    if operator == '/':
        return number1 / number2
    
number1 = float(input('Enter your first number: '))
number2 = float(input('Enter your second number: '))
operator = input('choose the operation: ')

print(f"{number1} {operator} {number2}")

print(calculator(number1, number2, operator))

print(eval(f"{number1} {operator} {number2}"))

