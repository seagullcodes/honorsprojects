def vampire(hour, awake):
    if((hour < 6 or hour >22) and awake):
    
            #print("they are a vamp!")
            return(True)
    
    else:
        #print("they are not a vamp")
        return(False)

#print(vampire(7,True))
#vampire(7,False)
#vampire(2, True)
#vampire(23, True)

def vampireTest(hour, awake, expected):
    result = vampire(hour,awake)
    if(result == expected):
        return("this worked")
    else:
        return ("you can't code")
    
print(vampireTest(3,False,False))
print(vampireTest(2,True,True))