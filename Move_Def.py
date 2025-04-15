import Constants

GRAVEDAD = 9.81  # m/s^2
ESCALA = 0.2     # factor para convertir de m a pixeles
DT = 0.1         # intervalo de tiempo ficticio entre frames

# Variables globales de velocidad
velocidad = 0

def actualizar_movimiento():
    global velocidad

    m1 = Constants.masa1_valor
    m2 = Constants.masa2_valor

    # Si las masas son iguales, no hay movimiento
    if m1 == m2:
        velocidad = 0
        return

    # Calcular aceleración (Beer & Johnston)
    aceleracion = ((m1 - m2) * GRAVEDAD) / (m1 + m2)

    # Actualizar velocidad
    velocidad += aceleracion * DT

    # Calcular cambio de posición en píxeles
    dy = velocidad * DT * ESCALA * 100  # escalamos para hacerlo visible

    # Nuevas posiciones
    nueva_masa1_y = Constants.masa1_pos[1] + dy
    nueva_masa2_y = Constants.masa2_pos[1] - dy

    # Límites para que no pase la polea ni el suelo
    limite_superior = Constants.polea_pos[1] + Constants.polea_radius
    limite_inferior = Constants.Alto - Constants.masa1_size - 20

    # Verificar si hay espacio para moverse
    if limite_superior < nueva_masa1_y < limite_inferior and \
       limite_superior < nueva_masa2_y < limite_inferior:

        # Aplicar desplazamiento
        Constants.masa1_pos = (Constants.masa1_pos[0], nueva_masa1_y)
        Constants.end_pos_cuerda_1 = (Constants.end_pos_cuerda_1[0], nueva_masa1_y)

        Constants.masa2_pos = (Constants.masa2_pos[0], nueva_masa2_y)
        Constants.end_pos_cuerda_2 = (Constants.end_pos_cuerda_2[0], nueva_masa2_y)




