

def PrimeNumber():

    while True:
        print("Enter any number")

        number = input()
        
        if int(number) % 2 != 0:
            print("This is a prime number!")
            continue
        elif int(number) % 2 == 0:
            print("This is not a prime number.")
            continue


PrimeNumber()
