#Dada una lista DI con los nombres de los trabajadores del departamento de informática y una lista TP con
#  los nombres de los asistentes al trabajo productivo., 
# obtener una lista con los nombres de la lista DI contenidos en la lista TP?
def obtener_interseccion():
    lista_DI= []
    lista_TP =[]
    while True:
        nombre = input('Introduzca un nombre de la lista DI y presione enter ')
        if nombre == '':
            break
        if nombre.isalpha():
            lista_DI.append(nombre)
        else:
            print('No debe introducir numeros')
        
    while True:
        nombre_tp = input('Introduzca un nombre de la lista TP y presione enter ')
        if nombre_tp == '':
            break
        if nombre_tp.isalpha():
            lista_TP.append(nombre_tp)
        else:
            print('No debe introducir numeros')
    
    var_tp = set(lista_TP)
    var_di = set(lista_DI)
    interseccion = var_di & var_tp
    print(f'los nombres que se intersenctan son {interseccion}')


if __name__=='__main__':
    obtener_interseccion()