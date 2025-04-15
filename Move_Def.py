import Constants

def Move_Masas1():
    limite_superior = Constants.polea_pos[1] + Constants.polea_radius  # margen para el centro del círculo
    limite_inferior = Constants.Alto - Constants.masa2_size - 20

    if Constants.masa1_pos[1] > limite_superior and Constants.masa2_pos[1] < limite_inferior:
        Constants.masa1_pos = (Constants.masa1_pos[0], Constants.masa1_pos[1] - 1)
        Constants.end_pos_cuerda_1 = (Constants.end_pos_cuerda_1[0], Constants.end_pos_cuerda_1[1] - 1)

        Constants.masa2_pos = (Constants.masa2_pos[0], Constants.masa2_pos[1] + 1)
        Constants.end_pos_cuerda_2 = (Constants.end_pos_cuerda_2[0], Constants.end_pos_cuerda_2[1] + 1)


def Move_Masas2():
    limite_superior = Constants.polea_pos[1] + Constants.polea_radius
    limite_inferior = Constants.Alto - Constants.masa1_size - 20

    if Constants.masa1_pos[1] < limite_inferior and Constants.masa2_pos[1] > limite_superior:
        Constants.masa1_pos = (Constants.masa1_pos[0], Constants.masa1_pos[1] + 1)
        Constants.end_pos_cuerda_1 = (Constants.end_pos_cuerda_1[0], Constants.end_pos_cuerda_1[1] + 1)

        Constants.masa2_pos = (Constants.masa2_pos[0], Constants.masa2_pos[1] - 1)
        Constants.end_pos_cuerda_2 = (Constants.end_pos_cuerda_2[0], Constants.end_pos_cuerda_2[1] - 1)


def actualizar_movimiento():
    if Constants.masa2_valor > Constants.masa1_valor:
        Move_Masas1()
    elif Constants.masa1_valor > Constants.masa2_valor:
        Move_Masas2()


