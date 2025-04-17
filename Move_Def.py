import Constants
import pygame

GRAVEDAD = 9.81  # m/s²
ESCALA = 0.25  # metros a píxeles
DT = 0.05  # segundos por frame
n = 3  # Número de poleas móviles (2^n segmentos)

velocidad = 0  # Velocidad global del sistema (m/s)
velocidad_mostrada = 0
aceleracion = 0
aceleracion_mostrada = 0

def actualizar_movimiento():
    global velocidad, aceleracion

    m1 = Constants.masa1_valor
    m2 = Constants.masa2_valor

    # Relación de reducción por el sistema de poleas
    relacion = 2 ** n

    # Verificación de equilibrio (diferencia mínima de fuerzas)
    if abs(m2 - m1 * relacion) < 0.01:
        velocidad = 0
        aceleracion = 0
        return

    # Cálculo de fuerza neta (considerando distribución de fuerza en polipasto)
    fuerza_neta = (m2 * GRAVEDAD) - (m1 * relacion * GRAVEDAD)
    masa_total = m1 + m2

    # Aceleración del sistema
    aceleracion = fuerza_neta / masa_total
    velocidad += aceleracion * DT

    # Desplazamiento en metros
    desplazamiento_m = velocidad * DT

    # Refuerzo visual si la velocidad es muy pequeña pero no cero
    if abs(velocidad) < 0.1 and velocidad != 0:
        factor_visual = 0.3  # Ajusta esto para más/menos movimiento visual
        desplazamiento_m = (0.1 if velocidad > 0 else -0.1) * factor_visual * DT

    # Convertir a pixeles
    desplazamiento_px = desplazamiento_m * ESCALA * 100  # 1 metro = 100 píxeles

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
        velocidad = 0
        aceleracion = 0
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


def dibujar_info_velocidad(pantalla):
    global velocidad_mostrada, velocidad
    # Interpolación suave (puedes ajustar el 0.05 para que sea más o menos lento)
    velocidad_mostrada += (velocidad - velocidad_mostrada) * 0.05

    fuente = pygame.font.SysFont("Arial", 20)
    texto = fuente.render(f"Vel: {velocidad_mostrada:.2f} m/s", True, (255, 255, 255))
    fondo_rect = pygame.Rect(10, Constants.Alto - 40, 160, 30)  # parte inferior
    pygame.draw.rect(pantalla, (0, 0, 0), fondo_rect)
    pantalla.blit(texto, (20, Constants.Alto - 35))
    
def dibujar_info_aceleracion(pantalla):
    global aceleracion_mostrada, aceleracion
    # Interpolación suave (puedes ajustar el 0.05 para que sea más o menos lento)
    aceleracion_mostrada += (aceleracion - aceleracion_mostrada) * 0.05

    fuente = pygame.font.SysFont("Arial", 20)
    texto = fuente.render(f"Acel: {aceleracion_mostrada:.2f} m/s²", True, (255, 255, 255))
    fondo_rect = pygame.Rect(Constants.ancho - 180, Constants.Alto - 40, 160, 30)  # parte inferior derecha
    pygame.draw.rect(pantalla, (0, 0, 0), fondo_rect)
    pantalla.blit(texto, (Constants.ancho - 170, Constants.Alto - 35))

