import tareas
print("Seleccione una opcion")
print("1)Nueva Tarea")
print("2)Listar Tarea")
print("3)Tareas Hechas")
print("4)Eliminar Tareas")
op=input("Ingrese la opcion:")
if op=="1":
    print("NUEVA TAREA")
    tit=input("Ingrese el titulo")
    des=input("Ingrese la descripcion")
    obj = tareas.__añadir_tarea__(0,tit, des)
    for i in enumerate(obj):
        obj2=tareas.__añadir_tarea__(i,tit,des)
elif op=="2":
    print("LISTADO DE TAREAS")
    print
elif op==3:
    print("TAREAS HECHAS")
elif op==4:
    print("ELIMINAR TAREAS")