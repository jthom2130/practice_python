#Create a program that asks the user for a number and then prints out a list of all the divisors of that number. 


print("Enter a number")
num = input() #remember that input() is ALWAYS a string value

list1 = []   #create a blank list

for i in range(1,int(num)): #for integers in the range(1, user number input)...convert num to integer
    if int(num) % i == 0:   #if num can be divided by an integer in this range and remainder = 0...convert num to integer again
        list1.append(i)     #append list1 to contain those integers
        
print(list1)
