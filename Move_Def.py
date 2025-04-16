import Constants

def Move_Masas1():
    Constants.contador_longitud_cuerda += 1
    if Constants.contador_longitud_cuerda < Constants.longitud_cuerda_1 - 20:
        Constants.masa1_pos = (Constants.masa1_pos[0], Constants.masa1_pos[1] - 1)
        Constants.end_pos_cuerda_1 = (Constants.end_pos_cuerda_1[0], Constants.end_pos_cuerda_1[1] - 1)
        Constants.masa2_pos = (Constants.masa2_pos[0], Constants.masa2_pos[1] + 1)
        Constants.end_pos_cuerda_2 = (Constants.end_pos_cuerda_2[0], Constants.end_pos_cuerda_2[1] + 1)

def Move_Masas2():
    Constants.contador_longitud_cuerda += 1
    if Constants.contador_longitud_cuerda < Constants.longitud_cuerda_1 - 20:
        Constants.masa1_pos = (Constants.masa1_pos[0], Constants.masa1_pos[1] + 1)
        Constants.end_pos_cuerda_1 = (Constants.end_pos_cuerda_1[0], Constants.end_pos_cuerda_1[1] + 1)
        Constants.masa2_pos = (Constants.masa2_pos[0], Constants.masa2_pos[1] - 1)
        Constants.end_pos_cuerda_2 = (Constants.end_pos_cuerda_2[0], Constants.end_pos_cuerda_2[1] - 1)

def actualizar_movimiento():
    if Constants.masa1_valor > Constants.masa2_valor:
        Move_Masas1()
    elif Constants.masa2_valor > Constants.masa1_valor:
        Move_Masas2()