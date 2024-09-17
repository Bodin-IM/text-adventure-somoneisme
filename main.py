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
climbingPoints = random.randint(1,2)
pointsClimed = 0
walkingSpeed = 0
inStartRoom = True
distanceWalked = 0
playerPosition = 0
distance = 0
landmarkPosition = 0
answer = 0
    
    
def bleeding():
    global bleed, health
    health -= bleed

def climbing(wallType):
    global stamina, climbingPoints, pointsClimed
    print("you started to climb the wall")
    if wallType == 1:
        while pointsClimed < 30:
                climbingPoints = randint(1,2)
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
        while pointsClimed < 50:
            climbingPoints = randint(1,2)
            pointToClimb = input("type one or two to pick wich rock you want to climb on. and type down if you want to go down ")
            pointToClimb = int(pointToClimb)
            if pointToClimb == climbingPoints:
                print("you moved up")
                pointsClimed += 10
            else:
                pointsClimed += 10
                print("you failed")
                break
    if wallType == 3:
        while pointsClimed < 100:
            pointToClimb = input("type one or two to pick wich rock you want to climb on. and type down if you want to go down ")
            climbingPoints = randint(1,2)
            pointToClimb = int(pointToClimb)
            if pointToClimb == climbingPoints:
                print("you moved up")
                pointsClimed += 10
            else:
                pointsClimed += 10
                print("you failed")
                break
            if pointsClimed == 100:
                print("you did it")
    stamina -= pointsClimed
def campfire(position):
    global playerPosition
    campfirePosition = position - playerPosition
    print(f"there is a campfire {campfirePosition} feet away")
    if playerPosition == campfirePosition:
        print("you are at the campfire")
    elif playerPosition < 0:
        campfirePosition *= -1
        print(f"there is a campfire at {abs(campfirePosition)} feet behind you")
def roomExit(position):
    global playerPosition, answer
    exitPosition = position - playerPosition
    print(f"the exit to the room is {exitPosition} feet away")
    if playerPosition == position:
        print("you are now at the exit to the room")
        print("do you want to go through tpye yes or no")
        answer = input(": ").lower()
        if answer == "yes":
            room(2)
    elif answer == "no":
        room(1)
def walking():
    global stamina, playerPosition, distanceWalked
    distanceWalked = input(f"the room is {distance} feet long you are at {playerPosition} feet through how far do you want to walk ")
    distanceWalked = int(distanceWalked)
    stamina -= distanceWalked
    playerPosition += distanceWalked
    if playerPosition > distance:
            playerPosition = distance
    print(f"you walked {distanceWalked} feet and are now at {playerPosition}")
    print(f"you now have {stamina} stamina left")
def wall(position):
    global stamina, playerPosition
    wallposition = playerPosition - position
    print(f"there is a wall {wallposition} feet away from you")

    


def room(roomType):
    global stamina, heat, outsideHeat, inStartRoom, distanceWalked, playerPosition, distance, health 
    while roomType == 1:
        distance = 20
        walking()

        campfire(10)
        roomExit(position=20)
        if answer =="yes":
            break
    if roomType == 2:
        playerPosition = 0    
        while roomType == 2:
            distance = 40
            walking()
            wall(30)


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
            room(1)
        if answer == "b":
            print("you slept for the night and gained 20 stamina")
            stamina += 20
            dayPass()
            room(1)
    elif answer == "b":
        print("you walk for a whole day and pass out")
        dayPass()