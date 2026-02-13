# Insertar un departamento
# Tenemos la posibilidad de poner un alias a este namespace
from services import service02oracledepartamentos as serv
print ("Bienvenido a mi servicio Eliminación de departamentos")
# Creamos la clase
servicio=serv.ServiceDepartamentos()
print("Insertar departamento")
numero=int(input("Id departamento:"))
nombre=input("Nombre departamento:")
localidad=input("Localidad: ")
# # Le pasamos los datos para insertar los datos que nos han dado
reg=servicio.insertarDepartamento(numero, nombre, localidad)
print(f"Insertados:{reg}")
# ahora eliminamos un departmento
servicio=serv.ServiceDepartamentos()
print("Eliminar departamento")
print("Dame el Id del departamentoa elminar:")
numero=int(input())
reg=servicio.eliminarDepartamento(numero)
print(f"Eliminados: {reg}")
print("Fin del programa")
# ahora update un departmento por su id
servicio=serv.ServiceDepartamentos()
print("Actualizar departamento")
id=int(input("Id departamento:"))
nombre=input("Nombre departamento:")
localidad=input("Localidad: ")
reg=servicio.updateDepartamento(id, nombre, localidad)
print(f"Insertados:{reg}")