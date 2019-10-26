import pygame, sys

#Importa los nombres de las teclas y variables a referencias constantes 
from pygame.locals import * 

#Inicia el modulo pygame
pygame.init()
pygame.display.set_caption('Pygame Read Color') 

#Iniciamos la ventana de dibujo
size = [800, 500]
screen = pygame.display.set_mode( size , pygame.RESIZABLE)

#Cargamos la imagen y obtenemos su tamanio con la funcino size
## Puedes cambiar la ruta de la imagen por otra que mas te guste
background_image = pygame.image.load("src/mariogrid.png").convert()

#Definimos el tamaño de nuestra interfaz, y cargamos el tamanio de la ventana
palete_size = ( 120 , 120 )
size = background_image.get_rect().size
total_size = background_image.get_rect().size[0], background_image.get_rect().size[1] + palete_size[1]

screen = pygame.display.set_mode( total_size  , pygame.RESIZABLE)


#Definimos el mensaje que aparecera en la pantalla
font = pygame.font.Font('freesansbold.ttf', 25) 
WHITE = (255, 255, 255)
AQUA = (  0, 128, 128)
text = font.render('Click on the image', True, WHITE, AQUA )
textRect = text.get_rect() 
textRect.center = ( total_size[0]// 4, total_size[1] - palete_size[1]/2 ) 


while True: # main game loop 
	#Muestra la imagen y el texto
	screen.blit( background_image, [0,0] )
	screen.blit(text, textRect) 

	for event in pygame.event.get():
		key = pygame.key.get_pressed()
		
		#Obtener el color de un pixel si presionamos el raton sobre la imagen
		if event.type == pygame.MOUSEBUTTONUP:
			#Obtenemos las coordenadas
			coords = pygame.mouse.get_pos()
			#Definimos las coordenadas del rectangulo con su posicion inicial x, y, anchura y altura
			rect_color  = pygame.Rect( (size[0]-palete_size[0])/2 , size[1] , palete_size[0], palete_size[1] )

			#Obtenemos el color y dibujamos 
			color = screen.get_at( coords )
			pygame.draw.rect( screen, color , rect_color)
			print( color )

		#Evento para cerrar la ventana
		if event.type == QUIT  or (event.type == KEYDOWN and event.key == K_ESCAPE): 
			pygame.quit() 
			sys.exit()
	pygame.display.update()