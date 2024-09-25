import random
from random import randint
stats=["health","food","water","heat","stamina"]
health = 100
stats.append(health)
food = 100
stats.append(food)
water = 100 
stats.append(water)
heat = 100
stats.append(heat)
bleed = 0
oxygen = 1000
stamina = 100
stats.append(stamina)
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
climbingTrue = 0
endingTryAgain = False
player = {
    "health":100,
    "food":100,
    "water":100,
    "heat":100,
    "stamina":100
}
def betterInput(yes=None,no=None,Resting=False,Check=False):
    global stamina
    inputAnswer = False
    while inputAnswer == False:
        inputAnswer = input(": ")
        if inputAnswer == yes and Resting == True:
            inputAnswer = yes
            stamina = 100
            print(f"you rested and gained {stamina} stamina")
        elif inputAnswer == no and Resting == True:
            inputAnswer = no
            print("you did not rest")
        if inputAnswer == yes and Check == True:
            print(player)
        elif inputAnswer == no and Check == True:
            print("you did not check your stats")
        else:
            print("not good enough try again")
            inputAnswer = False     
    

def check():
    print("do you want to check your stats")
    betterInput("yes","no",False,True)
    
def bleeding():
    global bleed, health
    health -= bleed
def climbing(wallType):
    global stamina, climbingPoints, pointsClimed
    climbingWin = False
    if stamina > 0:
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
                    if pointsClimed == 100:
                        print("you did it")
                        climbingWin = True
                        return climbingWin

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
                if pointsClimed == 100:
                    print("you did it")
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
    else:
        print("you do not have enough stamina to climb the wall")
        Rest()
def Rest():
    global stamina,distanceWalked
    print("do you want to rest type yes or no")
    Answer = betterInput("yes","no",True)
def campfire(position):
    global playerPosition
    campfirePosition = position - playerPosition
    print(f"there is a campfire {campfirePosition} feet away")
    if playerPosition == campfirePosition:
        print("you are at the campfire")
    elif playerPosition < 0:
        campfirePosition *= -1
        print(f"there is a campfire at {abs(campfirePosition)} feet behind you")
def roomStart(position,RoomNumber):
    global playerPosition
    Startposition = position - playerPosition
    print(f"the start to the room is {Startposition} feet away")
    if playerPosition == position:
        print("you are at the Start of the room")
        print("do you want to go back to the last room type yes or no")
        answer = input(": ")
        if answer == "yes" and RoomNumber == 1:
            print("You cant go through this yet")
        if answer == "yes" and RoomNumber == 2:
            room(1,20,20,20,False,None,None,True,10,True,True,0,)
def roomExit(position):
    global playerPosition, answer
    exitPosition = position - playerPosition
    print(f"the exit to the room is {exitPosition} feet away")
    if playerPosition == position:
        print("you are now at the exit to the room")
        print("do you want to go through to the next room type yes or no")
        answer = input(": ").lower()
        if answer == "yes":
            room(2,40,40,0,True,30,1)
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
    elif stamina == 0 or stamina < 0:
        print("you did not have enough stamina to walk any more")
        Rest()
        playerPosition -= distanceWalked
        distanceWalked = 0 
    print(f"you walked {distanceWalked} feet and are now at {playerPosition}")
    print(f"you now have {stamina} stamina left")
def wall(positionOfWall,wallType):
    global stamina, playerPosition, climbingTrue
    wallDistanceToPlayer = positionOfWall - playerPosition
    if playerPosition > positionOfWall:
        playerPosition = positionOfWall
    if playerPosition == positionOfWall:
        print("you now stand at the wall")
        print("do you want to try to climb it")
        climbingTrue = input("yes or no ").lower()
        if climbingTrue == "yes":
            climbingWin = climbing(wallType)
            if climbingWin:
                ClimbingWinAgain = climbingWin
                playerPosition = positionOfWall + 1
                print(playerPosition)
                return climbingWin
            elif climbingWin and ClimbingWinAgain:
                playerPosition = positionOfWall - 1
                ClimbingWinAgain = False
                


       
    if playerPosition > positionOfWall:
        playerPosition = positionOfWall
        wallDistanceToPlayer = 0
            
    print(f"there is a wall {wallDistanceToPlayer} feet away from you")
        

    


def room(roomType, roomLength,exitPosition,playerPoint, hasWall=False,wallPosition=None,wallType=None, hasCampfire=False,campfirePosition=None,hasExit=True,HasStart=True,StartPosition=0):
    global stamina, heat, outsideHeat, inStartRoom, distanceWalked, playerPosition, distance, health, climbingTrue
    distance = roomLength
    playerPosition = playerPoint

    climbingWin = False
    while True:
        if hasWall:
            climbingWin = wall(wallPosition,wallType)
        if hasCampfire:
            campfire(campfirePosition)
        if hasExit:
            roomExit(exitPosition)
        if HasStart:
            roomStart(StartPosition,roomType)
        check()
        walking()




def dayPass():
    global bleed, health, oxygen, food, water, heat, stamina
    bleeding()
    print(f"you have {health} health {food} food {water} water {heat} heat {oxygen} oxygen {stamina} stamina")
    if bleed > 0:
        bleed -= 1
        print("you are bleeding")
    heat -= outsideHeat
def ending(Ending):
    global endingTryAgain
    if Ending == 1:
        print(f"you were found dead by the other climbers")
        print("and became a landmark for other people climbing the mountain")
    print(f"you had these stats at the end of you run")
    print(f"{health}health, {stamina}, stamina {food} food, {water} water, {heat} heat, {oxygen} oxygen")
    print("THE END")
    print("do you want to try again type yes or no")
    endingTryAgain = input(": ").lower()
    



    


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
            room(1, 20,20,10,False,None,None,True,10,)
        if answer == "b":
            print("you slept for the night and gained 20 stamina")
            stamina += 20
            dayPass()
            room(1, 20,20,10,False,None,None,True,10,)
    elif answer == "b":
        print("you walk for a whole day and pass out")
        ending(1)
while endingTryAgain == "yes":
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
                room(1, 20,20,10,False,None,None,True,10,)
            if answer == "b":
                print("you slept for the night and gained 20 stamina")
                stamina += 20
                dayPass()
                room(1, 20,20,10,False,None,None,True,10,)
        elif answer == "b":
            print("you walk for a whole day and pass out")
            ending(1)