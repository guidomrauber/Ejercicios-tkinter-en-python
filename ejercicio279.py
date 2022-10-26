import pymysql

conexion1=pymysql.connect(host='localhost',
                                user='root',
                                password='',
                                db='bd1')
cursor1=conexion1.cursor()
cursor1.execute("select codigo, descripcion, precio from articulos")
for fila in cursor1:
    print(fila)
conexion1.close()  