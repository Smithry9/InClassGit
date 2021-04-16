def divisors(x):
    currentNum = x
    divisorList = []
    while(currentNum > 0):
        if(x % currentNum == 0):
            divisorList.append(currentNum)
        currentNum -= 1

print("Enter an integer: ", end="")
num = int(input())
divisors(num)
