
# se importa la clase math para calculos matematicos
import math
from constructores.c_circulo import CCircculo

class NegocioCirculo:

    def calcular_area_circulo(self, obj_circulo: CCircculo) -> float: #se crea funcion para calcular el area del circulo, se le pasa un objeto por 
                                                                #parametro y no una variable ya que si requerimos usar una o mas caracteristicas 
                                                                # del objeto pordemos usarlas colocando el nombre del objeto seguido por un punto
    
     # se calcula el area del circulo usando la formula A = pi * r^2, donde r es el radio del circulo el "**" se utiliza para elevar a la potencia, en este caso se eleva el radio al cuadrado
    #area = math.pi * (obj_circulo.radio ** 2)    #** nos entrega un valor entero o decimal dependiendo del valor raiz
        area = math.pi * math.pow(obj_circulo.radio, 2) # math.pow siempre nos entrega un numero con decimales 
        return area
        

    def calcular_perimetro_circulo(self, obj_circulo: CCircculo) -> float:
    # se calcula el perimetro del circulo usando la formula P = 2 * pi * r, donde r es el radio del circulo
        perimetro = 2 * math.pi * obj_circulo.radio
        return perimetro

    def area_mayor_100(self, area: float) -> bool: 
        
        # se verifica si el area del circulo es mayor a 100
        if area > 100:
            return True
        else:
            return False

    