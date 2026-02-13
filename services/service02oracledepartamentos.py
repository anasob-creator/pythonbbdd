# crear un service de oracle sobre los dptos.
#     Tendrá un método para insertar un dpto.
#     sobre services creamos una nueva clase llamada
#     service02oracledepartamentos.py

import oracledb
# Importamos la clase departamento
from models import departamento

class ServiceDepartamentos:
    def __init__ (self):
        self.connection=oracledb.connect(user="SYSTEM",
                                        password="oracle", 
                                        dsn="localhost/FREEPDB1")
        
    def insertarDepartamento(self, numero, nombre, localidad):
        cursor=self.connection.cursor()
        sql="insert into DEPT values(:num, :nom, :loc)"
        cursor.execute(sql, (numero, nombre, localidad,))
        self.connection.commit()
        registros=cursor.rowcount
        cursor.close()
        return registros
    
    def eliminarDepartamento(self, numero):
        cursor=self.connection.cursor()
        sql="delete from DEPT where DEPT_NO=:id"
        cursor.execute(sql, (numero,))
        self.connection.commit()
        registros=cursor.rowcount
        cursor.close()
        return registros
    
    def updateDepartamento(self, id, nombre, localidad):
        cursor=self.connection.cursor()
        sql="update DEPT set DNOMBRE=:nombre, LOC=:loc where DEPT_NO=:id"
        cursor.execute(sql, (nombre,localidad,id,))
        self.connection.commit()
        registros=cursor.rowcount
        cursor.close()
        return registros
    
    def getNombreDepartamento(self, id):
        cursor=self.connection.cursor()
        sql="select DNOMBRE from DEPT where DEPT_NO=:id"
        cursor.execute(sql, (id,))
        row=cursor.fetchone()
        nombre=row[0]
        cursor.close()
        return nombre
    
    def getDepartamento(self, id):
        cursor=self.connection.cursor()
        sql="select * from DEPT where DEPT_NO=:id"
        cursor.execute(sql, (id,))
        row=cursor.fetchone()
        # Creamos un nuevo departamento
        dept=departamento.Departamento()
        dept.idDepartamento=row[0]
        dept.nombre=row[1]
        dept.localidad=row[2]
        cursor.close()
        return dept

    
    
    
