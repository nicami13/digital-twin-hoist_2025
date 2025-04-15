#ALTO Y ANCHO DE LA PANTALLA 
Alto=400
ancho=600
#COLORES
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
#LONGITUDES DE CUERDA
longitud_cuerda_1 = 100
longitud_cuerda_2 = 50
longitud_cuerda_3 = 70
contador_longitud_cuerda = 0
#POSICION-CARACTERISTICAS POLEAS
polea_pos = (150, 100)  # (x, y)
polea_radius = 30       # Radio del círculo
#POSICION_CARATERISRICAS POLES
polea1_pos = (203, 147)
#POSICION-CARACTERISTICAS CUERDAS
start_pos_cuerda_1 = (125, 100)
end_pos_cuerda_1 = (start_pos_cuerda_1[0], start_pos_cuerda_1[1] + longitud_cuerda_1)
start_pos_cuerda_2 = (175, 100)
end_pos_cuerda_2 = (start_pos_cuerda_2[0], start_pos_cuerda_2[1] + longitud_cuerda_2)
start_pos_cuerda_3= (200, 100)

# Tamaño visual constante
masa1_size = 40
masa2_size = 40
masa1_pos = (end_pos_cuerda_1[0]-masa1_size//2,end_pos_cuerda_1[1])
#POSICION-CARACTERISTICAS MASA FINAL
masa2_pos = (end_pos_cuerda_2[0]-masa2_size//2,end_pos_cuerda_2[1])
# Masa real (afecta el movimiento)
masa1_valor = 40
masa2_valor = 40