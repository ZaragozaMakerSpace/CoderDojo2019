import pygame, sys

#Importa los nombres de las teclas y variables a referencias constantes 
from pygame.locals import * 

#Inicia el modulo pygame
pygame.init()
pygame.display.set_caption('Pygame Move Player') 

#Iniciamos la ventana de dibujo
size = [800, 500]
screen = pygame.display.set_mode( size , pygame.RESIZABLE)

#Cargamos la imagen y obtenemos su tamanio con la funcion size
background_image = pygame.image.load("src/back_tree.png").convert()
#Como la imagen no tiene la misma anchura y altura que el fondo, vamos a reescarlala para que se adapte a la pantalla
print ( background_image.get_rect().size)
background_image = pygame.transform.scale(background_image, size )

#Cargamos la imagen del personaje
player = pygame.image.load("src/Player/pilot.png").convert()

#Definimos las variables de posicion del personaje
posX = 120
posY = 120

#Ahora definimos la velocidad del jugador
speed = 10
coords =[posX, posY]

while True: # main game loop 
	#Muestra la imagen y el texto
	screen.blit( background_image, [0,0] )

	##Ahora queremos que las coordenadas de nuestro personaje se actualicen al presionar el raton
	screen.blit(player , coords ) 

	for event in pygame.event.get():

		key = pygame.key.get_pressed()
		if key[pygame.K_DOWN]: 
			posY = posY + 1
		if key[pygame.K_UP]:
			posY = posY - 1

		if key[pygame.K_RIGHT]: 
			posX = posX + 1
		if key[pygame.K_LEFT]:
			posX = posX - 1

		if event.type == pygame.MOUSEBUTTONUP:
			#Obtenemos las coordenadas
			coords = pygame.mouse.get_pos()
			print (coords)
			#Obtenemos el color  
			color = screen.get_at( coords )
			print( color )

		#Evento para cerrar la ventana
		if event.type == QUIT  or (event.type == KEYDOWN and event.key == K_ESCAPE): 
			pygame.quit() 
			sys.exit()

	pygame.display.update()