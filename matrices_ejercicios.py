#Ejercicios matrices
matriz = []

for i in range(0,6):
    matriz.append([0]*6)

#print(matriz)
def mostrar (elemento):
    for x in elemento:
        print(x)

#mostrar(matriz)

pos_actual = -1
for x in matriz:
    pos_actual += 1
    for j in range(len(matriz)-1):
        x[pos_actual] = 1

# mostrar(matriz)ckl

pos_actual = 0
for x in matriz:
    pos_actual += -1
    for j in range(len(matriz)-1):
        x[pos_actual] = 1

mostrar(matriz)