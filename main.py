import os

tasks = []

#Listar todas Las Tareas

def verTareas(tasks):
  borrarPantalla()
  if len(tasks) == 0:
    print("No tiene tareas pendiente")
  else:
    print("Tareas Pendientes:")
    #tasks.reverse()
    for task in tasks:
      print(f"{tasks.index(task)} - {task}")

#Agregar una Nueva Tarea
def agregarTareas(tasks, task):
  tasks.append(task)
  #return tasks


  #eliminarIndex
def eliminarTareas(index):
  tasks.pop(index)
  print("Tarea eliminada con éxito!")

def borrarPantalla():
  if os.name == "posix":
    os.system("clear")
  elif os.name == "ce" or os.name == "nt" or os.name == "dos":
    os.system("cls")

def menu(tasks):
  borrarPantalla()
  print("****Menu Pricipal****")

  print(
    "1- Ver todas las tareas pendientes\n2- Agregar una nueva tarea \n3- Eliminar una tarea"
  )
  opcion = input("Seleccione una opción => ")
  if opcion.isdigit():
    opcion = int(opcion)
    if opcion == 1 or opcion == 2 or opcion == 3:
      opciones(opcion, tasks)
    else:
      print("Ingrese una opción valida")
  else:
    print("Ingrese una opción valida")

def regresarMenuPrincipal(tasks):
  regresar = input("Regresar al menu principal s\\n => ").lower()
  if regresar == "s":
    menu(tasks)

def opciones(opcion, tasks):
  if opcion == 1:
    #borrarPantalla()
    verTareas(tasks)
    regresarMenuPrincipal(tasks)

  if opcion == 2:
    cantidadTareas = input("Ingrese la cantidad de Tareas a Ingresar => ")
    vueltas = 1
    if cantidadTareas.isdigit():
      borrarPantalla()
      while vueltas <= int(cantidadTareas):
        task = input(f"Ingrese la Tarea {vueltas} => ")
        agregarTareas(tasks, task)
        verTareas(tasks)
        vueltas += 1
    else:
      print("Debe ingrear un número.")

  if opcion == 3:
    borrarPantalla()
    if len(tasks) == 0:
      print("No tiene tareas pediente para eliminar.")
    else:
      verTareas(tasks)
      index = input("Ingrese el número de la tarea a eliminar => ")
      if index.isdigit():
        index = int(index)
        try:
          eliminarTareas(index)
          verTareas(tasks)
        except:
          print("Error, indicar un numero de tarea válido")

  regresarMenuPrincipal(tasks)


menu(tasks)
