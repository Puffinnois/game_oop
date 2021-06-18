import classes

rpgClasses = ["berserk","paladin"]

heroes = []

def choosePlayerNbr():
    a = input("choose the number of players: ")
    nbPlayer = False
    while type(nbPlayer) is not int: 
        try:
            nbPlayer = int(a)
        except:
            a = input("integer needed, enter the number again: ")
    return nbPlayer 

def createHero():
    name = input("choose your name: ")
    x_wanted = int(input("choose your position on x axis: "))
    y_wanted = int(input("choose your position on y axis: "))
    
    print("choose your class")
    for idx, i in enumerate(rpgClasses):
        print(f"{i}: {idx + 1}")
    choice = int(input("choice: "))
    if choice == 1:
        class BerserkHero(classes.Hero, classes.Berserk):  
            def __init__(self, name, xpos, ypos, lvl = 1, exp = 0, exptolvlup = 100, expvalue = 50, hp = 100, mana = 10, atk = 20, dfs = 0, matk = 0, mdfs  = 0,  spd = 1, rge = 1, critFactor = 0, critRate = 0, movement = 1, tpmovement = 5, items = {}, rage = 0):
                super().__init__(name, xpos, ypos, lvl, exp, exptolvlup, expvalue, hp, mana, atk, dfs, matk, mdfs, spd, rge, critFactor, critRate, movement, tpmovement, items)
                self.rage = rage

        heroes.append(BerserkHero(name = name, xpos = x_wanted, ypos = y_wanted))

    if choice == 2:
        class PaladinHero(classes.Hero, classes.Paladin):  
            def __init__(self, name, xpos, ypos, lvl = 1, exp = 0, exptolvlup = 100, expvalue = 50, hp = 100, mana = 10, atk = 20, dfs = 0, matk = 0, mdfs  = 0,  spd = 1, rge = 1, critFactor = 0, critRate = 0, movement = 1, tpmovement = 5, items = {}, holiness = 0):
                super().__init__(name, xpos, ypos, lvl, exp, exptolvlup, expvalue, hp, mana, atk, dfs, matk, mdfs, spd, rge, critFactor, critRate, movement, tpmovement, items)
                self.holiness = holiness

        heroes.append(PaladinHero(name = name, xpos = x_wanted, ypos = y_wanted))


