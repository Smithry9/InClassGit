def calc(x, y):
    total = x + y
    diff = x - y
    product = x * y
    quotient = x / y
    answerList = [total, diff, product, quotient]
    print("Answers (sum, difference, product, quotient): ", end="")
    print(answerList)
    listTotal = 0
    for i in answerList:
        listTotal += i
    print("Sum of List: " + str(listTotal))

calc(10, 5)
