import pygame
pygame.init()



# Create a display

window = pygame.display.set_mode((500, 500))

playerWidth = playerHeight = 30

playerPosX = 225
playerPosY = 300
playerColorRed = (255, 0, 0)
vel = 5


run = True
while run:

	pygame.time.delay(100)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	direction = pygame.key.get_pressed()

	if direction[pygame.K_UP]:
		playerPosY	+= vel

	if direction[pygame.K_DOWN]:
		playerPosY -= vel	

	if direction[pygame.K_LEFT]:
		playerPosX -= vel

	if direction[pygame.K_RIGHT]:
		playerPosX += vel

	pygame.draw.rect(window, playerColorRed, (playerPosX, playerPosY, playerWidth, playerHeight))
	pygame.draw.rect(window, playerColorRed, (playerPosX+100, playerPosY+100, playerWidth, playerHeight))
	pygame.display.update()





pygame.quit()