import random
import time

food=100
day=0
prevbiochoice="forest"
biochoice=""
mosq=0

class Bio():
    name=['forest','taiga','steppe','desert','praire','jungle','marsh']
    def desc(self):
        desc_str="You have discovered the %s." % (self.name)
        return desc_str

class Eat():
    name=['small game','venison','buffalo','beef','chicken','pork','berries']
    fill=""
    def desc(self):
        global food
        desc_str="You ate some %s. The meal satiated you by %s points." % (self.name, self.fill)
        food=food+self.fill
        return desc_str
        return food

forest=Bio()
forest.name='forest'
taiga=Bio()
taiga.name='taiga'
steppe=Bio()
steppe.name='steppe'
desert=Bio()
desert.name='desert'
prairie=Bio()
prairie.name='prairie'
jungle=Bio()
jungle.name='jungle'
marsh=Bio()
marsh.name='marsh'

game=Eat()
game.name='small game'
game.fill=10
deer=Eat()
deer.name='venison'
deer.fill=25
bison=Eat()
bison.name='buffalo'
bison.fill=50
beef=Eat()
beef.name='beef'
beef.fill=35
chicken=Eat()
chicken.name='chicken'
chicken.fill=15
pork=Eat()
pork.name='pork'
pork.fill=10
berry=Eat()
berry.name='berries'
berry.fill=3

def Spawn():
    print("Being born...")
    time.sleep(1)
    print(forest.desc())
    prevbiochoice="forest"
    day=1
    return prevbiochoice
    return day

def HC():
    global food
    if(food > 100):
        food=100
    if(food < 1):
        food=0
    print("You are " + str(food) + "% full.")

def HDT():
    global food, day, mosq
    food=food-5
    day=day+1

    if(mosq>0):
        food=food-2
        mosq=mosq-1
        if(mosq<1):
            print("The mosquitoes have left you.")

    if(food<1):
        print("You have died from hunger.")
        Death()

def Death():
    print("You have survived " + str(day) + " days!")
    time.sleep(5)
    exit()

def MosqAtt():
    global mosq
    mosq=mosq+7

def ForestHunt():
    foodchance=random.randint(1,100)
    if(foodchance<=35):
        print("You found nothing to eat.")
        
    elif(36<=foodchance<=75):
        print(game.desc())
        
    elif(76<=foodchance<=100):
        deathchance=random.randint(1,100)
        
        if(deathchance<=15):
            print("You died from an accident with an aggressive buck.")
            Death()
            
        else:
            print(deer.desc())

def TaigaHunt():
    foodchance=random.randint(1,100)
    if(foodchance<=55):
        print("You found nothing to eat.")
        
    elif(56<=foodchance<=80):
        print(game.desc())
        
    elif(81<=foodchance<=90):
        deathchance=random.randint(1,100)
        
        if(deathchance<=15):
            print("You died from an accident with an aggressive buck.")
            Death()
        else:
            print(deer.desc())
            
    elif(91<=foodchance<=100):
        deathchance=random.randint(1,100)
        
        if(deathchance<=25):
            print("You died from an accident with an aggressive buffalo.")
            Death()
            
        else:
            print(bison.desc())

def SteppeHunt():
    foodchance=random.randint(1,100)
    if(foodchance<=35):
        print("You found nothing to eat.")
        
    elif(36<=foodchance<=55):
        print(game.desc())
        
    elif(56<=foodchance<=65):
        deathchance=random.randint(1,100)
        
        if(deathchance<=10):
            print("You died from an accident with an aggressive bull.")
            Death()
            
        else:
            print(beef.desc())

    elif(66<=foodchance<=75):
        print(pork.desc())

    elif(76<=foodchance<=90):
        print(chicken.desc())
            
    elif(91<=foodchance<=100):
        deathchance=random.randint(1,100)
        
        if(deathchance<=25):
            print("You died from an accident with an aggressive buffalo.")
            Death()
            
        else:
            print(bison.desc())

def DesertHunt():
    foodchance=random.randint(1,100)
    if(foodchance<=65):
        print("You found nothing to eat.")
        
    elif(66<=foodchance<=100):
        print(game.desc())

def MarshHunt():
    foodchance=random.randint(1,100)
    if(foodchance<=45):
        print("You found nothing to eat.")
        
    elif(46<=foodchance<=100):
        print(game.desc())
        
    mosqchance=random.randint(1,100)
    if(mosqchance<=65):
        print("You have been swarmed by mosquitoes!")
        MosqAtt()
        
def JungleHunt():
    foodchance=random.randint(1,100)
    if(foodchance<=30):
        print("You found nothing to eat.")
        
    elif(31<=foodchance<=70):
        print(game.desc())

    elif(71<=foodchance<=100):
        print(chicken.desc())
        
    mosqchance=random.randint(1,100)
    if(mosqchance<=10):
        print("You have been swarmed by mosquitoes!")
        MosqAtt()

def PrairieHunt():
    foodchance=random.randint(1,100)
    if(foodchance<=50):
        print("You found nothing to eat.")
        
    elif(51<=foodchance<=65):
        print(game.desc())

    elif(66<=foodchance<=80):
        print(pork.desc())

    elif(81<=foodchance<=100):
        deathchance=random.randint(1,100)
        
        if(deathchance<=10):
            print("You died from an accident with an aggressive bull.")
            Death()
            
        else:
            print(beef.desc())
        
    mosqchance=random.randint(1,100)
    if(mosqchance<=10):
        print("You have been swarmed by mosquitoes!")
        MosqAtt()

def Hunt():
    global biochoice
    print("Hunting...")
    time.sleep(1)
    print("You spent the day hunting in the "+ (biochoice) +".")
    if(biochoice=="forest"):
        ForestHunt()
    elif(biochoice=="taiga"):
        TaigaHunt()
    elif(biochoice=="steppe"):
        SteppeHunt()
    elif(biochoice=="desert"):
        DesertHunt()
    elif(biochoice=="prairie"):
        PrairieHunt()
    elif(biochoice=="jungle"):
        JungleHunt()
    elif(biochoice=="marsh"):
        MarshHunt()

def Loc():
    global prevbiochoice, biochoice
    print("Forest, Taiga, Steppe, Desert, Prairie, Jungle, and Marsh")
    biochoice=input("Where would you like to go? (type in lowercase letters): ")
    if(biochoice==prevbiochoice):
        print("You are already there.")
        Loc()

    elif(biochoice!=prevbiochoice):
        if(biochoice=="forest"):
            print(forest.desc())
            biochoice="forest"
            prevbiochoice="forest"
            HDT()
            HDT()
            HC()

        elif(biochoice=="taiga"):
            print(taiga.desc())
            biochoice="taiga"
            prevbiochoice="taiga"
            HDT()
            HDT()
            HC()

        elif(biochoice=="steppe"):
            print(steppe.desc())
            biochoice="steppe"
            prevbiochoice="steppe"
            HDT()
            HDT()
            HC()

        elif(biochoice=="desert"):
            print(desert.desc())
            biochoice="desert"
            prevbiochoice="desert"
            HDT()
            HDT()
            HC()

        elif(biochoice=="prairie"):
            print(prairie.desc())
            biochoice="prairie"
            prevbiochoice="prairie"
            HDT()
            HDT()
            HC()

        elif(biochoice=="jungle"):
            print(jungle.desc())
            biochoice="jungle"
            prevbiochoice="jungle"
            HDT()
            HDT()
            HC()

        elif(biochoice=="marsh"):
            print(marsh.desc())
            biochoice="marsh"
            prevbiochoice="marsh"
            HDT()
            HDT()
            HC()

        elif(biochoice=="n"):
            print("You have decided to stay where you are.")

        else:
            print("Invalid choice.")
            Loc()

    else:
        print("Invalid choice.")
        Loc()
    biochoice=prevbiochoice

    return prevbiochoice, biochoice

def Option():
    huntchoice=input("Would you like to hunt? Y/N: ")
    if(huntchoice=="Y"):
        Hunt()

    elif(huntchoice=="N"):
        print("You have decided not to hunt for today.")

        huntchoice=input("Would you like to gather berries? Y/N: ")
        if(huntchoice=="Y"):
            print("You spent the whole day looking for some berries.")
            foodchoice=random.randint(1,100)

            if(foodchoice<=50):
                deathchance=random.randint(1,100)
                if(deathchance<=1):
                    print("You have died from eating a poisonous berry.")
                    Death()

                if(2<=foodchoice<=4):
                    print("You ate a bad berry!")
                    food=food-2
                else:
                    print(berry.desc())
            else:
                print("You found nothing to eat.")
        elif(huntchoice=="N"):
            print("You have decided not to eat for today.")

        else:
            print("Invalid choice.")
            Option()

    else:
        print("Invalid choice.")
        Option()

    HDT()
    HC()
    Loc()
    Option()

Spawn()
HC()
Loc()
Option()
        
            
