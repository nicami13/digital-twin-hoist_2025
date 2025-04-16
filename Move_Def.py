import Constants

GRAVEDAD = 9.81  # m/s²
ESCALA = 0.25
DT = 0.1
n = 3  # Número de poleas móviles (2^n segmentos)

# Variable de velocidad global
velocidad = 0

def actualizar_movimiento():
    global velocidad

    m1 = Constants.masa1_valor
    m2 = Constants.masa2_valor

    # Verificar si está en equilibrio (sin movimiento)
    if abs(m1 - m2 / (2 ** n)) < 0.01:
        velocidad = 0
        return

    # Fuerza efectiva de m2 con polipasto (R)
    F_teorica = (m2 * GRAVEDAD) / (2 ** n)

    # Fuerza generada por m1 (F)
    F_real = m1 * GRAVEDAD

    # Aceleración del sistema
    a = (F_teorica - F_real) / (m1 + m2)
    velocidad += a * DT

    # Desplazamiento en metros → píxeles (signo incluido)
    desplazamiento = velocidad * DT * ESCALA * 100

    # Movimiento según dirección real (positivo o negativo)
    nueva_masa1_y = Constants.masa1_pos[1] - desplazamiento
    nueva_polea3_y = Constants.polea3_pos[1] + desplazamiento / 2
    nueva_masa2_y = nueva_polea3_y + Constants.polea_radius

    # Las otras poleas bajan o suben junto con polea3
    delta_poleas = desplazamiento / 2
    nueva_polea1_y = Constants.polea1_pos[1] + delta_poleas
    nueva_polea2_y = Constants.polea2_pos[1] + delta_poleas

    # Verificamos límites para evitar que las masas se salgan
    if (
        nueva_masa1_y < 80 or nueva_masa1_y > Constants.Alto - 80 or
        nueva_masa2_y < 80 or nueva_masa2_y > Constants.Alto - 80 or
        nueva_polea1_y < Constants.polea_pos[1] + 15 or
        nueva_polea2_y < Constants.polea_pos[1] + 15 or
        nueva_polea3_y < Constants.polea_pos[1] + 15
    ):
        return

    # Actualizamos posiciones
    Constants.masa1_pos = (Constants.masa1_pos[0], nueva_masa1_y)
    Constants.polea3_pos = (Constants.polea3_pos[0], nueva_polea3_y)
    Constants.masa2_pos = (Constants.masa2_pos[0], nueva_masa2_y)
    Constants.polea1_pos = (Constants.polea1_pos[0], nueva_polea1_y)
    Constants.polea2_pos = (Constants.polea2_pos[0], nueva_polea2_y)

    # Actualizamos posiciones de las cuerdas
    Constants.end_pos_cuerda_1 = (Constants.start_pos_cuerda_1[0], Constants.masa1_pos[1])
    Constants.end_pos_cuerda_2 = (Constants.start_pos_cuerda_2[0], Constants.polea1_pos[1])
    Constants.end_pos_cuerda_3 = (Constants.start_pos_cuerda_3[0], Constants.polea1_pos[1])
    Constants.end_pos_cuerda_4 = (Constants.start_pos_cuerda_4[0], Constants.polea2_pos[1])
    Constants.end_pos_cuerda_5 = (Constants.start_pos_cuerda_5[0], Constants.polea3_pos[1])
    Constants.end_pos_cuerda_6 = (
        Constants.polea3_pos,
        (Constants.polea3_pos[0], Constants.masa2_pos[1])
    )
