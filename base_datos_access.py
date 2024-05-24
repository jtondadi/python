import pyodbc
import pandas as pd

obSQL=pyodbc.connect(r'DRIVER={"Microsoft Access Driver (*.mdb, *.accdb)"};DBQ=C:\Users\juan\CURSOS.accdb')
cursor=obSQL.cursor()

#ahora un query basico
cursor.execute("SELECT * FROM CURSOS")
for row in cursor.fetchall():
    print (row)

#    
#import pyodbc
#obSQL = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\USUARIO\Downloads\Nueva carpeta\DATABASE.accdb')
#cursor = obSQL.cursor()
#cursor.execute("select Distinct PERSONAS.`NOMBRE COMPLETO`,PERSONAS.PROVINCIA as `ID PROVINCIA`,BASE.PROVINCIA from PERSONAS LEFT Join BASE ON BASE.CPRO=PERSONAS.PROVINCIA ORDER BY PERSONAS.[NOMBRE COMPLETO]")  
#nCampo = [column[0] for column in cursor.description]
#print(nCampo)
#for i in cursor.fetchall():
#    print (i)