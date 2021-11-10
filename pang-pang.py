
from random import randint

class Player():

    def __init__(self, lifes):
        self.lifes = lifes
        self.scores = 0
        self.did_hit = False
        self.is_hitted = False

    def fire(self):
        sikta = randint(1, 5)
        if sikta in {1, 2, 3}:
            self.did_hit = True

        ont = randint  (1, 5)
        if ont in {1}:
            self.is_hitted = True
       # Här sker "eldväxlingen"

    def inc_scores(self):
        self.scores += 1
       # Här ska poängen öka

    def reduce_lifes(self):
        self.lifes -= 1
        # Här ska antalet liv minska



a_player = Player(3)       # Initiera en spelare med tre liv
while True:
    input("Tryck 'enter' för att sjuta ")
    a_player.fire()            # Spelaren skjuter
    
    if a_player.did_hit is True:
       print('Träff!')
       a_player.inc_scores() # Antalet poäng ökas med 1
       a_player.did_hit = False

    else:
       print('Miss, sikta bättre')

    if a_player.is_hitted is True:
       print('Aaaaaah')
       a_player.reduce_lifes() # Antalet liv minskas med 1
       a_player.is_hitted = False

    else:
       print('Du klarade dig denna gång!')

    if a_player.lifes <= 0:
        break
    
    print(a_player.scores)
    print(a_player.lifes)
    
print("")
print(f"Din slutpoäng blev: {a_player.scores}")
