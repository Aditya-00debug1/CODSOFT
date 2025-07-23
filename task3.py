import random

youDict = {"Rock": 1, "Paper": -1, "Scissors": 0}
reverseDict = {1: "Rock", -1: "Paper", 0: "Scissors"}

while True:
    computer = random.choice([-1, 0, 1])
    youstr = input("Enter a choice: ")
    you = youDict[youstr]
    print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

    if (computer == you):
        print("Draw")
    else:
        if (computer == -1 and you == 1):
            print("You lose!!")
        elif (computer == -1 and you == 0):
            print("You win!!")
        elif (computer == 1 and you == -1):
            print("You win!!")
        elif (computer == 1 and you == 0):
            print("You lose!!")
        elif (computer == 0 and you == 1):
            print("You win!!")
        elif (computer == 0 and you == -1):
            print("You lose!!")
        else:
            print("Something went wrong")

    again = input("Do you want to play again? (yes/no): ")
    if again.lower() != "yes":
        break


    

    
        