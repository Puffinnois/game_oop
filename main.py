import game
from game import heroes

nbPlayers = game.choosePlayerNbr()

for i in range(nbPlayers):
    game.createHero()


for i in range(len(heroes)):
   heroes[i].showStats()

roundNbr = 0
aliveCount = [1 for hero in heroes if hero.alive == True]

while len(aliveCount) > 1:
    roundNbr += 1
    print(f"=========Round {roundNbr}=========") 
    for i in range(len(heroes)):
        if heroes[i].alive == True:
            print(f"-----{heroes[i].name}'s turn-----")
            game.chooseAction(heroes[i])



