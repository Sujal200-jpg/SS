import random as rd
user = int(input("Enetr \n for Snake \n 2 for Water \n 3 for Gun \n Your choice:"))
comp = rd.randint(1, 3)

def check(comp, user):
    if(comp ==  user):
        print("Its a DRAW!")
    elif(comp == 1 and user == 2):
        print("You LOSE!")
    elif(comp == 3 and user == 1):
        print("You LOSE!")
    elif(comp == 2 and user == 3):
        print("You LOSE!")
    else:
        print("You WON!")

check(comp, user)
print("Your choice:", user)
print("Computer's choice:", comp)
    