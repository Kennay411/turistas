def mostrar_menu():
    """Muestra el menú principal con las opciones disponibles"""
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Agregar un Pokémon")
    print("2. Buscar un Pokémon")
    print("3. Eliminar un Pokémon")
    print("4. Ver todos los Pokémones")
    print("5. Salir")
    print("----------------------")

def obtener_opcion():
    """Pide al usuario que seleccione una opción del menú"""
    while True:
        opcion = input("Elige una opción (1-5): ")
        if opcion in ["1", "2", "3", "4", "5"]:
            return opcion
        print("¡Opción incorrecta! Debe ser un número del 1 al 5")

def agregar_pokemon():
    """Función para agregar un nuevo Pokémon a la lista"""
    print("\n--- AGREGAR POKÉMON ---")
    
    # Pedir ID del Pokémon
    while True:
        try:
            id_pokemon = int(input("ID del Pokémon (número positivo): "))
            if id_pokemon > 0:
                break
            print("El ID debe ser mayor que cero")
        except:
            print("Debes ingresar un número válido")
    
    # Pedir nombre del Pokémon
    while True:
        nombre = input("Nombre del Pokémon: ").strip()
        if not nombre:
            print("El nombre no puede estar vacío")
            continue
        
        # Verificar si el nombre ya existe
        existe = False
        for p in lista_pokemones:
            if p["nombre"].lower() == nombre.lower():
                existe = True
                break
        
        if existe:
            print("¡Ya existe un Pokémon con ese nombre!")
        else:
            break
    
    # Pedir código del Pokémon
    while True:
        codigo = input("Código del Pokémon (mínimo 8 caracteres con letras y números): ").strip()
        
        # Validar el código
        valido = True
        
        # 1. Verificar longitud mínima
        if len(codigo) < 8:
            print("El código debe tener al menos 8 caracteres")
            valido = False
        
        # 2. Verificar que tenga al menos un número
        elif not any(c.isdigit() for c in codigo):
            print("El código debe contener al menos un número")
            valido = False
        
        # 3. Verificar que tenga al menos una letra
        elif not any(c.isalpha() for c in codigo):
            print("El código debe contener al menos una letra")
            valido = False
        
        # 4. Verificar que no tenga espacios
        elif " " in codigo:
            print("El código no puede contener espacios")
            valido = False
        
        if valido:
            break
    
    # Pedir tipo del Pokémon
    tipos_permitidos = ["fuego", "agua", "hierba", "veneno", "psiquico", "luchador", "eléctrico"]
    
    while True:
        print("\nTipos permitidos:", ", ".join(tipos_permitidos))
        tipo = input("Tipo del Pokémon: ").strip().lower()
        
        if tipo in tipos_permitidos:
            break
        print("Tipo no válido. Intenta nuevamente")
    
    # Crear el diccionario con los datos del Pokémon
    nuevo_pokemon = {
        "id": id_pokemon,
        "nombre": nombre,
        "codigo": codigo,
        "tipo": tipo
    }
    
    # Agregar a la lista
    lista_pokemones.append(nuevo_pokemon)
    print(f"\n¡Pokémon {nombre} agregado correctamente!")

def buscar_pokemon():
    """Función para buscar un Pokémon por su nombre"""
    print("\n--- BUSCAR POKÉMON ---")
    
    if not lista_pokemones:
        print("No hay Pokémones registrados")
        return
    
    nombre_buscado = input("Nombre del Pokémon a buscar: ").strip().lower()
    
    encontrado = False
    for pokemon in lista_pokemones:
        if pokemon["nombre"].lower() == nombre_buscado:
            print("\n--- INFORMACIÓN DEL POKÉMON ---")
            print(f"ID: {pokemon['id']}")
            print(f"Nombre: {pokemon['nombre']}")
            print(f"Tipo: {pokemon['tipo']}")
            print(f"Código: {pokemon['codigo']}")
            encontrado = True
            break
    
    if not encontrado:
        print("No se encontró el Pokémon")

def eliminar_pokemon():
    """Función para eliminar un Pokémon por su nombre"""
    print("\n--- ELIMINAR POKÉMON ---")
    
    if not lista_pokemones:
        print("No hay Pokémones registrados")
        return
    
    nombre_eliminar = input("Nombre del Pokémon a eliminar: ").strip().lower()
    
    eliminado = False
    for i in range(len(lista_pokemones)):
        if lista_pokemones[i]["nombre"].lower() == nombre_eliminar:
            del lista_pokemones[i]
            print("Pokémon eliminado correctamente")
            eliminado = True
            break
    
    if not eliminado:
        print("No se encontró el Pokémon para eliminar")

def listar_pokemones():
    """Función para mostrar todos los Pokémones registrados"""
    print("\n--- LISTA DE POKÉMONES ---")
    
    if not lista_pokemones:
        print("No hay Pokémones registrados")
        return
    
    for pokemon in lista_pokemones:
        print(f"ID: {pokemon['id']} - {pokemon['nombre']} ({pokemon['tipo']})")

def main():
    """Función principal que controla el flujo del programa"""
    print("BIENVENIDO AL SISTEMA DE GESTIÓN DE POKÉMONES")
    
    while True:
        mostrar_menu()
        opcion = obtener_opcion()
        
        if opcion == "1":
            agregar_pokemon()
        elif opcion == "2":
            buscar_pokemon()
        elif opcion == "3":
            eliminar_pokemon()
        elif opcion == "4":
            listar_pokemones()
        elif opcion == "5":
            print("\n¡Gracias por usar el sistema! Hasta pronto.")
            break
if __name__ == "__main__":
    main()


    
