import random

wins = 0
losses = 0
ties = 0

print("Welcome to Python Rock, Paper, Scissors!")
print(f"Wins: {wins}, Losses: {losses}, Ties: {ties}")
print("Please choose to continue...")

computer = random.randint(1, 3)
user = input("[1] Rock, [2] Paper, [3] Scissors, [9] Quit\n")

rock = "Computer chose Rock..."
paper = "Computer chose Paper..."
scissors = "Computer chose Scissors..."

you_win = "You win! (•o•)"
comp_win = "Computer wins! [•0•]"

while not user == 9:
    if user == 1:
        if computer == 1:
            print(f"{rock} Tie!")
            ties += 1
        elif computer == 2:
            print(f"{paper} {comp_win}")
            losses += 1
        elif computer == 3:
            print(f"{scissors} {you_win}")
            wins += 1
    elif user == 2:
        if computer == 1:
            print(f"{rock} {you_win}")
            wins += 1
        elif computer == 2:
            print(f"{paper} Tie!")
            ties += 1
        elif computer == 3:
            print(f"{scissors} {comp_win}")
            losses += 1
    elif use == 3:
        if computer == 1:
            print(f"{rock} {comp_win}")
            losses += 1
        elif computer == 2:
            print(f"{paper} {you_win}")
            wins += 1
        elif computer == 3:
            print(f"{scissors} Tie!")
            ties += 1
