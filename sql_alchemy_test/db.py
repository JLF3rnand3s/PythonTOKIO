#IMPORTS-----------------------------------
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

#El engine es el que dira en que lenguaje de programacion de bases de datos programaremos, en este caso sqlite
#ADVERTENCIA: el engine no conecta con la bd directamente, eso se hace luego
engine = create_engine('sqlite:///database/personas.db')

'''Ahora creamos la sesion que nos permite realizar transacciones (operaciones) de nuestra db'''
Session = sessionmaker(bind=engine)
#con esto podemos realizar las operaciones de la bd
session = Session()
#ahora vamos al fichero models.py y lo que nos interese que se conviertan en tablas le añadiremos la siguiente variable
Base = declarative_base()