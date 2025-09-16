class Scorekeeper:
    def __init__(self, score):
        self.score = score
       

    def scoreNormal(self):
        return(self.score+100)
    def scoreBonus(self):
        return(self.score+1000)

Nina = Scorekeeper(100)
print(Nina.scoreNormal())
print(Nina.scoreBonus())

Ramya = Scorekeeper(200)
print(Ramya.scoreNormal())
print(Ramya.scoreBonus())
