#Ejercicios matrices
matriz = []

for i in range(0,6):
    matriz.append([0]*6)

#print(matriz)
def mostrar (elemento):
    for x in elemento:
        print(x)

#mostrar(matriz)
#[1, 0, 0, 0, 0, 0]
#0, 1, 0, 0, 0, 0]
#[0, 0, 1, 0, 0, 0]
#[0, 0, 0, 1, 0, 0]
#[0, 0, 0, 0, 1, 0]
#[0, 0, 0, 0, 0, 1]
#***************************************************
# pos_actual = -1
# for x in matriz:
#     pos_actual += 1
#     for j in range(len(matriz)-1):
#         x[pos_actual] = 1

# mostrar(matriz)
#**********************************************************
#[0, 0, 0, 0, 0, 1]
#[0, 0, 0, 0, 1, 0]
#[0, 0, 0, 1, 0, 0]
#[0, 0, 1, 0, 0, 0]
#[0, 1, 0, 0, 0, 0]
#[1, 0, 0, 0, 0, 0]
# pos_actual = 0
# for x in matriz:
#     pos_actual += -1
#     for j in range(len(matriz)-1):
#         x[pos_actual] = 1

# mostrar(matriz)
#***********************************************************
#[1, 0, 0, 0, 0, 0]
#[1, 1, 0, 0, 0, 0]
#[1, 1, 1, 0, 0, 0]
#[1, 1, 1, 1, 0, 0]
#[1, 1, 1, 1, 1, 0]
#[1, 1, 1, 1, 1, 1]
# cont =0
# lista=[]

# for x in matriz:
#     lista.append(cont)
#     #print(lista)
#     for j in range(len(lista)):
#         x[j] = 1
#     cont += 1
# mostrar(matriz)
#**************************************************
#[0, 0, 0, 0, 0, 1]
#[0, 0, 0, 0, 1, 1]
#[0, 0, 0, 1, 1, 1]
#[0, 0, 1, 1, 1, 1]
#[0, 1, 1, 1, 1, 1]
#[1, 1, 1, 1, 1, 1]
cont =0
lista=[0]

for x in matriz:
    lista.append(cont)
    #print(lista)
    for j in range(1,len(lista)):
        x[-j] = 1
    cont += -1
mostrar(matriz)