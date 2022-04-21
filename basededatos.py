import sqlite3

datos = [(234,'pintura',651,23.4),(235,'aluminio',651,56),(236,'escaoba',652,676),(237,'palo',652,56.7)]
def insertar(db,tabla,elemento):
    for i in elemento:
        db.execute(f'insert into {tabla} (cod,nombre,coda,precio) values(?,?,?,?)',(i))
        db.commit()


def insertar_almacen(db):
    cod = input('Introduzca el codigo del almacen: ')
    nombre = input('Introduzca el nombre del almacen: ') 
    cod_centro = input('Introduzca el nombre del centro: ')
    nombre_centro = input('Introduzca el nombre del centro: ')
    db.execute('insert into centro (cod,nombre) values (?,?)',(cod_centro,nombre_centro))
    db.commit()
    db.execute('insert into almacen (cod,nombre) values (?,?)',(cod,nombre))
    db.commit()

def leer(db,llave,tabla):
    db.row_factory = sqlite3.Row
    cursor = db.execute(f'select * from {tabla} where coda = ?',(llave,))
    for row in cursor:
        print('{} : {} : {}'.format(row['cod'],row['nombre'],row['precio']))
    return cursor.fetchone()

def principal():
    db = sqlite3.connect('empresa.db')
    #sustituyendolas en cada llamado pk las crea en memoria y luego te da error
    db.execute('drop table if exists almacen')
    db.execute('drop table if exists centro')
    db.execute('drop table if exists producto')
    #creando tablas
    db.execute('create table almacen (cod int,nombre text)')
    db.execute('create table centro (cod int,nombre text)')
    db.execute('create table producto (cod int,nombre text,coda int,precio float)')

    insertar_almacen(db)
    insertar(db,'producto',datos)
    leer(db,651,'producto')
principal()