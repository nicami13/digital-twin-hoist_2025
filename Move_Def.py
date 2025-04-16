import time  
import Constants  

def Move_Masas1():  
    Constants.contador_longitud_cuerda += 1  
    if Constants.contador_longitud_cuerda < Constants.longitud_cuerda_1 - 20:  
        # Actualiza posición masa 1  
        Constants.masa1_pos = (  
            Constants.masa1_pos[0],  
            Constants.masa1_pos[1] - 1  
        )  
        # Actualiza cuerda 1  
        Constants.end_pos_cuerda_1 = (  
            Constants.end_pos_cuerda_1[0],  
            Constants.end_pos_cuerda_1[1] - 1  
        )  
        # Actualiza posición masa 2  
        Constants.masa2_pos = (  
            Constants.masa2_pos[0],  
            Constants.masa2_pos[1] + 1  
        )  
        # Actualiza cuerda 2  
        Constants.end_pos_cuerda_2 = (  
            Constants.end_pos_cuerda_2[0],  
            Constants.end_pos_cuerda_2[1] + 1  
        )  

def Move_Masas2():  
    Constants.contador_longitud_cuerda += 1  
    if Constants.contador_longitud_cuerda < Constants.longitud_cuerda_1 - 20:  
        Constants.masa1_pos = (Constants.masa1_pos[0], Constants.masa1_pos[1] + 1)  
        Constants.end_pos_cuerda_1 = (Constants.end_pos_cuerda_1[0], Constants.end_pos_cuerda_1[1] + 1)  
        Constants.masa2_pos = (Constants.masa2_pos[0], Constants.masa2_pos[1] - 1)  
        Constants.end_pos_cuerda_2 = (Constants.end_pos_cuerda_2[0], Constants.end_pos_cuerda_2[1] - 1)  

def run_simulation():  
    while Constants.contador_longitud_cuerda < Constants.longitud_cuerda_1 - 20:  
        Move_Masas1()  # Llama a Move_Masas1 o Move_Masas2 según tus necesidades  
        print("Posición Masa 1:", Constants.masa1_pos)  
        print("Posición Masa 2:", Constants.masa2_pos)  
        print("Contador de longitud de cuerda:", Constants.contador_longitud_cuerda)  

          
        time.sleep(0.5)  