#compresion de listas 
numeros = [1,2,3,4,5,6,8,7,9,10]
multiplicado =[]

for num in numeros:
    multiplicado.append(num * 10)

#print(multiplicado)
#[ variable for variable in rango, lista, elemento ,iterable ]
multiplo = [x * 10 for x in numeros]
#print (multiplo)

nombre = 'python'

mayuscula = [i.upper() for i in nombre]
#print (mayuscula)

convierte = [str(x) for x in numeros ]

#print (convierte)
#condicionales 
pares = [valor for valor in numeros if valor % 2 == 0 ]

impar = [valor for valor in numeros if valor % 2 != 0]

#print ('pares', pares ,'impares', impar)

#[<expresion >for <variable> in <secuencia> if <condicion>]listas comprimidas con condicionles

#ejercicio 1
#crear lista con potencia de dos en un rango de 10 numeros
lista_potencia =[x**2 for x in range(0,11)]
#print(lista_potencia)
#ejercicio 2
