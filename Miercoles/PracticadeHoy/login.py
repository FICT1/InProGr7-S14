# login.py
import pwinput
import os

ARCHIVO_USUARIOS = "usuario.txt"

def agregar_usuario(usuario, clave):
    with open(ARCHIVO_USUARIOS, "a") as archivo:
        archivo.write(f"{usuario}:{clave}\n")

def cargar_usuario():
    usuarios = {}
    if os.path.exists(ARCHIVO_USUARIOS):
        with open(ARCHIVO_USUARIOS, "r") as archivo:
            for linea in archivo:
                if ':' in linea:
                    usuario, clave = linea.strip().split(":")
                    usuarios[usuario] = clave
    return usuarios

def iniciar_sesion():
    print("\n--- Inicio de sesión ---")
    usuarios = cargar_usuario()
    usuario = input("Ingrese su usuario: ")
    clave_ingresada = pwinput.pwinput("Ingrese su contraseña: ", mask="*")
    if usuario in usuarios and usuarios[usuario] == clave_ingresada:
        print("Inicio de sesión exitoso.\n")
    else:
        print("Usuario o contraseña incorrectos.\n")

def menu():
    print("\n--- Menú Principal ---")
    print("1. Agregar usuario")
    print("2. Iniciar sesión")
    print("3. Salir")
    return input("Ingrese una opción: ")

def menu_principal():
    while True:
        opcion = menu()
        if opcion == "1":
            usuario = input("Ingrese su nuevo usuario: ")
            clave = input("Ingrese su contraseña: ")
            agregar_usuario(usuario, clave)
        elif opcion == "2":
            iniciar_sesion()
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
