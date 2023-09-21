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
    choice = input() 
    choice = choice.upper()
    if x == 1 and y == 1:
        print("You can travel: (N)orth.")
        
        if choice == "N":
            y += 1
        else:
            print("Direction: Not a valid direction!")

    elif x == 1 and y == 2:
        print("You can  travel (N)orth, (S)outh, (E(ast. " )
        
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
        
        if choice == "S":
            y -= 1
        elif choice == "E":
            x += 1
        else:
            print("Direction: Not a valid direction!")

    elif x == 2 and y == 1:
        print("You can travel: (N)" )
        
        if choice == "N":
            y += 1
        else:
            print("Direction: Not a valid direction!")

    elif x == 2 and y == 2:
        print("You can travel: (S)outh, and (W)est. ")
        
        if choice == "S":
            y -= 1
        elif choice == "W":
            x -= 1
        else:
            print("Direction: Not a valid direction!")
    elif x == 2 and y == 3:
        print("You can travel: (E)ast, and (W)est. ")
        
        if choice == "E":
            x += 1
        elif choice == "W":
            x -= 1
        else:
            print("Direction: Not a valid direction!")
    elif x == 3 and y == 1:
        print("Direction: Victory!")
        OnOff = False
    elif x == 3 and y == 2:
        print("Direction: (N)orth, (S)outh")
        if choice == "N":
            y += 1
        elif choice == "S":
            y -= 1
    elif x == 3 and y == 3:
        print("Direction: (W)est, (S)outh)")
        if choice == "W":
            x -= 1
        elif choice == "S":
            y -= 1





    