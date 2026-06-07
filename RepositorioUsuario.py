import Usuario
import random

usuarios = []

#Mantenimiento de un CRUD (Create, Read, Update, Delete)

#CREATE
def crearUsuario():

    cedula = random.randint(100000000, 899999999)

    for usuario in usuarios:
        if usuario.cedula == cedula:
            print("Esta cedula ya esta en el registro")
            return

    nombre = input("Ingrese su nombre: ")

    anno = int(input("Ingrese su anno de nacimiento: "))
    mes = int(input("Ingrese su mes de nacimiento: "))
    dia = int(input("Ingrese su dia de nacimiento: "))

    nuevo_usuario = Usuario.Usuario(cedula, nombre, anno, mes, dia )
    usuarios.append(nuevo_usuario)  

    print("Usuario agregado satisfactoriamente")

#READ 
def leerUsuarios():
    
    if len(usuarios) == 0:
        print("No hay usuarios en el sistema")
        return
    
    for usuario in usuarios:
        usuario.mostrarDatos()
    
def buscarUsuario():
    cedula = int(input("Digite su cedula: ")) 
    for usuario in usuarios:
        if usuario.cedula == cedula:
            return usuario
    
    return None

#UPDATE
def actualizarUsuario():
    usuario = buscarUsuario()

    if usuario:
        nombre = input("Digite su nuevo nombre: ")

        usuario.nombre = nombre
        print("Se ha actualizado con exito")

    else:
        print("No se ha encontrado el usuario que quiere modificar.")

def eliminarUsuario():
    usuario = buscarUsuario()

    if usuario:
        usuarios.remove(usuario)
        print("Se ha eliminado con exito")

    else:
        print("No se ha encontrado el usuario que quiere eliminar.")