import functions as fnc

env = [[' ', ' ', ' '],[' ', ' ', ' '],[' ', ' ', ' ']]

fnc.show_env(env) 
print('*'*20)

while True:
  
    c = True
    while c:      
        user = input('Please put your choice: (enter row and then column numbers which are separated by ","): ').split(',')
        [c, env] = fnc.update_env(env, user, True)
    
    [c1, c2] = fnc.check_win(env)
    
    if c1:
        print('The game is over!')
        fnc.show_env(env) 
        print('*'*20)  
        
        if c2 == 0:
            print('User won!')
        else:
            print('Bot won!')
        
        break  
        
    fnc.show_env(env) 
    print('*'*20)
    
    c = True
    while c:
        [c, env] = fnc.update_env(env, fnc.bot_choice(), False)
        
    [c1, c2] = fnc.check_win(env)
    
    if c1:
        print('The game is over!')
        fnc.show_env(env) 
        print('*'*20)  
        
        if c2 == 0:
            print('User won!')
        else:
            print('Bot won!')
        
        break 
    
    fnc.show_env(env) 
    print('*'*20)
    
    
        

