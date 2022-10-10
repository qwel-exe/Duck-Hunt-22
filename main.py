"""
Main source file for the Duck Hunt Game
"""

# pylint: disable=wildcard-import, wrong-import-position, no-member, invalid-name, undefined-variable, unused-wildcard-import

from typing_extensions import Self
import pygame, sys ,os 


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

class Player(pygame.sprite.Sprite):
	def __init__(self, pos_x, pos_y):
		super().__init__()
		self.attack_animation = False
		self.sprites = []
		self.sprites.append(pygame.transform.scale(pygame.image.load('media/Dog/W1.png'),(160,160)))
		self.sprites.append(pygame.transform.scale(pygame.image.load('media/Dog/W2.png'),(160,160)))
		self.sprites.append(pygame.transform.scale(pygame.image.load('media/Dog/W3.png'),(160,160)))
		self.sprites.append(pygame.transform.scale(pygame.image.load('media/Dog/W4.png'),(160,160)))
		self.sprites.append(pygame.transform.scale(pygame.image.load('media/Dog/W5.png'),(160,160)))
		self.sprites.append(pygame.transform.scale(pygame.image.load('media/Dog/W5.png'),(160,160)))
		self.sprites.append(pygame.transform.scale(pygame.image.load('media/Dog/W1.png'),(160,160)))
		self.sprites.append(pygame.transform.scale(pygame.image.load('media/Dog/W2.png'),(160,160)))
		self.sprites.append(pygame.transform.scale(pygame.image.load('media/Dog/W3.png'),(160,160)))
		self.sprites.append(pygame.transform.scale(pygame.image.load('media/Dog/W4.png'),(160,160)))
		self.sprites.append(pygame.transform.scale(pygame.image.load('media/Dog/W5.png'),(160,160)))
		self.sprites.append(pygame.transform.scale(pygame.image.load('media/Dog/J1.png'),(160,160)))
		self.sprites.append(pygame.transform.scale(pygame.image.load('media/Dog/J2.png'),(160,160)))
		self.sprites.append(pygame.transform.scale(pygame.image.load('media/Dog/J3.png'),(160,160)))
		self.sprites.append(pygame.transform.scale(pygame.image.load('media/Dog/J3.png'),(160,160)))
		self.sprites.append(pygame.transform.scale(pygame.image.load('media/Dog/J3.png'),(160,160)))		
		self.current_sprite = 0
		self.image = self.sprites[self.current_sprite]

		self.rect = self.image.get_rect()
		self.rect.left, self.rect.top  = pos_x,pos_y

	def attack(self):
		self.attack_animation = True
		self.x = 1
		self.y = 350
		self.vel = 10
		self.walk_animation = True  

	def update(self,speed):
		if self.attack_animation == True:
			self.current_sprite += speed
			if int(self.current_sprite) >= len(self.sprites):
				self.current_sprite = 0
				self.attack_animation = False

		self.image = self.sprites[int(self.current_sprite)]  
  
  
	def Walk(self):
		if self.walk_animation == True:
			self.x += self.vel
		self.rect.left = self.x 
  
           

pic = Background('media/background.jpg', [0,0])
screen.blit(pygame.transform.scale(pic.image, (800, 600)), pic.rect)
# Creating the sprites and groups
moving_sprites = pygame.sprite.Group()
x = 350
y = 350
vel = 100
player = Player(x, y)
moving_sprites.add(player)



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
    
    
    player.attack()
    #player.Walk()
 	# Drawing
    moving_sprites.draw(screen)
    moving_sprites.update(0.20)
    pygame.display.flip()
    screen.blit(pic.image,(0,0))
    mainClock.tick(25)
    