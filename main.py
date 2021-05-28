from classes import Unit, Hero

atralb  = Unit("Atralb", xpos = 1, ypos = 1, atk = 10, rge = 3)

malkesuras = Hero("Malkesuras", xpos = 1, ypos = 2, items = {"potions": 1})

atralb.getPos()

malkesuras.getPos()

malkesuras.attack(atralb)

atralb.move(0,1)

atralb.attack(malkesuras)

atralb.move(1,0)

atralb.attack(malkesuras)

malkesuras.items["boost"]  = 2

malkesuras.getItems()

malkesuras.usePotion()

malkesuras.getItems()

malkesuras.usePotion()

malkesuras.teleport(4,0)

print(Hero.positions)
