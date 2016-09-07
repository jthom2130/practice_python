#Ask the user for a number. Print out whether the number is odd or even.
#hint: how does an even/odd number react differently when divided by 2?
    #answer: odd numbers have remainders when divided by 2.
    #this means that we have to figure out how to write a program to recognize when a remainder is present.

print("Please enter a number")
num = input()

if (int(num) % 2) == 0: #int() needs to go before num to ensure that it is read as an integer. num is initially set to string format.
    print("This is an even number!")
elif (int(num) % 2) != 0:
    print("This is an odd number!")

if (int(num) % 4) == 0:
    print("This number is divisible by 4!")
    
