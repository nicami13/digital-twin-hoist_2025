import pygame
import Constants

pygame.init()
fuente = pygame.font.SysFont("Arial", 20)

masa1_valor = Constants.masa1_valor
masa2_valor = Constants.masa2_valor
slider_seleccionado = 0

def alternar_menu_con_sliders(screen, visible, eventos):
    global masa1_valor, masa2_valor, slider_seleccionado

    ancho_rectangulo = 300
    alto_rectangulo = 250
    x = (Constants.ancho - ancho_rectangulo) // 2
    y = (Constants.Alto - alto_rectangulo) // 2

    if visible:
        pygame.draw.rect(screen, (180, 180, 180), (x, y, ancho_rectangulo, alto_rectangulo))
        pygame.draw.rect(screen, (0, 0, 255), (x, y, ancho_rectangulo, alto_rectangulo), 4)

        def dibujar_slider(x_slider, y_slider, valor, max_valor, color, label):
            largo_slider = 200
            alto_slider = 6
            radio_punto = 10
            largo_activo = int((valor / max_valor) * largo_slider)
            pygame.draw.rect(screen, (150, 150, 150), (x_slider, y_slider, largo_slider, alto_slider))
            pygame.draw.rect(screen, color, (x_slider, y_slider, largo_activo, alto_slider))
            pygame.draw.circle(screen, color, (x_slider + largo_activo, y_slider + alto_slider // 2), radio_punto)
            texto = fuente.render(f"{label}: {valor}", True, (0, 0, 0))
            screen.blit(texto, (x_slider, y_slider - 25))

        dibujar_slider(x + 50, y + 60, masa1_valor, 100, (0, 100, 255), "Masa 1")
        dibujar_slider(x + 50, y + 130, masa2_valor, 100, (0, 150, 100), "Masa 2")

        for event in eventos:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    slider_seleccionado = 1
                elif event.key == pygame.K_2:
                    slider_seleccionado = 2
                elif event.key == pygame.K_UP:
                    if slider_seleccionado == 1 and masa1_valor < 100:
                        masa1_valor += 1
                    elif slider_seleccionado == 2 and masa2_valor < 100:
                        masa2_valor += 1
                elif event.key == pygame.K_DOWN:
                    if slider_seleccionado == 1 and masa1_valor > 0:
                        masa1_valor -= 1
                    elif slider_seleccionado == 2 and masa2_valor > 0:
                        masa2_valor -= 1

        # Asignar valores reales a Constants (sin tocar tamaños visuales)
        Constants.masa1_valor = masa2_valor
        Constants.masa2_valor = masa1_valor
