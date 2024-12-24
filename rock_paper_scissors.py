print("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors")
import random

#user input 
a = [0,1,2]
user_choice = int(input("* "))
if user_choice == 0:
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
    
elif user_choice == 1:
    print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
    
elif user_choice == 2:
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
    
else:
    print("Invalid input. Please try again.")
    

#computer choice
choice = random.randint(0,2)

if choice == 0:
    print('''computer chose :
          
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
          
          ''')
elif choice == 1 :
    print('''computer chose :
          
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)

          ''')
else:
    print('''computer chose 
          
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

          ''')

print(choice)

if user_choice==0 and choice == 2 or user_choice == 1 and choice == 0 or user_choice == 2 and choice == 1 :
    print("You wins!")
elif user_choice == choice:
    print("It's a tie!")
else:
    print("Computer wins")