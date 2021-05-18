import random
from time import sleep
rep= "Y"
while rep == "Y":
    user = int(input("""Choose: 
    [1] - ROCK
    [2] - PAPER
    [3] - SCISSORS:  
     """))
    if user ==1:
        print(f'You chose ROCK')
    elif user ==2:
        print("You chose PAPER")
    elif user ==3:
        print("You chose SCISSORS")
    else:
        print("\33[7:31:40mINVALID OPTION!\33[m")
    print("JO")
    sleep(1)
    print("KEN")
    sleep(1)
    print("PO!")
    sleep(1)
    comp = random.randint(1,3)
    if comp==1:
        print("I chose ROCK")
    elif comp==2:
        print("I You chose PAPER")
    elif comp==3:
        print("I You chose SCISSORS")
    if user ==comp:
        print("TIE!")
    elif user == 3 and comp ==1:
        print("I WIN!")
    elif user ==1 and comp ==3:
        print("YOU WIN! CONGRATULATIONS!")
    elif user < comp:
        print("YOU WIN! CONGRATULATIONS!")
    elif comp < user:
        print("I WIN!")

