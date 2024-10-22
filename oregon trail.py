import random
import os
from os import system
import time
robberhere=False
ox=3
food=20
family=4
day=1
play2=0
visits =0
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
        event=10
        #event = random.randint(1,20)# 
        
        
        if event == 1:
            print("An ox is roaming the fields, you can bait it with food if you want (-3 food) or you can try to catch it but it seems risky (-1 family if failure) but you could ignore it")
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
            else:
                print("You stand there staring at the ox, it takes this as a sign of violence (-1 family)")
                family -=1
        
        elif event == 2:
            print("An ox is roaming the fields, you can bait it with food if you want (-3 food) or you can try to catch it but it seems risky (-1 family if failure) but you could ignore it")
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
            else:
                print("You stand there staring at the ox, it takes this as a sign of violence (-1 family)")
                family -=1
        
        elif event == 3:
            print("An ox is roaming the fields, you can bait it with food if you want (-3 food) or you can try to catch it but it seems risky (-1 family if failure) but you could ignore it")
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
                robber = 1
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
            diseased= random.randint(0,2)
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
            print("Theres a house coming up. We could ask if they could help us?")
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
            
            if robberhere==True:
                print("The man we saved was a thief! We found him missing this morning. -1 family")
                family -= 1
                time.sleep(3)
            
            
            os.system("CLS")
            print("DAY",day)
        else:
            print("There is nobody left...")










