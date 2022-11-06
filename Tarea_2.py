import requests
import json

print("Bienvenid@, a continuación te presento las opciones que puedes realizar:")
print(
    "Opción 1: Listar pokemones por generación.\nOpción 2: Listar pokemones por forma.\nOpción 3: Listar pokemones por habilidades")
print("Opción 4: Listar pokemones por habitat.\nOpción 5: Listar pokemones por tipo.\n")

opcion = 0

while (True):
    try:
        opcion = int(input("Ingresa el número de la opción que deseas realizar (Del 1-5): "))
    except ValueError:
        print("El valor ingresado debe ser un número.")
    except NameError:
        print("El valor ingresado debe ser un número.")
    finally:
        if (opcion == 1 or opcion == 2 or opcion == 3 or opcion == 4 or opcion == 5):
            break
