import random
def gameWin(comp,You):
    if comp == You:
        return None
    elif comp == 's':
        if You == 'w':
            return False
        elif You == 'g':
            return True
    elif comp == 'w':
        if You == 's':
            return True
        elif You == 'g':
            return False
    elif comp == 'g':
        if You == 's':
            return False
        elif You == 'w':
            return True
print("Comp Turn: Snake(s),Water(w) or Gun(g)?")
randNo = random.randint(1,3)
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g'
You = input("Your Turn: Snake(s),Water(w) or Gun(g)? ")
a = gameWin(comp,You)
print(f"Computer chose {comp}")
print(f"You chose {You}")
if a == None:
    print("The game is Tie!")
elif a:
    print("You win!")
else:
    print("You Lose!")