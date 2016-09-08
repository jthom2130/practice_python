#write program that returns a list that contains only the elements that
#are common between the lists (NO DUPLICATES).
#Make sure program works on two lists of different sizes. 


a = [1,1,2,3,5,8,13,21,34,55,89]
b = [1,1,2,3,4,5,6,7,8,9,10,11,12,13]

List = []

#This block creates the "List" that contains all common elements, but includes duplicates.
for i in a: 
    if i in b:
        List.append(i)
print("With Duplicates " + str(List))

List2 = []

#by creating "List2" ^^ we can remove the duplicates.
for i in List: #for the elements in "List"
    if i not in List2: #if the element is not in List2, 
        List2.append(i)#append List2 to contain those elements. (no duplicates)
  
print("Without Duplicates " + str(List2))
    


#By creating List2 the elements in List are copied without duplicates.
#You basically do the same "trick" twice to reduce down to having no duplicates.
