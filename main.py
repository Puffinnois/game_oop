import game

nbPlayers = game.choosePlayerNbr()

for i in range(nbPlayers):
    game.createHero()


for i in range(len(game.heroes)):
   game.heroes[i].showStats()
