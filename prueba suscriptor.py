#prueba suscriptor
#ingresar cadena minimo 8 caracteres y que cada caracter sea diferente no se repita 
#en casso de que algo no sea valido , se le solicita al usuario que ingrese el correcto 
# cuando inglrese el correcto guardarlo en un txt

# una funcion para que me realice la comprobacion de los datos introducidos
def comprobar():
    texto = input('ingrese no menos de 8 caracteres: \n')
    if len(texto) > 8:#condicion para comprobar que tenga mas de 8 
        for y in texto:#primer ciclo del texto
            cont=0 #contador en cero para que me cuente la cant de ocurrencias del mismo caracter
            for i in texto:#aqui al ser un ciclo anidado por cada elemento del primer ciclo compara con todos los del segundo
                if i == y :# condicion de comparacion
                    cont += 1# incrementa para saber que cuando el contador pase de dos debe parar
            if cont >= 2:#condicion para saber que ya tenemos repetidos
                print(f'existen repetidos {cont}')
                return True#retornar true para que en el while siga preguntando hasta que este correcto          
          
    else:# si es menor que 8 te lanza el mensjaje y devuelve retorna true la funcion para que sirva de condicion par ael while
        print('mas de 8 caracteres')
        return True
    return False     #si todo es correcto retorna false y ya pararia de preguntar en el while

#while que me preguntara si la funcion comprobar esta devolviendo true se sigue ejecutando si devuelve false todo OK
while True:
    if comprobar() == True:
        True
    else:
        False
        print('Continue todo OK')
        break
