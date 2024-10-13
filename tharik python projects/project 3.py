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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
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
a=input("you are at the cross road type left or type right:").lower()
if a=="left":
    print("you are now in front of sea ")
    b=input('do you\'ve to swim or wait for the boat press "swim" or "wait"').lower
    if b=="swim":
        print("you have eaten by shark")
        print("Game Over")
    else:
        print("the boat is coming to pick you up")
        print("boat came contenuos travel")
        c=input("There is three door  yellow and blue and red select correct door to win type Y for yellow door and B for blue door and R for red door").lower()
        if c=="y":
            print("ghost attack\nGame over")
        elif c=="b":
            print(" You are the winner hurreyyy")
        elif c=="r":
            print("leopard attack\n Game over")
elif a=="right":
    print("you have caught to the lion and got eaten ")
    print("Game over")
else:
    print("please choose left or right ")
