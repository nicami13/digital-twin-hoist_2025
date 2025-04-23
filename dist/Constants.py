import pygame
# Dimensiones de la pantalla
Alto = 400
ancho = 400

input_texto_velocidad = ""
input_texto_masa2 = ""
velocidad_deseada = 0
definir_input = "velocidad"


# Colores
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Masa real (afecta el movimiento)
masa1_valor = 26.87
masa2_valor = 211

# Tamaño visual constante
masa1_size = 40
masa2_size = 40

# Posiciones iniciales de poleas
polea_pos = (150, 100)
polea_radius = 30

polea1_pos = (203, 150)
polea2_pos = (230, 220)
polea3_pos = (258, 280)

# Posiciones de masas
masa1_pos = (
    125 - masa1_size // 2,  # Centrada con la cuerda 1
    150                     # Altura inicial ajustable
)

masa2_pos = (
    polea3_pos[0] - masa2_size // 2,    
    polea3_pos[1] + polea_radius + 10
)

# CUERDAS (inicio y fin completamente verticales)
start_pos_cuerda_1 = (125, polea_pos[1])
end_pos_cuerda_1 = (start_pos_cuerda_1[0], masa1_pos[1])

start_pos_cuerda_2 = (175, polea_pos[1])
end_pos_cuerda_2 = (start_pos_cuerda_2[0], polea1_pos[1])

start_pos_cuerda_3 = (230, 20)
end_pos_cuerda_3 = (start_pos_cuerda_3[0], polea1_pos[1])

start_pos_cuerda_4 = (255, 20)
end_pos_cuerda_4 = (start_pos_cuerda_4[0], polea2_pos[1])

start_pos_cuerda_5 = (285, 20)
end_pos_cuerda_5 = (start_pos_cuerda_5[0], polea3_pos[1])

start_pos_cuerda_6 = (258-polea_radius/2, polea3_pos[1])
end_pos_cuerda_6 = (polea3_pos[0], masa2_pos[1])

#Diseños
new_width = 2 * polea_radius  
new_height = 2 * polea_radius 
polea_img = pygame.image.load("polea.png")
polea_img = pygame.transform.scale(polea_img, (2 * polea_radius, 2 * polea_radius))

