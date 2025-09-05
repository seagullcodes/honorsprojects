def sum(n):
    thing = 0
    for i in range(1, n+1):
        thing += i*i
    return thing

def unitSum(n, expected):
    res = sum(n)
    if(res == expected):
        print("works")
    else:
        print("you're failing")

unitSum(1,1)
unitSum(2,5)
unitSum(3,14)
