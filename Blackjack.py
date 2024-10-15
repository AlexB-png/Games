import random
import os
import time
from os import system
lose=0
os.system('CLS')
card1 = random.randint(1,10)

print (card1,"Total:",card1)
total = card1
while total < 22:
    add = input("Would you like another card? yes or no")
    if add == "yes":
        card3=random.randint(1,10)
        os.system('CLS')
        print("You drew a",card3)
        total=total+card3
        print("Your new total is",total)
    if add == "no":
        final=total
        break
os.system('CLS')
comptotal=0
if total == 21:
    print("Exactly 21!!")
else:
    print("Your total was",total)
if total > 21:
    print("You lose :(")
    final=total
    lose=1
if lose == 0:
    time.sleep(2)
    print("Computers turn")
    comp1=random.randint(1,10)
    comptotal += comp1
    print("Card 1 was a",comp1)
    print("Computer total:",comptotal)
    time.sleep(1)

    comp2 = random.randint(1,10)
    comptotal+= comp2
    print("The computer drew a",comp2)
    print("Computer total:",comptotal)
    time.sleep(1)
    while comptotal < final and comptotal <22:
        card3=random.randint(1,10)
        comptotal += card3
        print("Computer drew a",card3)
        print("Computer total:",comptotal)
        time.sleep(1)
    os.system('CLS')
    if comptotal > 21:
        print("You win!")
        print("You had",final,"The computer had",comptotal-card3)
    elif comptotal == final:
        print("The house always wins")
        print("You had",final,"The computer had",comptotal)
    else:
        print("You lose")
        print("You had",final,"The computer had",comptotal)

