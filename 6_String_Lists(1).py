#ask user for a string an dprint out whether this sting is a
#palindrome or not. (palindrome is a string that reads the
#same forwards and backwards)



print("Please enter a palindrome.")
word = input()

List1 = [] #create two lists
List2 = []

List1.append(list(word)) #appends List1 to a list version of the string variable 
List2.append(list(word)[::-1]) #appends List2 to a reverse list version of the string variable
                               #the [::-1] will reverse the list
if List1 == List2:
    print("This word is a palindrome!")
else:
    print("This word is NOT a palindrome :(")
    
#if the two lists are == , BAM! you have a palindrome :)
