
donantes = []

def menu_ej():
    while True:
        print("-------------------")
        print("Menú")
        print("1. Donaciones")
        print("2. Resultados")
        print("3. Mayor Donador")
        print("4. Terminar")
        print("-------------------")
        opc = int(input("Inserte la opción deseada: "))
        switcher_demo(opc)
        
def switcher_demo(argument):
    switcher = {
        1: Donaciones,
        2: Resultados,
        3: Mayor_Donador,
        4: Terminar
    }
    switcher[argument]()
    
def Donaciones():
    numdonaciones = 0
    donaciones = {
    Nombre : " ",
    Donacion : 0,
    Grupo : 0
}
    while True:
        numdonaciones = int(input("Ingrese cuantos donadores hay: "))
        Nombre = str(input("Ingrese el nombre del donador: "))
        Donacion = float(input("Ingrese la cantidad que se dona: "))
        Grupo = int(input("A que grupo se dona:"))
        Total= Donacion + (Grupo)
        donantes.append(donaciones)
        
        
def Resultados():
    print("Total aportado a el grupo Niños: ", Contador[0], "pesos")
    print("Total aportado a el grupo Adolescentes: ", Contador[1], "pesos")
    print("Total aportado a el grupo Adultos: ", Contador[2], "pesos")
    print("Total aportado a el grupo Adultos mayores: ", Contador[3], "pesos")
    print("Total recaudado," Total)
        
def Terminar():
    print("Hasta luego")
    exit()
    
def Mayor_Donador():
    print("El mayor donador fue")

def invalida():
    print("Opcion invalida")

print(menu_ej())