def reversestring(change):
    newastring = '' 
    for i in range(len(change)):
        newastring += change[len(change)-1-i]
    return newastring


def unitReverse(namea1, expected):
    res = reversestring(namea1)
    if(res == expected):
        print("works")
    else:
        print("you're failing")

unitReverse("bad", "dab")
unitReverse("Hello, world!", "!dlrow ,olleH")