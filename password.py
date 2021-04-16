import random

def generate(x):
    password = ""
    for i in range(x):
        charType = randint(1,3)
        if(charType == 1):
            #Add a number
            char = randint(48,57)
            char = chr(char)
        elif(charType == 2):
            #Add a Uppercase Letter
            char = randint(65,90)
            char = chr(char)
        else:
            #Add a Lowercase Letter
            char = randint(97,122)
            char = chr(char)

        password += char
    print(password)

print("Enter a length for the password: ", end="")
num = int(input())
generate(num)
