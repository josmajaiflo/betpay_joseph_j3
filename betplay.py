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

def registrar_equipos (nombres, pj, pg, pp, pe, gf, gc, puntos):

    '''ingrese los nombres de los equipos a registrar'''
    print('\n---REGISTRO DE EQUIPOS---')
    try:
        cantidad = int(input('¿cuantos equipos vas a registrar?'))

    except ValueError:
        print('error: debes ingresar un numero entero.')
        return #sale de la funcion si no es un numero
    
    for i in range (cantidad):
        while True: #se asegura de que no se ingrese un ombre vacio u otro 
            nuevo_equipo = input(f'nombre de equipo {i+1}:').capitalize().strip()
            if nuevo_equipo: #verifica que no este vacio
                break
            else:
                print('el nombre del equipo no puede estar vacio.intente de nuevo.')
            
            #verificamos si el equipo ya existe en nuestra lista para no tener duplicados    
        if nuevo_equipo in nombres:
            print(f'el equipo {nuevo_equipo} ya esta registrado. no se añadio.')
        else:
            #si no existe, lo agregamos
            nombres.append(nuevo_equipo)
            #y tambien agregamos sus valores iniciales en cero a todas las demas listas 

            pj.append(0)
            pg.append(0)
            pp.append(0)
            pe.append(0)
            gf.append(0)
            gc.append(0)
            puntos.append(0)

            print(f'equipo "{nuevo_equipo}" registrado con exito')

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
            print('registrar equipo') # Llamamos a la función y le pasamos TODAS nuestras listas
            registrar_equipos(nombres_equipos,
                              partidos_jugados,
                              partidos_ganados,
                              partidos_perdidos,
                              partidos_empatados,
                              goles_a_favor,
                              goles_en_contra,
                              puntos_equipo)
        elif opcion == '2':
            print('elije "Programar fecha".')
            pass
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