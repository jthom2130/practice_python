 #This program asks user for their name and tells them what year
#they will turn 100 years old.

print("Hello There!")
print("What is your name?")
Name = input()
print("Nice to meet you " + Name)
print("How old are you?")
Age = input()
print(Name + " you will be 100 in " + str(-int(Age) + 100) + "years!") # Must put -int() to return the negative number (-25+100=75)
print("Do you know what year that will be?")
print("The year "  + str((2016 - int(Age)) + 100) + "!")       #Order of ops: 1. Age is converted to integer value
                                                               #              2. 2016 - 25 is calculated
                                                               #              3. 1991 + 100 is calculated
                                                               #              4. 2091 is converted to string value
                                                               
                                                               #int() must be used before every variable that you intend to be a number
                                                               #str() must be used to convert integer to string value

                                                            
 



