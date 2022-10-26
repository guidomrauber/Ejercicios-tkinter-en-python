import pymysql

conexion1=pymysql.connect(host='localhost',
                                user='root',
                                password='',
                                db='bd1')
cursor1=conexion1.cursor()
cursor1.execute("show tables")
for tabla in cursor1:
    print(tabla)
conexion1.close()   