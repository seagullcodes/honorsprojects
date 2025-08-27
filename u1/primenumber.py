def is_prime(n):
    
    for i in range(2, 101):
        if(n%i == 0 and n != i):
            return(False)
            
        else:
            return(True)
    


def testPrime(n, expected):
    result = is_prime(n)
    if(result == expected):
        print('it works')
    else:
        print("you failed")

testPrime(3, True)
testPrime(6, False)
testPrime(19, True)
testPrime(7, True)
testPrime(30, False)