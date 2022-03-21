import sqlite3



def insertar(db,elemento):
    db.execute('insert into almacen (a1,i1) values(?,?)',(elemento['a1'],elemento['i1']))
    db.commit()

def leer(db,llave):
    cursor = db.execute('select * from almacen where a1 = ?',(llave,))
    return cursor.fetchone()#se detiene linea a linea

def actualizar(db,llave):
    db.execute('update almacen set i1 = ? where a1 = ?',(llave['i1'],llave['a1']))
    db.commit()

def eliminar(db,llave):
    db.execute('delete from almacen where a1 = ?',(llave,))
    db.commit()

def mostrar(db):
    cursor = db.execute('select * from almacen')
    for row in cursor:
        print('{} : {}'.format(row['a1'],row['i1']))

def principal():
    db = sqlite3.connect('almacen.db')
    db.row_factory = sqlite3.Row
    print('creando tablas')
    db.execute('drop table if exists almacen')
    db.execute('create table almacen (a1 text, i1 int)')
   
    print('insertando elementos')
    insertar(db,dict(a1='campo1',i1=90))
    insertar(db,dict(a1='campo2',i1=390))
    insertar(db,dict(a1='campo3',i1=290))
    insertar(db,dict(a1='campo4',i1=10))
    insertar(db,dict(a1='campo5',i1=50))
    mostrar(db)
    
    print('leyendo datos')
    print(dict(leer(db,'campo2')),dict(leer(db,'campo5')))

    print('Actualizando datos')
    actualizar(db,dict(a1 ='campo3',i1= 5))
    mostrar(db)
    
    print('eliminando datos')
    eliminar(db,'campo1')
    mostrar(db)

principal()
