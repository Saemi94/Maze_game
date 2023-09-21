##tile Traveler
movement = ""

## y = N og S, x = W og E
def checkbox(x,y):
    if x == 1 and y == 1:
        movement = "N"
    elif x == 1 and y == 2:
        movement = "N S W"
    elif x == 1 and y == 3:
        movement = "S A"
    #elif x == 1 and y ==4:
        #movement = "N S"


x = 1
y = 1
OnOff = False

while OnOff:
    if x == 1 and y == 1:
        print("You can travel: (N)orth.")
        choice = input()
        if choice == "N":
            y += 1
        else:
            print("Direction: Not a valid direction!")

    elif x == 1 and y == 2:
        print("You can  travel (N)orth, (S)outh, (E(ast. " )
        choice = input()
        if choice == "N":
            y += 1
        elif choice == "S":
            y -= 1    
        elif choice == "E":
            x += 1
        else:
            print("Direction: Not a valid direction!")
    
    elif x == 1 and y == 3:
        print("You can travel: (S)outh, and (E)ast. " )
        choice = input()
        if choice == "S":
            y -= 1
        elif choice == "E":
            x += 1
        else:
            print("Direction: Not a valid direction!")

    elif x == 2 and y == 1:
        print("You can travel: (N)" )
        choice = input()
        if choice == "N":
            x += 1
        else:
            print("Direction: Not a valid direction!")

    if x == 2 and y == 2:
        print("You can travel: (S)outh, and (W)est. ")
        choice = input()
        if choice == "S":
            y -= 1
        elif choice == "W":
            x -= 1
        else:
            print("Direction: Not a valid direction!")
    if x == 2 and y == 3:
        print("You can travel: (E)ast, and (W)est. ")
        choice = input()
        if choice == "E":
            x += 1
        elif choice == "W":
            x -= 1
        else:
            print("Direction: Not a valid direction!")