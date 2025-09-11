def factorial(change):
    newNum = 1
    for i in range(change):
        newNum *= change-i
    return(newNum)




def unitFact(namea1, expected):
    res = factorial(namea1)
    if(res == expected):
        print("works")
    else:
        print("you're failing")

unitFact(0,1)
unitFact(1,1)
unitFact(2,2)
unitFact(3,6)
unitFact(4,24)
unitFact(5,120)

