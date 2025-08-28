import random
choices = ('rock', 'paper', 'scissor')

player_choice = input("Enter rock, paper, or scissor: ").lower()
computer_choice = random.choice(choices)

if player_choice == computer_choice:
    print("tie")
elif (player_choice == "rock" and computer_choice == "scissor") or \
     (player_choice == "scissor" and computer_choice == "paper") or \
     (player_choice == "paper" and computer_choice == "rock"):
    print("you win !!!!")
else:
    print("you loose")