from random import randint
from time import sleep

from pygame import init, event, display, image, Surface
import pygame
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    K_r, 
    K_f,
    KEYDOWN,
    KEYUP,
    QUIT,
)

init()
w, h = 640, 480
root = display.set_mode((w, h))
display.set_caption("The fall of Rome")
back = background()
hr = hero(w / 2, h / 2)
hr.draw()
en = enemy()
attacked = False
running = True
l, r, u, d = False, False, False, False
speeds = [0.1, 0.05]
speedNow = 0

score = 101

class background():
	global root
	Path = "map.png"
	def __init__(self):
		pass
	def redraw(self):
		global root
		root.blit(image.load(self.Path), (0, 0))
class enemy():
	global root
	att = "attack.png"
	batSet = "battle.png"
	def attack(self):
		global root, w, h
		root.blit(image.load(self.att), (w//2, 0))
	def newBattle(self):
		global root, w, h
		root.blit(image.load(self.batSet), (w//2, 0))
class hero():
	global root
	x, y, size = 0, 0, 3;
	def __init__(self, x_, y_):
		self.x, self.y = x_, y_
	def draw(self):
		global root
		pygame.draw.circle(root, (0, 0, 0), (self.x, self.y), self.size, 1)

def screenText(text, color):
	global root
	font = pygame.font.SysFont(None, 30)
	img = font.render(text, True, color)
	root.blit(img, (20, 20))
	display.flip()

def battle():
	global w, h, root, back, hr, en, attacked, running, l, r, u, d, speeds, speedNow, score
	battle = True

	while battle:
		for e in event.get():
			if e.type == QUIT:
				battle = False
			if e.type == KEYDOWN:
				if e.key == K_LEFT:
	    			#LEFT
	    			l = True
	    		if e.key == K_RIGHT:
	    			#Right
	    			r = True
	    		if e.key == K_UP:
	    			#UP
	    			u = True
	    		if e.key == K_DOWN:
	    			#DOWN
	    			d = True
	    	if e.type == KEYUP:
	    		if e.key == K_LEFT:
	    			#LEFT
	    			l = False
	    		if e.key == K_RIGHT:
	    			#Right
	    			r = False
	    		if e.key == K_UP:
	    			#UP
	    			u = False
	    		if e.key == K_DOWN:
	    			#DOWN
	    			d = False
	    		if e.key == K_r:
	    			score -= 50
	    			attacked = 0
	    		if e.key == K_f:
	    			pass
	    if root.get_at((int(hr.x), int(hr.y))) == root.get_at((1, 1)):
	    	speedNow = 1
	    else:
	    	speedNow = 0
	    if l:
	    	hr.x -= 1
	    if r:
	    	hr.x += 1
	    if u:
	    	hr.y -= 1
	    if d:
	    	hr.y += 1
	    back.redraw()
	    hr.draw()
	    if (randint(0, 100) == 0) and (attacked == 0):
	    	en.attack()
	    	attacked = 1
	    if attacked:
	    	attacked += 1
	    	#score -= 1
	    	en.attack()
	    	if attacked == 200:
		   		attacked = 0
		   		score -= 100	
	    if score > 0:
	    	screenText("SCORE : " + str(score), "BLUE")
	    display.flip()
	    sleep(speeds[speedNow])
	    if (score <= 0):
	        screenText("Sorry, you score is less than 0", "RED")
	        sleep(4)
	        break

def start():
	global w, h, root, back, hr, en, attacked, running, l, r, u, d, speeds, speedNow, score

	while running:
	    for e in event.get():
	    	if e.type == QUIT:
	    		running = False
	    	if e.type == KEYDOWN:
	    		if e.key == K_LEFT:
	    			#LEFT
	    			l = True
	    		if e.key == K_RIGHT:
	    			#Right
	    			r = True
	    		if e.key == K_UP:
	    			#UP
	    			u = True
	    		if e.key == K_DOWN:
	    			#DOWN
	    			d = True
	    	if e.type == KEYUP:
	    		if e.key == K_LEFT:
	    			#LEFT
	    			l = False
	    		if e.key == K_RIGHT:
	    			#Right
	    			r = False
	    		if e.key == K_UP:
	    			#UP
	    			u = False
	    		if e.key == K_DOWN:
	    			#DOWN
	    			d = False
	    		if e.key == K_r:
		    		if attacked:
		    			score -= 50
		    			attacked = 0
	    		if e.key == K_f:
	    			attacked =  0
	    			battle()
	    if root.get_at((int(hr.x), int(hr.y))) == root.get_at((1, 1)):
	    	speedNow = 1
	    else:
	    	speedNow = 0
	    if l:
	    	hr.x -= 1
	    if r:
	    	hr.x += 1
	    if u:
	    	hr.y -= 1
	    if d:
	    	hr.y += 1
	    back.redraw()
	    hr.draw()
	    if (randint(0, 100) == 0) and (attacked == 0):
	    	en.attack()
	    	attacked = 1
	    if attacked:
	    	attacked += 1
	    	#score -= 1
	    	en.attack()
	    	if attacked == 200:
		   		attacked = 0
		   		score -= 100	
	    if score > 0:
	    	screenText("SCORE : " + str(score), "BLUE")
	    display.flip()
	    sleep(speeds[speedNow])
	    if (score <= 0):
	        screenText("Sorry, you score is less than 0", "RED")
	        sleep(4)
	        break

	 #quit()

def new_game():
	global root
	font1 = pygame.font.SysFont(None, 24)
	font = pygame.font.SysFont(None, 40)
	img = font.render('''They are comming or the fall of Rome''', True, "RED")
	img1 = font1.render('''You need to capture Rome. And now play!''', True, "BLUE")
	root.blit(img, (20, 20))
	root.blit(img1, (20, 60))
	display.flip()
	global start
	sleep(5)
	start()

new_game()