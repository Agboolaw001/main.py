import random

print("Welcome to Rock, Paper, or Scissors game, Enjoy!")
print("R for Rock, P for Paper, S for Scissors")

while True:
    choices = ["rock", "paper", "scissors"]
    
    CPU = random.choice(choices)
    player = input("rock, paper, or scissors?: ").lower()

    while player not in choices:
        print("Error!, try again")
        
    
    if player == CPU:
        print("player: ", player)
        print("computer: ", CPU)
        print("Tie!")


    elif player == "scissors":
        if CPU == "rock":
            print("player: ", player)
            print("computer: ", CPU)
            print("winner", ",", CPU, "beat", player)

        if CPU == "paper":
            print("player: ", player)
            print("computer: ", CPU)
            print("winner", ",", player, "beat", CPU)
                

    elif player == "rock":
        if CPU == "paper":
            print("player: ", player)
            print("computer: ", CPU)
            print("winner", ",", CPU, "beat", player)

        if CPU == "scissors":
            print("player: ", player)
            print("computer: ", CPU)
            print("winner", ",", player, "beat", CPU)
    

    elif player == "paper":
        if CPU == "scissors":
            print("player: ", player)
            print("computer: ", CPU)
            print("winner", ",", CPU, "beat", player)
            
        if CPU == "rock":
            print("player: ", player)
            print("computer: ", CPU)
            print("winner", ",", player, "beat", CPU)
            

    play_again = input("Play again? (yes/no): ").lower()


    if play_again != "yes":
        break
print("Goodbye")




