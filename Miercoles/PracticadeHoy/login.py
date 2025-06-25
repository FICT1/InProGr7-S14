# utilizando contraseña para ingresar al
# programa
ARCHIVO = "estudiantes.txt"
CLAVE = "4567"

import pwinput
import os
os.system("cls")

def inicio():
    print("Inicio de Sesion")
    usuarios = cargar_usuario()
    usuario = input("Ingrese su usuario: ")
    clave_ingresada = pwinput.pwinput("Ingrese su contraseña: ", mask="*")
    if usuario in usuarios and usuarios[usuario] == clave_ingresada:
        print("Inicio de sesion exitoso\n")
        return True
    else:
        print("Usuario o contraseña incorrectos\n")
        return False
    

def agregar_usuario(usuario, clave):
    with open("usuario.txt", "a") as archivo:  # CAMBIO: de 'w' a 'a'
        archivo.write(f"{usuario}:{clave}\n")  # Agrega salto de línea

def cargar_usuario():
    usuarios = {}
    if os.path.exists("usuario.txt"):
        with open("usuario.txt", "r") as archivo:
            for linea in archivo:
                if ':' in linea:
                    usuario, clave = linea.strip().split(":")
                    usuarios[usuario] = clave
    return usuarios

if __name__ == "__main__":
    # Esto es solo para agregar usuarios de prueba (puedes comentarlo luego)
    agregar_usuario("admin", "1234")  # 🔹 Agrega este usuario solo una vez

    inicio()
