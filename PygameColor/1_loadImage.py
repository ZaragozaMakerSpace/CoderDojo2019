import pygame, sys

#Importa los nombres de las teclas y variables a referencias constantes 
from pygame.locals import * 

#Inicia el modulo pygame
pygame.init()
pygame.display.set_caption('Pygame Load Image') 

#Iniciamos la ventana de dibujo
size = [800, 500]
screen = pygame.display.set_mode( size , pygame.RESIZABLE)

#Cargamos la imagen y obtenemos su tamanio con el atributo size
## Puedes cambiar la ruta de la imagen por otra que mas te guste.
#IMPORTANTE - Hay que dirigir correctamente la ruta
background_image = pygame.image.load("src/mariogrid.png").convert()

while True: # main game loop 

	#Preparamos la imagen que queremos que aparezca 
	screen.blit( background_image, [0,0] )


	# ES MUY IMPORTANTE DISPONER DE UNA OPCION PARA CERRAR LA EJECUCION DEL BUCLE DEL PROGRAMA
	# En este caso podremos cerrar el programa presionando el boton ESC o presionando la X de la esquina superior de la ventana
	for event in pygame.event.get():
		#key = pygame.key.get_pressed()
		
		#Evento para cerrar la ventana
		if event.type == QUIT  or (event.type == KEYDOWN and event.key == K_ESCAPE): 
			pygame.quit() 
			sys.exit()

	#Actualiza la pantalla
	pygame.display.update()