def attention(test):
    print(test[0:9])
    if(test[0:9] == "Hey, you!"):
        return True
    else:
        return False
    
def unitAttention(testa, expected):
    result = attention(testa)
    if(result == expected):
        print("IT'S WORKING")
    else:
        print("you are awful at coding")

unitAttention("Hello, my name is Inigo Montoya.", False)
unitAttention("Excuse me, Dr. Kessner?", False)
unitAttention("Hey, you! Give me your code!", True)