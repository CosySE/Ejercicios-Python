import json

def crear_json_paises_cortos():
    lista_de_longitud = []
    paises_cortos = []

    with open('countries.json','r') as leer :
        paises = json.load(leer)
    
    for pais in paises:
        var = pais['Name']
        lista_de_longitud.append(len(var))
    #print(lista_de_longitud)
    peque = min(lista_de_longitud)

    for pais in paises:
        if len(pais['Name']) == peque:
            paises_cortos.append(pais)
    #print(paises_cortos)
    with open('countries_new.json', 'w') as nuevo:
        json.dump(paises_cortos,nuevo)
    
    with open('countries_new.json') as leer:
        ver = json.load(leer)
    
    return print(f' Los paises de longitud mas corta son  {ver}')

    
crear_json_paises_cortos()