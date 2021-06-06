from classes import Unit, Hero

atralb  = Hero("Atralb", xpos = 1, ypos = 1, atk = 100, rge = 3)

malkesuras = Hero("Malkesuras", xpos = 1, ypos = 2, expvalue = 40, items = {"potions": 1})

atralb.showStats()

atralb.move(0,1)

atralb.attack(malkesuras)

malkesuras = Hero("Malkesuras", xpos = 1, ypos = 2, expvalue = 40, items = {"potions": 1})

atralb.attack(malkesuras)

malkesuras = Hero("Malkesuras", xpos = 1, ypos = 2, expvalue = 40, items = {"potions": 1})

atralb.attack(malkesuras)

unit = Unit("unit", xpos = 1, ypos = 0)

atralb.attack(unit)

hero = Hero("test", xpos = 0, ypos = 1)

atralb.attack(hero)

atralb.showStats()

atralb.move(1,0)

print(Hero.positions)


