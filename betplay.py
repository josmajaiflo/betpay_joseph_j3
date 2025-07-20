'''Autor : Joseph Manuel Jaimes Florez
grupo : j3
Descripcion : 
Fecha : 19/07/2025
'''

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

def registrar_marcador(nombres_equipo, pj, pg, pp, pe, gf, gc, puntos,
                       partidos_fecha, partidos_local, partidos_visitante,
                       partidos_goles_l, partidos_goles_v):
    
    '''registra el resultado de un partido pendiente y actualiza las estadisticas'''
    
    print('\n--- REGISTRO DE MARCADOR : ---')

    #1. partidos que no tienen marcador 
    
    partidos_pendientes = []
    for i in range(len(partidos_fecha)):
        if partidos_goles_l[i] is None:
            partidos_pendientes.append(i)
    
    #2. validar partidos pendientes 
    if not partidos_pendientes:
        print('no hay partidos pendientes.')
        return
    
    #3. mostrar el usuario los partidos pendientes 
    print('selecciona el partido par registrar marcador:')
    for i, idx_partido in enumerate(partidos_pendientes):
        local = partidos_local[idx_partido]
        visitante = partidos_visitante[idx_partido]
        print(f'{i+1}. {local} vs {visitante} (fecha: {partidos_fecha[idx_partido]})')
    
    #4. que el ususario elija una opcion 
    try:
        opcion_usuario = int(input('elija el numero del partido: '))
        if not (1<= opcion_usuario <= len(partidos_pendientes)):
            print('error: opcion fuera del rango.')
            return
    except ValueError:
        print('error: desbes ingresar un numero.')
        return
    
    #5. obtener el indice real del partido en las listas originales 
    indice_real = partidos_pendientes[opcion_usuario - 1]

    #6. pedir y validarlos goles
    while True:
        try:
            goles_l = int(input(f'goles de {partidos_local[indice_real]}:'))
            if goles_l >= 0: break
            else: print('los goles no pueden ser negativos.')

        except ValueError:
            print('error:ingresa un numero de goles validos')

    while True:
        try:
            goles_v = int(input(f"Goles de {partidos_visitante[indice_real]}: "))
            if goles_v >= 0: break
            else: print("Los goles no pueden ser negativos.")
        except ValueError:
            print("Error: Ingresa un número de goles válido.")
    
    #7. actualizar el resultados de las listas 
    partidos_goles_l[indice_real] = goles_l
    partidos_goles_v[indice_real] = goles_v

    #8. actualizar las estadisticas de los equipos involucrados 
    nombre_local = partidos_local[indice_real]
    nombre_visitante = partidos_visitante[indice_real]

    idx_local = nombres_equipo.index(nombre_local)
    idx_visitante = nombres_equipo.index(nombre_visitante)

    #9. actualizar PJ, GF, GC para ambos
    pj[idx_local] += 1
    pj[idx_visitante] += 1
    gf[idx_local] += goles_l
    gf[idx_visitante] += goles_v
    gc[idx_local] += goles_v
    gc[idx_visitante] += goles_l

    # Actualizar PG, PP, PE y Puntos
    if goles_l > goles_v: # Gana el local
        pg[idx_local] += 1
        pp[idx_visitante] += 1
        puntos[idx_local] += 3
    elif goles_v > goles_l: # Gana el visitante
        pp[idx_local] += 1
        pg[idx_visitante] += 1
        puntos[idx_visitante] += 3
    else: # Empate
        pe[idx_local] += 1
        pe[idx_visitante] += 1
        puntos[idx_local] += 1
        puntos[idx_visitante] += 1

    print("\n¡Marcador registrado y tabla de posiciones actualizada con éxito!")

def tabla_posiciones(nombres, pj, pg, pp, pe, gf, gc, puntos):
    '''enpaqueta, ordena y muestra la tabla de pocicion del torneo.'''
    print('\n'+'='*66)
    print(' ' * 24 + 'TABLA DE POCICIONS' + ' ' * 23)
    print('='*66)

    #1. validar equipos 
    if not nombres:
        print("Aún no se han registrado equipos en el torneo.")
        print("="*66)
        return
    
    #2. ordenar los datos juntos 
    tabla_combinada = []
    for i in range(len(nombres)):
        diferencias_goles = gf[i] - gc[i]
        info_equipo = [
            puntos[i],
            diferencias_goles[i],
            gf[i],
            nombres[i],
            pj[i],
            pg[i],
            pp[i],
            pe[i],
            gc[i]
            ]
        tabla_combinada.append(info_equipo)

    #3. Ordenar la lista de listas. `reverse=True` para ordenar de mayor a menor
    tabla_combinada.sort(reverse=True)
     
    #4. tabla formateada 
    print(f'{"POS":<4}{"EQUIPO":<15} {"PTS":>4} {"PJ":>4} {"PG":>4} {"PE":>4} {"PP":>4} {"GF":>4} {"GC":>4} {"DG":>4}')
    print('-'*66)

    #tabla
    for i, info in enumerate(tabla_combinada):
        pts, dg, gf_val, nombre, pj_val, pg_val, pp_val, pe_val, gc_val = info
        print(f"{i+1:<4} {nombre:<15} {pts:>4} {pj_val:>4} {pg_val:>4} {pe_val:>4} {pp_val:>4} {gf_val:>4} {gc_val:>4} {dg:>4}")
    
    print("=" * 66)

def mostrar_reportes(nombres, gf, gc):
    '''reportes especificos el equipo mas goleador y el mas goleado'''
    print('\n' + '='*40)
    print('' * 10 + 'REPORTES DEL TORNEO' + ' ' * 10)
    print('='*40)

    #1. validar si hay equipos
    if not nombres:
        print('no hay equipos registrados par generar reportes')
        print('='*40)
        return
    
    #2. equipo con mas goles a favor 
    max_goles_favor = -1
    equipo_mas_goleador = ''
    for i in range(len(nombres)):
        if gf[i] > max_goles_favor:
            max_goles_favor = gf[i]
            equipo_mas_goleador = nombres[i]
    
    #3. encontrar equipo con mas goles en contra
    max_goles_contra = -1
    equipo_mas_goleado = ''
    for i in range(len(nombres)):
        if gc[i] > max_goles_contra:
            max_goles_contra = gc[i]
            equipo_mas_goleado = nombres[i]

    print(f'equipo con mas goles a favor:{equipo_mas_goleador}({max_goles_favor}goles)')
    print(f'equipo con mas goles en contra:{equipo_mas_goleado}({max_goles_contra}goles)')
    print('='*40)

def registrar_plantel(nombres_equipos, j_equipo, j_nombre, j_dorsal, j_pos, j_edad, ct_equipo, ct_nombre, ct_cargo):
    
    '''registrar una persona (jugador o CT) en un equipo. '''
    print('\n--- REGISTRO DE PLANTEL ---')

    # Paso 1: Validar y seleccionar el equipo
    if not nombres_equipos:
        print('Error: Primero debes registrar al menos un equipo.')
        return

    print("Equipos disponibles:", ", ".join(nombres_equipos))
    nombre_equipo = input('Ingresa el nombre del equipo para el registro: ').strip().upper()

    if nombre_equipo not in nombres_equipos:
        print(f"Error: El equipo '{nombre_equipo}' no está registrado.")
        return

    # Paso 2: Preguntar qué tipo de persona se va a registrar
    print(f"\n¿Qué deseas registrar para {nombre_equipo}?")
    print("1. Jugador")
    print("2. Entrenador (CT)")
    tipo_registro = input("Elige una opción: ")

    # Paso 3: Pedir los datos según la elección
    if tipo_registro == '1':
        print("\n-- Registrando Jugador --")
        nombre = input("Nombre del jugador: ").strip()
        posicion = input("Posición: ").strip()
        try:
            dorsal = int(input("Dorsal: "))
            edad = int(input("Edad: "))
        except ValueError:
            print("Error: Dorsal y edad deben ser números. Registro cancelado.")
            return # Salimos de la función si los datos son incorrectos
        
        # Guardar los datos del jugador en sus listas
        j_equipo.append(nombre_equipo)
        j_nombre.append(nombre)
        j_dorsal.append(dorsal)
        j_pos.append(posicion)
        j_edad.append(edad)
        print(f"¡Jugador {nombre} añadido a {nombre_equipo} con éxito!")

    elif tipo_registro == '2':
        print("\n-- Registrando Entrenador (CT) --")
        nombre = input("Nombre del miembro del CT: ").strip()
        cargo = input("Cargo (ej. Entrenador, Asistente): ").strip()
        
        # Guardar los datos del CT en sus listas
        ct_equipo.append(nombre_equipo)
        ct_nombre.append(nombre)
        ct_cargo.append(cargo)
        print(f'{cargo} {nombre} añadido a {nombre_equipo} con éxito')
        
    else:
        print('Opción no válida. Volviendo al menú principal.')

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

     # Listas para planteles

    jugadores_equipo = []

    jugadores_nombre = []

    jugadores_dorsal = []

    jugadores_posicion = []

    jugadores_edad = []


    ct_equipo = []

    ct_nombre = []

    ct_cargo = []

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
            print('registrar marcador:')
            registrar_marcador(
                nombres_equipos, partidos_jugados, partidos_ganados, partidos_perdidos,
                partidos_empatados, goles_a_favor, goles_en_contra, puntos_equipo,
                partidos_fecha, partidos_local, partidos_visitante,
                partidos_goles_local, partidos_goles_visitante
                )

        elif opcion == '4': 
            print('\n---equipos registrados---.')
            tabla_posiciones(
                nombres_equipos, partidos_jugados, partidos_ganados, partidos_perdidos,
                partidos_empatados, goles_a_favor, goles_en_contra, puntos_equipo
            )
        elif opcion == '5':
            print('elije "Ver reportes".')
            mostrar_reportes(nombres_equipos, goles_a_favor, goles_en_contra)

        elif opcion == '6':
            print('elije "Registrar plantel".')
            registrar_plantel( nombres_equipos,
            jugadores_equipo, jugadores_nombre, jugadores_dorsal,
            jugadores_posicion, jugadores_edad,
            ct_equipo, ct_nombre, ct_cargo
        )
        else:
             print('opcion no valida. porfavor, intente de nuevo.')
    
    # --- Punto de Entrada del Programa ---
    # # Esta línea asegura que la función main() se ejecute cuando corras el archivo.
main()