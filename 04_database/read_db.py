import mysql.connector
cnx=mysql.connector.connect(user='root', password='zhangyuru',host='127.0.0.1', database='farm', auth_plugin='mysql_native_password')

cursor = cnx.cursor()
query = ("SHOW DATABASES")
cursor.execute(query)

#loop
for row in cursor.fetchall():
    print(row)

query = ("INSERT INTO `Customers` VALUES ('gugu', 'dada', 'asfa@dsfdsf.com')")
cursor.execute(query)

#clean
cnx.commit()
cursor.close()
cnx.close()