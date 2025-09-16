import random

class MagicEightBall:
    def __init__(self):
        self.listq = ["It is certain", "Most likely", "My reply is no", "Very doubtfall", "Ask later", "Cannot predict now"]

    def ask(self, askme):
        random_item = random.choice(self.listq)
        return(random_item)

Nina = MagicEightBall()
print(Nina.ask("Will i get into college?"))
print(Nina.ask("Do i have any friends"))
print(Nina.ask("Am i hopeless?"))