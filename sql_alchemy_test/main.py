import sys
import db
from models import Persona
from sqlalchemy import and_, or_, text


#FUNCIONES -----------------------

def agregarPersonasIniciales():
    p1 = Persona("Jorge", 25)
    p2 = Persona("Gary", 30)
    p3 = Persona("Gari", 13)
    p4 = Persona("Danie", 85)
    p5 = Persona("Maria", 12)
    p6 = Persona("Sara", 20)
    p7 = Persona("Luisa", 45)
    #Mandar toda la informacion a la base de datos

    #ejemplo de añadir un solo objeto
    #db.session.add(p1)

#Para añadirlos todos hay que hacer una lista y añadir todos los objetos:
    listaPersonas = [p1, p2, p3, p4, p5, p6, p7]
    db.session.add_all(listaPersonas)

    db.session.commit()
    db.session.close()

def consultasdePrueba():
    print("\n #1 Obtener un objeto a partir de su id (PK). Si no la encuentra devuelve None.")
    #result = db.session.query(Persona).get(3) --> forma antigua, dentro del get pones el id que buscas
    result = db.session.get(Persona, 3) #forma actual (tabla, id)
    print(result)

    print("\n #2 Obtener todos los objetos de una tabla")
    resulta = db.session.query(Persona).all()
    for p in resulta:
        print(f"\t Nombre: {p.nombre} -> Edad: {p.edad}")

    print("\n #3. Obtener el primer objeto de una consulta")
    resultado = db.session.query(Persona).first()
    print(resultado)

    print("\n #4. Contar el numero de elementos devueltos por una consulta")
    resultadito = db.session.query(Persona).count()
    print("El numero de personas registradas es de {}".format(resultadito))

    print("\n #5. Ordenar el resultado de una consulta")
    result = db.session.query(Persona).order_by("nombre").all()
    for p in result:
        print(p)

    print("\n #6. Ordenar el resultado de una consulta y mostrar los primeros 3 resultados")
    result = db.session.query(Persona).order_by("nombre").limit(3)
    for p in result:
        print(p)

    print("\n #7. Aplicar filtros a una consulta con el filter")
    result = db.session.query(Persona).filter(Persona.edad < 25)
    for p in result:
        print(p)

    print("\n #8. Aplicar filtro like")
    result = db.session.query(Persona).filter(Persona.nombre.ilike("%rg%")).all
    for p in result:
        print(p)

    print("\n #9. Aplicar filtro in_")
    result = db.session.query(Persona).filter(Persona.id_persona.in_([1,2,6])).all()
    #result = db.session.query(Persona).filter(Persona.nombre.in_(["Jorge","Sara"])).all()
    for p in result:
        print(p)
    print("\n #10. Aplicar filtro and_")
    c1 = Persona.edad < 18
    c2 = Persona.edad < 50
    result = db.session.query(Persona).filter(and_(c1, c2)).all() #and(condicion1, condicion2)
    for p in result:
        print(p)

    print("\n #11. Aplicar filtro or_")
    c1 = Persona.edad == 18
    c2 = Persona.edad == 50
    result = db.session.query(Persona).filter(or_(c1, c2)).all() #and(condicion1, condicion2)
    for p in result:
        print(p)

    print("\n #12. Ejecutar instrucciones SQL Explicitas")
    result = db.session.query(Persona).from_statement(text("SELECT * from persona")).all
    for p in result:
        print(p)

def agregarPersonas():
   print("\n >>>>> Agregar Persona")

   nombre = input("Nombre de la persona: ")
   edad = int(input("Edad de la persona: "))
   #añadimos las personas a la tabla que querramos
   db.session.add(Persona(nombre,edad))
   #guardamos y cerramos la db
   db.session.commit()
   db.session.close()
   print("PERSONA CREADA")

def editarPersonas():
    print("\n > Editar Persona")
    #para saber cual persona queremos editar le preguntamos al user el id de la persona por ejemplo
    persona_id = int(input("ID de la persona a editar"))

    #Ahora intentamos localizar a la persona con el identificador pedido
    person = db.session.query(Persona).filter(
        Persona.id_persona == persona_id).first() #--> si le ponemos ".first" nos devuelve
    #el primer registro encontrado

#la linea anterior basicamente dice lo siguiente: buscame en la tabla "persona" y si
#consigues un id en tu tabla que coincida con el que tengo, pasamelo

    #EJEMPLO PARA EDITAR
    if person is None:
        print("La persona no existe")
    else:
        #si encuentra la persona
        print(person)
        edad_nueva = int(input("Introduzca la edad nueva"))
        person.edad = edad_nueva

        db.session.commit()
        db.session.close()
        print("PERSONA ACTUALIZADA")
    #puedes pedirle tambien pedirle que te haga cosas como pedir una persona en especifico:
    #person = db.session.query(Persona).filter(Persona.nombre == "Jorge") --> para que te saque la persona que le pides


def eliminarPersonas():
    print("\n > Eliminar Persona")
    persona_id = int(input("ID de la persona a eliminar"))

    person = db.session.query(Persona).filter(
        Persona.id_persona == persona_id).first()  # --> si le ponemos ".first" nos devuelve

    # EJEMPLO PARA EDITAR
    if person is None:
        print("La persona no existe")
    else:
        # si encuentra la persona
        db.session.delete(person)
        db.session.commit()
        db.session.close()
        print("PERSONA ELIMINADA")

def verPersonas():
    print("\n > VER PERSONAS:")
    #sacamos la informacion de la tabla Persona, pero tenemos que pasarle el nombre de la
    #clase que tenemos en el models.py y con el .all() sacamos todos los registros

   #EL QUERY te devuelve una lista de objetos traidos de las bd
    personas = db.session.query(Persona).all()
    for x in personas:
        print(f"\n > ID: {x.id_persona} Nombre: {x.nombre} Edad: {x.edad}")

#PROGRAMA ------------------------



if __name__ == "__main__":
    #Resetamos la bd si existe
    db.Base.metadata.drop_all(db.engine, checkfirst=True)

    #indicacion para SQLAlchemy para que cree las tablas que se encuentre en models.py
    db.Base.metadata.create_all(db.engine)

#Creacion de menu el cual nos pemitira comprobar que nuestra bd corre bien
    while(True):
        print("\n1. Agregar personas iniciales\n"
              "2. Consultas de prueba\n"
              "3. Agregar persona\n"
              "4. Editar persona\n"
              "5. Eliminar persona\n"
              "6. Ver persona\n"
              "7. Salir")
        opcion = int(input("Introduzca una opcion (1-7)"))

        if opcion == 1:
            agregarPersonasIniciales()
        elif opcion == 2:
            consultasdePrueba()
        elif opcion == 3:
            agregarPersonas()
        elif opcion == 4:
            editarPersonas()
        elif opcion == 5:
            eliminarPersonas()
        elif opcion == 6:
            verPersonas()
        elif opcion == 7:
            sys.exit(1)
        else:
            print("Opción no valida")