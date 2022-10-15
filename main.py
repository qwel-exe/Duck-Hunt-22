"""
Main source file for the Duck Hunt Game
"""

# pylint: disable=wildcard-import, wrong-import-position, no-member, invalid-name, undefined-variable, unused-wildcard-import

import pygame, sys ,os 
from random import *


# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()
from pygame.locals import *

pygame.init()
pygame.display.set_caption('game base')
monitor_size = [pygame.display.Info().current_w, pygame.display.Info().current_h]
screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
fullscreen = False

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.base_image = pygame.image.load(image_file)
        self.image = pygame.transform.scale(self.base_image, (800,600))
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

class Dog(pygame.sprite.Sprite):
	def __init__(self, pos_x, pos_y):
		super().__init__()
		self.attack_animation = False
		self.sprites = []
		self.sprites.append(pygame.transform.scale(pygame.image.load('media/Dog/W1.png'),(160,160)).convert_alpha())
		self.sprites.append(pygame.transform.scale(pygame.image.load('media/Dog/W2.png'),(160,160)).convert_alpha())
		self.sprites.append(pygame.transform.scale(pygame.image.load('media/Dog/W3.png'),(160,160)).convert_alpha())
		self.sprites.append(pygame.transform.scale(pygame.image.load('media/Dog/W4.png'),(160,160)).convert_alpha())
		self.sprites.append(pygame.transform.scale(pygame.image.load('media/Dog/W5.png'),(160,160)).convert_alpha())
		self.sprites.append(pygame.transform.scale(pygame.image.load('media/Dog/W5.png'),(160,160)).convert_alpha())
		self.sprites.append(pygame.transform.scale(pygame.image.load('media/Dog/W1.png'),(160,160)).convert_alpha())
		self.sprites.append(pygame.transform.scale(pygame.image.load('media/Dog/W2.png'),(160,160)).convert_alpha())
		self.sprites.append(pygame.transform.scale(pygame.image.load('media/Dog/W3.png'),(160,160)).convert_alpha())
		self.sprites.append(pygame.transform.scale(pygame.image.load('media/Dog/W4.png'),(160,160)).convert_alpha())
		self.sprites.append(pygame.transform.scale(pygame.image.load('media/Dog/W5.png'),(160,160)).convert_alpha())
		self.sprites.append(pygame.transform.scale(pygame.image.load('media/Dog/J1.png'),(160,160)).convert_alpha())
		self.sprites.append(pygame.transform.scale(pygame.image.load('media/Dog/J2.png'),(160,160)).convert_alpha())
		self.sprites.append(pygame.transform.scale(pygame.image.load('media/Dog/J3.png'),(160,160)).convert_alpha())
		self.sprites.append(pygame.transform.scale(pygame.image.load('media/Dog/J3.png'),(160,160)).convert_alpha())
		self.sprites.append(pygame.transform.scale(pygame.image.load('media/Dog/J3.png'),(160,160)).convert_alpha())
		self.sprites.append(pygame.transform.scale(pygame.image.load('media/Dog/J3.png'),(160,160)).convert_alpha())
		self.sprites.append(pygame.transform.scale(pygame.image.load('media/Dog/J3.png'),(160,160)).convert_alpha())		
		self.current_sprite = 0
		self.image = self.sprites[self.current_sprite]

		self.rect = self.image.get_rect()
		self.rect.left, self.rect.top  = pos_x,pos_y


	def attack(self):
		self.attack_animation = True
		self.x = 1
		self.y = 350
		self.vel = 5
		self.walk_animation = 10

	def update(self,speed):
		if self.attack_animation == True:
			self.current_sprite += speed
			if int(self.current_sprite) >= len(self.sprites):
				self.current_sprite = 0
				self.attack_animation = False

		self.image = self.sprites[int(self.current_sprite)]  
  
  
	def Walk(self):
		if self.rect.x < 340 :
			self.rect.x += self.vel
		if self.rect.x == 340:
			self.rect.y -= 10
		if self.rect.y == 250:
			self.kill()
		mainClock.tick(40)   

class Duck(pygame.sprite.Sprite):
	def __init__(self,pos_x,pos_y):
		super().__init__()
		self.flyRight = []
		self.flyRight.append(pygame.transform.scale(pygame.image.load('media/Bird/Red/img1.png'),(100,100)).convert_alpha())
		self.flyRight.append(pygame.transform.scale(pygame.image.load('media/Bird/Red/img2.png'),(100,100)).convert_alpha())
		self.flyRight.append(pygame.transform.scale(pygame.image.load('media/Bird/Red/img3.png'),(100,100)).convert_alpha())
		self.flyStraightRight = []
		self.flyStraightRight.append(pygame.transform.scale(pygame.image.load('media/Bird/Red/img4.png'),(100,100)).convert_alpha())
		self.flyStraightRight.append(pygame.transform.scale(pygame.image.load('media/Bird/Red/img5.png'),(100,100)).convert_alpha())
		self.flyStraightRight.append(pygame.transform.scale(pygame.image.load('media/Bird/Red/img6.png'),(100,100)).convert_alpha())
  
		self.flyLeft = []
		self.flyLeft.append(pygame.transform.flip(pygame.transform.scale(pygame.image.load('media/Bird/Red/img1.png'),(100,100)).convert_alpha() ,True, False))
		self.flyLeft.append(pygame.transform.flip(pygame.transform.scale(pygame.image.load('media/Bird/Red/img2.png'),(100,100)).convert_alpha() ,True, False))
		self.flyLeft.append(pygame.transform.flip(pygame.transform.scale(pygame.image.load('media/Bird/Red/img3.png'),(100,100)).convert_alpha() ,True, False))
		self.flyStraightLeft = []
		self.flyStraightLeft.append(pygame.transform.flip(pygame.transform.scale(pygame.image.load('media/Bird/Red/img4.png'),(100,100)).convert_alpha() ,True, False))
		self.flyStraightLeft.append(pygame.transform.flip(pygame.transform.scale(pygame.image.load('media/Bird/Red/img5.png'),(100,100)).convert_alpha() ,True, False))
		self.flyStraightLeft.append(pygame.transform.flip(pygame.transform.scale(pygame.image.load('media/Bird/Red/img6.png'),(100,100)).convert_alpha() ,True, False))


		self.die =[]
		self.die.append(pygame.transform.scale(pygame.image.load('media/Bird/Red/img10.png'),(100,100)).convert_alpha())
		self.die.append(pygame.transform.scale(pygame.image.load('media/Bird/Red/img11.png'),(100,100)).convert_alpha())
		self.die.append(pygame.transform.flip(pygame.transform.scale(pygame.image.load('media/Bird/Red/img11.png'),(100,100)).convert_alpha() ,True, False))
        # Direction Constants
		self.RIGHT = 1
		self.LEFT = 2
		self.directionCount=0
        
        # Duck Variables
		self.alive = True
		self.direction = randint(1, 2)
		self.straight = False # True if duck is flying straight
  
        # Animation Frames
		self.frames = [self.flyRight, self.flyStraightRight, self.flyLeft, self.flyStraightLeft, self.die]
		self.current_duck = 0
		self.duck = self.frames[self.current_duck]
		self.current_sprite = 0
		self.image = self.duck[self.current_sprite]
  
  

		self.rect = self.image.get_rect()
		self.rect.left, self.rect.top  = pos_x,pos_y

	def change_direction(self):
		""" Decide to change duck's direction """
		randomNum = randint(1, 350)
		
		if randomNum % 5 == 0:
			self.straight = not self.straight
			# Switch the duck's direction
			if self.direction == self.RIGHT:
				self.direction = self.LEFT
				self.dx = -.5
				
			else:
				self.direction = self.RIGHT
				self.dx = .5

	def fly(self):
		self.fly_animation = True
  
	def update(self,speed):
		if self.fly_animation == True:
			self.current_sprite += speed
			if int(self.current_sprite) >= len(self.duck):
				self.current_sprite = 0
				self.fly_animation = False
		self.image = self.duck[int(self.current_sprite)]  
  


  
class RoundStart(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.round = 1
		pygame.font.init()
		self.font = pygame.font.Font("media/arcadeclassic.ttf",32)
		self.round_text = self.font.render("Round   "+ str(self.round),True,(255,255,255))

	def start(self):
		dog.attack()
		duck.fly()
		dog.Walk()
		screen.blit(self.round_text,(10,10))
		self.round =+1    
			
pic = Background('media/background.jpg', [0,0])
screen.blit(pygame.transform.scale(pic.image, (800, 600)), pic.rect)
# Creating the sprites and groups
moving_sprites = pygame.sprite.Group()
x = 0
y = 350
vel = 100
rand= randint(0,650)
dog = Dog(x, y)
duck = Duck(rand,350)
moving_sprites.add(dog)
moving_sprites.add(duck)

while True:    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == VIDEORESIZE:
            pic.image = pygame.transform.scale(pic.base_image, event.size)
            screen=pygame.display.set_mode(event.dict['size'],HWSURFACE|DOUBLEBUF|RESIZABLE)
            pic.rect.size = event.size
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_f:
                fullscreen = not fullscreen
                if fullscreen:
                    screen = pygame.display.set_mode(monitor_size, pygame.FULLSCREEN)
                else:
                    screen = pygame.display.set_mode((screen.get_width(), screen.get_height()), pygame.RESIZABLE)
    
    roundstart= RoundStart()
    roundstart.start()
 	# Drawing
    moving_sprites.draw(screen)
    moving_sprites.update(0.20)
    pygame.display.flip()
    screen.blit(pic.image,(0,0))
    mainClock.tick(25)
    