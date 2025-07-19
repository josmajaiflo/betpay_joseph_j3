# --- Funciones del Menú y Estructura Principal ---
def mostrar_menu():
    '''esta funcion se encarga de mostrar las opciones de usuario'''
    print('\n--- MENU DE LA LIGA BETPLAY---')
    
    print('1. registrar equipos')
    
    print('2. programar fechas')
    
    print('3. registrar marcadores de los partidos')
    
    print('4. ver tabla de posiciones')
    
    print('5. ver reportes')
    
    print('6. registrar plantel')
    
    print('7. salir' )

def main():
    '''funcion que ejecuta el programa'''
    print('bienvenidos al sistema de gestion betplay')

    # --- NUESTRO ALMACÉN CENTRAL DE DATOS ---
    # Cada lista almacenará un dato específico de los equipos.
    # El índice de cada lista conectará los datos de un mismo equipo.
    nombres_equipos = []  # Guarda los nombres: ["MIL", "ATL", "DIM"]

    partidos_jugados = [] # Guarda PJ: [0, 0, 0]

    partidos_ganados = [] # Guarda PG: [0, 0, 0]

    partidos_perdidos = []# Guarda PP: [0, 0, 0]

    partidos_empatados =[]# Guarda PE: [0, 0, 0]

    goles_a_favor = []    # Guarda GF: [0, 0, 0]

    goles_en_contra = []  # Guarda GC: [0, 0, 0]

    puntos_equipo = []    # Guarda Puntos: [0, 0, 0]

    #bucle principal del programa

    while True:
        mostrar_menu()
        opcion = input('por favor, elije una opcion:')

        if opcion == '1':
            print('registrar equipo')
            pass
        elif opcion == '2':
            print('elije "Programar fecha".')
        elif opcion == '3':
            print('elije "Registrar marcador".')
            pass
        elif opcion == '4':
            print('elije "Ver tabla de posiciones".')
            pass
        elif opcion == '5':
            print('elije "Ver reportes".')
            pass
        elif opcion == '6':
            print('elije "Registrar plantel".')
            break
        else:
             print('opcion no valida. porfavor, intente de nuevo.')

# --- Punto de Entrada del Programa ---
# Esta línea asegura que la función main() se ejecute cuando corras el archivo.
main()