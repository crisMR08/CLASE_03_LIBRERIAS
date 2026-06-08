#importacion de clase circulo y sus funciones
from Ejercicios_Notebook.vistas.v_circulo import ejecutar_ejercicio_circulo
#from Principal import menu

class Principal:
    
    #se crea un menu para organizar los diferentes ejercicios.
    def menu():
        try:
            while True:
                print("-----Listado de ejercicios-----",
                  "1. Ejercicio 1: Calcular el area y perimetro de un circulo ⚽",
                      "2. Ejercicio 2: Calculo de edad exacta 🤔",
                      "3. Ejercicio 3: Generador de combinaciones 🙌",
                      "4. Ejercicio 4: Historial de comandos interactivo 🖥️",
                      "5. Ejercicio 5: Estadisticas simples 📊" ,
                      "6. Salir 🚪", sep="\n")
                
                #se solicita y almacena el valor deseado por el usuario para ejecutar el ejercicio correspondiente
                opcion = int(input("Ingrese el numero del ejercicio que desea ejecutar: "))
                
                if opcion == 1:
                    ejecutar_ejercicio_circulo()
                elif opcion == 2:
                    break
                elif opcion == 3:
                    break
                elif opcion == 4:
                    break   
                elif opcion == 5:
                    break   
                elif opcion == 6:
                    print("Gracias por usar el programa, hasta luego!")
                    break
                else:
                    print("Opcion no valida, por favor ingrese una opcion valida.") 
        except ValueError:
            print("Error: Ingrese un numero valido.")
           # menu() # se llama a la funcion menu() para que el usuario pueda volver a ingresar una opcion valida despues de haber ingresado un valor no valido
            
        
    menu()