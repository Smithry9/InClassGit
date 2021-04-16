import random

def generate(x):
    password = ""
    for i in range(x):
        charType = randInt(1,3)
        if(charType == 1):
            #Add a number
            char = randInt(48,57)
            char = chr(char)
        elif(charType == 2):
            #Add a Uppercase Letter
        else:
            #Add a Lowercase Letter            

print("Enter a length for the password: ", end="")
num = int(input())
generate(num)
