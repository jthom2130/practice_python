#This program reduces code by means of list comprehension.
#We want to return only the even numbers in list a.
#one way to do so is by...


a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#b= []
#for i in a:
#    if i % 2 == 0:
#        b.append(i)
#print(b)
#This will return only the even numbers in a, but you could condense this code.


#This code will do the same thing as the code above, but has reduced the code to one line.

b = [i for i in a if i %2==0]
print(b)
 

