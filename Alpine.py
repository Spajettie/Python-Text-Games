import random
import time
import sys
i=0
class Area():
    name=""
    safe=""
    loot=""
    def desc(self):
        desc_str="%s | %s | %s loot" % (self.name, self.safe, self.loot)
        return desc_str
        

def quitgame():
    inp=input("Are you sure you would like to quit? Your progress will not be saved! Input: ")
    if(inp=="yes"):
        print("Quitting game...")
        exit
    if(inp=="no"):
        print("Resuming game...")

home=Area()
home.name="Home"
home.safe=100
home.loot="No"

summit=Area()
summit.name="Summit"
summit.safe=100
summit.loot="No"

shore=Area()
shore.name="Shore"
shore.safe=60
shore.loot="Some"

dropzone=Area()
dropzone.name="Dropzone"
dropzone.safe=70
dropzone.loot="Moderate"

deadforest=Area()
deadforest.name="Dead Forest"
deadforest.safe=35
deadforest.loot="Abundant"

garden=Area()
garden.name="Garden"
garden.safe=70
garden.loot="Some"

cave=Area()
cave.name="Cave"
cave.safe=15
cave.loot="Legendary"
