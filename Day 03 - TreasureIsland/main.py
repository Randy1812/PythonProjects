print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
ans = input("You're at a crossroad. Where do you want to go? Type 'left' or 'right'\n")
if ans != "left":
    print("You fell into a hole and died. Game Over!")
else:
    ans = input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. "
                "Type 'swim' to swim across.\n")
    if ans != "wait":
        print("You were attacked by a trout and died tragically. Game Over!")
    else:
        ans = input("You arrived at the island unharmed. There is a house with 3 doors. One red, one yelow and one "
                    "blue. Which color do you choose?\n")
        if ans == "blue":
            print("You are eaten by beasts. Game Over!")
        elif ans == "red":
            print("Ypu are burned by fire. Game Over!")
        elif ans == "yellow":
            print("You find the treasure and win!")
        else:
            print("You poked your nose where you shouldn't have and as a result the developer of this game who is the "
                  "God of this world has decided to kill you. Game Over!")
