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
    alto_rectangulo = 300
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

        dibujar_slider(x + 50, y + 60, masa1_valor, 1000, (0, 100, 255), "Masa 1")
        dibujar_slider(x + 50, y + 130, masa2_valor, 1000, (0, 150, 100), "Masa 2")

        # Dibujar botones
        boton_subir = pygame.Rect(x + 40, y + 200, 100, 30)
        boton_bajar = pygame.Rect(x + 160, y + 200, 100, 30)

        pygame.draw.rect(screen, (100, 200, 100), boton_subir)
        pygame.draw.rect(screen, (200, 100, 100), boton_bajar)

        texto_subir = fuente.render("Subir", True, (0, 0, 0))
        texto_bajar = fuente.render("Bajar", True, (0, 0, 0))
        screen.blit(texto_subir, (boton_subir.x + 25, boton_subir.y + 5))
        screen.blit(texto_bajar, (boton_bajar.x + 25, boton_bajar.y + 5))

        for event in eventos:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    slider_seleccionado = 1
                elif event.key == pygame.K_2:
                    slider_seleccionado = 2
                elif event.key == pygame.K_UP:
                    if slider_seleccionado == 1 and masa1_valor < 1000:
                        masa1_valor += 1
                    elif slider_seleccionado == 2 and masa2_valor < 1000:
                        masa2_valor += 1
                elif event.key == pygame.K_DOWN:
                    if slider_seleccionado == 1 and masa1_valor > 0:
                        masa1_valor -= 1
                    elif slider_seleccionado == 2 and masa2_valor > 0:
                        masa2_valor -= 1

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if boton_subir.collidepoint(event.pos):
                    # masa1 gana → sistema sube
                    masa1_valor = 40
                    masa2_valor = 150
                elif boton_bajar.collidepoint(event.pos):
                    # masa2 gana → sistema baja
                    masa1_valor = 20
                    masa2_valor = 500

        # Asignar valores reales a Constants (respetando el orden correcto)
        Constants.masa1_valor = masa1_valor
        Constants.masa2_valor = masa2_valor
