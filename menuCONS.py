j = 1
Asx = []
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
        des = input("Ingrese la descripcion ")
        tit = input("Ingrese el titulo ")
        hecho = float(input("ingresa 1 si esta hecho o 0 si no "))


        for i in M:
            Asx.append(hecho,tit,hecho)
            print(Asx)


        j = 1



    elif op == "2":
        print("LISTADO DE TAREAS")
        for i in M:
            Asx.append(des, tit, hecho)
            print(Asx)


    elif op == "3":
        print("LISTAR TAREAS HECHAS")
        for i in Asx:
            if hecho == 0:
             print(i, end=" ")

    elif op == "4":
        print("TAREAS ELIMINADAS")
        letras = ["", ""]

print("Programa terminado")





