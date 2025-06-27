turistas = {
    "001": ["John Doe", "Estados Unidos", "12-01-2024"],
    "002": ["Emily Smith", "Estados Unidos", "23-03-2024"],
    "012": ["Julian Martinez", "Argentina", "19-09-2023"],
    "014": ["Agustin Morales", "Argentina", "28-03-2024"],
    "005": ["Carlos Garcia", "Mexico", "10-05-2024"],
    "006": ["Maria Lopez", "Mexico", "08-12-2023"],
    "007": ["Joao Silva", "Brasil", "20-06-2024"],
    "003": ["Michael Brown", "Estados Unidos", "05-07-2023"],
    "004": ["Jessica Davis", "Estados Unidos", "15-11-2024"],
    "008": ["Ana Santos", "Brasil", "03-10-2023"],
    "010": ["Martin Fernandez", "Argentina", "13-02-2023"],
    "011": ["Sofia Gomez", "Argentina", "07-04-2024"],
}

def mostrar_menu():
    """Muestra el menú principal"""
    print("\n*** MENU PRINCIPAL ***")
    print("1.- Turistas por país")
    print("2.- Turista por mes")
    print("3.- Eliminar turista")
    print("4.- Salir")

def turistas_por_pais(pais):
    """Muestra los turistas de un país específico"""
    print(f"\nTuristas de {pais}:")
    encontrados = False
    for turista_id, datos in turistas.items():
        if datos[1].lower() == pais.lower():
            print(f"- {datos[0]}")
            encontrados = True
    
    if not encontrados:
        print(f"No se encontraron turistas de {pais}")

def turistas_por_mes(mes):
    """Calcula el porcentaje de turistas que visitaron en un mes específico"""
    total_turistas = len(turistas)
    turistas_mes = 0
    
    for datos in turistas.values():
        fecha = datos[2]  # Formato: "dd-mm-aaaa"
        mes_fecha = int(fecha.split("-")[1])  # Extraemos el mes
        
        if mes_fecha == mes:
            turistas_mes += 1
    
    porcentaje = (turistas_mes / total_turistas) * 100 if total_turistas > 0 else 0
    return round(porcentaje, 1)

def eliminar_turista():
    """Elimina un turista por nombre"""
    nombre = input("Ingrese el nombre del turista a eliminar: ").strip().lower()
    eliminado = False
    
    # Buscamos el turista por nombre (sin importar mayúsculas/minúsculas)
    for turista_id, datos in list(turistas.items()):
        if datos[0].lower() == nombre:
            del turistas[turista_id]
            eliminado = True
    
    if eliminado:
        print("Turista eliminado con éxito.")
    else:
        print("Turista no encontrado. No se pudo eliminar.")

def main():
    """Función principal del programa"""
    print("Sistema de Gestión de Turistas - Departamento de Turismo de Chile")
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-4): ")
        
        if opcion == "1":
            pais = input("Ingrese el país de origen: ")
            turistas_por_pais(pais)
        
        elif opcion == "2":
            while True:
                try:
                    mes = int(input("Ingrese el mes (1-12): "))
                    if 1 <= mes <= 12:
                        porcentaje = turistas_por_mes(mes)
                        print(f"\nPorcentaje de turistas en el mes {mes}: {porcentaje}%")
                        break
                    else:
                        print("El mes debe estar entre 1 y 12. Intente nuevamente.")
                except ValueError:
                    print("Debe ingresar un número válido entre 1 y 12.")
        
        elif opcion == "3":
            eliminar_turista()
        
        elif opcion == "4":
            print("Programa terminado...")
            break
        
        else:
            print("Opción no válida. Por favor seleccione una opción del 1 al 4.")

if __name__ == "__main__":
    main()