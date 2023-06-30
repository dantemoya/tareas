import numpy as np

flag = True
precio= np.random.randint [1000, 5000]
while flag:
    print ("bienvenido al liceo\n-------------------------------\ncoloque el numero de lo que desea hacer")
    print("-------------------------------")
    print("1) agregar a un alumno o modificar")
    print("2) buscar almuno por rut")
    print("3) imprimir certificado")
    print("4) salir")
    print("-------------------------------")
    opc = int(input())
    if opc == 1:
        ide = int(input("ingrese id"))
        gra = np.empty ((100, 7), dtype=object)
        gra[ide, 0] = input("escriba el rut: ")
        gra[ide, 1] = input("escriba el nombre: ")
        gra[ide, 2] = input("escriba el apellido: ")
        gra[ide, 3] = input("escriba la fecha de nacimiento: ")
        gra[ide, 4] = input("escriba la carrera: ")
        gra[ide, 5] = input("escriba la asignatura: ")
        gra[ide, 6] = input("escriba el promedio: ")
        gra[ide] = int(input("escriba el rut del alumno"))
    elif opc == 2:
        ide = int(input("coloque el id: "))
        print (gra[ide, 0], gra[ide, 1], gra[ide, 2], gra[ide, 3], gra[ide, 4], gra[ide, 5], gra[ide, 6])
    elif opc == 3:
        ide = int(input("coloque el id del alumno: "))
        print("---alumno regular---")
        print (gra[ide, 0], gra[ide, 1], gra[ide, 2], gra[ide, 3], gra[ide, 4], gra[ide, 5], gra[ide, 6])
        print(f"el precio es de: {precio}")
    elif opc == 4:
        flag = False