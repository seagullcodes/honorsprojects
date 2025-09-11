
def add_na(num1, a2):
    for i in range(num1):
        a2 = a2 + "na"
    return a2

def unitAdd_na(num22, a22, expected):
    res = add_na(num22, a22)
    if(res == expected):
        print("works")
    else:
        print("you're failing")
        
unitAdd_na(2, "ba", "banana")