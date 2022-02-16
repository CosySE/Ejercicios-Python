 
import hospital_clases as h

print('''
     ************************************************
     *Bienvenido al modulo  para la gestion de salas*
     ************************************************
     ''')
#menu de opciones para todo el script
def menu():
    # Comprobar si existe un fichero al levantar el scrip y dar la opcion de cargarlo
    h.Controladora().comprobarSiExisteFicheroycargar()
    print('''
     Elija una de las siguientes opciones 
     1) LLenar datos de la sala
     2) Ver listados de las salas con equipos en mal estado
     3) Cantidad de salas que cumplen indicador de Calidad
     4) Ver lista de todas las salas introducidas
     5) Entre un identificador para mostrar datos de la sala
     6) Guardar la informacion  
     7) Salir
    ''')
    eleccion = input('Escriba el numero de una de las opciones arriba: ')
    if eleccion == '1':
        recoger_datos_de_sala() # metodo par a llenar los datos de la sala 
        menu()
    elif eleccion == '2':
        visualizar_listado() # metodo para el ver las salas que estan con equipos en mal estado
    elif eleccion == '3': 
        contar_salas_con_IC()# cuenta las salas que cumplen el indicador de calidad
    elif eleccion == '4':
        h.Controladora().visualizarSalasIntroducidas()#visualiza todo lo que se ha introducido
        menu()
    elif eleccion == '5':
        valorDado = input('Escriba el identificador: ')#pedir al usuario identificador para buscar en las slas
        h.Controladora().mostrar_datos_segun_ID(valorDado)#metodo que resuelve lo anterior
        menu()
    elif eleccion == '6':
        h.Controladora().crearYGuardarFichero() #metodo para generar fichero pickle con los datos introducidos
        menu()
    elif eleccion == '7':
        print('Gracias por usar la aplicacion')
    else:
        salir()# metodo para gestionar la salida del usuario

def recoger_datos_de_sala():
    ident = input('Escriba el identificador de la sala: ')# es necesario especificar tipo de sala
    print('Elija que tipo de sala 1) General o 2)Terapia: ')
    numero_sala = input('')
    nombre_sala = input('Nombre de la sala: ')
    cant_camas = input('Cantidad de camas: ')
    cant_pacientes = input('Cantidad de pacientes: ') 
    if numero_sala == '1':
        nombre_medico = input('Nombre del medico: ')   
        h.Controladora().adicionar(h.General(ident,nombre_sala,cant_camas,cant_pacientes,nombre_medico))
        print('''
        *******************************************
        *Fueron adicionados a la lista los valores*
        *******************************************
        ''')
    else: 
        estado_equipo = input(
        '''
        Introduzca el estado del equipo
        1)Bueno 2) Regular 3) Malo
        ''')
        h.Controladora().adicionar(h.Terapia(ident,nombre_sala,cant_camas,cant_pacientes,estado_equipo))
        print('''
        *******************************************
        *Fueron adicionados a la lista los valores*
        *******************************************
        ''')
    

def visualizar_listado():
    control=h.Controladora()
    lista = control.listar_mal_estado()
    print(f'''
    **********************************************************
    *Nombres de las salas con equipos en mal estado:  {lista}
    **********************************************************
    ''') 
    return menu()

def contar_salas_con_IC():
    control=h.Controladora()
    cant = control.contarSalasCumplenIndCalidad()
    print(f'''
    *********************************************
    *La cantidad de salas que cumplen son {cant} 
    *********************************************
    ''')
    return menu()

def salir():
    salida = input('''No selecciono ninguna opcion valida.\n Desea Salir SI o NO\n''')
    if salida == 'SI' or salida == 'S' or salida == 'si' or salida == 'Si' or salida == 's':
        print('Gracias por usar nuestro modulo de gestion')
    else:
        print('Ingrese una opcion valida ')
        menu()


if __name__ == '__main__':
    menu()
 
