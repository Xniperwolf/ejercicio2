contactos = []
import csv

def menucontactos():
    print("Bienvenido al programa de contactos")
    print("-----------------------------------")
    print("1. Agregar contactos a la lista")
    print("2. Mostrar contactos de la lista")
    print("3. Guardar contactos en CSV")
    print("4. Salir")

    while True:
        try:
            opc = int(input("Ingrese opción: "))
            if opc in (1,2,3,4):
                break
            else:
                print("Ingrese una opción correcta entre 1 y 4")
        except:
            print("Debe ser un número entero")

def agregarcontacto():
    nombreyapellido_contacto = validar_nombre()
    numerotelefono_contacto = validar_telefono()
    correoelectrónico_contacto = validar_correo()
    contacto = {"Nombre": nombreyapellido_contacto,"Numero": numerotelefono_contacto, "Correo": correoelectrónico_contacto}
    contactos.append(contacto)

    print("Datos registrados con éxito")

def mostrarlista_contractos():
    if len(contactos) == 0:
            print("No hay trabajadores registrados, ocupe la opción 1 del menú.")
    else:
        print("Lista de contactos")
        for x in contactos:
            print(f"Nombre: {x['Nombre']}")
            print(f"Numero: {x['Numero']}")
            print(f"Correo: {x['Correo']}\n")

def imprimirencsvlalista():
    if len(contactos) == 0:
            print("No hay trabajadores en la lista, agregue para poder exportar a CSV")
    else:
        nombrearchivo = input("Ingrese nombre de archivo: ")+".csv"
        try:
            with open(nombrearchivo,"x", newline="") as archivo:
                escritor = csv.DictWriter(archivo, ["Nombre","Numero","Correo"])
                escritor.writerows(contactos)
            print("Archivo creado con éxito!")
        except:
             print("ERROR! El archivo ya existe, no puede ocupar el mismo nombre.")

def validar_nombre():
     while True:
          nom = input("Ingrese nombre: ")
          if len(nom) >= 3 and nom.isalpha():
               return nom
          else:
               print("Ingrese un nombre correcto, solo letras y mayor a 3 caracteres")

def validar_telefono():
    try:
          telef = int(input("Ingrese número de teléfono: "))
          if len(str(telef)) == 9 and str(telef)[0] == '9':
               return telef
          else:
               print("ERROR! el teléfono debe comenzar con 9 y tener 9 dígitos!")
    except:
         print("Ingrese un número entero")

def validar_correo():
     while True:
          cor = input("Ingrese correo: ")
          if cor.strip().lower().endswith("@gmail.com") and len(cor.strip()) >= 13:
               return cor
          else:
               print("ERROR!, correo incorrecto, solo pueden ser Gmail.")

