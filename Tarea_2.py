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

if (opcion == 1):

    print("Existen las siguientes generaciones de pokemones:")
    for num in range(8):
        print(f"- Generación {num + 1}")

    generacion = int(input("\nEscriba el número de la generación que desea buscar (Del 1-8): "))
    pokemon_generacion = {generacion: []}
    url1 = f'https://pokeapi.co/api/v2/generation/{generacion}'
    response1 = requests.get(url1)
    data1 = response1.json()

    for i in range(len(data1["pokemon_species"])):
        pokemon_generacion[generacion].append(data1["pokemon_species"][i]["name"])

    print(f"\nPokemones de la generación {generacion}:")
    print("--------------------------------")
    for cont, value in enumerate(pokemon_generacion[generacion], start=1):
        print(cont, ".", value)

elif (opcion == 2):

    url2 = f'https://pokeapi.co/api/v2/pokemon-shape/'
    response2 = requests.get(url2)
    data2 = response2.json()
    print("\nExisten las siguientes formas de pokemones:")
    lista_formas = []
    for num in range(len(data2["results"])):
        lista_formas.append(data2["results"][num]["name"])
    for n in lista_formas:
        print(f"- {n}")

    forma = input("\nEscriba la forma que desea buscar: ")
    pokemon_forma = {forma: []}
    url2 = f'https://pokeapi.co/api/v2/pokemon-shape/{forma}'
    response2 = requests.get(url2)
    data2 = response2.json()

    for i in range(len(data2["pokemon_species"])):
        pokemon_forma[forma].append(data2["pokemon_species"][i]["name"])

    print(f"\nPokemones con la forma {forma}:")
    print("--------------------------------")
    for cont, value in enumerate(pokemon_forma[forma], start=1):
        print(cont, ".", value)
