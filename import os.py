import os

def ingresar_nombre():
    #se crea una funcion para el ingreso de nombres
    #con el uso de while en caso de ser verdadero los datos pasamos al ingreso de notas en caso
    #de no ingresar ningun dato vuelve a pedirlo hasta que ingrese algun nombre
    while True:
        nombre = input("Ingrese el nombre del estudiante : ")
        if nombre=="":
            print("el nombre no puede estar vacio")
        else:
            return nombre

def ingresar_edad():  # Se crea una funcion para añadir la edad del alumno a una lista.
    edades = int(input("Ingrese la edad del estudiante: "))
    return edades	
 
def ingresar_nota():
#Para ingresar una nota creamos una funcion de nombre ingresar_nota
    while True:
        try:
            nota = float(input("Ingrese la nota del estudiante (0-10):"))
          #el uso del if else,determina si el numero ingresado es de 0 a 10
            if 0<=nota<=10:
                return nota
            else:
                print("La nota a ingresar tiene que estar entre 0 y 10")
        except:#Se utiliza except para que el programa no se caiga en caso de que se ingrese una letra o caracter en vez de numeros.
            print("la nota tiene que ser un valor numerico")
          
def promedio_notas(lista_notas):
  #usamos la palabra reservada len para que devuelva un valor entero la misma indica la cantidad de caracteres en la cadena de entrada.
    if len(estudiantes) == 0:
        return -1
    return sum(lista_notas)/len(lista_notas)
  
def buscar_Alumno(alumno, lista):
    # creo una funcion para encontrar un alumno por su nombre.
    if alumno in lista:  # Se verifica si el alumno se encuentra en la lista ya guardada.
        try:
            return lista.index(alumno)
          #El uso de index devuelve la primera aparición / índice del elemento en la lista dada como argumento de la función.
        except:  #El uso de try, se utiliza para levantar una excepción,el término levantar se refiere a la acción de generar una excepción es este caso por si el alumno no se encuentra en la lista. En ese caso retorna none.  
            return None
          
def cambio_Nota(alumno, listaAlumnos, listaNotas):
    # Funcion para cambiarle la nota a un alumno.
    # pido al usuario la nueva nota.
    nuevaNota = float(input("Ingrese la nueva nota: "))
    if 0 <= nuevaNota <= 10:  # determino si la nota es valida(entre 0 y 10)
        listaNotas[buscar_Alumno(alumno, listaAlumnos)] = nuevaNota
    else:
        print("La nota ingresada tiene que estar entre 0 y 10")

def ordenar_alfabeticamente(listaAlumnos, listaNotas):
    # hago uso de sorted para que devuelva una nueva lista ordenada
    return sorted(tuple(zip(listaAlumnos, listaNotas)))
    ## Usando la funcion ZIP y TUPLE, junto las dos listas en una tupla que corresponde al nombre del alumno y la nota.

def ordenado_de_Notas(listaNotas, listaAlumnos):
    # Funcion para ordenar la lista por notas de forma ascendente o descendente.
    # Se pregunta al usuario que orden desea.
    orden = int(
        input("Desea ordenar las notas de forma ascendente o descendente? (1/2): "))
    if orden == 1:
        # ordenar de forma ascendente 0..1..2..3..
        return sorted(tuple(zip(listaNotas, listaAlumnos)))
    elif orden == 2:
        # ordenar de forma descendente 10..9..8..7..
        return sorted(tuple(zip(listaNotas, listaAlumnos)), reverse=True)
    else:
        # Error.
        return "¡ERROR!. Elija 1 para Ascendente y 2 para Descendente."

def eliminar_Alumno(alumno, listaAlumnos, listaNotas):
    #creamos funcion para eliminar un alumno y su nota de las respectivas listas.
    # Busco el indice del alumno a eliminar.
    indice = listaAlumnos.index(alumno)
    # Hago uso de la funcion pop() para eliminar el alumno.
    alumno_eliminado = listaAlumnos.pop(indice)
    # Esta funcion guarda el valor eliminado, para poder volver a agregarlo en caso de necesitarlo.
    nota_eliminada = listaNotas.pop(indice)
    eliminado = [alumno_eliminado, nota_eliminada]
    return tuple(eliminado)
  
def promedio_de_Edades(listaEdades):
    promedio = sum(listaEdades)/len(listaEdades)
    return promedio      
 
def Menu():
    print("""-------------------------------------------------------
    Selecciona una opción...
    1 - Agregar estudiante
    2 - Buscar estudiante por nombre
    3 - Modificar nota
    4 - Listado ordenados por nombres
    5 - Listado ordenados por notas
    6 - Mostrar promedio de las notas
    7 - Borrar un estudiante
    8 - Calcular la edad promedio de los estudiantes
    0 - Salir""")

# --------------- Programa principal----------------------------

# definimos la lista que contendra una lista con cada estudiante
estudiantes = []
# definimos la lista que contendra las notas de cada estudiante
notas =[]
edades =[]

while True:
    Menu ()
 
    try:
        opcion = int(input("Ingrese el número de la opción escogida: "))
    except:
        opcion=-1
 
    if opcion == 1:
        #el uso de Append() Este método nos permite agregar nuevos elementos a una lista.
        estudiantes.append(ingresar_nombre())
        edades.append(ingresar_edad())
        notas.append(ingresar_nota())
        print(estudiantes)
        print(notas)
        os.system("pause")
        os.system("cls")

    elif opcion == 2:
        i=True
        while i:
          alumno=input("Escriba el nombre del alumno que desea encontrar: ")
          indice=buscar_Alumno(alumno,estudiantes)
          print(f"El alumno {alumno} se encuentra en el indice {indice}")
          cont = input("Desea buscar otro alumno? (S/N): ")
          #Usamos la funcion upper para el uso de mayuscula o viceversa
          if cont.upper() == "S":
                continue
          else:
              i = False
        os.system("pause")
        os.system("cls")
      
    elif opcion == 3:
        i = True
        while i:
            print("Debera ingresar la nota, entre los limites de 0 a 10: ")
            print("Las actuales notas son: ")
            print(tuple(zip(estudiantes, notas)))
            alumno = input("Ingrese el alumno al que desea cambiarle la nota: ")
            cambio_Nota(alumno, estudiantes, notas)
            print("Las nuevas notas ingresadas son: ")
            print(tuple(zip(estudiantes, notas)))
            cont = input("Desea cambiar alguna nota? (S/N): ")
            if cont.upper() == "S":
                continue
            else:
                i = False
        os.system("pause")
        os.system("cls")
      
    elif opcion == 4:
        print("Lista de estudiantes ordenada alfabéticamente: ")
        print(ordenar_alfabeticamente(estudiantes, notas))
        os.system("pause")
        os.system("cls")
      
    elif opcion == 5:
        print("Lista de alumnos ordenada por notas:")
        print(ordenado_de_Notas(notas, estudiantes))
        os.system("pause")
        os.system("cls")
        
    elif opcion == 6:

        promedio= promedio_notas(notas)
        print(f"El promedio de las notas del curso es de: {promedio}")
        os.system("pause")
        
    elif opcion == 7:
        alumno = input("Escriba el nombre del alumno que desea eliminar: ")
        print(f"Ha eliminado al alumno: {eliminar_Alumno(alumno,estudiantes,notas)}")
        print(f""" {"#"*32} 
        La nueva lista es: """)
        print(estudiantes)
        print(notas)
        os.system("pause")
        os.system("cls")
      
    elif opcion == 8:
        print(f"""El promedio de las notas del curso es de {promedio_de_Edades(edades)}""")
        os.system("pause")
        os.system("cls")
      
    elif opcion == 0:
        print("****************************************")
        print("* Gracias por utilizar esta aplicación *")
        print("****************************************")
        print("""
*********************************************                               
*   ____ ___    ________  _____  (_) ______  *    
*  / __ `__ \  / ____  / /__  / / / / __  /  *
* / / / / / / / /___/ / / ___/ / / / /_/ /   * 
*/_/ /_/ /_/ /_/   /_/ /_/\ \ /_/ /_____/    *
*********************************************
""")
        os.system("pause")
        break
    else:
        print("La opción ingresada no es correcta, indica una opción correcta")