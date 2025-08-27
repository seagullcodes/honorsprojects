def isGood(ogPrice, salePrice):
    if(salePrice < .75*ogPrice):
        return(True)
    else:
        return(False)
    
def unitTest(original, sale, expected):
    result = isGood(original, sale)
    if(result == expected):
        print("let's go!")
    else:
        print("that did not work")

unitTest(20, 5, True)  
unitTest(100, 75, False)              
unitTest(100, 74, True)