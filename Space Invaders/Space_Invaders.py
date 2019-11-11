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

class projectile(object):
	def __init__(self,x,y,radius,color,speed):
		self.x = x
		self.y = y
		self.radius = radius
		self.color = color
		self.speed = 3

	def draw(self,screen):
		pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

def printScreen():
	screen.blit(background, (0, 0))
	screen.blit(ship, (shipStats.x, shipStats.y))
	for bullet in bullets:
		bullet.draw(screen)
	pygame.display.update()

shipStats = dimensions(300,400,128,128)
bullets = []
run = True
while run:

	for bullet in bullets:
		if bullet.y < 700 and bullet.y > 0:
			bullet.y -= bullet.speed
		else:
			bullets.pop(bullets.index(bullet))

	key = pygame.key.get_pressed()

	if key[pygame.K_SPACE]:
		if len(bullets) < 5:
			bullets.append(projectile(round(shipStats.x + shipStats.width //2), round(shipStats.y + shipStats.height //2), 6, (255,0,0), 10))

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