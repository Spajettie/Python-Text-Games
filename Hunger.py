import random
import time

####Setup

#Class

class Biome():
    name=""
    danger=""
    def description(self):
        desc_str= "You have discovered the %s. They are %s dangerous." % (self.name, self.danger)
        return desc_str

class Eat():
    name=""
    eatfill=""
    def description(self):
        global food
        desc_str= "You ate some %s. It satiated you by %s points." % (self.name, self.eatfill)
        food=food+self.eatfill
        return desc_str

#End of Class
#biomes
                   
forest = Biome()
forest.name="woodlands"
forest.danger="not very"

savannah = Biome()
savannah.name="savannahs"
savannah.danger="somewhat"

desert = Biome()
desert.name="deserts"
desert.danger="very"

mountain = Biome()
mountain.name="taigas"
mountain.danger="worringly"

steppe = Biome()
steppe.name="steppes"
steppe.danger="somewhat"

marsh = Biome()
marsh.name="marshes"
marsh.danger="worringly"

rforest = Biome()
rforest.name="rainforests"
rforest.danger="very"

#food choices

game = Eat()
game.name="small game"
game.eatfill=10

deer = Eat()
deer.name="deer"
deer.eatfill=30

buffalo = Eat()
buffalo.name="buffalo"
buffalo.eatfill=65

cow = Eat()
cow.name="cow"
cow.eatfill=45

fish = Eat()
fish.name="fish"
fish.eatfill=10

goat = Eat()
goat.name="lamb"
goat.eatfill=20

camel = Eat()
camel.name="camel"
camel.eatfill=30

berry = Eat()
berry.name="berries"
berry.eatfill=3

#globals

global food, biomechoice, prevbiomechoice, day

prevbiomechoice=""

mosq=0

food=100

day=0

#Def

def Death():
    global day
    print("You have survived " + str(day) + " days! ")
    time.sleep(5)
    exit()

def HungerCheck():
    global food, day
    if (food > 100):
        food = 100
    if (food < 0):
        food = 0
    print("You are " + str(food) + "% full.")
    
    if((food)<1):
        print("You have died from hunger.")
        Death()

def Spawn():
    global prevbiomechoice, day
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("Being born...")
    time.sleep(1)
    spawn = forest
    print(forest.description())
    prevbiomechoice="forest"
    day=1

def MosquitoAtt():
    global mosq
    mosq=7

def HungerDayTax():
    global food, mosq, day
    food=food-5
    day=day+1
    
    if(mosq>0):
        food=food-2
        mosq=mosq-1

def Options():
    global biomechoice
    huntchoice=input("Would you like to hunt? Y/N: ")
    if(huntchoice=="Y"):
        print("Hunting...")
        
        if(biomechoice=="steppe"):
            print("You spent the whole day hunting in the steppes.")
            foodchoice=random.randint(1,100)
            
            if(foodchoice <= 5):
                deathchance=random.randint(1,100)
                if(deathchance <=20):
                    print("You have died from a bad accident with an aggressive buffalo.")
                    Death()

                else:   
                    print(buffalo.description())
                
            elif(6 <= foodchoice <= 10):
                deathchance=random.randint(1,100)
                if(deathchance <=15):
                    print("You have died from a bad accident with an aggressive bull.")
                    Death()

                else:   
                    print(cow.description())
                
            elif(11<= foodchoice <= 20):
                deathchance=random.randint(1,100)
                if(deathchance <=5):
                    print("You have died from a bad accident with an aggressive ram.")
                    Death()

                else:   
                    print(goat.description())
                
            elif(21 <= foodchoice <= 35):
                print(game.description())
                
            else:
                print("You found nothing to eat.")

        if(biomechoice=="forest"):
            print("You spent the whole day hunting in the woodlands.")
            foodchoice=random.randint(1,100)
            
            if(foodchoice <= 20):
                deathchance=random.randint(1,100)
                if(deathchance <=10):
                    print("You have died from a bad accident with an aggressive buck.")
                    Death()

                else:   
                    print(deer.description())
                
            elif(21 <= foodchoice <= 50):
                print(game.description())
                
            else:
                print("You found nothing to eat.")

        if(biomechoice=="desert"):
            print("You spent the whole day hunting in the deserts.")
            foodchoice=random.randint(1,100)
            
            if(foodchoice <= 20):
                deathchance=random.randint(1,100)
                if(deathchance <=10):
                    print("You have died from a bad accident with an aggressive camel.")
                    Death()

                else:   
                    print(camel.description())
                
            else:
                print("You found nothing to eat.")

        if(biomechoice=="savannah"):
            print("You spent the whole day hunting in the savannahs.")
            foodchoice=random.randint(1,100)
            
            if(foodchoice <= 20):
                deathchance=random.randint(1,100)
                if(deathchance <=20):
                    print("You have died from a bad accident with an aggressive buffalo.")
                    Death()

                else:   
                    print(buffalo.description())
                
            elif(21 <= foodchoice <= 40):
                print(game.description())
                
            else:
                print("You found nothing to eat.")

        if(biomechoice=="taiga"):
            print("You spent the whole day hunting in the taigas.")
            foodchoice=random.randint(1,100)
            
            if(foodchoice <= 20):
                deathchance=random.randint(1,100)
                if(deathchance <=5):
                    print("You have died from a bad accident with an aggressive ram.")
                    Death()

                else:   
                    print(goat.description())

            elif(21 <= foodchoice <= 30):
                print(game.description())

            else:
                print("You found nothing to eat.")

        if(biomechoice=="marsh"):
            print("You spent the whole day hunting in the marshes.")
            foodchoice=random.randint(1,100)
            
            if(foodchoice <= 30):
                print(fish.description())

            elif(31 <= foodchoice <= 45):
                print(game.description())

            else:
                print("You found nothing to eat.")

            mosquitochoice=random.randint(1,100)
            if(mosquitochoice <=60):
                print("You have been bitten by mosquitoes!")
                MosquitoAtt()

        if(biomechoice=="rforest"):
            print("You spent the whole day hunting in the rainforests.")
            foodchoice=random.randint(1,100)
            
            if(foodchoice <= 20):
                print(fish.description())

            elif(21 <= foodchoice <= 35):
                print(game.description())

            else:
                print("You found nothing to eat.")
                
    if(huntchoice=="N"):
        print("You have decided not to hunt for today.")

        huntchoice=input("Would you like to gather berries? Y/N: ")
        if(huntchoice=="Y"):
            print("You spent the whole day looking for some berries.")
            foodchoice=random.randint(1,100)
            
            if(foodchoice <= 50):
                deathchance=random.randint(1,100)
                if(deathchance <=2):
                    print("You have died from eating a bad berry.")
                    Death()

                else:   
                    print(berry.description())
            else:
                print("You found nothing to eat.")

        if(huntchoice=="N"):
            print("You have decided not to hunt for today.")
        
    HungerDayTax()
    HungerCheck()
    LocationC()
    Options()

def LocationC():
    global prevbiomechoice, biomechoice
    biomechoice=input("Where would you like to go? (Forest, Savannah, Desert, Taiga, Steppe, Marsh, Rainforest, N) ")
    if(biomechoice==prevbiomechoice):
        print("You are already there.")
        LocationC()
        
    elif(biomechoice=="forest"):
        print(forest.description())
        biomechoice="forest"
        prevbiomechoice="forest"
        HungerDayTax()
        HungerDayTax()
        HungerCheck()
        
    elif(biomechoice=="savannah"):
        print(savannah.description())
        prevbiomechoice="savannah"
        HungerDayTax()
        HungerDayTax()
        HungerCheck()
        
    elif(biomechoice=="desert"):
        print(desert.description())
        biomechoice="desert"
        prevbiomechoice="desert"
        HungerDayTax()
        HungerDayTax()
        HungerCheck()
        
    elif(biomechoice=="taiga"):
        print(mountain.description())
        biomechoice="taiga"
        prevbiomechoice="taiga"
        HungerDayTax()
        HungerDayTax()
        HungerCheck()

    elif(biomechoice=="steppe"):
        print(steppe.description())
        biomechoice="steppe"
        prevbiomechoice="steppe"
        HungerDayTax()
        HungerDayTax()
        HungerCheck()
        
    elif(biomechoice=="marsh"):
        print(marsh.description())
        biomechoice="marsh"
        prevbiomechoice="marsh"
        HungerDayTax()
        HungerDayTax()
        HungerCheck()
        
    elif(biomechoice=="rforest"):
        print(rforest.description())
        biomechoice="rforest"
        prevbiomechoice="rforest"
        HungerDayTax()
        HungerDayTax()
        HungerCheck()
        
    elif(biomechoice=="N"):
        biomechoice=prevbiomechoice
        print("You have decided to stay where you are.")

    else:
        print("Invalid choice.")
        LocationC()

#End of Def
####End of Setup
#Start Game

Spawn()

HungerCheck()

LocationC()

Options()


