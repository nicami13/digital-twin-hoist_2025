import pygame
import Constants

pygame.init()

# Fuentes
fuente = pygame.font.SysFont("Arial", 20)
fuente_pequena = pygame.font.SysFont("Arial", 16)
fuente_titulo = pygame.font.SysFont("Arial", 28, bold=True)

# Valores iniciales
masa1_valor = Constants.masa1_valor
masa2_valor = Constants.masa2_valor
slider_seleccionado = 0
menu_expandido = False
modo_menu = None

# Botones principales (más pequeños)
boton_graduacion = pygame.Rect(20, 20, 120, 35)
boton_calculo = pygame.Rect(150, 20, 100, 35)
boton_tensiones = pygame.Rect(260, 20, 120, 35)

# Variables para cálculo
definir_input = False
input_texto = ""
mostrar_resultado_calculo = False
resultado_masa1 = 0
Resultado_masa1 = 0
n = 3
input_rect = pygame.Rect(0, 0, 100, 30)
boton_realizar_calculo = pygame.Rect(0, 0, 100, 30)
mostrar_recuadro_principal = False

def alternar_menu_con_sliders(screen, visible, eventos):
    global masa1_valor, masa2_valor, slider_seleccionado, menu_expandido
    global definir_input, input_texto, mostrar_resultado_calculo, resultado_masa1, Resultado_masa1
    global modo_menu, input_rect, boton_realizar_calculo, mostrar_recuadro_principal

    for event in eventos:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if boton_graduacion.collidepoint(event.pos):
                menu_expandido = True
                modo_menu = "graduacion"
            elif boton_calculo.collidepoint(event.pos):
                menu_expandido = True
                modo_menu = "calcular"
            elif boton_tensiones.collidepoint(event.pos):
                menu_expandido = True
                modo_menu = "tensiones"

    if visible:
        # Dibujar botones principales
        pygame.draw.rect(screen, (70, 130, 180), boton_graduacion, border_radius=10)
        screen.blit(fuente.render("Grad. Manual", True, (255, 255, 255)), (boton_graduacion.x + 5, boton_graduacion.y + 8))

        pygame.draw.rect(screen, (180, 70, 130), boton_calculo, border_radius=10)
        screen.blit(fuente.render("Calcular", True, (255, 255, 255)), (boton_calculo.x + 20, boton_calculo.y + 8))

        pygame.draw.rect(screen, (100, 100, 220), boton_tensiones, border_radius=10)
        screen.blit(fuente.render("Tensiones C.", True, (255, 255, 255)), (boton_tensiones.x + 5, boton_tensiones.y + 8))

    if visible and menu_expandido and modo_menu == "graduacion":
        ancho_rect, alto_rect = 300, 280
        x = (Constants.ancho - ancho_rect) // 2
        y = (Constants.Alto - alto_rect) // 2

        def dibujar_slider(x_slider, y_slider, valor, max_valor, color, label):
            largo_slider = 200
            alto_slider = 5
            largo_activo = int((valor / max_valor) * largo_slider)
            pygame.draw.rect(screen, (200, 200, 200), (x_slider, y_slider, largo_slider, alto_slider), border_radius=3)
            pygame.draw.rect(screen, color, (x_slider, y_slider, largo_activo, alto_slider), border_radius=3)
            pygame.draw.circle(screen, color, (x_slider + largo_activo, y_slider + alto_slider // 2), 8)
            screen.blit(fuente.render(f"{label}: {valor}", True, (0, 0, 0)), (x_slider, y_slider - 22))

        pygame.draw.rect(screen, (240, 240, 240), (x, y, ancho_rect, alto_rect), border_radius=12)
        pygame.draw.rect(screen, (0, 0, 120), (x, y, ancho_rect, alto_rect), 3, border_radius=12)
        screen.blit(fuente_titulo.render("Graduación Manual", True, (0, 0, 0)), (x + 30, y + 10))

        dibujar_slider(x + 30, y + 70, masa1_valor, 1000, (0, 100, 255), "Masa 1")
        dibujar_slider(x + 30, y + 120, masa2_valor, 1000, (0, 150, 100), "Masa 2")

        boton_subir = pygame.Rect(x + 30, y + 170, 100, 30)
        boton_bajar = pygame.Rect(x + 160, y + 170, 100, 30)

        pygame.draw.rect(screen, (100, 200, 100), boton_subir, border_radius=6)
        pygame.draw.rect(screen, (200, 100, 100), boton_bajar, border_radius=6)
        screen.blit(fuente.render("Subir", True, (0, 0, 0)), (boton_subir.x + 25, boton_subir.y + 5))
        screen.blit(fuente.render("Bajar", True, (0, 0, 0)), (boton_bajar.x + 25, boton_bajar.y + 5))

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
                elif event.key == pygame.K_ESCAPE:
                    menu_expandido = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if boton_subir.collidepoint(event.pos):
                    masa1_valor, masa2_valor = 40, 150
                elif boton_bajar.collidepoint(event.pos):
                    masa1_valor, masa2_valor = 20, 500

        Constants.masa1_valor = masa1_valor
        Constants.masa2_valor = masa2_valor

    elif visible and menu_expandido and modo_menu == "calcular":
        ancho_rect, alto_rect = 300, 180
        x = (Constants.ancho - ancho_rect) // 2
        y = (Constants.Alto - alto_rect) // 2

        input_rect.update(x + (ancho_rect - 100) // 2, y + 60, 100, 30)
        boton_realizar_calculo.update(x + (ancho_rect - 100) // 2, input_rect.y + 40, 100, 30)

        pygame.draw.rect(screen, (250, 250, 250), (x, y, ancho_rect, alto_rect), border_radius=12)
        pygame.draw.rect(screen, (120, 0, 0), (x, y, ancho_rect, alto_rect), 3, border_radius=12)
        screen.blit(fuente_titulo.render("Cálculo de Masa 1", True, (0, 0, 0)), (x + (ancho_rect - fuente_titulo.size("Cálculo de Masa 1")[0]) // 2, y + 10))

        color_input = (255, 255, 255) if not definir_input else (220, 220, 255)
        pygame.draw.rect(screen, color_input, input_rect, border_radius=5)
        texto_input = fuente.render(input_texto or "masa2", True, (0, 0, 0))
        screen.blit(texto_input, (input_rect.x + (input_rect.width - texto_input.get_width()) // 2, input_rect.y + 5))

        pygame.draw.rect(screen, (150, 150, 250), boton_realizar_calculo, border_radius=6)
        screen.blit(fuente.render("Calcular", True, (0, 0, 0)), (boton_realizar_calculo.x + 15, boton_realizar_calculo.y + 5))

        if mostrar_resultado_calculo:
            texto_resultado = fuente_pequena.render(f"Masa 1 necesaria: {Resultado_masa1:.2f}", True, (0, 0, 0))
            screen.blit(texto_resultado, (x + (ancho_rect - texto_resultado.get_width()) // 2, boton_realizar_calculo.y + 40))

        for event in eventos:
            if event.type == pygame.KEYDOWN:
                if definir_input:
                    if event.key == pygame.K_BACKSPACE:
                        input_texto = input_texto[:-1]
                    elif event.unicode.isdigit() or event.unicode == ".":
                        input_texto += event.unicode
                if event.key == pygame.K_RETURN:
                    try:
                        m2 = float(input_texto)
                        resultado_masa1 = m2 / (2 ** n) * 2.5
                        Resultado_masa1 = resultado_masa1 / 2.5
                        masa1_valor = resultado_masa1
                        masa2_valor = m2
                        Constants.masa1_valor = masa1_valor
                        Constants.masa2_valor = masa2_valor
                        mostrar_resultado_calculo = True
                        mostrar_recuadro_principal = True
                    except:
                        pass
                elif event.key == pygame.K_ESCAPE:
                    menu_expandido = False
                    mostrar_resultado_calculo = False
                    mostrar_recuadro_principal = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                definir_input = input_rect.collidepoint(event.pos)
                if boton_realizar_calculo.collidepoint(event.pos):
                    try:
                        m2 = float(input_texto)
                        resultado_masa1 = m2 / (2 ** n) * 2.5
                        Resultado_masa1 = resultado_masa1 / 2.5
                        masa1_valor = resultado_masa1
                        masa2_valor = m2
                        Constants.masa1_valor = masa1_valor
                        Constants.masa2_valor = masa2_valor
                        mostrar_resultado_calculo = True
                        mostrar_recuadro_principal = True
                    except:
                        pass

    elif visible and menu_expandido and modo_menu == "tensiones":
        ancho_rect, alto_rect = 350, 280
        x = (Constants.ancho - ancho_rect) // 2
        y = (Constants.Alto - alto_rect) // 2

        pygame.draw.rect(screen, (240, 240, 255), (x, y, ancho_rect, alto_rect), border_radius=12)
        pygame.draw.rect(screen, (0, 0, 180), (x, y, ancho_rect, alto_rect), 3, border_radius=12)
        screen.blit(fuente_titulo.render("Tensiones en Cables", True, (0, 0, 0)), (x + 40, y + 10))

        gravedad = 9.8
        R = masa2_valor * gravedad
        tensiones = [R / 2, R / 2, R / 4, R / 4, R / 8, R / 8]

        for i, t in enumerate(tensiones):
            texto = fuente.render(f"Tensión cable {i+1}: {t:.2f} N", True, (0, 0, 0))
            screen.blit(texto, (x + 30, y + 50 + i * 30))

        texto_f = fuente.render(f"F (fuerza aplicada): {R / 8:.2f} N", True, (180, 0, 0))
        screen.blit(texto_f, (x + 30, y + 50 + len(tensiones) * 30))

        for event in eventos:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                menu_expandido = False

def obtener_resultado():
    return mostrar_resultado_calculo, resultado_masa1, mostrar_recuadro_principal

def dibujar_recuadro_masa(screen):
    if mostrar_recuadro_principal:
        rect = pygame.Rect(10, 70, 180, 30)
        pygame.draw.rect(screen, (255, 255, 220), rect, border_radius=6)
        pygame.draw.rect(screen, (180, 180, 100), rect, 2, border_radius=6)
        screen.blit(fuente_pequena.render(f"Masa 1 necesaria: {Resultado_masa1:.2f}", True, (0, 0, 0)), (rect.x + 10, rect.y + 7))







