import random
from time import sleep
out= False
while out==False:
        
    print("=*=*="*20)
    print("\U0001F3B2\33[7:30:45mDICE SIMULATOR!\33[m\U0001F3B2")
    print("=*=*="*20)
    print("Roll two dice. If the result is even, the computer wins. If the result is odd, you win!")
    n1= random.randint(1,6)
    print(f"The first dice is: {n1}")
    n2= random.randint(1,6)
    print(f"The second dice is: {n2}")
    print("PROCESSING..................")
    sleep(2)
    resul=n1+n2
    print(f"\033[04:33:40mFinal Result: {resul}\33[m")
    if resul %2==0:
        print("\033[7:30:41mEven result, the computer won!\033[m\U0001F5A5")
    else:
        print("\033[07:30:32m Odd result!!!\033[m\n"
              "\033[01:30:32mCongratulations! you won!\033[m")
            
    test = input("Type 'yes' to quit or ENTER to play again:  ").lower().strip()
    if test == "yes":
        out = True

