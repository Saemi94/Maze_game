
# ## y = N og S, x = W og E
# def checkbox(x,y):
#     if x == 1 and y == 1:
#         movement = "N"
#     elif x == 1 and y == 2:
#         movement = "N S W"
#     elif x == 1 and y == 3:
#         movement = "S A"
#     #elif x == 1 and y ==4:
#         #movement = "N S"



x = 1
y = 1
Hasbeen12 = False
Hasbeen13 = False
Hasbeen21 = False
Hasbeen22 = False
Hasbeen23 = False
Hasbeen31 = False
Hasbeen32 = False
Hasbeen33 = False
HasMovedSquare = False
OnOff = True


while OnOff:
    if x == 1 and y == 1:
        print("You can travel: (N)orth.")
        choice = input() 
        choice = choice.upper()
        if choice == "N":
            y += 1
            HasMovedSquare = True
        else:
            print("Direction: Not a valid direction!")

    elif x == 1 and y == 2:
        if Hasbeen12 == True:
            print("You can travel: (N)orth or (E)ast or (S)outh.")
        else:
            print("Direction: You can travel: (N)orth or (E)ast or (S)outh.")
        Hasbeen12 = True
        choice = input() 
        choice = choice.upper()
        if choice == "N":
            y += 1
            HasMovedSquare = True
        elif choice == "S":
            y -= 1
            HasMovedSquare = True    
        elif choice == "E":
            x += 1
            HasMovedSquare = True
        else:
            print("Direction: Not a valid direction!")
            HasMovedSquare = False
    
    elif x == 1 and y == 3:
        if Hasbeen13:
            print("You can travel: (E)ast or (S)outh.")
        else:
            print("Direction: You can travel: (E)ast or (S)outh.")
        Hasbeen13 = True
        choice = input() 
        choice = choice.upper()
        if choice == "S":
            y -= 1
            HasMovedSquare = True
        elif choice == "E":
            x += 1
            HasMovedSquare = True
        else:
            print("Direction: Not a valid direction!")
            HasMovedSquare = False

    elif x == 2 and y == 1:
        if Hasbeen21:
            print("You can travel: (N)orth.")
        else:
            print("Direction: You can travel: (N)orth." )
        choice = input() 
        choice = choice.upper()
        if choice == "N":
            y += 1
            HasMovedSquare = True
        else:
            print("Direction: Not a valid direction!")
            HasMovedSquare = False

    elif x == 2 and y == 2:
        if Hasbeen22:
            print("You can travel: (S)outh or (W)est.")
        else:
            print("Direction: You can travel: (S)outh or (W)est.")
        Hasbeen22 = True
        choice = input() 
        choice = choice.upper()
        if choice == "S":
            y -= 1
            HasMovedSquare = True
        elif choice == "W":
            x -= 1
            HasMovedSquare = True
        else:
            print("Direction: Not a valid direction!")
            HasMovedSquare = False
    elif x == 2 and y == 3:
        if Hasbeen23:
            print("You can travel: (E)ast or (W)est.")
        else:
            print("Direction: You can travel: (E)ast or (W)est.")
        Hasbeen23 = True
        choice = input() 
        choice = choice.upper()
        if choice == "E":
            x += 1
            HasMovedSquare = True
        elif choice == "W":
            x -= 1
            HasMovedSquare = True
        else:
            print("Direction: Not a valid direction!")
            HasMovedSquare = False
    elif x == 3 and y == 1:
        print("Direction: Victory!")
        OnOff = False
    elif x == 3 and y == 2:
        if Hasbeen32:
            print("You can travel: (N)orth or (S)outh.")
        else:
            print("Direction: You can travel: (N)orth or (S)outh.")
        Hasbeen32 = True
        choice = input() 
        choice = choice.upper()
        if choice == "N":
            y += 1
            HasMovedSquare = True
        elif choice == "S":
            y -= 1
            HasMovedSquare = True
        else: 
            print("Direction: Not a valid direction!")
            HasMovedSquare = False
    elif x == 3 and y == 3:
        if Hasbeen33:
            print("You can travel: (S)outh or (W)est.")
        else:
            print("Direction: You can travel: (S)outh or (W)est.")
        Hasbeen33 = True
        choice = input() 
        choice = choice.upper()
        if choice == "W":
            x -= 1
            HasMovedSquare = True
        elif choice == "S":
            y -= 1
            HasMovedSquare = True
        else: 
            print("Direction: Not a valid direction!")
            HasMovedSquare = False