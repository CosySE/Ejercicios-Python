#diccionarios en python
#
#los diccionarios pueden contener en sus valores cualquier tipo de elemento ya sea tupla , lista u otro diccionario , son elementos mutables

# mi_diccionario = {
# "ke4":<valuy1":<value1>,
# "key2":<value2>,
# "key3":<value3>,
# "keye4>}

# prueba = dict()
# print(type(prueba))

pruebita = {
    1 : "Casillas", 15 : "Ramos",
    3 : "Pique", 5 : "Puyol",
    11 : "Capdevila", 14 : "Xabi Alonso",
    16 : "Busquets", 8 : "Xavi Hernandez",
    18 : "Pedrito", 6 : "Iniesta",
    7 : "Villa"
}

print(type(pruebita))

pruebita[16]= 'Dayana' # modificar

# for i,j in pruebita.items(): # aqui lo recorro por llave y valor
#     print(i,j)
#     print('*******************************')
# del pruebita[7] #eliminar

for i in pruebita.keys(): #aqui se recorren por sus llaves
    print(i)
    # print('*********************por keys**********')

pruebita[34]='Dayitecnologia'

for i in pruebita.values(): #aqui se recorren por sus valores
    print(i)
    print('************values*******************')