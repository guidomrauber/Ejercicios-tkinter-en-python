import pymysql

conexion1=pymysql.connect(host='localhost',
                                user='root',
                                password='',
                                db='bd1')
cursor1=conexion1.cursor()
cursor1.execute("show databases")
for base in cursor1:
    print(base)
conexion1.close()  