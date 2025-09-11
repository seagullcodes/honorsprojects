def findA(namea1):
    num1 = 0
    count = 0
    for i in range(len(namea1)):
        if(namea1[i] == "a" and count<1):
            count += 1
        elif(namea1[i] == "a" and count == 1):
            num1 = i
            return i
           



def unitFinda(namea, expected):
    res = findA(namea)
    if(res == expected):
        print("works")
     
    else:
        print("you're failing")
        
unitFinda("banana", 3)
unitFinda("happy birthday", 12)