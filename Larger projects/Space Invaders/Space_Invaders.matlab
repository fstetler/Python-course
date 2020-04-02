# Load and initialize pygame
import pygame
pygame.init()

# Create a display
screenWidth = 640
screen = pygame.display.set_mode((screenWidth,screenWidth))
pygame.display.set_caption('Space Invaders')

# Time
clock = pygame.time.Clock()

# Load images
background = pygame.image.load('Background.png')
ship = pygame.image.load('Ship.png')
enemypic = pygame.image.load('enemyship.png')

# Play music
music = pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1)

# Class dimensions of the spaceship
class dimensions():
	def __init__(self,x,y,width,height):

		# Overall variables in class
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.speed = 2
		self.hitbox = (self.x, self.y, self.width, self.height)
		self.health = 1
		self.visible = True

	# Function which draws the ship
	def draw(self, screen):
		if self.visible:
			self.hitbox = (self.x, self.y, self.width, self.height)
			screen.blit(ship, (self.x, self.y))

	# Function which processes when the ship gets hit 
	def hit(self):
		self.visible = False
		font1 = pygame.font.SysFont('comicsans', 50)
		text = font1.render('The Empire has won', 1, (255,0,0))
		screen.blit(text, (320 - (text.get_width()/2), 200))
		pygame.display.update()
		i = 0
		while i < 300:
			pygame.time.delay(10)
			i += 1
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					i = 301
		pygame.quit()

# Class dimensions of the enemy ship
class enemy(object):
	def __init__(self, x, y, width, height, end):

		# Overall variables in the class
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.end = end
		self.path = [self.x, self.end]
		self.speed = 2
		self.hitbox = (self.x, self.y, self.width, self.height)
		self.health = 5 
		self.visible = True

	# Function which draws the enemy
	def draw(self,screen):
		if self.visible:
			self.move()
			screen.blit(enemypic, (self.x, self.y))
			self.hitbox = (self.x, self.y, self.width, self.height)
			#pygame.draw.rect(screen, (255, 0, 0), self.hitbox, 2)
			pygame.draw.rect(screen, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
			pygame.draw.rect(screen, (0,255,0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (10 * (5-self.health)), 10))

	# Function which treats the movement of the enemy
	def move(self):
		if self.speed > 0:
			if self.x + self.speed < self.path[1]:
				self.x += self.speed
			else:
				self.speed = self.speed * -1
		else:
			if self.x - self.speed > self.path[0]:
				self.x += self.speed
			else:
				self.speed = self.speed *-1 
		self.y += 0.05

	# Function which treats enemy getting hit, losing hp each hit, and in the end dying
	def hit(self):
		if self.health > 0:
			self.health -= 1
		else:
			self.visible = False
			font1 = pygame.font.SysFont('comicsans', 50)
			text = font1.render('The Rebels have won', 1, (0,255,0))
			screen.blit(text, (320 - (text.get_width()/2), 200))
			pygame.display.update()
			i = 0
			while i < 300:
				pygame.time.delay(10)
				i += 1
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						i = 301
			pygame.quit()

# Class dimensions of the laser
class laser(object):
	def __init__(self,x,y,radius,color,speed):

		# Overall variables of the class
		self.x = x
		self.y = y
		self.radius = radius
		self.color = color
		self.speed = 3

	# Function which draws the laser
	def draw(self,screen):
		pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

# Function where every image is printed
def printScreen():
	screen.blit(background, (0, 0))
	if shipPos.visible == False:
		text = font.render('The Empire has won', 1, (255,0,0))
		screen.blit(text, (320 - (text.get_width()/2), 200))
	if shipPos.visible == True:
		shipPos.draw(screen)
	if stormtrooper.visible == True:
		stormtrooper.draw(screen)
	for missile in missiles:
		missile.draw(screen)
	for missile in enemymissiles:
		missile.draw(screen)
	pygame.display.update()

# Variables defined for loop
font = pygame.font.SysFont('comicsans', 30)
shipPos = dimensions(300,400,128,128)
missiles = []
enemymissiles = []
stormtrooper = enemy(100,100,64,64,450)
start_ticks = pygame.time.get_ticks()
run = True

# Running the loop
while run:

	# Runs the screen at 75 fps
	clock.tick(75)

	# missile from ship hits the enemy
	for missile in missiles:
		if missile.y - missile.radius	< stormtrooper.hitbox[1] + stormtrooper.hitbox[3] and missile.y + missile.radius > stormtrooper.hitbox[1]:
			if missile.x + missile.radius > stormtrooper.hitbox[0] and missile.x - missile.radius < stormtrooper.hitbox[0] + stormtrooper.hitbox[2]:
				stormtrooper.hit()
				missiles.pop(missiles.index(missile))
	
	# missile speed from the ship
	for missile in missiles:
		if missile.y > 0:
			missile.y -= missile.speed
		else:
			missiles.pop(missiles.index(missile))

	# Enemy crashes into the ship
	if stormtrooper.y - stormtrooper.height	< shipPos.hitbox[1] + shipPos.hitbox[3] and stormtrooper.y + stormtrooper.height > shipPos.hitbox[1]:
		if stormtrooper.x + stormtrooper.width > shipPos.hitbox[0] and stormtrooper.x - stormtrooper.width < shipPos.hitbox[0] + shipPos.hitbox[2]:
			shipPos.hit()
			
	# missile from enemy hits the ship
	for missile in enemymissiles:
		if missile.y - missile.radius	< shipPos.hitbox[1] + shipPos.hitbox[3] and missile.y + missile.radius > shipPos.hitbox[1]:
			if missile.x + missile.radius > shipPos.hitbox[0] and missile.x - missile.radius < shipPos.hitbox[0] + shipPos.hitbox[2]:
				shipPos.hit()
				enemymissiles.pop(enemymissiles.index(missile))
	
	# missile speed from the enemy
	for missile in enemymissiles:
		if missile.y < 600:
			missile.y += missile.speed
		else:
			enemymissiles.pop(enemymissiles.index(missile))

	# Input buttons for movement for the ship and firing
	key = pygame.key.get_pressed()
	if key[pygame.K_SPACE]:
		if len(missiles) < 1:
			missiles.append(laser(round(shipPos.x + shipPos.width //2), round(shipPos.y + shipPos.height //2), 6, (255,0,0), shipPos.speed))
	if key[pygame.K_LEFT] and shipPos.x > shipPos.speed:
		shipPos.x -= shipPos.speed
	if key[pygame.K_RIGHT] and shipPos.x < screenWidth - shipPos.width - shipPos.speed:
		shipPos.x += shipPos.speed
	
	# Enemy shooting once every second
	if len(enemymissiles) < 1:
		seconds = (pygame.time.get_ticks()-start_ticks)/1000
		if seconds > 1:
			enemymissiles.append(laser(round(stormtrooper.x + stormtrooper.width //2), round(stormtrooper.y + stormtrooper.height //2), 6, (0,255,0), stormtrooper.speed))

	# Continuesly runs the loop so it doesnt crash
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	# Prints the screen in the end of the loop
	printScreen()

# Exits the program
pygame.quit()