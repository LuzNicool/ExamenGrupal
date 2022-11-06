import csv

lista = list()


class Libro:
    def __init__(self):
        self.id = []
        self.titulo = []
        self.genero = []
        self.isbn = []
        self.editorial = []
        self.autores = []


def menu():
    opcion = 0
    while opcion != 11:
        print("""
        Menú
        --------
        1. Cargar 3 libros
        2. Listar libros
        3. Agregar libro
        4. Eliminar libro
        5. Buscar libro por ISBN o por título
        6. Ordenar libros por título
        7. Buscar libros por autor, editorial o género
        8. Buscar libro por número de autores
        9. Editar o actualizar datos de un libro
        10. Guardar libros
        11. Salir
        """)
        opcion = int(input("Digite una opción: "))
        if opcion == 1:
            pass
        elif opcion == 2:
            listar()
        elif opcion == 3:
            registrar()
        elif opcion == 4:
            eliminar()
        elif opcion == 5:
            buscar_1()
        elif opcion == 6:
            pass
        elif opcion == 7:
            buscar_2()
        elif opcion == 8:
            buscar_3()
        elif opcion == 9:
            pass
        elif opcion == 10:
            pass
        elif opcion == 11:
            salir()


def registrar():
    print("""
    Registro del libro)
    ------------------------
    """)
    l = Libro()
    l.id = int(input("ID: "))
    l.titulo = input("Ingrese el nombre del libro: ")
    l.genero = input("Ingrese el genero del libro: ")
    l.isbn = int(input("Ingrese el ISBN del libro: "))
    l.editorial = input("Ingrese la editorial del libro: ")
    l.autores = int(input("Numero de Autor(es): "))
    lista.append(l)
    print(lista)


def listar():
    print("""
    Listado de alumnos
    ---------------------
    """)
    for l in lista:
        print(f"ID: {l.id}, Título: {l.titulo}, Género: {l.genero}, ISBN: {l.isbn}, Editorial: {l.editorial}, Autor(es): {l.autores}")


def buscar_1():
    print("""
    Resultado de la búsqueda
    ---------------------------
    """)
    x = input("Ingrese el ISB o el título del libro que desea buscar: ")
    for l in lista:
        if (l.isb == x or l.titulo == x):
            print(f"ID: {l.id}, Título: {l.titulo}, Género: {l.genero}, ISBN: {l.isbn}, Editorial: {l.editorial}, Autor(es): {l.autores}")


def salir():
    print("Gracias por utilizar, este programa.")

def buscar_2():
    print("""
    Resultados de la búsqueda
    ---------------------------
    """)
    y = input("Ingrese el autor, editorial o género del libro que desea buscar: ")
    for l in lista:
        if (l.autores == y or l.editorial == y or l.genero == y):
            print(f"ID: {l.id}, Título: {l.titulo}, Género: {l.genero}, ISBN: {l.isbn}, Editorial: {l.editorial}, Autor(es): {l.autores}")

def buscar_3():
    z = int(input("Numero de autor(es):"))
    for l in lista:
        if (l.autores == z):
            print(f"ID: {l.id}, Título: {l.titulo}, Género: {l.genero}, ISBN: {l.isbn}, Editorial: {l.editorial}, Autor(es): {l.autores}")

def eliminar():
    print("""
    Eliminando libro
    -------------------
    """)
    titu = input("Ingrese el titulo del libro que desea eliminar: ")
    for k in list:
        if(lista[k] == titu):
            lista.pop(k)



menu()




























