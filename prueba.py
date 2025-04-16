import pygame
import Constants

def dibujar_sistema(pantalla):
    pantalla.fill(Constants.Blanco)

    # 1. Draw Support Bar
    pygame.draw.line(pantalla, Constants.Negro,
                     (Constants.pos_soporte_inicio_x, Constants.pos_soporte_y),
                     (Constants.pos_soporte_fin_x, Constants.pos_soporte_y), 5)

    # 2. Draw Pulleys
    # Fixed Pulley
    pygame.draw.circle(pantalla, Constants.Azul, Constants.pos_polea_fija, Constants.radio_polea)
    pygame.draw.circle(pantalla, Constants.Negro, Constants.pos_polea_fija, Constants.radio_polea, 2) # Outline
    # Link fixed pulley to support
    pygame.draw.line(pantalla, Constants.Negro,
                     (Constants.pos_polea_fija[0], Constants.pos_soporte_y),
                     (Constants.pos_polea_fija[0], Constants.pos_polea_fija[1] - Constants.radio_polea), 3)


    # Movable Pulleys
    for pos in Constants.pos_poleas_moviles:
        pygame.draw.circle(pantalla, Constants.Azul, pos, Constants.radio_polea)
        pygame.draw.circle(pantalla, Constants.Negro, pos, Constants.radio_polea, 2) # Outline

    # 3. Draw Load
    load_rect = pygame.Rect(Constants.pos_carga[0], Constants.pos_carga[1], Constants.size_carga[0], Constants.size_carga[1])
    pygame.draw.rect(pantalla, Constants.Rojo, load_rect)
    # Link load to last movable pulley (simple line)
    last_pulley_pos = Constants.pos_poleas_moviles[-1]
    load_attach_point = (load_rect.centerx, load_rect.top)
    pulley_bottom = (last_pulley_pos[0], last_pulley_pos[1] + Constants.radio_polea)
    pygame.draw.line(pantalla, Constants.Negro, pulley_bottom, load_attach_point, 3)
    # Maybe draw a hook or bracket for movable pulleys later

    # 4. Draw Effort Mass
    effort_rect = pygame.Rect(Constants.pos_esfuerzo[0], Constants.pos_esfuerzo[1], Constants.size_esfuerzo[0], Constants.size_esfuerzo[1])
    pygame.draw.rect(pantalla, Constants.Verde, effort_rect)


    # 5. Draw Rope (Simplified: Vertical Lines connecting key points)
    # This requires careful ordering based on the path:
    # Anchor1 -> P3(bottom) -> P0(top) -> P2(bottom) -> P1(top) -> Anchor2
    # Effort Rope: P0(top) -> Effort Mass

    p0 = Constants.pos_polea_fija
    p1, p2, p3 = Constants.pos_poleas_moviles[0], Constants.pos_poleas_moviles[1], Constants.pos_poleas_moviles[2] # Assuming order P1, P2, P3 top-down
    a1 = Constants.pos_anclaje_1
    a2 = Constants.pos_anclaje_2
    eff = effort_rect.midtop # Attach point for effort mass

    # Define points on pulleys (approximate top/bottom)
    p0_top = (p0[0], p0[1] - Constants.radio_polea)
    p0_bottom = (p0[0], p0[1] + Constants.radio_polea)
    p1_top = (p1[0], p1[1] - Constants.radio_polea)
    p1_bottom = (p1[0], p1[1] + Constants.radio_polea)
    p2_top = (p2[0], p2[1] - Constants.radio_polea)
    p2_bottom = (p2[0], p2[1] + Constants.radio_polea)
    p3_top = (p3[0], p3[1] - Constants.radio_polea)
    p3_bottom = (p3[0], p3[1] + Constants.radio_polea)

    rope_color = Constants.Negro
    rope_width = 2

    # Segment 1: Anchor 1 to P3 Bottom (via side)
    pygame.draw.line(pantalla, rope_color, a1, (p3_bottom[0] - Constants.radio_polea, a1[1]), rope_width) # Horizontal from anchor
    pygame.draw.line(pantalla, rope_color, (p3_bottom[0] - Constants.radio_polea, a1[1]), (p3_bottom[0] - Constants.radio_polea, p3_bottom[1]), rope_width) # Down
    pygame.draw.line(pantalla, rope_color, (p3_bottom[0] - Constants.radio_polea, p3_bottom[1]), p3_bottom, rope_width) # Under pulley (arc needed ideally)

    # Segment 2: P3 Bottom to P0 Top (via side)
    pygame.draw.line(pantalla, rope_color, p3_bottom, (p3_bottom[0] + Constants.radio_polea, p3_bottom[1]), rope_width) # Under pulley
    pygame.draw.line(pantalla, rope_color, (p3_bottom[0] + Constants.radio_polea, p3_bottom[1]), (p0_top[0] + Constants.radio_polea, p3_bottom[1]), rope_width) # Vertical up
    pygame.draw.line(pantalla, rope_color, (p0_top[0] + Constants.radio_polea, p3_bottom[1]), (p0_top[0] + Constants.radio_polea, p0_top[1]), rope_width) # Vertical up
    pygame.draw.line(pantalla, rope_color, (p0_top[0] + Constants.radio_polea, p0_top[1]), p0_top, rope_width) # To pulley top (arc needed ideally)

    # Segment 3: P0 Top to P2 Bottom
    pygame.draw.line(pantalla, rope_color, p0_top, (p0_top[0] - Constants.radio_polea, p0_top[1]), rope_width) # Over pulley
    pygame.draw.line(pantalla, rope_color, (p0_top[0] - Constants.radio_polea, p0_top[1]), (p2_bottom[0] - Constants.radio_polea, p0_top[1]), rope_width) # Vertical Down
    pygame.draw.line(pantalla, rope_color, (p2_bottom[0] - Constants.radio_polea, p0_top[1]), (p2_bottom[0] - Constants.radio_polea, p2_bottom[1]), rope_width) # Vertical Down
    pygame.draw.line(pantalla, rope_color, (p2_bottom[0] - Constants.radio_polea, p2_bottom[1]), p2_bottom, rope_width) # To pulley bottom

    # Segment 4: P2 Bottom to P1 Top
    pygame.draw.line(pantalla, rope_color, p2_bottom, (p2_bottom[0] + Constants.radio_polea, p2_bottom[1]), rope_width) # Under pulley
    pygame.draw.line(pantalla, rope_color, (p2_bottom[0] + Constants.radio_polea, p2_bottom[1]), (p1_top[0] + Constants.radio_polea, p2_bottom[1]), rope_width) # Vertical Up
    pygame.draw.line(pantalla, rope_color, (p1_top[0] + Constants.radio_polea, p2_bottom[1]), (p1_top[0] + Constants.radio_polea, p1_top[1]), rope_width) # Vertical Up
    pygame.draw.line(pantalla, rope_color, (p1_top[0] + Constants.radio_polea, p1_top[1]), p1_top, rope_width) # To pulley top

    # Segment 5: P1 Top to Anchor 2
    pygame.draw.line(pantalla, rope_color, p1_top, (p1_top[0] - Constants.radio_polea, p1_top[1]), rope_width) # Over pulley
    pygame.draw.line(pantalla, rope_color, (p1_top[0] - Constants.radio_polea, p1_top[1]), (a2[0], p1_top[1]), rope_width) # Vertical Up
    pygame.draw.line(pantalla, rope_color, (a2[0], p1_top[1]), a2, rope_width) # Horizontal to Anchor

    # Effort Rope Segment: P0 Top to Effort Mass
    # (This assumes effort pulls from top-left side of fixed pulley)
    pygame.draw.line(pantalla, rope_color, (p0_top[0] - Constants.radio_polea, p0_top[1]), (eff[0], p0_top[1]), rope_width) # Horizontal from pulley top-left side? This might need adjustment based on where effort pulls from P0. Let's assume it comes straight down from P0's attachment point for simplicity.
    pygame.draw.line(pantalla, rope_color, (p0[0], p0_top[1]), (p0[0], eff[1]), rope_width) # Simpler: Vertical from P0 center down
    pygame.draw.line(pantalla, rope_color, (p0[0], eff[1]), eff, rope_width) # Horizontal to effort mass mid-top
    # --> Adjust this line based on desired visual connection point


    # --- Display Update ---
    pygame.display.flip() # Update the full display