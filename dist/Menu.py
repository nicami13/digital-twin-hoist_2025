import pygame
import Constants

pygame.init()

mostrar_error = False
mensaje_error = ""

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

# Botones principales
boton_graduacion = pygame.Rect(20, 20, 120, 35)
boton_calculo = pygame.Rect(150, 20, 100, 35)
boton_tensiones = pygame.Rect(260, 20, 120, 35)

# Variables cálculo
definir_input = False
input_texto = ""
input_texto_velocidad= Constants.input_texto_velocidad
input_texto_masa2 = Constants.input_texto_masa2
velocidad_deseada = Constants.velocidad_deseada
definir_input = Constants.definir_input
mostrar_resultado_calculo = False
resultado_masa1 = 0
Resultado_masa1 = 0
input_rect = pygame.Rect(0, 0, 100, 30)
boton_realizar_calculo = pygame.Rect(0, 0, 100, 30)
mostrar_recuadro_principal = False

# Rect para velocidad
input_rect_velocidad = pygame.Rect(0, 0, 100, 30)
Constants.input_velocidad = ""

def alternar_menu_con_sliders(screen, visible, eventos):
    global masa1_valor, masa2_valor, slider_seleccionado, menu_expandido
    global input_texto_velocidad,input_texto_masa2, velocidad_deseada, definir_input
    global definir_input, input_texto, mostrar_resultado_calculo, resultado_masa1, Resultado_masa1,input_texto_velocidad
    global modo_menu, input_rect, boton_realizar_calculo, mostrar_recuadro_principal, input_rect_velocidad,mostrar_error,mensaje_error

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
        pygame.draw.rect(screen, (70, 130, 180), boton_graduacion, border_radius=10)
        screen.blit(fuente.render("Grad. Manual", True, (255, 255, 255)), (boton_graduacion.x + 5, boton_graduacion.y + 8))

        pygame.draw.rect(screen, (180, 70, 130), boton_calculo, border_radius=10)
        screen.blit(fuente.render("Calcular", True, (255, 255, 255)), (boton_calculo.x + 20, boton_calculo.y + 8))

        pygame.draw.rect(screen, (100, 100, 220), boton_tensiones, border_radius=10)
        screen.blit(fuente.render("Tensiones C.", True, (255, 255, 255)), (boton_tensiones.x + 5, boton_tensiones.y + 8))

    if visible and menu_expandido and modo_menu == "graduacion":
        # Menu de graduación manual
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
        ancho_rect, alto_rect = 360, 310
        x = (Constants.ancho - ancho_rect) // 2
        y = (Constants.Alto - alto_rect) // 2

        input_rect_velocidad.update(x + 150, y + 65, 120, 30)
        input_rect_masa2 = pygame.Rect(x + 150, y + 115, 120, 30)
        boton_realizar_calculo.update(x + (ancho_rect - 100) // 2, y + 230, 100, 35)

        pygame.draw.rect(screen, (250, 250, 250), (x, y, ancho_rect, alto_rect), border_radius=14)
        pygame.draw.rect(screen, (120, 0, 0), (x, y, ancho_rect, alto_rect), 3, border_radius=14)

        titulo = fuente_titulo.render("Cálculos", True, (0, 0, 0))
        screen.blit(titulo, (x + (ancho_rect - titulo.get_width()) // 2, y + 15))

        screen.blit(fuente.render("Velocidad:", True, (0, 0, 0)), (x + 30, y + 70))
        screen.blit(fuente.render("Masa 2 manual:", True, (0, 0, 0)), (x + 30, y + 120))
        screen.blit(fuente.render("Masa 1 resultante:", True, (0, 0, 0)), (x + 30, y + 165))

        pygame.draw.rect(screen, (255, 255, 255), input_rect_velocidad, border_radius=6)
        screen.blit(fuente.render(f'{input_texto_velocidad} m/s', True, (0, 0, 0)), (input_rect_velocidad.x + 5, input_rect_velocidad.y + 5))

        pygame.draw.rect(screen, (255, 255, 255), input_rect_masa2, border_radius=6)
        screen.blit(fuente.render(f'{input_texto_masa2} kg' , True, (0, 0, 0)), (input_rect_masa2.x + 50, input_rect_masa2.y + 5))

        # ACTUALIZACIÓN AUTOMÁTICA EN TIEMPO REAL
        try:
            if definir_input == "velocidad":
                velocidad_deseada = float(input_texto_velocidad or 0)
                Constants.masa2_valor = velocidad_deseada * 8
                Constants.masa1_valor = velocidad_deseada * 2.5
                input_texto_masa2 = f"{Constants.masa2_valor:.2f}"
            elif definir_input == "masa2":
                Constants.masa2_valor = float(input_texto_masa2 or 0)
                velocidad_deseada = Constants.masa2_valor / 8
                Constants.masa1_valor = velocidad_deseada * 2.5
                input_texto_velocidad = f"{velocidad_deseada:.2f}"
        except:
            Constants.masa1_valor = 0
            Constants.masa2_valor = 0

        texto_m1 = fuente.render(f"{Constants.masa1_valor:.2f} kg", True, (0, 0, 0))
        screen.blit(texto_m1, (x + 200, y + 165))

        pygame.draw.rect(screen, (170, 170, 255), boton_realizar_calculo, border_radius=8)
        screen.blit(fuente.render("Aplicar", True, (0, 0, 0)), (boton_realizar_calculo.x + 25, boton_realizar_calculo.y + 7))

        fuente_error = pygame.font.SysFont("Arial", 10)
        if mostrar_error:
            rect_error = pygame.Rect(x + 20, y + 275, ancho_rect - 40, 40)
            pygame.draw.rect(screen, (255, 220, 220), rect_error, border_radius=6)
            pygame.draw.rect(screen, (200, 0, 0), rect_error, 2, border_radius=6)
            mensaje_renderizado = fuente_error.render(mensaje_error, True, (150, 0, 0))
            screen.blit(mensaje_renderizado, (rect_error.x + 10, rect_error.y + 10))

        for event in eventos:
            if event.type == pygame.KEYDOWN:
                if definir_input == "velocidad":
                    if event.key == pygame.K_BACKSPACE:
                        input_texto_velocidad = input_texto_velocidad[:-1]
                    elif event.unicode.isdigit() or event.unicode in ".-":
                        input_texto_velocidad += event.unicode
                elif definir_input == "masa2":
                    if event.key == pygame.K_BACKSPACE:
                        input_texto_masa2 = input_texto_masa2[:-1]
                    elif event.unicode.isdigit() or event.unicode in ".-":
                        input_texto_masa2 += event.unicode

                if event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                    try:
                        if -2 <= velocidad_deseada <= 2:
                            mostrar_resultado_calculo = True
                            mostrar_recuadro_principal = True
                            mostrar_error = False
                        else:
                            mostrar_error = True
                            mensaje_error = "Haz generado una falla en el sistema: ruptura de cuerda 1 o cuerda 6"
                    except:
                        mostrar_error = True
                        mensaje_error = "Entrada inválida"

                elif event.key == pygame.K_ESCAPE:
                    try:
                        if not (-3 <= velocidad_deseada <= 3):
                            mostrar_error = True
                            mensaje_error = "Haz generado una falla en el sistema: ruptura de cuerda 1 o cuerda 6"
                        else:
                            menu_expandido = False
                            mostrar_resultado_calculo = False
                            mostrar_error = False
                    except:
                        mostrar_error = True
                        mensaje_error = "Entrada inválida"

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect_velocidad.collidepoint(event.pos):
                    definir_input = "velocidad"
                elif input_rect_masa2.collidepoint(event.pos):
                    definir_input = "masa2"
                elif boton_realizar_calculo.collidepoint(event.pos):
                    try:
                        if -2 <= velocidad_deseada <= 2:
                            mostrar_resultado_calculo = True
                            mostrar_recuadro_principal = True
                            mostrar_error = False
                        else:
                            mostrar_error = True
                            mensaje_error = "Haz generado una falla en el sistema: ruptura de cuerda 1 o cuerda 6"
                    except:
                        mostrar_error = True
                        mensaje_error = "Entrada inválida"




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


