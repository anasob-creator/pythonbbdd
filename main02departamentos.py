# Insertar un departamento
# Tenemos la posibilidad de poner un alias a este namespace
from services import service02oracledepartamentos as serv
print ("Bienvenido a mi servicio  de departamentos")
# Creamos la clase
servicio=serv.ServiceDepartamentos()
print ("---------Departamentos------------")
# Si queremos un menú simple
print("-------- Menú -------- ")
print("1. Insertar")
print("2. Mostrar")
print("Seleccione una opción:")
opcion=int(input())
if (opcion==1):
    #código de insertar
    # Vamos a buscar un dpto
    print("Buscar un dept:")
    print("Insertar departamento")
    numero=int(input("Id a buscar:"))
    dato=servicio.getDepartamento(numero)
    print(f"El nombre del departamento es{dato.nombre}")
    print(f"El nombre del departamento es{dato.localidad}")
    # aquí se inserta departamento
    print("Insertar departamento")
    numero=int(input("Id departamento:"))
    nombre=input("Nombre departamento:")
    localidad=input("Localidad: ")
    # Le pasamos los datos para insertar los datos que nos h1an dado
    reg=servicio.insertarDepartamento(numero, nombre, localidad)
    print(f"Insertados:{reg}")
else:
    # código de mostrar
    # Mostramos los dptos. Me tengo que traer la lista
    lista=servicio.getListaDepartamentos()
    for dept in lista:
        print((f"{dept.idDepartamento} - {dept.nombre} - {dept.localidad}"))
# # ahora eliminamos un departmento
# servicio=serv.ServiceDepartamentos()
# print("Eliminar departamento")
# print("Dame el Id del departamentoa elminar:")
# numero=int(input())
# reg=servicio.eliminarDepartamento(numero)
# print(f"Eliminados: {reg}")
# print("Fin del programa")
# # ahora update un departmento por su id
# servicio=serv.ServiceDepartamentos()
# print("Actualizar departamento")
# id=int(input("Id departamento:"))
# nombre=input("Nombre departamento:")
# localidad=input("Localidad: ")
# reg=servicio.updateDepartamento(id, nombre, localidad)
# print(f"Insertados:{reg}")