from tkinter import *
import sqlite3
from tkinter import ttk


class Producto:

    db = "database/productos.db"

    def __init__(self, root):
        self.ventana = root
        self.ventana.title("App Gestor de Productos") #titulo de la app
        self.ventana.resizable(1,1)#habilita la redimension, para quitarla ponemos (0,0)
        self.ventana.wm_iconbitmap("recursos\shop-icon_34368.ico")#icono de la app

        #Creacion del contenedor delFrame principal(en Tkinter t0do va por frames, columnas, filas y paquetes)
        frame = LabelFrame(self.ventana, text="Registrar un nuevo Producto")
        frame.grid(row=0, column=0, columnspan=3, pady=30)

        #Label Nombre
        self.etiqueta_nombre = Label(frame, text="Nombre")
        self.etiqueta_nombre.grid(row=1,column=0)

        #Entry Nombre
        self.nombre = Entry(frame)
        self.nombre.focus()
        self.nombre.grid(row=1,column=1)

        # Label Precio
        self.etiqueta_precio = Label(frame, text="precio")
        self.etiqueta_precio.grid(row=2, column=0)

        # Entry Precio
        self.precio = Entry(frame)
        self.precio.grid(row=2, column=1)

        #boton añadir producto
        self.boton_add = ttk.Button(frame, text="Guardar Producto", command=self.addProducto)
        self.boton_add.grid(row=3,columnspan=2, sticky=W+E) #El sticky es para poner el boton centrado
        #el sticky funciona con coordenadas (norte sur este oeste....)

        #Mensaje informativo para el usuario
        self.mensaje = Label(text="", fg="red")
        self.mensaje.grid(row=3, column=0, columnspan=2, sticky=W+E)


        #Tabla Productos (las tablas en tkinter tienen sus propios estilos que no se pueden cambiar mucho)
        # Estilo personalizado para la tabla
        style = ttk.Style()
        style.configure("mystyle.Treeview", highlightthickness=0, bd=0,
                        font=('Calibri', 11)) # Se modifica la fuente de la tabla
        style.configure("mystyle.Treeview.Heading",
                        font=('Calibri', 13, 'bold')) # Se modifica la fuente de las cabeceras
        style.layout("mystyle.Treeview",
                     [('mystyle.Treeview.treearea', {'sticky':'nswe'})]) # Eliminamos los bordes

        #Creamos la tabla
        self.tabla = ttk.Treeview(height=20, columns=2, style="mystyle.Treeview")
        self.tabla.grid(row=4,columnspan=2,column=0)
        #declaramos las cabeceras
        self.tabla.heading("#0", text="Nombre", anchor=CENTER)
        self.tabla.heading("#1", text="Precio", anchor=CENTER)

        # Estructura de la tabla
        self.tabla = ttk.Treeview(height = 20, columns = 2, style="mystyle.Treeview")
        self.tabla.grid(row = 4, column = 0, columnspan = 2)
        self.tabla.heading('#0', text = 'Nombre', anchor = CENTER) # Encabezado 0
        self.tabla.heading('#1', text='Precio', anchor = CENTER) # Encabezado 1

        #boton eliminar
        boton_eliminar = ttk.Button(text="ELIMINAR", command=self.delProducto)
        boton_eliminar.grid(row=5, column=0, sticky=W+E)
        boton_editar = ttk.Button(text="EDITAR", command=self.editProducto)
        boton_editar.grid(row=5,column=1,sticky=W+E)




        self.getProductos()

    def db_consulta(self,consulta,parametros=()):
        with sqlite3.connect(self.db) as con:
            cursor = con.cursor()

            resultado = cursor.execute(consulta,parametros)
            con.commit()

        return resultado

    def getProductos(self):

        registros_tabla = self.tabla.get_children()
        for fila in registros_tabla:
            self.tabla.delete(fila)

        query = "SELECT * FROM producto ORDER BY nombre DESC"
        registro = self.db_consulta(query)
        for r in registro:
            print(r)
            self.tabla.insert("",0, text=r[1],values=r[2])
            #identificador, el 0 es para cuando metas un valor se pone al principio
            #Los valores de r[1] te lo pone en la parte de la izquierda
            #los valores de r[2] te lo pone en la derecha
            #en otras palabras text es la columna de la izq y values es la de la derecha
            #para poner mas columnas ponemos el resto de columnas en values

    def validacion_nombre(self):
        return len(self.nombre.get()) != 0
    def validacion_precio(self):
        return len(self.precio.get()) != 0

    def addProducto(self):
        if self.validacion_nombre() and self.validacion_precio():
            query = 'INSERT INTO producto VALUES(NULL, ?, ?)'  # Consulta SQL (sin losdatos)
            parametros = (self.nombre.get(), self.precio.get())  # Parametros de la consulta SQL
            self.db_consulta(query, parametros)
            print("Datos Guardados")
            self.mensaje["text"] = "Producto {} añadido con exito".format(self.nombre.get())
            self.nombre.delete(0, END)  # Borrar el campo nombre del formulario
            self.precio.delete(0, END)  # Borrar el campo precio del formulario

            #Esto no es necesario, solo son comprobaciones
          #  print(self.nombre.get())
           # print(self.precio.get())
        elif self.validacion_nombre() and self.validacion_precio() == False:
            print("El precio es obligatorio")
            self.mensaje["text"] = "El precio es obligatorio"

        elif self.validacion_precio() and self.validacion_nombre() == False:
            print("El nombre es obligatorio")
            self.mensaje["text"] = "El nombre es obligatorio"

        else:
            print("El precio y nombre son obligatorios para añadir un producto")
            self.mensaje["text"] = "El precio y nombre son obligatorios para añadir un producto"


        self.getProductos()  # Cuando se finalice la insercion de datos volvemos a
        #invocar a este metodo para actualizar el contenido y ver los cambios

    def editProducto(self):
        #Creamos la variable nombre que utilizaremos mas tarde
        old_nombre = self.tabla.item(self.tabla.selection())["text"]
        old_precio = self.tabla.item(self.tabla.selection())["values"][0]

        print("Editar Producto")
        self.mensaje["text"]=""
        #creamos una nueva ventana
        self.ventana_editar = Toplevel()#Creamos la ventana
        self.ventana_editar.title("Editar Producto")
        self.ventana_editar.resizable(1,1)
        self.ventana_editar.wm_iconbitmap("recursos/shop-icon_34368.ico")

        titulo = Label(self.ventana_editar, text="Edicion de Productos", font=("Calibri", 50, "bold"))
        titulo.grid(row=0,column=0)
        frame_ep = LabelFrame(self.ventana_editar, text="Editar el siguiente producto")
        frame_ep.grid(row=1,column=0,columnspan=20,pady=20)

#-----------------------------------------------------------------------------------------------------------

        #nombre del label antiguo
        self.etiqueta_nombre_antiguo = Label(frame_ep, text="Nombre Antiguo: ", font=("Calibri", 13))
        self.etiqueta_nombre_antiguo.grid(row=2,column=0)

        #input en el cual aparecera el nombre antiguo y no sera modificable, es decir, sera un only read
        self.input_nombre_antiguo = Entry(frame_ep, textvariable=StringVar(self.ventana_editar,
                                                                           value= old_nombre),state="readonly", font=("Calibri", 13))
        self.input_nombre_antiguo.grid(row=2,column=1)

        #Label Nombre nuevo
        self.etiqueta_nombre_nuevo = Label(frame_ep, text="Nombre nuevo: ", font=("Calibri", 13))
        self.etiqueta_nombre_nuevo.grid(row=3, column=0)

        #Entry nombre nuevo
        self.input_nombre_nuevo = Entry(frame_ep, font=("Calibri", 13))
        self.input_nombre_nuevo.grid(row=3, column=1)

#-----------------------------------------------------------------------------------------------------------------
        # precio del label antiguo
        self.etiqueta_precio_antiguo = Label(frame_ep, text="Precio Antiguo: ", font=("Calibri", 13))
        self.etiqueta_precio_antiguo.grid(row=4, column=0)
        self.input_precio_antiguo = Entry(frame_ep, textvariable=StringVar(self.ventana_editar,
                                                                           value=old_precio), state="readonly",
                                          font=("Calibri", 13))
        self.input_precio_antiguo.grid(row=4, column=1)

        # Label Precio nuevo
        self.etiqueta_precio_nuevo = Label(frame_ep, text="Precio nuevo: ", font=("Calibri", 13))
        self.etiqueta_precio_nuevo.grid(row=5, column=0)

        # Entry nombre nuevo
        self.input_precio_nuevo = Entry(frame_ep, font=("Calibri", 13))
        self.input_precio_nuevo.grid(row=5, column=1)

        self.boton_actualizar = ttk.Button(frame_ep, text="Actualizar Producto",command=lambda: self.actualizarProd(self.input_nombre_nuevo.get(),
                                                                                                                    self.input_nombre_antiguo.get(),
                                                                                                                    self.input_precio_nuevo.get(),
                                                                                                                    self.input_precio_antiguo.get()))
       #Utilizamos "lambda" para enviar varios parametros ya que con command no podemos pasarle parametros a una funcion
        self.boton_actualizar.grid(row=6,columnspan=2,sticky=W+E)

    def delProducto(self):
        #print(self.tabla.item(self.tabla.selection()))
        print("Eliminar Producto")
        #borramos si tenemos algun mensaje anterior lo ponemos en blanco
        self.mensaje["text"] = ""

        nombre = self.tabla.item(self.tabla.selection())["text"]
        query = "DELETE FROM producto WHERE nombre = ?"
        self.db_consulta(query, (nombre,))
        self.mensaje["text"] = "Producto {} ha sido eliminado con exito.".format(nombre)
        self.getProductos()

    def actualizarProd(self, nuevo_nombre, antiguo_nombre, nuevo_precio, antiguo_precio):

        producto_modificado = False
        query = 'UPDATE producto SET nombre = ?, precio = ? WHERE nombre = ? AND precio = ?'
        if nuevo_nombre != '' and nuevo_precio != '':
            # Si el usuario escribe nuevo nombre y nuevo precio, se cambian ambos
            parametros = (nuevo_nombre, nuevo_precio, antiguo_nombre, antiguo_precio)
            producto_modificado = True
        elif nuevo_nombre != '' and nuevo_precio == '':
            # Si el usuario deja vacio el nuevo precio, se mantiene el pecio anterior
            parametros = (nuevo_nombre, antiguo_precio, antiguo_nombre, antiguo_precio)
            producto_modificado = True
        elif nuevo_nombre == '' and nuevo_precio != '':
            # Si el usuario deja vacio el nuevo nombre, se mantiene el nombre anterior
            parametros = (antiguo_nombre, nuevo_precio, antiguo_nombre, antiguo_precio)

            producto_modificado = True

        if (producto_modificado):
            self.db_consulta(query, parametros)  # Ejecutar la consulta
            self.ventana_editar.destroy()  # Cerrar la ventana de edicion de productos
            self.mensaje['text'] = 'El producto {} ha sido actualizado con éxito'.format(antiguo_nombre) # Mostrar mensaje para el usuario
            self.getProductos()  # Actualizar la tabla de productos
        else:
            self.ventana_editar.destroy()  # Cerrar la ventana de edicion de productos
            self.mensaje['text'] = 'El producto {} NO ha sido actualizado'.format(antiguo_nombre) # Mostrar mensaje para el usuario

if __name__ == "__main__":
    root = Tk()  # Instancia de la ventana principal
    app = Producto(root) # Se envia a la clase Producto el control sobre la ventana root
    root.mainloop() # Comenzamos el bucle de aplicacion, es como un while True