def countOccurrences(namea, repeated):
    count = 0
    for i in range (len(namea)):
        if repeated == namea[i:len(repeated)+i]:
            count+=1
    return(count)
    
def unitCount(namea1, repeated1, expected):
    res = countOccurrences(namea1, repeated1)
    if(res == expected):
        print("works")
    else:
        print("you're failing")


unitCount("Mississippi", "iss", 2)
unitCount("banananana", "na", 4)