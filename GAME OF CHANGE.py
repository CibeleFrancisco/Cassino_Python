import random
from time import sleep
out= False
while out==False:

    print("\U0001F340"*20)
    print("\U0001F340 \033[7:0:42mGAME OF CHANGE!\033[m \U0001F340 \n \033[1:32:40m TRY YOUR LUCKY! \033[m")
    print("\U0001F340" * 20)
    print("Try to guess one number between 1 and 100 \n"
          "If you hit the number earn 100% of the prize\n"
          "If you hit the corresponding ten, win 20% of the prize\n"
          "If you hit 2 numbers before or after you win 25% of the prize")
    repeate= False
    while repeate== False:
        
        x= int(input("Enter a number between 1 and 100: "))
        print("PROCESSING.........")
        sleep(2)
        if x not in range (1,100):
            print("\033[1:31:40m INVALID NUMBER!\033[m")
            repeate=False
        else:
            repeate = True
            
    y= random.randint(1,100)

    decimalx= x//10%100
    decimaly= y//10%100

    if decimalx==decimaly:
      print(f"Chosen number:  {y}")
      print("\U0001F340 \33[7:32:40mCONGRATULATIONS, YOU WON 20% OF THE PRIZE \33[m\U0001F340")

    elif x-1 ==y:
        print(f"Chosen number:  {y}")
        print("\U0001F340 \33[7:32:40mCONGRATULATIONS, YOU WON 25% OF THE PRIZE \33[m\U0001F340")

    elif x-2 ==y:
        print(f"Chosen number:  {y}")
        print("\U0001F340 \33[7:32:40mCONGRATULATIONS, YOU WON 25% OF THE PRIZE \33[m\U0001F340")

    elif x+1 ==y:
        print(f"Chosen number:  {y}")
        print("\U0001F340 \33[7:32:40mCONGRATULATIONS, YOU WON 25% OF THE PRIZE \33[m\U0001F340")

    elif x+2 ==y:
        print(f"Chosen number:  {y}")
        print("\U0001F340 \33[7:32:40mCONGRATULATIONS, YOU WON 25% OF THE PRIZE \33[m\U0001F340")

    elif x ==y:
        print(f"Chosen number:  {y}")
        print("\U0001F340 \U0001F340 \33[7:32:40mCONGRATULATIONS, YOU WON 100% OF THE PRIZE \33[m\U0001F340 \U0001F340")
    else:
        print(f"Chosen number:  {y}")
        print("You Lose \U0001F97A")

    test = input("Type 'yes' to quit or ENTER to play again:  ").lower().strip()
    if test == "yes":
        out = True


