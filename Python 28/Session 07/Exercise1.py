# Exercise1
player1 = input("Player1 -> choose your option: (rock, paper, scissors)")
player2 = input("Player2 -> choose your option: (rock, paper, scissors)")

if player1 == player2:
    print("draw")
elif player1=="rock" and player2=="scissors":
    print("Player1 won")
elif player1=="rock" and player2=="paper":
    print("Player2 won")
elif player1=="scissors" and player2=="paper":
    print("Player1 won")
elif player1=="scissors" and player2=="rock":
    print("Player2 won")
elif player1=="paper" and player2=="rock":
    print("Player1 won")
elif player1=="paper" and player2=="scissors":
    print("Player2 won")

