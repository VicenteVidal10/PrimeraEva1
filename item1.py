# item1.py

# Diccionario para almacenar la cantidad de cada dispositivo de red.
dispositivos_red = {
    "Router 1801": 0,
    "Router 2901": 0,
    "Router 2911": 0,
    "Router 4321": 0,
    "Router 4331": 0,
    "Switch 2960": 0,
    "Switch 3550": 0,
    "Switch 3560": 0,
    "Switch 9200": 0,
    "Access Point Serie Catalyst 9100": 0,
    "Access Point Serie Catalyst 9800": 0,
    "Access Point Serie Catalyst 4800": 0,
    "WLS Controladora Wireless Cisco 3504": 0
}

def solicitar_cantidades():
    """
    Función que solicita al usuario la cantidad de cada dispositivo.
    Permite al usuario salir del programa o continuar agregando dispositivos.
    """
    print("--- Registro de Dispositivos de Red ---")
    print("Ingrese la cantidad de cada dispositivo. Escriba 'Salir' o 'S' para finalizar el ingreso de datos.")

    while True:
        # Bucle principal para solicitar al usuario la cantidad de dispositivos.
        for dispositivo in dispositivos_red.keys():
            while True:
                # Bucle interno para validar la entrada del usuario.
                entrada = input(f"Ingrese la cantidad de '{dispositivo}': ").strip()

                # Condición para salir del programa y ofrecer opciones.
                if entrada.lower() == 'salir' or entrada.lower() == 's':
                    return 'opciones' # Retorna una cadena para indicar que se debe mostrar el menú de opciones.

                # Manejo de errores para entradas no numéricas.
                try:
                    cantidad = int(entrada)
                    # La cantidad no puede ser negativa.
                    if cantidad >= 0:
                        dispositivos_red[dispositivo] = cantidad
                        break  # Sale del bucle interno si la entrada es válida.
                    else:
                        print("Por favor, ingrese un número positivo.")
                except ValueError:
                    print("Entrada no válida. Por favor, ingrese un número entero.")
        
        # Después de recorrer todos los dispositivos, pregunta si desea continuar.
        continuar = input("\n¿Desea continuar agregando o modificando dispositivos? (s/n): ").strip().lower()
        if continuar != 's':
            return 'informe' # Retorna una cadena para indicar que se debe generar el informe.

def generar_informe():
    """
    Función que genera y muestra el informe detallado de los dispositivos y sus cantidades.
    """
    print("\n" + "="*40)
    print("        INFORME DE DISPOSITIVOS DE RED")
    print("="*40)

    # Itera sobre el diccionario para imprimir cada dispositivo y su cantidad.
    for dispositivo, cantidad in dispositivos_red.items():
        # Alinea la salida para una mejor presentación del informe.
        print(f"{dispositivo:<45}: {cantidad}")
    
    print("="*40)
    print("¡Proceso finalizado!")
    print("="*40)

# El punto de entrada principal del script.
if __name__ == "__main__":
    
    while True:
        # La variable 'accion' captura el valor de retorno de la función.
        accion = solicitar_cantidades()

        if accion == 'opciones':
            print("\n¿Qué desea hacer?")
            print("1. Volver a ingresar datos.")
            print("2. Generar informe y finalizar.")
            print("3. Salir del programa sin generar informe.")
            
            opcion = input("Ingrese su opción (1, 2, 3): ").strip()
            
            if opcion == '1':
                continue  # Vuelve al inicio del bucle while para solicitar datos nuevamente.
            elif opcion == '2':
                generar_informe()
                break # Sale del bucle principal para finalizar el programa.
            elif opcion == '3':
                print("\nEl proceso ha sido finalizado por el usuario.")
                break # Sale del bucle principal para finalizar el programa.
            else:
                print("Opción no válida. Por favor, ingrese 1, 2 o 3.")
        
        elif accion == 'informe':
            generar_informe()
            break # Sale del bucle principal para finalizar el programa.