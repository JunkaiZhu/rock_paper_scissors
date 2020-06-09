import random


def comp_chose_rock():
    if user_choice == "rock":
        print("computer chose rock")
        print("draw")
    elif user_choice == "paper":
        print("computer chose rock")
        print("you win")
    elif user_choice == "scissors":
        print("computer chose rock")
        print("you lose")
    else:
        print("Invalid input, please input rock, paper or scissors")

def comp_chose_paper():
    if user_choice == "rock":
        print("computer chose paper")
        print("you lose")
    elif user_choice == "paper":
        print("computer chose paper")
        print("draw")
    elif user_choice == "scissors":
        print("computer chose paper")
        print("you win")
    else:
        print("Invalid input, please input rock, paper or scissors")

def comp_chose_scissors():
    if user_choice == "rock":
        print("computer chose scissors")
        print("you win")
    elif user_choice == "paper":
        print("computer chose scissors")
        print("you lose")
    elif user_choice == "scissors":
        print("computer chose scissors")
        print("draw")
    else:
        print("Invalid input, please input rock, paper or scissors")

def rndm():
    if random_comp_choice == 0:
        comp_chose_rock()
    elif random_comp_choice == 1:
        comp_chose_paper()
    elif random_comp_choice == 2:
        comp_chose_scissors()

while True:
    user_choice = input("Enter your choice: ").lower()
    random_comp_choice = random.randint(0, 2)
    rndm()
    play_again = input("Play again? (Y/N) Enter: ").lower()
    if play_again[0] != "y":
        break
  
    
