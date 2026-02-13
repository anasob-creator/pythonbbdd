from .services import service01prueba
print("Soy un Main, tengo los prints tins tins")
texto=service01prueba.getSaludo()
print(texto)
perro=service01prueba.getMascota()
leona=service01prueba.getMascota2()
print(f"Nombre: {perro.nombre}, Raza: {perro.raza}")
print(leona.nombre)
print(leona.edad)
lista=service01prueba.getListaMascotas()
for dato in lista:
    print(dato.nombre)
