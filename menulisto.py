k = 0
j = 1
idl = []
letras = []
des = []
hec = []
while j == 1:
    print
    print("Seleccione una opcion")
    print("1)Nueva Tarea")
    print("2)Listar Tarea")
    print("3)Tareas Hechas")
    print("4)Eliminar Tareas")
    op = input("Ingrese la opcion:")
    if op == "1":
        print("NUEVA TAREA")

        for i in range(1):
            k = k + 1
            idl.append(k)

        for i in range(1):
            tit = input("Ingrese el titulo ")
            letras.append(tit)
            print(letras)

        for i in range(1):
            descr = input("Ingrese la descripcion ")
            des.append(descr)
            print(des)

        for i in range(1):
            hec.append("por hacer")

        j = 1



    elif op == "2":
        print("LISTADO DE TAREAS")
        for i in range(1):
            print(idl)
            print(letras)
            print(des)
            print(hec)


    elif op == "3":
        num = int(input("Ingrese el numero de la tarea que ya ha hecho"))
        hec[num-1] = "hecho"



    elif op == "4":

        numer = int(input("Ingrese el numero de la tarea que quiere eliminar"))
        del idl[numer-1]
        del letras[numer - 1]
        del hec[numer - 1]
        del des[numer - 1]

print("Programa terminado")
