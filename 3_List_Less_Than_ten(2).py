#Take a list and write a program that makes a new list that contains all integers that are less than 5.


list1 = [1,1,2,3,5,8,13,21,34,55,89]#original list

list2 = [] #create a new blank list

for i in list1: #for integer(i) in list 1: "for the integers in list 1"
    if i < 5:   #if integer(i) is less than 5
        list2.append(i) #append blank list2 to contain thoses integers
print(list2) #print out the appended list2


    
