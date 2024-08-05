# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 10:53:49 2024

@author: teodo
"""

# Example file showing a basic pygame "game loop"
import pygame
import math
import time

def ortogonal(list,index,Overwrite=None):
    if index==0:
        Point1=list[-1]
    elif index!=0:
        Point1=list[index-1]
    try:
        Point2=list[index+1]
    except IndexError:
        Point2=list[0]
    #print(Point1,Point2)
    #Make vector
    Xpart=Point2[0]-Point1[0]
    Ypart=Point2[1]-Point1[1]
    vector= [Xpart,Ypart]
    #print(vector)
    if Overwrite==None:
        ortogonal=[vector[1]*-1,vector[0]]
    elif Overwrite==True:
        ortogonal=[vector[1],vector[0]*-1]
    #print(ortogonal)
    return(ortogonal)


# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True


radius=100 #pixels
CenterPoint=(int(1280/2), int(720/2))

CirclePos=[]
for i in range(361):
    Angle = i
    Radian = math.radians(Angle)
    Vx=radius*math.cos(Radian)
    Vy=radius*math.sin(Radian)
    Xpoint=CenterPoint[0]+Vx
    Ypoint=CenterPoint[1]+Vy
    #print(Xpoint,Ypoint)
    CurrentPoint=(Xpoint,Ypoint)
    CirclePos.append(CurrentPoint)
CircleThickness=2

ortogonals=[]
for i in range(361):
    ortogonals.append(ortogonal(CirclePos,i))
    #print(i)
    #print(ortogonal(CirclePos,i))
#print(ortogonals)
BallSpeed=[-100,-100]
BallStartPos=[int(1280/2)+75, int(720/2)]
dt=0
BallPos=BallStartPos
BallRadius=10

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")
    
    #Physci
    BallPos[0]+=BallSpeed[0]*dt
    BallPos[1]+=BallSpeed[1]*dt
    pygame.draw.circle(screen,"purple",BallPos,BallRadius)
    #pygame.draw.line(screen,"black",BallPos,(BallPos[0]+BallSpeed[0]*radius,BallPos[1]+BallSpeed[1]*radius))
    
    
    
    # RENDER YOUR GAME HERE
    for point in CirclePos:
        #print(point)
        pygame.draw.circle(screen,"black",point,CircleThickness)


    for i in range(len(ortogonals)):
        #pygame.draw.circle(screen,"black",CirclePos[i],1)
        #pos2=(CirclePos[i][0]+ortogonals[i][0]*5,CirclePos[i][1]+ortogonals[i][1]*5)
        #pygame.draw.line(screen,"black",CirclePos[i],pos2)
        pass
        
    #Trigger
    Edge=CircleThickness+BallRadius
    distance = math.sqrt((BallPos[0]-CenterPoint[0])**2+(BallPos[1]-CenterPoint[1])**2)+Edge-1
    #print(distance)
    if distance >= radius:
        
        #print closest point
        #This is a really terrible way
        ClosestPoint=[99999,99999]
        ClosestDistance=radius**10
        for point in CirclePos:
            distance=math.sqrt((BallPos[0]-point[0])**2+(BallPos[1]-point[1])**2)
            if distance < ClosestDistance:
                ClosestDistance=distance
                ClosestPoint=point
        #print(ClosestPoint,ClosestDistance)
        pygame.draw.circle(screen,"red",ClosestPoint,3)
        #print(ClosestPoint)
        index=CirclePos.index(ClosestPoint)
        #print(ortogonals[index])
        BallSpeed[0]=BallSpeed[0]+ortogonals[index][0]
        BallSpeed[1]=BallSpeed[1]+ortogonals[index][1]
        print(math.sqrt(BallSpeed[0]**2+BallSpeed[1]**2))
        
            
    
    
    # flip() the display to put your work on screen
    pygame.display.flip()

    #clock.tick(60)  # limits FPS to 60
    dt = clock.tick(60) / 1000

pygame.quit()
