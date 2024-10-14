# import numpy as np

# # Env = [[0, 0, 0], 
# #        [0, 0, 0], 
# #        [0, 0, 0]]

# Env = np.array([[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']], dtype=str)

# envNumber = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# turn = True
# counter = 0
# Nappar = True
# while Nappar:
#     if turn:
#         turn = not turn  
#         print(Env)      
              
#         print(envNumber)      
#         p1 = int(input('Enter your choice: '))
        
#         solutions = np.argwhere(envNumber == p1)
#         Env[solutions[0][0]][solutions[0][1]] = 'X'
        
#     else:
#         turn = not turn  
#         print(Env)      
              
#         print(envNumber)      
#         p2 = int(input('Enter your choice: '))
        
#         solutions = np.argwhere(envNumber == p2)
#         Env[solutions[0][0]][solutions[0][1]] = 'O'
    
#     for i in range(3):
            
#         if Env[i][0] == Env[i][1] and Env[i][0] == Env[i][2] and Env[i][0] == 'X':
#             print('X won')
#             Nappar = False
        
#         if Env[i][0] == Env[i][1] and Env[i][0] == Env[i][2] and Env[i][0] == 'O':
#             print('O won')
#             Nappar = False
        
#         if Env[0][i] == Env[1][i] and Env[0][i] == Env[2][i] and Env[0][i] == 'X':
#             print('X won')
#             Nappar = False
        
#         if Env[0][i] == Env[1][i] and Env[0][i] == Env[2][i] and Env[0][i] == 'O':
#             print('O won')
#             Nappar = False
        
#     if Env[0][0] == Env[1][1] and Env[0][0] == Env[2][2] and Env[0][0] == 'X':
#         print('X won')
#         Nappar = False
    
#     if Env[0][0] == Env[1][1] and Env[0][0] == Env[2][2] and Env[0][0] == 'O':
#         print('O won')
#         Nappar = False
    
#     if Env[0][2] == Env[1][1] and Env[0][2] == Env[2][0] and Env[0][2] == 'X':
#         print('X won')
#         Nappar = False
    
#     if Env[0][2] == Env[1][1] and Env[0][2] == Env[2][0] and Env[0][2] == 'O':
#         print('O won')
#         Nappar = False
    
#     counter = counter+1
    
#     if counter > 9:
#         Nappar = False
    
        
        
        
myName = 'Morteza'
mylist = ['M', 'o', 'r', 't', 'e', 'z', 'a']

# mylist[2] = 'z'
# myName[2] = 'z'

print(mylist[2])
print(myName[2])

print(mylist[0:3])
print(mylist[:3])

print(mylist[3:6])

print(mylist[4:7])
print(mylist[4:])

print(mylist[:])

print(mylist[6])
print(mylist[-1])

print(mylist[3])
print(mylist[-4])



