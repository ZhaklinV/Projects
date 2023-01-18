import random

rock = "Rock"
paper = "Paper"
scissors = "Scissors"

player_choice = input("Choose Rock[r] or Paper[p] or Scissors[s]: ")

if player_choice == "r":
    player_choice = rock
    print(f"Your choice is {player_choice}!")
elif player_choice == "p":
    player_choice = paper
    print(f"Your choice is {player_choice}!")
elif player_choice == "s":
    player_choice = scissors
    print(f"Your choice is {player_choice}")
else:
    raise SystemExit("Invalid exit! Try again!")

comp_move = ""
computer_choice = random.randint(1, 3)
if computer_choice == 1:
    comp_move = rock
elif computer_choice == 2:
    comp_move = paper
elif computer_choice == 3:
    comp_move = scissors
print(f"Computer choose {comp_move}")


win_options = (player_choice == rock and comp_move == scissors) or (player_choice == paper and comp_move == rock) or (
            player_choice == scissors and comp_move == paper)
lose_options =(player_choice == rock and comp_move == paper) or (player_choice == paper and comp_move == scissors) or (
            player_choice == scissors and comp_move == rock)


if comp_move == player_choice:
    print("Draw")
elif win_options:
    print("You win!")
elif lose_options:
    print("You lose!")
