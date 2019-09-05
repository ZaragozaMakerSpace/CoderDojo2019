import pygame, sys

#Importa los nombres de las teclas y variables a referencias constantes 
from pygame.locals import * 

#Inicia el modulo pygame
pygame.init()
pygame.display.set_caption('Pygame Read surrounding color pixels') 

#Iniciamos la ventana de dibujo
size = [800, 500]
screen = pygame.display.set_mode( size , pygame.RESIZABLE)

#Cargamos la imagen y obtenemos su tamanio con la funcino size
## Puedes cambiar la ruta de la imagen por otra que mas te guste
background_image = pygame.image.load("src/mariogrid.jpg").convert()

#Definimos el tamaño de nuestra interfaz, y cargamos el tamanio de la ventana
palete_size = ( 200 , 200 )
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

def read_surroundColors( position, nx = 3, ny = 3 ):

	#Calculamos los valores de color de alrededor

	dx = palete_size[0]/nx
	dy = palete_size[1]/ny

	#Realizamos un bucle para representar 3 filas y 3 columnas
	for x in range(-int(nx/2), int(nx/2) + 1):
		for y in range(-int(ny/2), int(ny/2) +1):
			color = screen.get_at( ( position[0] +x, position[1] +y) )
			#print( ' Px: ', x , ' Py: ', y ,' Color: ',color)
			
			rect_color  = pygame.Rect( (size[0]-palete_size[0])/2+dx*(x+int(ny/2)) , size[1]+dy*(y+int(ny/2)) , dx , dy )
			pygame.draw.rect( screen, color , rect_color)
	#Dibujamos la malla
	drawGrid( nx, ny )
	#print()

def drawGrid( nx = 3, ny = 3  ):

	dx = palete_size[0]/nx
	dy = palete_size[1]/ny
	BLACK = (0, 0, 0)
	for x in range(-int(nx/2), int(nx/2) + 1):
		for y in range(-int(ny/2), int(ny/2) + 1):
			#print( ' Px: ', x , ' Py: ', y )
			rect_color  = pygame.Rect( (size[0]-palete_size[0])/2+dx*(x+int(ny/2)) , size[1]+dy*(y+int(ny/2)) , dx , dy )
			#Dibujamos un cuadrado vacio en cada posicion del bucle para definir la malla
			pygame.draw.rect( screen, BLACK , rect_color, True)
	#print()


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

			#Obtenemos el color y dibujamos 
			read_surroundColors( coords, 15,15 )

		#Evento para cerrar la ventana
		if event.type == QUIT  or (event.type == KEYDOWN and event.key == K_ESCAPE): 
			pygame.quit() 
			sys.exit()
	pygame.display.update()