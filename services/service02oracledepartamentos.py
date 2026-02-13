# crear un service de oracles sobre los dptos.
#     Tendrá un método para insertar un dpto.
#     sobre services creamos una nueva clase llamada
#     service02oracledepartamentos.py

import oracledb

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
    
    
    
