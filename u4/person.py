class Person:
    def __init__(self, name, pets):
        self.name = name
        self.pets = pets

    def greeting(self):
        return(f"Hello, my name is {self.name}. I have {self.pets} pets.")
    
Nina = Person("nina", 2)
print(Nina.greeting())

Ramya = Person("Ramya", 0)
print(Ramya.greeting())

Jane = Person("jane", 18)
print(Jane.greeting())