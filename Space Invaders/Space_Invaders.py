import pygame
pygame.init()



# Create a display

screenWidth = 640
screen = pygame.display.set_mode((screenWidth,screenWidth))
pygame.display.set_caption('Space Invaders')

background = pygame.image.load('Background.png')
ship = pygame.image.load('Ship.png')

class dimensions():
	def __init__(self,x,y,width,height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.speed = 2

class shots():
	def __init__(self,x,y,radius,color):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.color = color
		self.speed = 10

	def draw(screen):
		pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))


def printScreen():
	screen.blit(background, (0, 0))
	screen.blit(ship, (shipStats.x, shipStats.y))
	pygame.display.update()


shipStats = dimensions(300,400,128,128)
projectiles = []
run = True
while run:


	key = pygame.key.get_pressed()

	if key[pygame.K_LEFT] and shipStats.x > shipStats.speed:
		shipStats.x -= shipStats.speed

	if key[pygame.K_RIGHT] and shipStats.x < screenWidth - shipStats.width - shipStats.speed:
		shipStats.x += shipStats.speed

	if key[pygame.K_UP] and shipStats.y > shipStats.speed:
		shipStats.y -= shipStats.speed

	if key[pygame.K_DOWN] and shipStats.y < screenWidth - shipStats.height - shipStats.speed:
		shipStats.y += shipStats.speed


	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	printScreen()



pygame.quit()