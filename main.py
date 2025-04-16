import pygame
import Constants
import Move_Def
import Menu
import pymunk

pygame.init()
Screen = pygame.display.set_mode((Constants.ancho, Constants.Alto))
Clock = pygame.time.Clock()
simulation_time = 0
running = True
menu_visible = False

while running:
    dt = Clock.tick(60)  # 60 FPS
    simulation_time += dt

    eventos = pygame.event.get()
    for event in eventos:
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                menu_visible = not menu_visible

    Screen.fill(Constants.WHITE)

    # Dibujar cuerdas y masas
    pygame.draw.line(Screen, Constants.BLACK, Constants.start_pos_cuerda_1, Constants.end_pos_cuerda_1, 5)
    pygame.draw.rect(Screen, Constants.RED, (Constants.masa1_pos[0], Constants.masa1_pos[1], Constants.masa1_size, Constants.masa1_size))
    pygame.draw.line(Screen, Constants.BLACK, Constants.start_pos_cuerda_2, Constants.end_pos_cuerda_2, 5)
    # Dibujar polea y barra
    pygame.draw.line(Screen, Constants.BLACK, (0, 20), (600, 20), 25)
    pygame.draw.line(Screen, Constants.BLACK, (Constants.polea_pos[0], Constants.polea_pos[1]), (Constants.polea_pos[0], Constants.polea_pos[1] - 80), 5)
    pygame.draw.circle(Screen, Constants.BLUE, Constants.polea_pos, Constants.polea_radius)
    # Dibujar segunda polea
    pygame.draw.line(Screen, Constants.BLACK, Constants.start_pos_cuerda_3, Constants.end_pos_cuerda_3, 5)
    pygame.draw.line(Screen, Constants.BLACK, ((Constants.polea1_pos[0]), Constants.polea1_pos[1]), (Constants.polea1_pos[0], Constants.polea1_pos[1] + 60), 5)
    pygame.draw.circle(Screen, Constants.BLUE, Constants.polea1_pos, Constants.polea_radius)
    # Dibujar Tercer polea
    pygame.draw.line(Screen, Constants.BLACK, Constants.start_pos_cuerda_4, Constants.end_pos_cuerda_4, 5)
    pygame.draw.line(Screen, Constants.BLACK, ((Constants.polea2_pos[0]), Constants.polea2_pos[1]), (Constants.polea2_pos[0], Constants.polea2_pos[1] + 60), 5)
    pygame.draw.circle(Screen, Constants.BLUE, Constants.polea2_pos, Constants.polea_radius)
    # Dibujar cuarta polea
    pygame.draw.line(Screen, Constants.BLACK, Constants.start_pos_cuerda_5, Constants.end_pos_cuerda_5, 5)
    pygame.draw.line(Screen, Constants.BLACK, ((Constants.polea3_pos[0]), Constants.polea3_pos[1]), (Constants.polea3_pos[0], Constants.polea3_pos[1] + 40), 5)
    pygame.draw.circle(Screen, Constants.BLUE, Constants.polea3_pos, Constants.polea_radius)
    pygame.draw.rect(Screen, Constants.RED, (Constants.masa2_pos[0], Constants.masa2_pos[1], Constants.masa2_size, Constants.masa2_size))
    
    
    
    
    # Movimiento automático solo si el menú está oculto
    if not menu_visible:
        Move_Def.actualizar_movimiento()

    # Mostrar menú si está visible
    Menu.alternar_menu_con_sliders(Screen, menu_visible, eventos)

    # Actualizar pantalla
    pygame.display.flip()

pygame.quit()

