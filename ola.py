def main():
    pokemones = []
    
    while True:
        print("\n--- Menú Principal ---")
        print("1.- Ingresar pokemon")
        print("2.- Buscar pokemon")
        print("3.- Eliminar pokemon")
        print("4.- Listar pokemones")
        print("5.- Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            ingresar_pokemon(pokemones)
        elif opcion == "2":
            buscar_pokemon(pokemones)
        elif opcion == "3":
            eliminar_pokemon(pokemones)
        elif opcion == "4":
            listar_pokemones(pokemones)
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor seleccione una opción del 1 al 5.")

def ingresar_pokemon(pokemones):
    print("\n--- Ingresar nuevo Pokémon ---")
    
    # Validar ID
    while True:
        try:
            id_pokemon = int(input("Ingrese ID del Pokémon: "))
            if id_pokemon <= 0:
                print("El ID debe ser un número positivo.")
                continue
            break
        except ValueError:
            print("Debe ingresar un número válido para el ID.")
    
    # Validar nombre (no repetido)
    while True:
        nombre = input("Ingrese nombre del Pokémon: ").strip()
        if not nombre:
            print("El nombre no puede estar vacío.")
            continue
        
        # Verificar si el nombre ya existe
        nombre_existe = any(pokemon['nombre'].lower() == nombre.lower() for pokemon in pokemones)
        if nombre_existe:
            print("Error: Ya existe un Pokémon con ese nombre.")
        else:
            break
    
    # Validar código
    while True:
        codigo = input("Ingrese código del Pokémon: ").strip()
        
        # Verificar largo mínimo
        if len(codigo) < 8:
            print("El código debe tener al menos 8 caracteres.")
            continue
        
        # Verificar al menos 1 número
        if not any(c.isdigit() for c in codigo):
            print("El código debe contener al menos 1 número.")
            continue
        
        # Verificar al menos 1 letra
        if not any(c.isalpha() for c in codigo):
            print("El código debe contener al menos 1 letra.")
            continue
        
        # Verificar espacios en blanco
        if ' ' in codigo:
            print("El código no puede contener espacios en blanco.")
            continue
        
        break
    
    # Validar tipo
    tipos_validos = {"fuego", "agua", "hierba", "veneno", "psiquico", "luchador", "eléctrico"}
    while True:
        tipo = input("Ingrese tipo del Pokémon (fuego, agua, hierba, veneno, psiquico, luchador, eléctrico): ").strip().lower()
        if tipo not in tipos_validos:
            print("Tipo no válido. Los tipos permitidos son: fuego, agua, hierba, veneno, psiquico, luchador, eléctrico")
        else:
            break
    
    # Crear y agregar el Pokémon
    nuevo_pokemon = {
        'id': id_pokemon,
        'nombre': nombre,
        'codigo': codigo,
        'tipo': tipo
    }
    
    pokemones.append(nuevo_pokemon)
    print(f"¡Pokémon {nombre} ingresado exitosamente!")

def buscar_pokemon(pokemones):
    print("\n--- Buscar Pokémon ---")
    nombre_buscar = input("Ingrese el nombre del Pokémon a buscar: ").strip()
    
    encontrado = False
    for pokemon in pokemones:
        if pokemon['nombre'].lower() == nombre_buscar.lower():
            print("\nInformación del Pokémon:")
            print(f"ID: {pokemon['id']}")
            print(f"Nombre: {pokemon['nombre']}")
            print(f"Tipo: {pokemon['tipo']}")
            print(f"Código: {pokemon['codigo']}")
            encontrado = True
            break
    
    if not encontrado:
        print("El Pokémon no se encuentra registrado.")

def eliminar_pokemon(pokemones):
    print("\n--- Eliminar Pokémon ---")
    nombre_eliminar = input("Ingrese el nombre del Pokémon a eliminar: ").strip()
    
    eliminado = False
    for i, pokemon in enumerate(pokemones):
        if pokemon['nombre'].lower() == nombre_eliminar.lower():
            del pokemones[i]
            print("¡Pokémon eliminado!")
            eliminado = True
            break
    
    if not eliminado:
        print("No se pudo eliminar Pokémon!")

def listar_pokemones(pokemones):
    print("\n--- Listado de Pokémones ---")
    if not pokemones:
        print("No hay Pokémones registrados.")
        return
    
    for pokemon in pokemones:
        print(f"ID: {pokemon['id']} - Nombre: {pokemon['nombre']} - Tipo: {pokemon['tipo']}")

if __name__ == "__main__":
    main()