#ALTO Y ANCHO DE LA PANTALLA 
Alto=400
ancho=400
#COLORES
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
#LONGITUDES DE CUERDA
longitud_cuerda_1 = 100
longitud_cuerda_2 = 50
longitud_cuerda_3 = 130
longitud_cuerda_4= 187
longitud_cuerda_5= 255
contador_longitud_cuerda = 0
#POSICION-CARACTERISTICAS POLEAS
polea_pos = (150, 100)  
polea_radius = 30       
#POSICION_CARATERISRICAS POLEaS
polea1_pos = (203, 150)
polea2_pos = (230, 220) 
polea3_pos = (258, 280) 
#POSICION-CARACTERISTICAS CUERDAS
start_pos_cuerda_1 = (125, 100)
end_pos_cuerda_1 = (start_pos_cuerda_1[0], start_pos_cuerda_1[1] + longitud_cuerda_1)
start_pos_cuerda_2 = (175, 100)
end_pos_cuerda_2 = (start_pos_cuerda_2[0], start_pos_cuerda_2[1] + longitud_cuerda_2)
start_pos_cuerda_3= (225, 20)
end_pos_cuerda_3 = (start_pos_cuerda_3[0], start_pos_cuerda_3[1] + longitud_cuerda_3)
start_pos_cuerda_4= (255,20)
end_pos_cuerda_4=(start_pos_cuerda_4[0], start_pos_cuerda_4[1] + longitud_cuerda_4)
start_pos_cuerda_5= (285,20)
end_pos_cuerda_5=(start_pos_cuerda_5[0], start_pos_cuerda_5[1] + longitud_cuerda_5)
Cuerda_6 = ((polea3_pos[0], polea3_pos[1]), (polea3_pos[0], polea3_pos[1] + 40))

# Tamaño visual constante
masa1_size = 40
masa2_size = 40
masa1_pos = (end_pos_cuerda_1[0]-masa1_size//2,end_pos_cuerda_1[1])
#POSICION-CARACTERISTICAS MASA FINAL
masa2_pos = (Cuerda_6[1][0] - masa2_size // 2, Cuerda_6[1][1])
# Masa real (afecta el movimiento)
masa1_valor = 40
masa2_valor = 40