from random import randint


print('''
        Bienvenidos al super juego de carros
''')

jugadores = []
while True:
    var = input('Introduzca los jugadores: ')
    if var == '':
        break
    else:
        jugadores.append(var)

#print(jugadores)
pista = []
size = 30
posiciones = []
for x in range(len(jugadores)):
    posiciones.append([])
    pista.append(['-']*size)

#print(posiciones)
def mostrar(pista):
    for i in pista:
        print(''.join(i))

#mostrar(pista)

def mov(pista,jugadores):
    cant_meta = 0
    while True:
        cont=0
        for i in pista:
            pos = randint(1,size-1)
            #print(pos)
            posiciones[cont].append(pos)
            if pos >= max(posiciones[cont]):
                i[pos]=jugadores[cont]
            if pos == size -1 :
                print(f'El jugador {jugadores[cont]} ha llegado a la meta')
                cant_meta += 1
            cont += 1
            #print(posiciones)
        mostrar(pista)
        print('*'*30)
        if cant_meta >= len(jugadores)+1:
            break

print(mov(pista,jugadores))
