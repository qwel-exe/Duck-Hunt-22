import pygame, sys

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
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

class Player(pygame.sprite.Sprite):
	def __init__(self, pos_x, pos_y):
		super().__init__()
		self.attack_animation = False
		self.sprites = []
		self.sprites.append(pygame.image.load('media/Dog/img1.png'))
		self.sprites.append(pygame.image.load('media/Dog/img2.png'))
		self.sprites.append(pygame.image.load('media/Dog/img3.png'))
		self.sprites.append(pygame.image.load('media/Dog/img4.png'))
		self.sprites.append(pygame.image.load('media/Dog/img5.png'))
		self.sprites.append(pygame.image.load('media/Dog/img1.png'))
		self.sprites.append(pygame.image.load('media/Dog/img2.png'))
		self.sprites.append(pygame.image.load('media/Dog/img3.png'))
		self.sprites.append(pygame.image.load('media/Dog/img4.png'))
		self.sprites.append(pygame.image.load('media/Dog/img5.png'))
		self.sprites.append(pygame.image.load('media/Dog/img6.png'))
		self.sprites.append(pygame.image.load('media/Dog/img6.png'))
		self.sprites.append(pygame.image.load('media/Dog/img6.png'))
		self.sprites.append(pygame.image.load('media/Dog/img7.png'))
		self.sprites.append(pygame.image.load('media/Dog/img8.png'))   
		self.current_sprite = 0
		self.image = self.sprites[self.current_sprite]

		self.rect = self.image.get_rect()
		self.rect.left, self.rect.top  = [pos_x,pos_y]

	def attack(self):
		self.attack_animation = True

	def update(self,speed):
		if self.attack_animation == True:
			self.current_sprite += speed
			if int(self.current_sprite) >= len(self.sprites):
				self.current_sprite = 0
				self.attack_animation = False

		self.image = self.sprites[int(self.current_sprite)]



pic = Background('media/background.jpg', [0,0])
screen.blit(pygame.transform.scale(pic.image, (800, 600)), pic.rect)
# Creating the sprites and groups
moving_sprites = pygame.sprite.Group()
player = Player(100,100)
moving_sprites.add(player)



while True:    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == VIDEORESIZE:
            screen=pygame.display.set_mode(event.dict['size'],HWSURFACE|DOUBLEBUF|RESIZABLE)
            screen.blit(pygame.transform.scale(pic.image,event.dict['size']),(0,0))
            pygame.display.flip()
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
 	# Drawing
    moving_sprites.draw(screen)
    moving_sprites.update(0.25)
    pygame.display.flip()
    mainClock.tick(25)
    player.attack()
    