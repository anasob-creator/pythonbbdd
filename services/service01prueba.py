# Creamos un método para comprobar si lo podemos llamar desde el main
from models import mascota
def getSaludo():
    return "Hoy es juernes"
# Un modelo es un class con propiedades. Sobre models creamos 
# una nueva clase llamada mascota. 
def getMascota():
   dato=mascota.Mascota()
   dato.nombre="FLounder"
   dato.raza="Perro"
   dato.edad=10
   return dato
def getMascota2():
    dato=mascota.Mascota()
    dato.nombre="Nala"
    dato.raza="Leona"
    dato.edad=14
    return dato
def getListaMascotas():
    listaMascotas=[]
    dato=mascota.Mascota()
    dato.nombre="Milton"
    dato.raza="Python"
    dato.edad=8
    return dato

