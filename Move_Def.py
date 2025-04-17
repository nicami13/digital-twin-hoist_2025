import Constants

GRAVEDAD = 9.81  # m/s²
ESCALA = 0.25  # metros a píxeles
DT = 0.05  # segundos por frame
n = 3  # Número de poleas móviles (2^n segmentos)

velocidad = 0  # Velocidad global del sistema (m/s)

def actualizar_movimiento():
    global velocidad

    m1 = Constants.masa1_valor
    m2 = Constants.masa2_valor

    # Relación de reducción por el sistema de poleas
    relacion = 2 ** n

    # Verificación de equilibrio (diferencia mínima de fuerzas)
    if abs(m2 - m1 * relacion) < 0.01:
        velocidad = 0
        return

    # Cálculo de fuerza neta (considerando distribución de fuerza en polipasto)
    fuerza_neta = (m2 * GRAVEDAD) - (m1 * relacion * GRAVEDAD)
    masa_total = m1 + m2

    # Aceleración del sistema
    aceleracion = fuerza_neta / masa_total
    velocidad += aceleracion * DT

    # Desplazamiento en metros, luego lo convertimos a píxeles
    desplazamiento_m = velocidad * DT
    desplazamiento_px = desplazamiento_m * ESCALA * 100  # 1 metro = 100 pixeles

    # Movimiento (masa1 sube si desplazamiento es negativo)
    nueva_masa1_y = Constants.masa1_pos[1] - desplazamiento_px
    nueva_polea3_y = Constants.polea3_pos[1] + desplazamiento_px / 2
    nueva_masa2_y = nueva_polea3_y + Constants.polea_radius

    # Las poleas 1 y 2 se mueven junto con la 3 (simetría)
    nueva_polea1_y = Constants.polea1_pos[1] + desplazamiento_px / 2
    nueva_polea2_y = Constants.polea2_pos[1] + desplazamiento_px / 2

    # Límites para que no se salgan del área de la simulación
    margen = 80
    if (
        nueva_masa1_y < margen or nueva_masa1_y > Constants.Alto - margen or
        nueva_masa2_y < margen or nueva_masa2_y > Constants.Alto - margen or
        nueva_polea1_y < Constants.polea_pos[1] + 15 or
        nueva_polea2_y < Constants.polea_pos[1] + 15 or
        nueva_polea3_y < Constants.polea_pos[1] + 15
    ):
        return

    # Actualizar posiciones
    Constants.masa1_pos = (Constants.masa1_pos[0], nueva_masa1_y)
    Constants.polea3_pos = (Constants.polea3_pos[0], nueva_polea3_y)
    Constants.masa2_pos = (Constants.masa2_pos[0], nueva_masa2_y)
    Constants.polea1_pos = (Constants.polea1_pos[0], nueva_polea1_y)
    Constants.polea2_pos = (Constants.polea2_pos[0], nueva_polea2_y)

    # Actualizar cuerdas
    Constants.end_pos_cuerda_1 = (Constants.start_pos_cuerda_1[0], nueva_masa1_y)
    Constants.end_pos_cuerda_2 = (Constants.start_pos_cuerda_2[0], nueva_polea1_y)
    Constants.end_pos_cuerda_3 = (Constants.start_pos_cuerda_3[0], nueva_polea1_y)
    Constants.end_pos_cuerda_4 = (Constants.start_pos_cuerda_4[0], nueva_polea2_y)
    Constants.end_pos_cuerda_5 = (Constants.start_pos_cuerda_5[0], nueva_polea3_y)
    Constants.end_pos_cuerda_6 = (
        Constants.polea3_pos,
        (Constants.polea3_pos[0], nueva_masa2_y)
    )
