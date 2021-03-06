import classes

rpgClasses = ["berserk","paladin"]

heroes = []

def choosePlayerNbr():
    a = input("choose the number of players: ")
    nbPlayer = False
    while type(nbPlayer) is not int or nbPlayer <= 0: 
        try:
            nbPlayer = int(a)
            assert nbPlayer > 0
        except:
            a = input("positive integer needed, enter the number again: ")
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

def chooseTarget():
    for i in range(len(heroes)):
        print(heroes[i].name)
    targetName = input("choose target: ")
    target = None
    for i in range(len(heroes)):
        if heroes[i].name == targetName:
            target = heroes[i]
    if target == None:
      target = chooseTarget()
    return target

def chooseAction(object):

    # https://stackoverflow.com/a/39061905

    method_list = [func for func in dir(object.__class__) 
        if callable(getattr(object.__class__, func)) 
        and not func.startswith("_")
        ]
    print(method_list)
    
    choice = input("action choice: ")

    if choice in method_list:
        if choice in ["attack", "sanctify"]:
            target = chooseTarget()
            getattr(object, choice)(target)
        elif choice in ["move", "teleport"]:
            x_wanted = int(input("How much movement on x axis: "))
            y_wanted = int(input("How much movement on y axis: "))
            getattr(object, choice)(x_wanted, y_wanted)  
        else:
            getattr(object, choice)()
    else:
        print("You have chosen a non-existent action, choose again!")
        chooseAction(object)
