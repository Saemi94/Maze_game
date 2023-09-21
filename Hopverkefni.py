##tile Traveler
movement = ""

## y = N og S, x = W og E
def checkbox(x,y):
    if x == 1 and y == 1:
        movement = "N"
    elif x == 1 and y == 2:
        movement = "N S W"
    elif x == 1 and y == 3:
        movement = "S W"

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