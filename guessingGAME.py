

import random
# Guessing number game
f=True
tot=0

while(f):
    com=random.randint(1,100)
    score=0
    tot+=1
    while True:

        hum=int(input("guess your number(1-100):"))
        score+=1

        if hum==com:
            print(f"yeah!! you guessed it right! and your score is {score} and this is {tot} try")
            
           
            while(True):
                ch=input("do u want to play again!(y/n):")
                if ch=='y':
                    f=True
                    break
                    
                elif ch=='n':
                    f=False
                    break
                    
                else:
                    print("please enter a valid choice!(y/n)")
            break
            


            
                

            
        elif hum>com:
            print("your guess is too higher")
        else:
            print("your guess is too lower")
