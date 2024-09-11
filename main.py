import random
from random import randint
health = 100
food = 100
water = 100 
heat = 100
bleed = 0
oxygen = 1000
stamina = 100
outsideHeat = random.randint(1,100)
climbingPoints = randint(1,2)
print(climbingPoints)
pointsClimed = 0



def bleeding():
    global bleed, health
    health -= bleed

def climbing(wallType):
    global stamina, climbingPoints, pointsClimed
    print("you started to climb the wall")
    if wallType == 1:
        pointToClimb = input("type one or two to pick wich rock you want to climb on. and type down if you want to go down ")
        pointToClimb = int(pointToClimb)
        if pointToClimb == climbingPoints:
            print("you moved up")
            pointsClimed += 10
        else:
            pointsClimed += 10
            print("you failed")
        while pointsClimed < 30:
                climbingPoints == randint(1,2)
                pointToClimb = input("type one or two to pick wich rock you want to climb on. and type down if you want to go down ")
                pointToClimb = int(pointToClimb)
                if pointToClimb == climbingPoints:
                    print("you moved up")
                    pointsClimed += 10
                else:
                    pointsClimed += 10
                    print("you failed")
                    break
    if wallType == 2:
        pointToClimb = input("type one or two to pick wich rock you want to climb on. and type down if you want to go down ")
        pointToClimb = int(pointToClimb)
        if pointToClimb == climbingPoints:
            print("you moved up")
            pointsClimed += 10
        else:
            pointsClimed += 10
            print("you failed")
        while pointsClimed < 50:
            pointToClimb = input("type one or two to pick wich rock you want to climb on. and type down if you want to go down ")
            pointToClimb = int(pointToClimb)
            if pointToClimb == climbingPoints:
                print("you moved up")
                pointsClimed += 10
            else:
                pointsClimed += 10
                print("you failed")
    if wallType == 3:
        while pointsClimed < 100:
            pointToClimb = input("type one or two to pick wich rock you want to climb on. and type down if you want to go down ")
            pointToClimb = int(pointToClimb)
            if pointToClimb == climbingPoints:
                print("you moved up")
                pointsClimed += 10
                climbingPoints == randint(1,2)
            else:
                pointsClimed += 10
                print("you failed")
                break
            if pointsClimed == 100:
                print("you did it")
    stamina -= pointsClimed

def wall():
    print("yes")
    
    
    
def dayPass():

    global bleed, health, oxygen, food, water, heat, stamina
    bleeding()
    print(f"you have {health} health {food} food {water} water {heat} heat {oxygen} oxygen {stamina} stamina")
    if bleed > 0:
        bleed -= 1
        print("you are bleeding")
    heat -= outsideHeat
     


    


print("you are lost on a snowy mountain after falling off a cliff")
print("its cold dark and your wet from the snow")
print("the other climbers think you are dead so theres no one coming to help you")
print("from what you see in the surrounding area you have a two choises")
print("a try to climb back up the way you came")
print("b go up another way")
answer = input().lower()
if answer == "a":
    print("you now stand before a large cliff the same one you fell down moments ago you have decided to try to climb back up")
    print("you attemt to climb up you have no gear so this wont be easy but it might be possible")
    print("you start the climb")
    climbing(3)
if answer == "b":
    print("you find yourself climbing a new part of the mountain wich you have never climed before")
    print("after climbing a while you find a cave")
    print("yet again you find yourself with two options")
    print("a stay a night in the cave")
    print("b keep going up")
    answer = input("")
    if answer == "a":   
        print("you decided to stay in the cave for the night")
        print("you can now choose if you want to")
        print("a try too set up a campfire for warmth")
        print("b try too get some rest")
        answer = input("")
        if answer == "a":
            print("you found some wood and set up a campfire")
            print("you gained 20 warmth")
            heat += 20
            dayPass()
        if answer == "b":
            print("you slept for the night and gained 20 stamina")
            stamina += 20
            dayPass()
    if answer == "b":
        print("you walk for a whole day and pass out")
        dayPass()