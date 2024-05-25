import pyodbc
conn = pyodbc.connect("Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=cursos.accdb")
cursor=conn.cursor()

#ahora un query basico
cursor.execute("SELECT * FROM CURSOS")
for row in cursor.fetchall():
    print (row)

conn.close()
#
# pyodbc (librería para tratamiento de la base de datos)
# instalación libreria pyodbc [** pip (! pip -m install pyodbc )]** para que pueda realizar la conexión a la base de datos
# conn - conexión a la base de datos
# cursor - se utiliza para poder recorrer posteriormente la base de datos
# execute - consulta sql 
# for - recorrido del cursor, y crear resultado en row
# basado en este ejemplo
# cursos.accdb (base de datos de Access 2019) archivo python donde el fichero de la base de datos
#
#import pyodbc
#obSQL = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\USUARIO\Downloads\Nueva carpeta\DATABASE.accdb')
#cursor = obSQL.cursor()
#cursor.execute("select Distinct PERSONAS.`NOMBRE COMPLETO`,PERSONAS.PROVINCIA as `ID PROVINCIA`,BASE.PROVINCIA from PERSONAS LEFT Join BASE ON BASE.CPRO=PERSONAS.PROVINCIA ORDER BY PERSONAS.[NOMBRE COMPLETO]")  
#nCampo = [column[0] for column in cursor.description]
#print(nCampo)
#for i in cursor.fetchall():
#    print (i)
