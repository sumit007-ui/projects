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
/______/______/______/______/______/______/______/______/______/______/________
*******************************************************************************  ''')

print("Welcome to the Tresure island!")
print("Your goal is to find the hidden treasure on this island.")
print("You are stand a cross road. Where do you want to go? "
      "You can either go left or right.")
start = input("* ")
if start == "left":
    print("You have come to lake. There is an island in the middle of the lake.")
    print("Type 'wait' to wait for a boat.Type 'swim' for to swim across")
    lake = input("* ")
    if lake == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors.")
        print("    One red, one yellow and one blue. which colour do you choose?")
        house = input("* ")
        if house == "yellow":
            print("You have won the game!")
        elif house == "red":
            print("Burned by fire. Game over!")
        elif house == "blue":
            print("Eaten by beasts. Game over!")
        else:
            print("You chose a door that does not exist. Game over!")
    
    elif lake == "swim":
        print("You got crocodile attacked. Game over!")

else:
    print("you fell in the hole. Game over!")

    

 