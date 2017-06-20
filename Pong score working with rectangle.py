from graphics import *
import tkinter as tk
import random
import math
import time
import winsound
import pygame
import sys

pygame.init()

root = tk.Tk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
centreHoriz = screen_width/2
centreVert = screen_height/2
speed = 1
horizSpeed = speed
vertSpeed = speed
ballRadius = 10
player1Score = 0
player2Score = 0
#ballAngle = randInt(30,150)
score1Text = Text(Point((screen_width/2),50), "Player 1 : " + str(player1Score))
score2Text = Text(Point((screen_width/2),100), "Player 2 : " + str(player2Score))
score1Text.setTextColor('green')
score2Text.setTextColor('green')
win = GraphWin("Pong", screen_width, screen_height)
win.setBackground('black')
c = Circle(Point(centreHoriz,centreVert), ballRadius)
p1Paddle = Rectangle(Point(50,screen_height/2-250),Point(150,screen_height/2+250))
p1Paddle.setFill('green')
p1Paddle.draw(win)
p2Paddle = Rectangle(Point(screen_width-150,screen_height/2-250),Point(screen_width-50,screen_height/2+250))
p2Paddle.setFill('green')
p2Paddle.draw(win)
c.setFill('green')
c.setOutline('green')
c.draw(win)    
score1Text.setText("Player 1 : " + str(player1Score))
score1Text.draw(win)    
score2Text.setText("Player 2 : " + str(player2Score))
score2Text.draw(win)

while (player1Score != 10 or player2Score != 10):
    c.undraw()
    p1Paddle.undraw()
    p2Paddle.undraw()
    c = Circle(Point(centreHoriz,centreVert), ballRadius)
    c.setFill('green')
    c.draw(win)
    p1Paddle.draw(win)
    p2Paddle.draw(win)
    #c = Circle(Point(centreHoriz,centreVert), ballRadius)
    #p1Paddle = Rectangle(Point(50,screen_height/2-250),Point(150,screen_height/2+250))
    #p1Paddle.setFill('green')
    #p1Paddle.draw(win)
    #p2Paddle = Rectangle(Point(screen_width-150,screen_height/2-250),Point(screen_width-50,screen_height/2+250))
    #p2Paddle.setFill('green')
    #p2Paddle.draw(win)
    #c.setFill('green')
    #c.setOutline('green')
    #c.draw(win)    
    #score1Text.setText("Player 1 : " + str(player1Score))
    #score1Text.draw(win)    
    #score2Text.setText("Player 2 : " + str(player2Score))
    #score2Text.draw(win)
    #c.move(speed, speed)
    time.sleep(speed/1000)
    #c.undraw()
    #score1Text.undraw()
    #score2Text.undraw()
    #p1Paddle.undraw()
    #p2Paddle.undraw()
    centreHoriz = centreHoriz+ horizSpeed
    centreVert = centreVert+ vertSpeed
    #if (int(c.p1.X) >= int(p2Paddle.p1.X) and int(c.p1.getY) <= int(p2Paddle.p2.getY)) :
     #   if (c.p1.getY >= p2Paddle.p1.getY):
      #      horizSpeed = -horizSpeed
          
    if centreVert >= (screen_height - ballRadius - 100) or centreVert <= ballRadius:
        vertSpeed = -vertSpeed
        winsound.PlaySound('Ball bounce.wav',winsound.SND_FILENAME)
    if centreHoriz >= (screen_width - ballRadius):
        #horizSpeed = -horizSpeed
        winsound.PlaySound('Ball bounce.wav',winsound.SND_FILENAME)
        #ballAngle = randInt(30,150)
        #ballAngle = -ballAngle
        player2Score += 1
        score2Text.undraw()
        score2Text.setText("Player 2 : " + str(player2Score))
        score2Text.draw(win)
        centreHoriz = screen_width/2
        centreVert = screen_height/2
    if centreHoriz <= ballRadius:
        winsound.PlaySound('Ball bounce.wav',winsound.SND_FILENAME)
        player1Score += 1
        score1Text.undraw()
        score1Text.setText("Player 1 : " + str(player1Score))
        score1Text.draw(win)
        #ballAngle = ballAngle = randInt(30,150)
        centreHoriz = screen_width/2
        centreVert = screen_height/2
speed = 0
if player1Score >= 10:
    print ('Player 1 wins!')

if player2Score >=10:
    print ('Player 2 wins!')
    
