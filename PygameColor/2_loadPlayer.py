import pygame, sys

#Importa los nombres de las teclas y variables a referencias constantes 
from pygame.locals import * 

#Inicia el modulo pygame
pygame.init()
pygame.display.set_caption('Pygame Load Player') 

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


while True: # main game loop 
	#Muestra la imagen y el texto
	screen.blit( background_image, [0,0] )
	## Tenemos que modificar la posicion del personaje para que aparezca sobre la superficie de tierra
	##Definimos dos variables
	posX = 0;
	posY = 0;
	screen.blit(player , [ posX, posY ]) 


	for event in pygame.event.get():
		key = pygame.key.get_pressed()
		
		#Evento para cerrar la ventana
		if event.type == QUIT  or (event.type == KEYDOWN and event.key == K_ESCAPE): 
			pygame.quit() 
			sys.exit()
	pygame.display.update()