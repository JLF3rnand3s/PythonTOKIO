#IMPORTS ---------------------------------
from sqlalchemy import Column, String, Integer
import db
#EL "DB.BASE" lo que hace es que marca la clase creada y la mapea automaticamente
#para asi poder agregarla a las bd como tablas.
class Persona(db.Base):

    __tablename__ = "persona" #nombre de la tabla de la bd
    __table_args__ = {'sqlite_autoincrement': True} #hace que haya algun elemento que se autoincremente
    #columna id_persona que sera un integer y tendra una clave primaria
    id_persona = Column(Integer, primary_key = True)
    #los tributos (nombre y edad) tienen que coincidir con los que tengas en la programacion
    #lo especiales (id_persona) o necesariamente tienen que estar en la app
    nombre = Column(String, nullable=False) #no puede ser falso o no puede estar en blanco el campo nombre
    edad = Column(Integer)
#El modelo es mas o menos el siguiente COLUMN(TIPODATO, ETC)

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        print("Persona creada correctamente")

    def __str__(self):
       return f"Persona con nombre {self.nombre} y edad {self.edad}"