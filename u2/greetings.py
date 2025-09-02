def greetings(name):
    return("Hello, " + name + " byee?")

def unitGreetings(name, expected):
    result = greetings(name)
    print(result)
    if(result == expected):
        return("working")
    else:
        return("bad")
    
print(unitGreetings("ramya", "Hello, ramya byee?"))
print(unitGreetings("nina", "Hello, nina byee?"))
                