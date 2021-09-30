import random
print ("An Ice Serpent appears!")
print ("Press 1 to hit it with a sword.")
print ("Press 2 to hit it with Fire")
print ("Press 3 to hit it with Electricity")
move = int(input("What do you want to hit it with?")) #First turn

enemyhp = 100
sworddamage = 25
criticalsword = 100
fire = 60
chance = random.randint(0,20)
elec = 35 + chance
iceserpdamage = 27 + random.randint(0,8)
iceserpdamage2 = 27 + random.randint(0,8)
iceserpdamage3 = 27 + random.randint(0,8)
iceserpdamage4 = 27 + random.randint(0,8)
hp = 100


if (move == 1) and (chance == 20):
    print ("Critical hit! Dealt " + str (criticalsword) + " damage!")
    remaininghp = enemyhp - criticalsword
elif (move == 1) and (chance != 20):
    print ("Dealt " + str (sworddamage) + " damage!")
    remaininghp = enemyhp - sworddamage
elif (move == 2):
    print ("Dealt " + str (fire) + " damage!")
    remaininghp = enemyhp - fire
elif (move == 3) and (chance <= 6):
    print ("Dealt " + str (elec) + " damage!")
    remaininghp = enemyhp - elec
elif (move == 3) and (chance > 6):
    print ("Dealt " + str (elec) + " damage!")
    print ("The enemy is now paralyzed")
    remaininghp = enemyhp - elec

if remaininghp <= 0:
    print ("The Ice Serpent has been defeated!")
    exit()
elif (move == 3) and (chance >= 6):
    print ("The Ice Serpent has " + str (remaininghp) + "HP left.")
    print ("The Ice Serpent is paralyzed, so it can't attack")
    iceserpdamage = 0
    currenthp = hp
    print ("You have " + str (currenthp) + "HP left")
else:
    print ("The Ice Serpent has " + str (remaininghp) + "HP left.")
    print ("The Ice Serpent attacks! " + str (iceserpdamage) + " HP dealt!")
    currenthp = hp - iceserpdamage
    print ("You have " + str(currenthp) + "HP left")

move2 = int(input("What do you want to hit it with?")) #Second turn

if (move2 == 1) and (chance == 20):
    print ("Critical hit! Dealt " + str (criticalsword) + " damage!")
    remaininghp2 = remaininghp - criticalsword
elif (move2 == 1) and (chance != 20):
    print ("Dealt " + str (sworddamage) + " damage!")
    remaininghp2 = remaininghp - sworddamage
elif (move2 == 2):
    print ("Dealt " + str (fire) + " damage!")
    remaininghp2 = remaininghp - fire
elif (move2 == 3) and (chance <= 6):
    print ("Dealt " + str (elec) + " damage!")
    remaininghp2 = remaininghp - elec
elif (move2 == 3) and (chance > 6):
    print ("Dealt " + str (elec) + " damage!")
    print ("The enemy is now paralyzed")
    remaininghp2 = remaininghp - elec

if remaininghp2 <= 0:
    print ("The Ice Serpent has been defeated!")
    exit()
elif (move2 == 3) and (chance >= 6):
    print ("The Ice Serpent has " + str (remaininghp2) + "HP left.")
    print ("The Ice Serpent is paralyzed, so it can't attack")
    iceserpdamage2 = 0
    currenthp2 = hp - iceserpdamage - iceserpdamage2
    print ("You have " + str (currenthp2) + "HP left")
else:
    print ("The Ice Serpent has " + str (remaininghp2) + "HP left.")
    print ("The Ice Serpent attacks! " + str (iceserpdamage2) + " HP dealt!")
    currenthp2 = hp - iceserpdamage - iceserpdamage2
    if currenthp2 <=0:
        print ("You have fallen to the Ice Serpent!")
        end()
    else:
        print ("You have " + str (currenthp2) + "HP left")

move3 = int(input("What do you want to hit it with?")) #Third turn

if (move3 == 1) and (chance == 20):
    print ("Critical hit! Dealt " + str (criticalsword) + " damage!")
    remaininghp3 = remaininghp2 - criticalsword
elif (move3 == 1) and (chance != 20):
    print ("Dealt " + str (sworddamage) + " damage!")
    remaininghp3 = remaininghp2 - sworddamage
elif (move3 == 2):
    print ("Dealt " + str (fire) + " damage!")
    remaininghp3 = remaininghp2 - fire
elif (move3 == 3) and (chance <= 6):
    print ("Dealt " + str (elec) + " damage!")
    remaininghp3 = remaininghp2 - elec
elif (move3 == 3) and (chance > 6):
    print ("Dealt " + str (elec) + " damage!")
    print ("The enemy is now paralyzed")
    remaininghp3 = remaininghp2 - elec

if (remaininghp3 <= 0) and (move == 1) and (move2 == 2) and (move3 == 3):
    print ("The Ice Seprent has been defeated!")
    print ("Found the secret Ice Crystal!")
    exit()
elif remaininghp3 <= 0:
    print ("The Ice Serpent has been defeated!")
    exit()
elif (move3 == 3) and (chance >= 6):
    print ("The Ice Serpent has " + str (remaininghp3) + "HP left.")
    print ("The Ice Serpent is paralyzed, so it can't attack")
    currenthp3 = currenthp2
    print ("The Ice Serpent has " + str (remaininghp3) + "HP left.")
else:
    print ("The Ice Serpent has " + str (remaininghp3) + "HP left.")
    print ("The Ice Serpent attacks! " + str (iceserpdamage3) + " HP dealt!")
    currenthp3 = hp - iceserpdamage - iceserpdamage2 - iceserpdamage3
    if currenthp3 <=0:
        print ("You have fallen to the Ice Serpent!")
        exit()
    else:
        print ("You have " + str(currenthp3) + "HP left")

move4 = int(input("What do you want to hit it with?")) #Fourth turn

if (move4 == 1) and (chance == 20):
    print ("Critical hit! Dealt " + str (criticalsword) + " damage!")
    remaininghp4 = remaininghp3 - criticalsword
elif (move4 == 1) and (chance != 20):
    print ("Dealt " + str (sworddamage) + " damage!")
    remaininghp4 = remaininghp3 - sworddamage
elif (move4 == 2):
    print ("Dealt " + str (fire) + " damage!")
    remaininghp4 = remaininghp3 - fire
elif (move4 == 3) and (chance <= 6):
    print ("Dealt " + str (elec) + " damage!")
    remaininghp4 = remaininghp3 - elec
elif (move3 == 3) and (chance > 6):
    print ("Dealt " + str (elec) + " damage!")
    print ("The enemy is now paralyzed")
    remaininghp4 = remaininghp3 - elec


if remaininghp4 <= 0:
    print ("The Ice Serpent has been defeated!")
    exit()
elif (move4 == 3) and (chance >= 6):
    print ("The Ice Serpent has " + str (remaininghp) + "HP left.")
    print ("The Ice Serpent is paralyzed, so it can't attack")
    iceserpdamage4 = 0
    print ("You have " + str (currenthp4) + "HP left")
else:
    print ("The Ice Serpent has " + str (remaininghp) + "HP left.")
    print ("The Ice Serpent attacks! " + str (iceserpdamage4) + " HP dealt!")
    currenthp4 = hp - iceserpdamage - iceserpdamage2 - iceserpdamage3 - iceserpdamage4
    if currenthp4 <=0:
        print ("You have fallen to the Ice Serpent!")
        exit()
    else:
        print ("You have " + str(currenthp4) + "HP left")
