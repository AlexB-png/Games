import random
import os
from os import system
import time
ox=3
food=20
family=4
day=1
play2=0
print("THE OREGON TRAIL")
play=input("Ready to play? : ")
if play == "yes":
    play=="no"
    print("the game has begun")
    #time.sleep(2)
    os.system("CLS")
    print("You have",family,"members, each eats 1 food a day")
    print("You have",ox,"each one pulls the wagon, you can kill an ox for 5 food, this option appears after you run out of food")
    print("You have",food,"food, each family member eats 1 food a day")
    #time.sleep(6)
    while play2 != "yes" :
        play2=input("Understand?")
    while family > 0 and ox >0:
        event=4
        #event = random.randint(1,20)# 
        
        
        if event == 1:
            print("An ox is roaming the fields, you can bait it with food if you want (-3 food) or you can try to catch it but it seems risky (-1 family if failure) but you could ignore it")
            choice=input("bait / risk / ignore")
            
            if choice == "bait":
                print("The ox approaches and joins your team. +1 Ox -3 food")
                ox += 1
                food -=3
            if choice == "risk":
                risk=random.randint(1,2)
                if risk == 1:
                    print("The ox gets violent and one of you are killed, the ox gets away -1 family")
                    family -=1
                else:
                    print("You manage to catch the ox, what a relief")
                    ox +=1
            if choice == "ignore":
                print("You figure it was best to leave the ox alone, time to carry on the trail")
            else:
                print("You stand there staring at the ox, it takes this as a sign of violence (-1 family)")
                family -=1
        
        if event == 2:
            print("An ox is roaming the fields, you can bait it with food if you want (-3 food) or you can try to catch it but it seems risky (-1 family if failure) but you could ignore it")
            choice=input("bait / risk / ignore")
            
            if choice == "bait":
                print("The ox approaches and joins your team. +1 Ox -3 food")
                ox += 1
                food -=3
            if choice == "risk":
                risk=random.randint(1,2)
                if risk == 1:
                    print("The ox gets violent and one of you are killed, the ox gets away -1 family")
                    family -=1
                else:
                    print("You manage to catch the ox, what a relief")
                    ox +=1
            if choice == "ignore":
                print("You figure it was best to leave the ox alone, time to carry on the trail")
            else:
                print("You stand there staring at the ox, it takes this as a sign of violence (-1 family)")
                family -=1
        
        if event == 3:
            print("An ox is roaming the fields, you can bait it with food if you want (-3 food) or you can try to catch it but it seems risky (-1 family if failure) but you could ignore it")
            choice=input("bait / risk / ignore")
            
            if choice == "bait":
                print("The ox approaches and joins your team. +1 Ox -3 food")
                ox += 1
                food -=3
            if choice == "risk":
                risk=random.randint(1,2)
                if risk == 1:
                    print("The ox gets violent and one of you are killed, the ox gets away -1 family")
                    family -=1
                else:
                    print("You manage to catch the ox, what a relief")
                    ox +=1
            if choice == "ignore":
                print("You figure it was best to leave the ox alone, time to carry on the trail")
            else:
                print("You stand there staring at the ox, it takes this as a sign of violence (-1 family)")
                family -=1
        
        if event == 4:
            print("Theres another traveller along the path. we could try to rob them?")
            rob=input("Rob (high risk but high reward) Ignore (Nothing) Talk (something could happen?) Trade (anything could happen)")
            
            if rob == "Rob":
                risk=random.randint(1,4)
                if risk == 1 or risk == 2 or risk == 3:
                    print("The traveller had weapons and now they're holding us hostage, how the tables have turned")
                    rob2=input("There are 3 options ... -2 people (people) / -5 food (food) / -1 ox (ox) ")
                    if rob2 == "ox":
                        print("The ox pulls their trailer now...")
                        ox -=1
                    if rob2 == "food":
                        print("They took the food and left...")
                        food -= 5
                    if rob2 == "people":
                        print("They're gone...")
                        family -= 2
                    else:
                        print("We ignored them...they took some hostages (-2 people)")
                        family -=2
            if rob == "ignore":
                print("It was best to leave them alone")
            if rob =="Talk":
                print("We approach the traveller...he threatens us with weapons and tells us to get away. Good idea we didn't rob him")
                                


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        time.sleep(3)
        os.system("CLS")
        print("You have",family,"family members")
        print("You have",food,"food left")
        print("There are",ox,"ox left")
        time.sleep(3)
        print("Your",family,"family members eat 1 food each")
        print("-",family,"food")
        food -= family
        while food <0 and family > 0:
            print("You are out of food, there is only one option")
            debt=food * -1
            execute = input("Execute the ox.")
            if execute == "yes":
                if ox >= 1:
                    ox -= 1
                    food +=5
                else:
                    print("You have no ox left, this is the end for you. It will be a miracle if you survive the STARVATION")
            else:
                print("You didn't choose to sacrifice the ox? I guess they mean more to you than your family")
                print(debt,"family members will die for your negligence")
                family -= debt
                print("There are",family,"family members left")
        time.sleep(3)
        day+=1
        os.system("CLS")
        print("You fall asleep for the night...")
        time.sleep(2)
        os.system("CLS")
        print("DAY",day)










