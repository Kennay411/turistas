def main():
    pokemones = []
    
    while True:
        print("--- Menu Principal ---")
        print("1.- Ingresar un pokemon")
        print("2.- Buscar un pokemon")
        print("3.- Eliminar un pokemon")
        print("4.- Listar un pokemon")
        print("5.- Salir")  
    
        opcion = int(input("seleccione una opcion"))
    
        if opcion == "1":
            ingresar_pokemon(pokemones)
        elif opcion == "2":
            buscar_pokemon(pokemones)
        elif opcion == "3":
            eliminar_pokemon(pokemones)
        elif opcion == "4":
            listar_pokemon(pokemones)
        elif opcion == "5":
            print("nos vemos")
            break
        else:
            print("Opcion no valida")

def ingresar_pokemon(pokemones):
    print("Ingrese un nuevo pokemon")
    
    while True:
        try:
            id_pokemon = int(input("Ingrese ID del pokemon"))
            if id_pokemon <= 0:
                print("El ID debe ser un numero positivo")
                continue
            break
        except ValueError:
            print("Debe ingresar un numero valido para el ID")