class Polea:  
    def __init__(self, radio):  
        self.radio = radio  

    def calcular_desplazamiento(self, fuerza):  
        # El desplazamiento es inversamente proporcional al radio  
        return fuerza / self.radio  


def main():  
    # Fuerza aplicada en el sistema  
    fuerza_total = 10  # por ejemplo, en Newtons  
    
    # Definir el radio de las poleas  
    radio = 8  # Por ejemplo, puedes cambiarlo según el caso  

    # Crear una polea  
    polea = Polea(radio)  

    # Calcular desplazamiento  
    desplazamiento = polea.calcular_desplazamiento(fuerza_total)  
    print(f"Desplazamiento de cada polea con radio {radio}: {desplazamiento:.2f} m")  


if __name__ == "__main__":  
    main()  