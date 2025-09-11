import math
def sumOfPowers(num1):
    secondnum = 1
    sum1 = 1
    if(num1 == 0):
        return 0
    for i in range(num1-1):
        sum1 = sum1*2
        secondnum += sum1
       
    return secondnum



def unitSum(num4, expected):
    res = sumOfPowers(num4)
    if(res == expected):
        print("works")
    else:
        print("you're failing")
    
unitSum(0,0) 
unitSum(1,1) 
unitSum(2,3)
unitSum(3,7)