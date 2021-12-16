import random
from time import sleep

answers = ['rock', 'paper', 'scissors']
""" Conditions: rock wins over scissors,
                paper wins over rock,
                scissors wins over paper.
    Tie: when both answers are the same """

def Game() -> str:
    user_input = str(input("\nInput Answer: "))
    comp_choice = random.choice(answers)
    try:
        if user_input == comp_choice:
            print("TIE. You Both choose {}".format(user_input))
        elif user_input == 'rock' and comp_choice == 'scissors':
            print(f"YOU WIN\nComputer Choose: {comp_choice}")
        elif user_input == 'paper' and comp_choice == 'rock':
            print(f"YOU WIN\nComputer Choose: {comp_choice}")
        elif user_input == 'scissors' and comp_choice == 'paper':
            print(f"YOU WIN\nComputer Choose: {comp_choice}")
        else:
            print(f"COMPUTER WIN\nYou Choose: {user_input}\nComputer Choose: {comp_choice}")
    except Exception:
        print("Invalid Input. Error Detected. Try Again")

if __name__ == '__main__':
    print("WELCOME TO ROCK-PAPER-SCISSORS_101")
    sleep(2)
    print("MOVES:\tInput Values are \'rock, scissors or  paper\'")
    sleep(1.4)
    for start in range(3, 0, -1):
        print(f"Game starts in {start} second")
        sleep(0.5)
    while True:
        Game()
