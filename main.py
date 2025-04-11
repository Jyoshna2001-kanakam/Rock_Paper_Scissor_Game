#Rock wins against scissors
#scissors win against paper
#paper wins against Rock 

import random
rock=0
paper=1
scissor=2
a=True
while a:
     print("Rock Paper Scissor Game")
     user_number=int(input("Enter your number:"))
     computer_number=int(random.randrange(0,3))

     print(f"computer number is :{computer_number}")

     if user_number==0 and computer_number==1:
          print("You lose")
     elif user_number==0 and computer_number==2:
          print("You win...!")
     elif user_number==1 and computer_number==0:
          print("You win...!")
     elif user_number==1 and computer_number==2:
          print("You lose.")
     elif user_number==2 and computer_number==0:
          print("You lose.")
     elif user_number==2 and computer_number==1:
          print("You win..!.")
     elif user_number==computer_number:
          print("It's a draw")
     else:
          print("You entered a wrong number...You lose")

     choose=input("Want to continue enter y else n:")
     if choose.lower()=='y':
          a=True
     else:
          break
