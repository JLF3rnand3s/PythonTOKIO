#IMPORTS
from flask import Flask, render_template, request, redirect, url_for
import db
from models import Tarea

app = Flask(__name__)# En app se encuentra nuestro servidor web de Flask

#definimos una ruta --> lo que vaya dentro de las comillas es la ruta
#de la pag, es decir por ejemplo para eliminar accedeas a:
#app.route("/eliminar")
@app.route("/")
def home():
    #para pasarle el archivo html que tengo usamos "render_template" de Flask
    print("Estoy en el home")
    #consulta para sacar todos los registros de la tabla de tareas e imprimirlos por pantalla cuando inicie la app
    todas_las_tareas = db.session.query(Tarea).all()
    for i in todas_las_tareas:
        print(i)
    return render_template("index.html", listaTareas = todas_las_tareas)
#PD: si los html no estan en la carpeta templates, no funcionará

#recuerda que existe otro metodo que es el "get"
@app.route("/crear-tarea", methods=["POST"])
def crear():

    #con el "request.form" y poniendo el "name" del input o boton al cual queramos acceder podemos programar las
    #acciones que querramos que haga el formulario cuando pulsemos dicho boton
    tarea = Tarea(contenido=request.form["contenido_tarea"], hecha=False)
    db.session.add(tarea)
    db.session.commit()
    db.session.close()
    #cuando creamos una tarea, en vez de redireccionarnos a otro lado nos
    #redirecciona a la misma pagina
    return redirect(url_for("home"))

#por ende puedes tener mas de una ruta, ejemplo

@app.route("/tarea-hecha/<id>")
def hecha(id):
    tarea = db.session.query(Tarea).filter_by(id_tarea=id).first()
#esto lo que hara es que se cambiara el estado del booleano actual (es decir si es true se pondra en false o viceversa)ç
    tarea.hecha = not(tarea.hecha)
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/eliminar-tarea/<id>")
def eliminar(id):
    tarea = db.session.query(Tarea).filter_by(id_tarea=id).delete()
    db.session.commit()

    return redirect(url_for("home"))



# El debug=True hace que cada vez que reiniciemos el
#servidor o modifiquemos codigo, el servidor de Flask se reinicie solo
if __name__ == "__main__":
    #Creamos la db
    #db.Base.metadata.drop_all(db.engine, checkfirst=True)
    #indicacion para SQLAlchemy para que cree las tablas que se encuentre en models.py
    db.Base.metadata.create_all(db.engine)
    app.run(debug=True)
