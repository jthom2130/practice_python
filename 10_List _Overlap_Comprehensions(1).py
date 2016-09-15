#program returns a list that contains only the elements that
#are common between the lists(no duplicates).
#Use List Comprehension.


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


List = [i for i in set(a) if i in b]#list comprehension
#using set() will remove duplicates from being printed.
print(List)
