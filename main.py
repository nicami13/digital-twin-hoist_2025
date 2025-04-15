import pygame
import Constants
import Move_Def
import Menu

pygame.init()
Screen = pygame.display.set_mode((Constants.ancho, Constants.Alto))
Clock = pygame.time.Clock()
simulation_time = 0
running = True
menu_visible = False

while running:
    dt = Clock.tick(60)
    simulation_time += dt

    eventos = pygame.event.get()

    for event in eventos:
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                menu_visible = not menu_visible

    Screen.fill(Constants.WHITE)

    pygame.draw.line(Screen, Constants.BLACK, Constants.start_pos_cuerda_1, Constants.end_pos_cuerda_1, 5)
    pygame.draw.rect(Screen, Constants.RED, (Constants.masa1_pos[0], Constants.masa1_pos[1], Constants.masa1_size, Constants.masa1_size))
    pygame.draw.line(Screen, Constants.BLACK, Constants.start_pos_cuerda_2, Constants.end_pos_cuerda_2, 5)
    pygame.draw.rect(Screen, Constants.RED, (Constants.masa2_pos[0], Constants.masa2_pos[1], Constants.masa2_size, Constants.masa2_size))
    pygame.draw.line(Screen, Constants.BLACK, (0, 20), (600, 20), 10)
    pygame.draw.line(Screen, Constants.BLACK, (Constants.polea_pos[0], Constants.polea_pos[1]), (Constants.polea_pos[0], Constants.polea_pos[1] - 80), 7)
    pygame.draw.circle(Screen, Constants.BLUE, Constants.polea_pos, Constants.polea_radius)

    if not menu_visible:
        if Constants.masa1_valor == Constants.masa2_valor:
            pass
        elif Constants.masa1_valor < Constants.masa2_valor:
            Move_Def.Move_Masas1()
        elif Constants.masa1_valor > Constants.masa2_valor:
            Move_Def.Move_Masas2()

    Menu.alternar_menu_con_sliders(Screen, menu_visible, eventos)
    pygame.display.flip()

pygame.quit()
