from time import time
import timeit
# codigo_lineal ='''
# lista = [20,54,1,56,47,12,54,11,33,84,12]
# nueva_lista = [x for x in lista if x == 12]
# '''

# print(timeit.timeit(stmt=codigo_lineal,number=10000))

#complejidad exponecial
#mientras crecen los datos las operaciones crecen exponencialmente
# exponecnial = """
# for i in [1, 2, 3]:
#     for j in range(i):
#         print(f"i vale {i} y j vale {j}")
# """
# print(timeit.timeit(stmt=exponecnial,number=100))

#para el caso del la complejidad logaritmica se puede ver el ejemplo en los metodos
#de busqueda como divide y venceras
divide = """
import random
def ordenamiento_mezcla(lista):
    if len(lista) > 1: #garantizar que la lista sea cada vez mas pequena
        medio = len(lista) // 2
        izquierda = lista[:medio]
        derecha = lista[medio:]
        print(izquierda, '*'*5,derecha)

        #hacemos una llamada recursiva en cada mitad para ir haciendolo mas pequeña
        ordenamiento_mezcla(izquierda)
        ordenamiento_mezcla(derecha)
        #de aqui hacia arriba la parte del codigo tiene un crecimiento logaritmico cada
        #vez se vuelve mas pequeño
        #iteradores para recorrer las dos sublistas
        i = 0
        j = 0

        #iterador de la lista principal
        k = 0
    #esta segunda parte del codigo es para ir comparando las listas pequeñas e ir
    #recombinandolas
        while  i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1
            k += 1
        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k +=1
        while j < len(derecha):
            lista[k] = derecha[j]
            k += 1
            j += 1
        print(f'izquierda {izquierda}')
    return lista

tamano_de_lista = 7

lista = [random.randint(0,100) for i in range(tamano_de_lista)]
print(lista)
print('-' *20)

lista_ordenada = ordenamiento_mezcla(lista)
print(lista_ordenada)
"""
print(timeit.timeit(stmt=divide,number=3))