import pygame
pygame.init()



# Create a display

screen = pygame.display.set_mode((640,640))

background = pygame.image.load('Background.png')
ship = pygame.image.load('Ship.png')

class dimensions(object):
	def __init__(self,x,y,width,height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.vel = 2


def printScreen():
	screen.blit(background, (0, 0))
	screen.blit(ship, (shipStats.x, shipStats.y))
	pygame.display.update()


shipStats = dimensions(300,400,64,64)
run = True
while run:

	key = pygame.key.get_pressed()

	if key[pygame.K_LEFT]:
		shipStats.x -= shipStats.vel

	if key[pygame.K_RIGHT]:
		shipStats.x += shipStats.vel

	if key[pygame.K_UP]:
		shipStats.y -= shipStats.vel

	if key[pygame.K_DOWN]:
		shipStats.y += shipStats.vel


	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	printScreen()



pygame.quit()