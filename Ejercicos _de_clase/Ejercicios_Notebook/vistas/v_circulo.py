
#Se importan el constructor y la clase de negocio para poder usar sus funciones y caracteristicas en esta vista, la cual se encargara de mostrar los resultados al usuario.
from Ejercicios_Notebook.constructores.c_circulo import CCircculo
from Ejercicios_Notebook.negocio.n_circulo import NegocioCirculo


def ejecutar_ejercicio_circulo():
    
    print("-----Determinar el area y perimetro de un circulo en base a su radio-----")
    # se solicita al usuario que ingrese el radio del circulo
    radio = float(input("Ingrese el radio del circulo: "))
    
    #se crea un objeto de tipo circulo (constructor) y se le asigna el valor del radio ingresado por el usuario
    obj_circulo = CCircculo(radio)  #capa de contrutores
    
    # se crea un objeto de tipo negocio circulo para poder usar sus funciones
    obj_negocio_circulo = NegocioCirculo()  # capa de negocio
    
    #se calcula el area del circulo usando la funcion calcular_area_circulo del objeto de negocio circulo, se le pasa como parametro el objeto circulo(obj_circulo)
    area = obj_negocio_circulo.calcular_area_circulo(obj_circulo) # trabaja la capa de negocio, con la capa de contructores
    
    # se calcula el perimetro del circulo usando la funcion calcular_perimetro_circulo del objeto de negocio circulo, se le pasa como parametro el objeto circulo creado anteriormente
    perimetro = obj_negocio_circulo.calcular_perimetro_circulo(obj_circulo) #trabaja la capa ne negocio con la capa de constructores
    
    # se calcula si el area es mayor a 100 usando la funcion area_mayor_100 del objeto de negocio circulo, se le pasa como parametro el area
    es_mayor_100 = obj_negocio_circulo.area_mayor_100(area) #trabaja la capa de negocio y se pasa como parametro el area calculada anteriormente
    
    # se muestra el resultado al usuario
    print(f"El area del circulo es: {area:.2f}") # se muestra el area del circulo con 2 decimales usando el formato de cadena f-string
    print(f"El perimetro del circulo es: {perimetro:.2f}") # se muestra el perimetro del circulo con 2 decimales usando el formato de cadena f-string
    if es_mayor_100: # se verifica si el area es mayor a 100, si es verdadero se muestra un mensaje indicando que el area es mayor a 100, de lo contrario se muestra un mensaje indicando que el area no es mayor a 100
        print("El area del circulo es mayor a 100") 
    else:
        print("El area del circulo no es mayor a 100")
        