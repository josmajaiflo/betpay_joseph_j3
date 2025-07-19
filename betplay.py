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
        cantidad = int(input('¿cuantos equipos vas a registrar?:'))

    except ValueError:
        print('error: debes ingresar un numero entero.')
        return #sale de la funcion si no es un numero
    
    for i in range (cantidad):
        while True: #se asegura de que no se ingrese un nombre vacio u otro 
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

def programar_fecha (nombres_equipo, fechas, locales, visitantes, goles_locales, goles_visitantes):

    '''permite programar varios partidos en una misma fecha espesifica'''
    print('\n---PROGRAMACION DE FECHA---')
    
    #1. validacion inicial
    if len(nombres_equipo) < 2:
        print('error:necesita registrar mas de dos equipos')
        return
   
    #2. perdidr datos
    fecha_partido = input('ingresa la fecha para esta jornada(DD/MM/AAAA)').strip()
    try:
        cantidad_partidos = int(input('cuantos partidos se jugaran en esta fecha'))
    except ValueError:
        print( 'error debes ingresar un numero entero.')
        return
   
    #3. bucle para rejistrar cada partido
    for i in range (cantidad_partidos):
        print(f'\n---programando partido {i+1} de {cantidad_partidos}---')

        #equipos ingresados validos 
        while True:
           
            #mostrar los equipos disponibles
            print('equipos diponibles:')
            for idx, nombre in enumerate(nombres_equipo):
                print(f'  - {nombre}')
            
            equipo_local = input('nombre del equipo local:').strip().capitalize()
            equipo_visitante = input('nombre del equipo visitante:').strip().capitalize()

             # 4. Realizamos las validaciones críticas
            if equipo_local not in nombres_equipo:
                print(f'error:el equipo {equipo_local} no esta registrado.')

            elif equipo_visitante not in nombres_equipo:
                print(f'error: el equipo {equipo_visitante} no esta registrado.')

            elif equipo_local == equipo_visitante :
                print(f'error: un equipo mo puede jugar contra si mismo.')

            else:
                # Si todo está bien, rompemos el bucle de validación
                break
        
        # 5. Guardamos la información del partido en nuestras listas paralelas
        fechas.append(fecha_partido)
        locales.append(equipo_local)
        visitantes.append(equipo_visitante)
        goles_locales.append(None)  # Marcador pendiente
        goles_visitantes.append(None)  # Marcador pendiente

        # 6. Mensaje de éxito
        print(f"¡Partido {equipo_local} vs {equipo_visitante} programado para el {fecha_partido}!")

def registrar_marcador(nombres_equipo, pj, pg. pp, pe, gf, gc, puntos, partidos_fecha, partidos_local, partidos_visitante, partidos_goles_l, partidos_goles_v):
    '''registra el resultado de un partido pendiente y actualiza las estadisticas'''
    print('\n--- REGISTRO DE MARCADOR : ---')
    #1. partidos que no tienen marcador 
    partidos_pendientes = []
    for i in range(len(partidos_fecha)):
        if partidos_goles
        
def main():
    '''funcion que ejecuta el programa'''
    print('bienvenidos al sistema de gestion betplay')

    # --- ALMACÉN CENTRAL DE DATOS ---
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


    # --- NUEVAS LISTAS PARA ALMACENAR PARTIDOS ---

    partidos_fecha = []

    partidos_local = []

    partidos_visitante = []

    partidos_goles_local = []

    partidos_goles_visitante = []

    # Bucle principal del programa
   
    while True:
        mostrar_menu()
        opcion = input('por favor, elije una opcion:')

        if opcion == '1':
            print('registrar equipo') # Llamamos a la función y le pasamos TODAS nuestras listas
            registrar_equipos(
                nombres_equipos,
                partidos_jugados,
                partidos_ganados,
                partidos_perdidos,
                partidos_empatados,
                goles_a_favor,
                goles_en_contra,
                puntos_equipo
                )
        elif opcion == '2':
             print('Programar fecha')
             programar_fecha(
                nombres_equipos,
                partidos_fecha,
                partidos_local,
                partidos_visitante,
                partidos_goles_local,
                partidos_goles_visitante
                )
        elif opcion == '3':
            print('\n ---partidos programados---')
            if not partidos_fecha:
                print('no hay partidos programados todavia.')
            else:
                for i in range (len(partidos_fecha)):
                    #muestra el estado del marcador
                    marcador = f'{partidos_goles_local[i]}-{partidos_goles_visitante[i]}' if partidos_goles_local[i] is not None else 'pendientes'
                    print(f'fecha:{partidos_fecha[i]} | {partidos_local[i]} vs {partidos_visitante[i]} | Marcador: {marcador}")')        

        elif opcion == '4':
            #  imprimir la lista de nombres de equipos
            print('\n---equipos registrados---.')
            if not nombres_equipos:
                print('aun no hay equipos registrados.')
            else:
                print(nombres_equipos)
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