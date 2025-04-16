# -*- coding: utf-8 -*-
"""
Created on Thu Mar 20 14:13:59 2025
video para entender el problema minuto 7
https://www.youtube.com/watch?v=VCZzaj2yRkE
@author: oscar
"""
import pygame
import time

# Inicializar Pygame
pygame.init()

# Configurar la ventana
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dibujar un círculo en Pygame")

# Definir colores
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

longitud_cuerda_1 = 100
longitud_cuerda_2 = 100
contador_longitud_cuerda = 0


# Posición y radio de polea
polea_pos = (300, 100)  # (x, y)
polea_radius = 30       # Radio del círculo

# posicion y caracteristicas cuerda 1 
start_pos_cuerda_1 = (272, 100)  # Punto superior de la cuerda
end_pos_cuerda_1 = (start_pos_cuerda_1[0], start_pos_cuerda_1[1] + longitud_cuerda_1)    # Punto inferior de la cuerda (100 píxeles más abajo)

# posicion y caracteristicas masa 1
masa1_size = 40 # Tamaño del lado del cuadrado
masa1_pos = (end_pos_cuerda_1[0]-masa1_size//2,end_pos_cuerda_1[1]) # (x, y) esquina superior izquierda

# posicion y caracteristicas cuerda 2
start_pos_cuerda_2 = (328, 100)  # Punto superior de la cuerda
end_pos_cuerda_2 = (start_pos_cuerda_2[0], start_pos_cuerda_2[1] + longitud_cuerda_2)    # Punto inferior de la cuerda (100 píxeles más abajo)

# posicion y caracteristicas masa 2
masa2_size = 40 # Tamaño del lado del cuadrado
masa2_pos = (end_pos_cuerda_2[0]-masa2_size//2,end_pos_cuerda_2[1]) # (x, y) esquina superior izquierda

# Bucle principal
# Crear un reloj para el control del tiempo
clock = pygame.time.Clock()
simulation_time = 0
running = True
while running:
    dt = clock.tick(60)  # Controla los FPS a 60 y obtiene el delta time en milisegundos
    # Actualizar el tiempo de simulación
    simulation_time += dt
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)  # Fondo blanco
    
    # dibujar cuerda 1
    pygame.draw.line(screen, BLACK, start_pos_cuerda_1, end_pos_cuerda_1, 5)  # Grosor de 5 píxeles
    # dibujar masa 1
    pygame.draw.rect(screen, RED, (masa1_pos[0], masa1_pos[1], masa1_size, masa1_size))
    # dibujar cuerda 1
    pygame.draw.line(screen, BLACK, start_pos_cuerda_2, end_pos_cuerda_2, 5)  # Grosor de 5 píxeles
    # dibujar masa 2
    pygame.draw.rect(screen, RED, (masa2_pos[0], masa2_pos[1], masa2_size, masa2_size))    
   
    #############################################################################
    # dibujar techo
    pygame.draw.line(screen, BLACK, (0,20), (600,20), 10)  # Grosor de 5 píxeles
    # dibujar cuerda techo
    pygame.draw.line(screen, BLACK, (polea_pos[0],polea_pos[1]), (polea_pos[0],polea_pos[1]-80), 7)  # Grosor de 5 píxeles
    # Dibujar el polea
    pygame.draw.circle(screen, BLUE, polea_pos, polea_radius)
    
    ###########################################################################
    #time.sleep(0.1)
    # dinamica del sistema
    if (masa1_size == masa2_size):
        pass
    elif(masa1_size < masa2_size):
        contador_longitud_cuerda += 1 
        #print(contador_longitud_cuerda)
        if (contador_longitud_cuerda < longitud_cuerda_1-20):
            #baja la masa1
            masa1_pos = (masa1_pos[0], masa1_pos[1] - 1)
            end_pos_cuerda_1 = (end_pos_cuerda_1[0] , end_pos_cuerda_1[1] - 1)
            # sube la masa 2
            masa2_pos = (masa2_pos[0], masa2_pos[1] + 1)
            end_pos_cuerda_2 = (end_pos_cuerda_2[0] , end_pos_cuerda_2[1] + 1)
    elif(masa1_size > masa2_size):
        contador_longitud_cuerda += 1 
        print(contador_longitud_cuerda)
        if (contador_longitud_cuerda < longitud_cuerda_1-20):
            #baja la masa1
            masa1_pos = (masa1_pos[0], masa1_pos[1] + 1)
            end_pos_cuerda_1 = (end_pos_cuerda_1[0] , end_pos_cuerda_1[1] + 1)
            # sube la masa 2
            masa2_pos = (masa2_pos[0], masa2_pos[1] - 1)
            end_pos_cuerda_2 = (end_pos_cuerda_2[0] , end_pos_cuerda_2[1] - 1)
        
    
    
    # Actualizar la pantalla
    pygame.display.flip()  

# Salir de Pygame
pygame.quit()
    