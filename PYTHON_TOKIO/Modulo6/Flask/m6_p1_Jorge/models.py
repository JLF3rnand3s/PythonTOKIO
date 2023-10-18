#IMPORTS ---------------------------------
from sqlalchemy import Column, String, Integer, Boolean
import db


#EL "DB.BASE" lo que hace es que marca la clase creada y la mapea automaticamente
#para asi poder agregarla a las bd como tablas.
class Tarea(db.Base):

    __tablename__ = "tarea" #nombre de la tabla de la bd
    __table_args__ = {'sqlite_autoincrement': True} #hace que haya algun elemento que se autoincremente
    #columna id_persona que sera un integer y tendra una clave primaria
    id_tarea = Column(Integer, primary_key = True)
    #los tributos (nombre y edad) tienen que coincidir con los que tengas en la programacion
    #lo especiales (id_persona) o necesariamente tienen que estar en la app
    contenido = Column(String(200), nullable=False) #no puede ser falso o no puede estar en blanco el campo nombre
    hecha = Column(Boolean)
#El modelo es mas o menos el siguiente COLUMN(TIPODATO, ETC)

    def __init__(self, contenido, hecha):
        self.contenido = contenido
        self.hecha = hecha
        print("Tarea creada correctamente")
    def __repr__(self):
        return "Tarea {}: {} ({})".format(self.id, self.contenido, self.hecha)

    def __str__(self):
       return f"Tarea: {self.id_tarea} --> {self.contenido} ({self.hecha})"