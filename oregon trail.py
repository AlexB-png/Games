import random
import os
from os import system
import time
robberhere=False
ox=3
food=20
family = 0
distance = 100
day=1
play2=0
visits =0
cooldown=0
print("THE OREGON TRAIL")
play=input("Ready to play? : ")
if play == "yes":
    play=="no"
    print("the game has begun")
    #time.sleep(2)
    os.system("CLS")
    print("You have family members, each eats 1 food a day")
    print("You have",ox,"each one pulls the wagon, you can kill an ox for 5 food, this option appears after you run out of food")
    print("You have",food,"food, each family member eats 1 food a day")
    #time.sleep(6)
    while play2 != "yes" :
        play2=input("Understand?")
    family = int(input("How many of your family should you bring?"))
    while family > 0 and ox >0:
        


        if family == 1 and cooldown ==0:
            if food > 7:
                event=12
            else:
                event=random.randint(1,14)
        elif family == 2 and cooldown ==0:
            if food >10:
                event=12
            else:
                event=random.randint(1,14)
        elif family == 3 and cooldown ==0:
            if food >15:
                event=12
            else:
                event=random.randint(1,14)
        elif family == 4 and cooldown ==0:
            if food > 24:
                event=12
            else:
                event=random.randint(1,14)
        elif family > 4 and cooldown ==0:
            if food> 30:
                event=12
            else:
                event=random.randint(1,14)
        else:
            event=random.randint(1,14)
        
        
        if event == 1:
            print("An ox is roaming the fields, you can bait it with food if you want (-3 food) or you can try to catch it but it seems risky (-1 family if failure) but you could (hunt) it for 3 food")
            choice=input("bait / risk / ignore / hunt")
            
            if choice == "bait":
                print("The ox approaches and joins your team. +1 Ox -3 food")
                ox += 1
                food -=3
            elif choice == "risk":
                risk=random.randint(1,2)
                if risk == 1:
                    print("The ox gets violent and one of you are killed, the ox gets away -1 family")
                    family -=1
                else:
                    print("You manage to catch the ox, what a relief")
                    ox +=1
            elif choice == "ignore":
                print("You figure it was best to leave the ox alone, time to carry on the trail")
            elif choice == "hunt":
                print("the ox was easily killed and harvested +3 food" )
                food += 3
            else:
                print("You stand there staring at the ox, it takes this as a sign of violence (-1 family)")
                family -=1
        
        elif event == 2:
            print("An ox is roaming the fields, you can bait it with food if you want (-3 food) or you can try to catch it but it seems risky (-1 family if failure) but you could (hunt) it for 3 food")
            choice=input("bait / risk / ignore / hunt")
            
            if choice == "bait":
                print("The ox approaches and joins your team. +1 Ox -3 food")
                ox += 1
                food -=3
            elif choice == "risk":
                risk=random.randint(1,2)
                if risk == 1:
                    print("The ox gets violent and one of you are killed, the ox gets away -1 family")
                    family -=1
                else:
                    print("You manage to catch the ox, what a relief")
                    ox +=1
            elif choice == "ignore":
                print("You figure it was best to leave the ox alone, time to carry on the trail")
            elif choice == "hunt":
                print("the ox was easily killed and harvested +3 food" )
                food += 3
            else:
                print("You stand there staring at the ox, it takes this as a sign of violence (-1 family)")
                family -=1
        
        elif event == 3:
            print("An ox is roaming the fields, you can bait it with food if you want (-3 food) or you can try to catch it but it seems risky (-1 family if failure) but you could (hunt) it for 3 food")
            choice=input("bait / risk / ignore")
            
            if choice == "bait":
                print("The ox approaches and joins your team. +1 Ox -3 food")
                ox += 1
                food -=3
            elif choice == "risk":
                risk=random.randint(1,2)
                if risk == 1:
                    print("The ox gets violent and one of you are killed, the ox gets away -1 family")
                    family -=1
                else:
                    print("You manage to catch the ox, what a relief")
                    ox +=1
            elif choice == "ignore":
                print("You figure it was best to leave the ox alone, time to carry on the trail")
            elif choice == "hunt":
                print("the ox was easily killed and harvested +3 food" )
                food += 3
            else:
                print("You stand there staring at the ox, it takes this as a sign of violence (-1 family)")
                family -=1
#EVENT 2#
        elif event == 4:
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
                    elif rob2 == "food":
                        print("They took the food and left...")
                        food -= 5
                    elif rob2 == "people":
                        print("They're gone...")
                        family -= 2
                    else:
                        print("We ignored them...they took some hostages (-2 people)")
                        family -=2
                else:
                    print("They gave us some food  +5 Food")
                    food+=5
            elif rob == "Ignore":
                print("It was best to leave them alone")
            elif rob =="Talk":
                print("We approach the traveller...he threatens us with weapons and tells us to get away. Good idea we didn't rob him")
            elif rob == "Trade":
                trade = random.randint(1,4)
                if trade == 1:
                    print("They have nothing to trade")
                elif trade == 2:
                    trade2=input("They offer 8 food for 1 ox")
                    if trade2 =="yes":
                        print("+8 food / -1 ox")
                        ox -=1 
                        food+=8
                    else:
                        print("We chose not to trade")
                elif trade == 3:
                    trade2=input("they offer 1 ox for 8 food")
                    if trade2 == "yes":
                        print("+1 ox / -8 food")
                        ox +=1 
                        food -= 8
                    else:
                        print("That was a bad trade anyway")
                else:
                    trade2=input("They offer to join your team for 5 food")
                    if trade2 == "yes":
                        print("The traveller joins your team! +1 family / -5 food")
                        food-=5
                        family+=1    
                    else:
                        print("We can't afford to feed another person") 
            else:
                print("they didn't seem to notice us")
        elif event == 5:
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
                    elif rob2 == "food":
                        print("They took the food and left...")
                        food -= 5
                    elif rob2 == "people":
                        print("They're gone...")
                        family -= 2
                    else:
                        print("We ignored them...they took some hostages (-2 people)")
                        family -=2
                else:
                    print("They gave us some food  +5 Food")
                    food+=5
            elif rob == "Ignore":
                print("It was best to leave them alone")
            elif rob =="Talk":
                print("We approach the traveller...he threatens us with weapons and tells us to get away. Good idea we didn't rob him")
            elif rob == "Trade":
                trade = random.randint(1,4)
                if trade == 1:
                    print("They have nothing to trade")
                elif trade == 2:
                    trade2=input("They offer 8 food for 1 ox")
                    if trade2 =="yes":
                        print("+8 food / -1 ox")
                        ox -=1 
                        food+=8
                    else:
                        print("We chose not to trade")
                elif trade == 3:
                    trade2=input("they offer 1 ox for 8 food")
                    if trade2 == "yes":
                        print("+1 ox / -8 food")
                        ox +=1 
                        food -= 8
                    else:
                        print("That was a bad trade anyway")
                else:
                    trade2=input("They offer to join your team for 5 food")
                    if trade2 == "yes":
                        print("The traveller joins your team! +1 family / -5 food")
                        food-=5
                        family+=1    
                    else:
                        print("We can't afford to feed another person")           
#EVENT 3#
        elif event == 6:
            print("Theres a person sat on the side of the road. We could help them? +1 family -2 food")
            save=input("save or die")
            if save == "save":
                print("They wake up and are thankful for the help +1 family / -2 food")
                family += 1
                food -= 2
                robber = random.randint(1,3)
                if robber == 1:
                    robberhere = True
                    
                    time.sleep(3)
                else:
                    pass
#EVENT 4#
        elif event == 7:
            print("Is that an earthquake out there? All our supplies will be ruined! We can only save one!")
            loss = input("family (-1) / food (-2) / ox (-1)")
            if loss=="family":
                print("some food fell off the shelf and an ox ran away  -2 food / -1 ox")
                food -= 2
                ox -=1
            elif loss =="food":
                print("A boulder rolled through.. (-1 family / -1 ox)")
                family -=1 
                ox -=1
            elif loss=="ox":
                print("Some food was destroyed and we have one unaccounted family member -2 food / -1 family")
                family -= 1
                food -= 2
            else:
                print("We chose to hide in the corner -1 food -1 family -1 ox")
                ox-=1
                family-=1
                food-=1
#EVENT 5#
        elif event == 8:
            print("WE'RE BEING RAIDED")
            bribe = input("food / ox / family or we could (fight) back   0-5 family lost")
            if bribe == "food":
                print("They gladly took some of our food -5 food")
                food -= 5
            elif bribe == "ox":
                print("They took some of our ox.. -2 ox")
                ox -=2
            elif bribe =="family":
                print("They're gone...")
            elif bribe =="fight":
                print("We will do our best")
                death = random.randint(0,5)
                if death >= family:
                    print("We lost..")
                    family = 0
                else:
                    family = family - death
                    print(death,"Family members died but we won")
            else:
                print("We couldn't make a choice in time, they took a bit of everything -1 family / -3 food / -1 ox")
                ox-=1
                food-=3
                family-=1
#EVENT 6#
        elif event == 9:
            present=True
            print("Theres a disease going round. We think its dysentery")
            diseased= random.randint(0,family-1)
            while present == True:
                if family > 0:
                    execution=int(input("How many people should we `leave behind`"))
                    if diseased >= family:
                        print("Everyone has been infected. This is the end")
                        family = 0
                    elif execution > family:
                        print("if you want your family dead that's fine")
                        family =0
                    elif diseased > execution:
                        print("i don't think that was everyone")
                        family -= execution
                        print(family,"members are left, more people have been infected")
                        diseased += 1
                    elif diseased==execution:
                        print("Thats everyone with dysentery removed")
                        present=False
                        family -= execution
                    elif execution > diseased:
                        print("That might've been too many.")
                        present=False
                        family -= execution
                else:
                    break

#EVENT 7#

        elif event ==10:
            print("Theres a house coming up. We could ask if they could help us? we have been there",visits,"times now")
            knock = input("ask / ignore")
            if knock == "ask":
                print("We knock on the door")
                for i in range(0,3):
                    print(".")
                    time.sleep(1)
                print("The door opens and a man is stood there, he asks us what we want?")
                ask = input("food / ox")
                
                if ask=="food":
                    chance=random.randint(0,3)
                    if chance==0:
                        print("he laughs at us and slams the door shut")
                        visits +=1
                    else:
                        if chance < visits:
                            os.system("CLS")
                            print("Haven't i seen you before? He recognises us...")
                            time.sleep(3)
                            print("He gets violent and attacks us. -1 family")
                            family -=1
                        else:
                            print("The man gives us",chance,"food")
                            food += chance
                            visits += 1
                elif ask=="ox":
                    print("The man looks angry, we all begin to run but he was faster. -1 family")
                    family -=1
                    visits +=1
#EVENT 8#
        elif event == 11:
            
            if family == 1:
                backpack=random.randint(1,5)
            elif family == 2:
                backpack=random.randint(2,7)
            elif family==3:
                backpack=random.randint(4,8)
            elif family ==4:
                backpack=random.randint(6,10)
            else:
                backpack=random.randint(6,12)
            print("There is a backpack on the road there is", backpack,"food inside")
            take=input("take or ignore? There could be expired food in there")
            if take == "take":
                if food < family:
                    expire=3
                else:
                    expire=random.randint(1,3)
                if expire == 1 or expire == 2:
                    print("The food was expired -1 family")
                    family -=1
                else:
                    print("The food was safe +",backpack,"food")
                    food += backpack
            else:
                print("We didn't know the condition of the food")
#EVENT 9#
        elif event == 12:
            print("There's someone knocking claiming to take from the rich and give to the poor")
            time.sleep(2)
            print("It's robin hood!")
            time.sleep(2)
            fight=input("should we (fight) back or let him in")
            if fight == "fight" and cooldown ==0:
                print("We'll try our best")
                death = random.randint(0,1)
                print("We lost",death,"family members, he won't be back for 3 days")
                family-=death
                cooldown=3
            else:
                if cooldown == 0:
                    if family == 1:
                        if food > 7:
                            food=7
                            print("We lost some food...")
                    elif family == 2:
                        if food >10:
                            food=10
                            print("We lost some food...")
                    elif family == 3:
                        if food >15:
                            food=15
                            print("We lost some food...")
                    elif family == 4:
                        if food > 24:
                            food=24
                            print("We lost some food...")
                    elif family > 4:
                        if food> 30:
                            food=30
                            print("We lost some food...")
                    else:
                        print("error")
                else:
                    print("When we opened the doors he recognised us and ran off")
#EVENT 10#
        elif event ==13:
            print("We're pretty sure one of our ox are sick. We could leave it behind?")
            leave = input("leave or ignore")
            if leave == "leave":
                print("It was for the best we let the ox run free -1 ox")
            else:
                print("We think the ox is fine")
                time.sleep(3)
                chance=random.randint(1,2)
                if chance == 1:
                    print("Turns out the ox was sick, we lost some progress +5 meters")
                    distance +=5
                else:
                    print("Turns out the ox was fine, in fact it seemed faster than usual -5 meters")
                    distance-=5
#EVENT 11#
        elif event ==14:
            print("Theres a salesman walking past us")
            print("He offers us 10 food for 1 person, seems a bit sketchy")
            trade=input("accept or deny")
            if trade == "accept":
                print("Seems a bit psychopathic but alright +10 food / -1 family")
                food += 10
                family -=10

                














        else:
            print("no")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        time.sleep(3)
        os.system("CLS")
        print("You have",family,"family members")
        print("You have",food,"food left")
        print("There are",ox,"ox left")
        time.sleep(3)
        if family > 0:    
            print("Your",family,"family members eat 1 food each")
            print("-",family,"food")
            food -= family
            print("You now have",food,"food left")
            
            
            while food <0 and family > 0 and ox > 0:
                print("You are out of food, there is only one option")
                debt=food * -1
                print(debt)
                execute = input("Execute the ox.")
                if execute == "yes":
                    food += 5
                    ox -= 1
                    os.system("CLS")
                else:
                    os.system("CLS")
                    print("You didn't choose to sacrifice the ox? I guess they mean more to you than your family")
                    time.sleep(2)
                    print(debt,"family members will die for your negligence")
                    family -= debt
                    time.sleep(1)
                    print("There are",family,"family members left")
                    food=0
            time.sleep(3)
            if ox != 0 and family > 0:
                day+=1
                os.system("CLS")
                print("You fall asleep for the night...")
                
                time.sleep(2)
                
                if robberhere==True:
                    print("The man we saved was a thief! We found him missing this morning. -1 family")
                    family -= 1
                    time.sleep(3)
                
                if distance <= 0:
                    print("You finally made it to the end!")
                    for i in range(0,1000000):
                        temp=input("")
                
                os.system("CLS")
                print("DAY",day)
                distance -= ox*2
                print("there is",distance,"m left")
                if cooldown > 0:
                    cooldown -=1
                    if cooldown == 0:
                        print("We found an arrow in our trailer...")
                        time.sleep(2)
                
            else:
                if ox <= 0:
                    print("You can't carry on with no ox")
                    print("There were",distance,"Meters left")
                elif people <= 0:
                    print("There were",distance,"Meters left")
                    print("There is nobody left...")

        else:
            print("There is nobody left...")
            print("There were",distance,"Meters left")
            










