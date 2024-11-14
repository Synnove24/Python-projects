import random  #imports random so the code can randomly pick between rock paper and scissors

#function name
def is_legal(x:str)->bool:
    """decides if the users input is a legal weapon"""
    #if statement to make sure the user typed in one of the three options
    if (x == "rock") or (x == "scissors") or (x == "paper"):
        return 3==3
    else:
        return 3==2
#function name
def beats(w:str,l:str)->bool:
    """decides if the computer or the user wins"""
    if w == "rock":      #if statement for first player choosing rock
        if l == "rock":
            return "tie"
        elif l == "scissors":
            return 3==3
        elif l == "paper":
            return 3==2
    if w == "paper":     #if statement for paper
        if l == "paper":
            return "tie"
        elif l == "rock":
            return 3==3
        elif l == "scissors":
            return 3==2        
    if w == "scissors":  #if statement for scissors
        if l == "scissors":
            return "tie"
        elif l == "paper":
            return 3==3
        elif l == "rock":
            return 3==2  


def RPS_game():   #defines function
    comp_choice = random.choice(["rock", "paper", "scissors"])  #randomly choses and lets user pick weapon
    player_choice = input("Choose rock, paper, or scissors: ")
    if not (is_legal(player_choice)):                           #if statement that makes sure the user picked rock paper or scissors
        print("You must select from rock, paper, or scissors")
    else:
        print("The computer chose", comp_choice)                #prints what the computer chooses and who wins
        if beats(player_choice, comp_choice):
            print("You win!")
        elif beats(comp_choice, player_choice):
            print("You lost. :(")
        else:
            print("It's a tie.")
RPS_game()
            
