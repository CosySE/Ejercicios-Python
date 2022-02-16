
import pickle

#clase base o padre 
class Sala():
    def __init__(self,ident,nombre_sala,cant_camas,cant_pacientes): 
        self.nombre_sala =nombre_sala
        self.cant_camas = cant_camas
        self.cant_pacientes =cant_pacientes
        self.ident = ident
    def indicador_calidad(self):#metodo polimorfico
        pass
 
class General(Sala): 
    def __init__(self, ident, nombre_sala, cant_camas, cant_pacientes,nombre_medico):
        super().__init__(ident, nombre_sala, cant_camas, cant_pacientes)
        self.nombre_medico = nombre_medico
        
    def indicador_calidad(self):# metodo virtual implementado para la clase hija
        if self.cant_pacientes < self.cant_camas and self.nombre_medico !=' ':
            return True
        else:
            return False
                   
class Terapia(Sala):
    def __init__(self, ident, nombre_sala, cant_camas, cant_pacientes,estado_equipo):
        super().__init__(ident, nombre_sala, cant_camas, cant_pacientes)
        self.estado_equipo = estado_equipo
    
    def indicador_calidad(self):#metodo virtual implementado para la clase hija
        if self.estado_equipo == '1':
            return True
        else:
            return False   
#clase controladora que contiene la lista polimrfica y solucion de todos los metodos del script para su solucion
class Controladora:

    lista_de_salas = [] #lista polimorfica

    def adicionar (self,elemento): # adiciona los datos introducidos por el usuario en el otro modulo
        self.lista_de_salas.append(elemento)

    def contarSalasCumplenIndCalidad(self):
        cantidad = 0
        for i in self.lista_de_salas:
            if isinstance(i,General) and i.indicador_calidad() == True:
                cantidad += 1
            elif isinstance(i,Terapia)and i.indicador_calidad() == True:
                cantidad += 1  
        return cantidad 
    
    def listar_mal_estado(self):
        lista_mal = []
        for lista in self.lista_de_salas:
            if isinstance(lista,Terapia):
                if lista.estado_equipo == '3':
                    lista_mal.append(lista.nombre_sala)
        return lista_mal

    def visualizarSalasIntroducidas(self):
        for dato in self.lista_de_salas:
            if isinstance(dato,General):
                print(f'Identificador : {dato.ident} \nNombre de sala: {dato.nombre_sala} \nCantidad de camas: {dato.cant_camas} \nCantidad de pacientes: {dato.cant_pacientes} \nNombre del medico: {dato.nombre_medico} ')
                print('**************************************')
            elif isinstance(dato, Terapia):
                print(f'Identificador : {dato.ident} \nNombre de sala: {dato.nombre_sala} \nCantidad de camas: {dato.cant_camas} \nCantidad de pacientes: {dato.cant_pacientes} \nEstado del equipo: {dato.estado_equipo} ')
                print('**************************************')
            else:
                print('La lista se encuentra vacia ')

    def mostrar_datos_segun_ID(self,valorDado):
        try:
            estado = False
            for dato in self.lista_de_salas:
                if dato.ident == valorDado:
                    print(f'Identificador : {dato.ident} \nNombre de sala: {dato.nombre_sala} \nCantidad de camas: {dato.cant_camas} \nCantidad de pacientes: {dato.cant_pacientes} \n')
                    print('**************************************')
                    estado = True
                    break
            if estado == False:
                raise Exception('Identificador no encontrado')    
        except Exception as error:
            print(error)    
            
    
       
    def crearYGuardarFichero(self):
        almacenar = input('Desea almacenar la informacion introducida hasta ahora: SI o NO \n')
        if almacenar =='SI' or almacenar == 'S' or almacenar == 'si' or almacenar == 'Si' or almacenar == 's':
            with open('fichero.pickle','wb') as file:
                pickle.dump(self.lista_de_salas,file)
                print('Datos almacenados satisfactoriamente ')
        else:
            print('Salir sin guardar')      

    def comprobarSiExisteFicheroycargar(self):
        try:
            with open('fichero.pickle','rb') as carga: 
                #preguntamos al usuario si esta interesado en cargar los datos almacenados en el fichero
                cargar = input('Existe un archivo con informacion, desea cargarlo antes de empezar:\n Si o NO : ')
                if cargar == 'Si' or cargar == 'S' or cargar == 'si' or cargar == 'SI' or cargar =='s':
                    cargado = pickle.load(carga)
                    #lo introducimos nuevamente a la lista para usarlos
                    for dato in cargado:
                        self.lista_de_salas.append(dato)
                    print('Datos cargados correctamente')      
                else:
                    print('Continue con la aplicacion')
        except:
            print('No existen archivos con datos almacenados')            


