import random

def generate(x):
    for i in range(x):
        charType = randInt(1,3)
        if(charType == 1):

        elif(charType == 2):

        else:
            

print("Enter a length for the password: ", end="")
num = int(input())
generate(num)
