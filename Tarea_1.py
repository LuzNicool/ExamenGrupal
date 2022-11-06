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






























