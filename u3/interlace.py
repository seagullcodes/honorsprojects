def interlace(a,b):
    new = ""
    for i in range(len(a)+len(b)):
        new = new + (a[i:i+1]+(b[i:i+1]))
    return new


def unitInter(a,b,expected):
    res = interlace(a,b)
    if(res == expected):
        print("works")
    else:
        print("you're failing")

unitInter("abc","123","a1b2c3")