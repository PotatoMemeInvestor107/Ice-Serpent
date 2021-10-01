move1dmg = 30
move2dmg = 15
move3dmg = 55
enemyhp = 100
while enemyhp > 0:
    move = int(input("Choose a move"))
    if move == 1:
        print ("Hit with move 1. " + str (move1dmg) + " damage dealt.")
        enemyhp = enemyhp - move1dmg
        print ("The enemy has " + str (enemyhp) + "HP left")
    elif move == 2:
        print ("Hit with move 2. 15 dmg dealt.")
        enemyhp = enemyhp - move2dmg
        print ("The enemy has " + str (enemyhp) + "HP left")
    elif move == 3:
        print ("Hit with move 3. " + str (move3dmg) + " damage dealt.")
        enemyhp = enemyhp - move3dmg
        print ("The enemy has " + str (enemyhp) + "HP left")
    if enemyhp <= 0:
        print ("The enemy has been defeated!")
        break
