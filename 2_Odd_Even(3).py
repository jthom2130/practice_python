print("Enter a number")
num = input()
print("Now enter another!")
check = input()

if int(num) % int(check) == 0:
    print(check + " divides evenly into " + num)
else:
    print(check + " does NOT divide evenly into " + num)
    
