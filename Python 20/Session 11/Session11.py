import keyboard
import sys

while True:
    try:
        user_input = input('Enter space-separated integers: ').split()
        if keyboard.is_pressed("z"):
            print(keyboard.is_pressed("z"))
            sys.exit()

        list_of_integers = [int(item) for item in user_input]

        print(list_of_integers)  # [1, 2, 3]
        print(list_of_integers[-1]+list_of_integers[-2])        
    except ValueError:
        print("Not an integer! Please enter an integer.")
        continue
    else:
        break


