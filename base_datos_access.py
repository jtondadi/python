import pyodbc
conn = pyodbc.connect("Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=cursos.accdb")
cursor=conn.cursor()

#ahora un query basico
cursor.execute("SELECT * FROM CURSOS")
for row in cursor.fetchall():
    print (row)

conn.close()
#    
#import pyodbc
#obSQL = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\USUARIO\Downloads\Nueva carpeta\DATABASE.accdb')
#cursor = obSQL.cursor()
#cursor.execute("select Distinct PERSONAS.`NOMBRE COMPLETO`,PERSONAS.PROVINCIA as `ID PROVINCIA`,BASE.PROVINCIA from PERSONAS LEFT Join BASE ON BASE.CPRO=PERSONAS.PROVINCIA ORDER BY PERSONAS.[NOMBRE COMPLETO]")  
#nCampo = [column[0] for column in cursor.description]
#print(nCampo)
#for i in cursor.fetchall():
#    print (i)