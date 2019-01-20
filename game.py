import pygame
import random
import time
import math
from ALIEN import *
from missile import *
from missi1 import *
from missII1 import *
pygame.init()
screen_width = 500
screen_height = 500
clock = pygame.time.Clock()
start=True
white = (255,255,255)
black=(0,0,0)
gameDisplay = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('THE GAME')
ship = pygame.image.load('ship.png')
alien = pygame.image.load('alien2.png')
alien2=pygame.image.load('alien3.png')
start_time=time.time()
score = 0
alienS=[]
MISSI=[]	
def DRAW(t):
	global start_time
	global score
	if((t-start_time)>=10):
		 start_time=t
		 x=random.randrange(0, screen_width-alien.get_width())
		 y=random.randrange(0,alien.get_height())
		 alienS.append(ALIEN(x,y,t,alien))
		 start_time=time.time()
	for i in range(len(alienS)):		
		if alienS[i] is not None:
			if time.time() >= alienS[i].end :
				alienS[i] = None					
			if alienS[i] is not None:
				gameDisplay.blit(alienS[i].name,(alienS[i].x,alienS[i].y))	
	for i in range(len(MISSI)):
		if MISSI[i] is not None: 
			if MISSI[i].y - MISSI[i].speed >0:
				MISSI[i].y -= MISSI[i].speed
			else:
				MISSI[i]=None
			if MISSI[i] is not None: 	
				pygame.draw.rect(gameDisplay,black, [MISSI[i].x,MISSI[i].y,MISSI[i].w,MISSI[i].h])
	for i in range(len(MISSI)):
		for j in range(len(alienS)):
			if alienS[j] is not None and MISSI[i] is not None:
				 if MISSI[i].y<=alienS[j].y+MISSI[i].h and MISSI[i].x >=alienS[j].x and MISSI[i].x+MISSI[i].w<=alienS[j].x+alienS[j].name.get_width():
						if MISSI[i].speed == 1:
							score += 1
							alienS[j] = None
						else:
							alienS[j].t=time.time()
							alienS[j].name=alien2
							alienS[j].end=time.time()+5


x = (screen_width * 0)
y = (screen_height * 0.9)

while  start:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			start = False

		if event.type==pygame.KEYDOWN:
			if event.key == pygame.K_a:
				if x - 20 >=0:
					x -= 20
			if event.key == pygame.K_d:
				if x + 20 + 40 < screen_width:
					x += 20
			if event.key == pygame.K_SPACE:
				MISSI.append(missi1(x+30,y))		
			if event.key == pygame.K_s:
				MISSI.append(missI1(x+30,y))	
			if event.key == pygame.K_q:
				start = False

	gameDisplay.fill(white)
	gameDisplay.blit(ship, (x,y))
	DRAW(time.time())		
	pygame.display.update()
	clock.tick(90)
print(score)
pygame.quit()
quit()