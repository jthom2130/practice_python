#Generate a random number between 1&9 and ask user to guess
#the number. then tell them if it's too low, high , or correct.


import random #imports the random module

num = random.randint(1, 9) #defines num to a random integer between 1 and 9 including 1&9

print("Can you guess what number I am thinking of?")
print("I'll give you a hint...it's between 1 and 9")
print("Take a guess! (or type exit to quit game)")

guess = 0 #you have to assign variable guess to something for the while loop to work. zero seems good 

while guess != num or "exit": #b/c guess = 0 the while loop initiates
    guess = input() #changes guess to what user inputs

    if guess == "exit":
        print("Thanks for playing!")
        break #stops code if user enters "exit"
    
    if int(guess) > num:
        print("Too high, try again!")
    elif int(guess)<num:
        print("Too low, try again!")
    else:
        print("That's correct!")
   

#Simple guess the number game using while loop.
