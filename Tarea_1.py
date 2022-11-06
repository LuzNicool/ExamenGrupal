import csv

import time

lista = list()


class Libro:
    def __init__(
        self,
    ):
        self.id = []
        self.titulo = []
        self.genero = []
        self.isbn = []
        self.editorial = []
        self.autores = []


def menu():
    seleccion = 0
    while seleccion != 12:
        print("Bienvenid@ al menu:")
        time.sleep(3)
        print("1.Cargar 3 libros")
        print("2.agregar libros")
        print("3.listar libro")
        print("4.Eliminar libro")
        print("5.buscar libro por titulo")
        print("6.Ordenar libro por titulo")
        print("7.Buscar libros por autor, editorial o género")
        print("8.Buscar libros por número de autores.")
        print("9.Editar o actualizar datos de un libro ")
        print("10.Guardar libros en archivo csv o txt")
        time.sleep(4)
        seleccion = int(input("Elija una opcion:"))
        if seleccion == 1:
            cargar()
        elif seleccion == 2:
            agregar()
        elif seleccion == 3:
            listar()
        elif seleccion == 4:
            eliminar()
        elif seleccion == 5:
            buscar()
        elif seleccion == 6:
            ordenar()
        elif seleccion == 7:
            tres_op()
        elif seleccion == 8:
            num_autores()
        elif seleccion == 9:
            editar()
        elif seleccion == 10:
            guardar()
        else:
            salir()


def cargar():
    print("leer csv")


with open("estoslibros.csv", "r") as dato:
    reader = csv.reader(dato)
    for dato in reader:
        print(dato)


def agregar():
    print("libro para agregar")
    time.sleep(3)
    libros = Libro()
    libros.id = int(input("ID: "))
    libros.titulo = input("Título: ")
    libros.genero = input("género: ")
    libros.isbn = int(input("ISBN: "))
    libros.editorial = input("Editorial: ")
    libros.autores = int(input("Numero de Autor(es): "))
    lista.append(libros)


def listar():
    print("Listado de libros:")
    for libros in lista:
        time.sleep(3)
        print(
            f"ID de libro: {libros.id}, Su titulo es {libros.titulo}, Género: {libros.genero}, ISBN: {libros.isbn}, Editorial: {libros.editorial}, Autores {libros.autores}"
        )


def eliminar():
    print("Esta seguro de eliminar un libro")


def buscar():
    print("Resultados de busqueda:")
    IoT = input("Ingrese ISBN o titulo:")
    for libros in lista:
        if libros.titulo == IoT or libros.isbn == IoT:
            print(
                f"Su genero es {libros.genero} ,se publico en {libros.editorial} . Numero de autores: {libros.autores} "
            )


def ordenar():
    print("Orden de libros por titulo:")


def tres_op():
    print("Resultados:")
    time.sleep(3)
    aeg = input("buscar libro por autor, editorial o género: ")
    for libros in lista:
        if libros.autores == aeg or libros.editorial == aeg or libros.genero == aeg:
            print(f"El libro es {libros.titulo}, su ISBN es {libros.isbn }")


def num_autores():
    nma = int(input("Numero de autor(es):"))
    for libros in lista:
        if libros.autores == nma:
            print(f"{libros.titulo} este libro tiene {nma} autor(es).")


def editar():
    print("Editar o actualizar")


def guardar():
    print("Guardando en el csv")


def salir():
    print("finalizado")


menu()
