import Constants
import pygame

GRAVEDAD = 9.81  # m/s²
ESCALA = 0.25  # metros a píxeles
DT = 0.05  # segundos por frame
n = 3  # Número de poleas móviles (2^n segmentos)

velocidad = 0  
velocidad_mostrada = 0
aceleracion = 0
aceleracion_mostrada = 0

def actualizar_movimiento():
    global velocidad, aceleracion, DT

    m1 = Constants.masa1_valor
    m2 = Constants.masa2_valor

    relacion = 2 ** n

    if abs(m2 - m1 * relacion) < 0.01:
        velocidad = 0
        aceleracion = 0
        return

    fuerza_neta = (m2 * GRAVEDAD) - (m1 * relacion * GRAVEDAD)
    masa_total = m1 + m2
    aceleracion = fuerza_neta / masa_total
    velocidad += aceleracion * DT

    desplazamiento_m = velocidad * DT

    if abs(velocidad) < 0.1 and velocidad != 0:
        desplazamiento_m = (0.1 if velocidad > 0 else -0.1) * 0.3 * DT

    desplazamiento_px = desplazamiento_m * ESCALA * 100

    nueva_masa1_y = Constants.masa1_pos[1] - desplazamiento_px
    nueva_polea3_y = Constants.polea3_pos[1] + desplazamiento_px / 2
    nueva_masa2_y = nueva_polea3_y + Constants.polea_radius

    nueva_polea1_y = Constants.polea1_pos[1] + desplazamiento_px / 2
    nueva_polea2_y = Constants.polea2_pos[1] + desplazamiento_px / 2

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

    Constants.masa1_pos = (Constants.masa1_pos[0], nueva_masa1_y)
    Constants.polea3_pos = (Constants.polea3_pos[0], nueva_polea3_y)
    Constants.masa2_pos = (Constants.masa2_pos[0], nueva_masa2_y)
    Constants.polea1_pos = (Constants.polea1_pos[0], nueva_polea1_y)
    Constants.polea2_pos = (Constants.polea2_pos[0], nueva_polea2_y)

    Constants.end_pos_cuerda_1 = (Constants.start_pos_cuerda_1[0], nueva_masa1_y)
    Constants.end_pos_cuerda_2 = (Constants.start_pos_cuerda_2[0], nueva_polea1_y)
    Constants.end_pos_cuerda_3 = (Constants.start_pos_cuerda_3[0], nueva_polea1_y)
    Constants.end_pos_cuerda_4 = (Constants.start_pos_cuerda_4[0], nueva_polea2_y)
    Constants.end_pos_cuerda_5 = (Constants.start_pos_cuerda_5[0], nueva_polea3_y)
    Constants.end_pos_cuerda_6 = (
        Constants.polea3_pos,
        (Constants.polea3_pos[0], nueva_masa2_y)
    )

    FPS_MIN = 5
    FPS_MAX = 40

    velocidad_visual = abs(velocidad)
    max_speed = Constants.velocidad_deseada if Constants.velocidad_deseada > 0 else 1  # evita división por cero
    factor = min(velocidad_visual / max_speed, 1.0)
    nuevo_fps = int(FPS_MIN + (FPS_MAX - FPS_MIN) * factor)
    Constants.Frames = nuevo_fps

    if Constants.Frames > 0:
        DT = 1.0 / Constants.Frames
    else:
        DT = 0.016

    desplazamiento_px *= factor
12

def dibujar_info_velocidad(pantalla):
    global velocidad_mostrada, velocidad
    velocidad_mostrada += (velocidad - velocidad_mostrada) * 0.05
    fuente = pygame.font.SysFont("Arial", 20)
    texto = fuente.render(f"Vel: {velocidad_mostrada:.2f} m/s", True, (255, 255, 255))
    fondo_rect = pygame.Rect(10, Constants.Alto - 40, 160, 30)
    pygame.draw.rect(pantalla, (0, 0, 0), fondo_rect)
    pantalla.blit(texto, (20, Constants.Alto - 35))

def dibujar_info_aceleracion(pantalla):
    global aceleracion_mostrada, aceleracion
    aceleracion_mostrada += (aceleracion - aceleracion_mostrada) * 0.05
    fuente = pygame.font.SysFont("Arial", 20)
    texto = fuente.render(f"Acel: {aceleracion_mostrada:.2f} m/s²", True, (255, 255, 255))
    fondo_rect = pygame.Rect(Constants.ancho - 180, Constants.Alto - 40, 160, 30)
    pygame.draw.rect(pantalla, (0, 0, 0), fondo_rect)
    pantalla.blit(texto, (Constants.ancho - 170, Constants.Alto - 35))

