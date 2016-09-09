#This is a Rock, Paper, Scissors game.



def Game():
    print("Player 1 please enter your move (rock/paper/scissors).")
    p1 = input()

    print("Player 2 please enter your move (rock/paper/scissors).")
    p2= input()

    
    while p1 == "rock":
        if p2 == "paper":
            print("Player 2 wins!")
            break
        elif  p2 == "scissors":
            print("Player 1 wins!")
            break
        elif p2 == "rock":
            print("Tie!")
            return
        
    while p1 == "paper":
        if p2 == "scissors":
            print("Player 2 wins!")
            break
        elif  p2 == "rock":
            print("Player 1 wins!")
            break
        elif p2 == "paper":
            print("Tie!")
            return
        
    while p1 == "scissors":
        if p2 == "rock":
            print("Player 2 wins!")
            break
        elif  p2 == "paper":
            print("Player 1 wins!")
            break
        elif p2 == "scissors":
            print("Tie!")
            return


playagain = "y"
while playagain == "y": 
    Game()
    print("Press 'y' to play again.")
    playagain = input()
    
Game()

