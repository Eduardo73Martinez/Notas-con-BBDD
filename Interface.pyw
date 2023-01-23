from tkinter import*
from tkinter import messagebox
import sqlite3 

#-----------------funciones------------------

def conexionBBDD():
	miConexion=sqlite3.connect("Usuarios")
	miCursor= miConexion.cursor()
	try:
	    miCursor.execute('''
		   CREATE TABLE DATOSUSUARIOS (
		   ID INTEGER PRIMARY KEY AUTOINCREMENT,
		   NOMBRE_USUARIO VARCHAR (50),
		   PASSWORD VARCHAR(50),
		   APELLIDO VARCHAR(10),
		   DIRECCION VARCHAR(50),
		   COMENTARIOS VARCHAR(100))
		   ''')
	    messagebox.showinfo("BBDD", "BBDD creada con exito")
	except:
		messagebox.showwarning("¡Atención", "La BBDD ya existe!")

def SalirAplicacion():
	valor=messagebox.askquestion("Salir", "¿Deseas salir de la aplicación?")
	if valor=="yes":
		root.destroy()

def limpiarCampos():
	miNombre.set("")
	miId.set("")
	miApellido.set("")
	miDireccion.set("")
	miPass.set("")
	TextoComentario.delete(1.0, END)

def crear():
	miConexion=sqlite3.connect("Usuarios")
	miCursor=miConexion.cursor()
	datos=miNombre.get(), miPass.get(),miApellido.get(), miDireccion.get(), TextoComentario.get("1.0",END)
	#miCursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL,'"+ miNombre.get()+ "','" + miPass.get()+ "','" + miApellido.get() + "','"+ miDireccion.get()+ "','"+ TextoComentario.get("1.0", END) + "')")
	miCursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL,?,?,?,?,?)", (datos))
	miConexion.commit()
	messagebox.showinfo("BBDD", "Registro asignado con exito")

def leer():
	miConexion=sqlite3.connect("Usuarios")
	miCursor= miConexion.cursor()
	miCursor.execute("SELECT * FROM DATOSUSUARIOS WHERE ID=" + miId.get())
	elUsuario=miCursor.fetchall()
	for Usuarios in elUsuario:
		miId.set(Usuarios[0])
		miNombre.set(Usuarios[1])
		miPass.set(Usuarios[2])
		miApellido.set(Usuarios[3])
		miDireccion.set(Usuarios[4])
		TextoComentario.insert(1.0, Usuarios[5])
	miConexion.commit()

def actualizar():
	miConexion=sqlite3.connect("Usuarios")
	miCursor=miConexion.cursor()
	miCursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO='" + miNombre.get()+ "', PASSWORD='" + miPass.get()+ "', APELLIDO='" + miApellido.get()+ "', DIRECCION='" + miDireccion.get()+ "', COMENTARIOS='" + TextoComentario.get("1.0",END)+ "'WHERE ID=" + miId.get())
	miConexion.commit()
	messagebox.showinfo("BBDD", "Registro actualizado con exito")

def eliminar():
	miConexion=sqlite3.connect("Usuarios")
	miCursor=miConexion.cursor()
	miCursor.execute("DELETE FROM DATOSUSUARIOS WHERE ID=" + miId.get())
	miConexion.commit()
	messagebox.showinfo("BBDD","¡Registro borrado con exito!")

root=Tk()


frame=Frame(root)
frame.pack()

Barramenu=Menu(frame)
root.config(menu=Barramenu)

BBDD=Menu(Barramenu,tearoff=0)
BBDD.add_cascade(label="conectar", command=conexionBBDD)
BBDD.add_cascade(label="salir", command= SalirAplicacion)



CRUD=Menu(Barramenu,tearoff=0)
CRUD.add_cascade(label="Crear", command=crear)
CRUD.add_cascade(label="Leer", command=leer)
CRUD.add_cascade(label="Actualizar", command=actualizar)

Borrar=Menu(Barramenu,tearoff=0)
Borrar.add_cascade(label="Borrar Campos",command=limpiarCampos)



Barramenu.add_cascade(label="BBDD", menu=BBDD)
Barramenu.add_cascade(label="CRUD", menu=CRUD)
Barramenu.add_cascade(label="Borrar", menu=Borrar)



#creo los label para orientarme
labelID=Label(frame, text="ID:  ")
labelID.grid(row=0, column=0, pady=10, padx=20)

labelNombre=Label(frame, text="Nombre:  ")
labelNombre.grid(row=1, column=0, pady=10, padx=20)

labelPassword=Label(frame, text="Password:  ")
labelPassword.grid(row=2, column=0, pady=10, padx=20)

labelApellido=Label(frame, text="Apellido:  ")
labelApellido.grid(row=3, column=0, pady=10, padx=20)

labelDireccion=Label(frame, text="Direccion:  ")
labelDireccion.grid(row=4, column=0, pady=10, padx=20)

#creo las entradas de texto

miId=StringVar()
miNombre=StringVar()
miApellido=StringVar()
miPass=StringVar()
miDireccion=StringVar()

EntradaID=Entry(frame, textvariable=miId, width=30)
EntradaID.grid(row=0,column=1)

EntradaNombre=Entry(frame, textvariable=miNombre,width=30)
EntradaNombre.grid(row=1,column=1)

EntradaPassword=Entry(frame, textvariable=miPass, width=30)
EntradaPassword.grid(row=2,column=1)

EntradaApellido=Entry(frame,textvariable=miApellido, width=30)
EntradaApellido.grid(row=3,column=1)

EntradaDireccion=Entry(frame,textvariable=miDireccion,  width=30)
EntradaDireccion.grid(row=4,column=1)

TextoComentario=Text(frame, width=30, height=10)
TextoComentario.grid(row=5,column=1)



scrollvert=Scrollbar(frame, command=TextoComentario.yview, width=10)
scrollvert.grid(row=5, column=2, sticky="snew")
TextoComentario.config(yscrollcommand = scrollvert.set)


#creo los botones que hay abajo
miFrame2=Frame(root)
miFrame2.pack()

BotonCreate=Button(miFrame2, text="Create", command=crear)
BotonCreate.grid(row=1, column=0, sticky="e", padx=10, pady=10)

BotonRead=Button(miFrame2, text="Read", command=leer)
BotonRead.grid(row=1, column=1, sticky="e", padx=10, pady=10)


BotonUpdate=Button(miFrame2, text="Update", command=actualizar )
BotonUpdate.grid(row=1, column=2, sticky="e", padx=10, pady=10)

BotonDelete=Button(miFrame2, text="Delete", command=eliminar)
BotonDelete.grid(row=1, column=3, sticky="e", padx=10, pady=10)




root.mainloop()