import tkinter as tk
from tkinter import messagebox
import mysql.connector


# CONEXIÓN A LA BASE DE DATOS


def conectar_bd():

    try:

        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="gestion_fauna_flora"
        )

        return conexion

    except mysql.connector.Error as err:

        messagebox.showerror(
            "Error",
            f"No se pudo conectar:\n{err}"
        )

        return None


# VARIABLES GLOBALES


ids_registros = []



# MOSTRAR REGISTROS


def mostrar_registros():

    global ids_registros

    conexion = conectar_bd()

    if conexion is None:
        return

    cursor = conexion.cursor()

    try:

        cursor.execute("""
            SELECT * FROM FaunaFlora
            ORDER BY ID ASC
        """)

        registros = cursor.fetchall()

        lista.delete(0, tk.END)
        ids_registros.clear()

        for i, reg in enumerate(registros, start=1):

            ids_registros.append(reg[0])

            lista.insert(
                tk.END,
                f"{i}. "
                f"{reg[1]} | "
                f"{reg[2]} | "
                f"{reg[3]} | "
                f"{reg[4]} | "
                f"{reg[5]}"
            )

    except mysql.connector.Error as err:

        messagebox.showerror(
            "Error",
            f"No se pudieron mostrar los registros:\n{err}"
        )

    finally:

        cursor.close()
        conexion.close()



# LIMPIAR CAMPOS


def limpiar_campos():

    entry_codigo.delete(0, tk.END)
    entry_nombre.delete(0, tk.END)
    entry_habitat.delete(0, tk.END)
    entry_estado.delete(0, tk.END)
    entry_region.delete(0, tk.END)


# AGREGAR REGISTRO

def agregar_registro():

    codigo = entry_codigo.get()
    nombre = entry_nombre.get()
    habitat = entry_habitat.get()
    estado = entry_estado.get()
    region = entry_region.get()

    if not (
        codigo and
        nombre and
        habitat and
        estado and
        region
    ):

        messagebox.showwarning(
            "Campos Vacíos",
            "Debe completar todos los campos."
        )

        return

    conexion = conectar_bd()

    if conexion is None:
        return

    cursor = conexion.cursor()

    try:

        cursor.execute("""
            INSERT INTO FaunaFlora
            (
                CodigoIdentificacion,
                NombreCientifico,
                Habitat,
                EstadoConservacion,
                RegionGeografica
            )
            VALUES (%s, %s, %s, %s, %s)
        """,
        (
            codigo,
            nombre,
            habitat,
            estado,
            region
        ))

        conexion.commit()

        messagebox.showinfo(
            "Éxito",
            "Registro agregado correctamente."
        )

        mostrar_registros()
        limpiar_campos()

    except mysql.connector.Error as err:

        messagebox.showerror(
            "Error",
            f"No se pudo agregar el registro:\n{err}"
        )

    finally:

        cursor.close()
        conexion.close()


# ELIMINAR REGISTRO


def eliminar_registro():

    seleccionado = lista.curselection()

    if not seleccionado:

        messagebox.showwarning(
            "Selección",
            "Seleccione un registro."
        )

        return

    indice = seleccionado[0]
    registro_id = ids_registros[indice]

    conexion = conectar_bd()

    if conexion is None:
        return

    cursor = conexion.cursor()

    try:

        cursor.execute(
            "DELETE FROM FaunaFlora WHERE ID = %s",
            (registro_id,)
        )

        conexion.commit()

        messagebox.showinfo(
            "Éxito",
            "Registro eliminado correctamente."
        )

        mostrar_registros()
        limpiar_campos()

    except mysql.connector.Error as err:

        messagebox.showerror(
            "Error",
            f"No se pudo eliminar:\n{err}"
        )

    finally:

        cursor.close()
        conexion.close()


# CARGAR CAMPOS

def cargar_campos(event):

    seleccionado = lista.curselection()

    if not seleccionado:
        return

    indice = seleccionado[0]
    registro_id = ids_registros[indice]

    conexion = conectar_bd()

    if conexion is None:
        return

    cursor = conexion.cursor()

    try:

        cursor.execute("""
            SELECT
                CodigoIdentificacion,
                NombreCientifico,
                Habitat,
                EstadoConservacion,
                RegionGeografica
            FROM FaunaFlora
            WHERE ID = %s
        """,
        (registro_id,))

        datos = cursor.fetchone()

        if datos:

            limpiar_campos()

            entry_codigo.insert(0, datos[0])
            entry_nombre.insert(0, datos[1])
            entry_habitat.insert(0, datos[2])
            entry_estado.insert(0, datos[3])
            entry_region.insert(0, datos[4])

    except mysql.connector.Error as err:

        messagebox.showerror(
            "Error",
            f"No se pudo cargar el registro:\n{err}"
        )

    finally:

        cursor.close()
        conexion.close()


# ACTUALIZAR REGISTRO

def actualizar_registro():

    seleccionado = lista.curselection()

    if not seleccionado:

        messagebox.showwarning(
            "Selección",
            "Seleccione un registro."
        )

        return

    indice = seleccionado[0]
    registro_id = ids_registros[indice]

    codigo = entry_codigo.get()
    nombre = entry_nombre.get()
    habitat = entry_habitat.get()
    estado = entry_estado.get()
    region = entry_region.get()

    conexion = conectar_bd()

    if conexion is None:
        return

    cursor = conexion.cursor()

    try:

        cursor.execute("""
            UPDATE FaunaFlora
            SET
                CodigoIdentificacion = %s,
                NombreCientifico = %s,
                Habitat = %s,
                EstadoConservacion = %s,
                RegionGeografica = %s
            WHERE ID = %s
        """,
        (
            codigo,
            nombre,
            habitat,
            estado,
            region,
            registro_id
        ))

        conexion.commit()

        messagebox.showinfo(
            "Éxito",
            "Registro actualizado correctamente."
        )

        mostrar_registros()
        limpiar_campos()

    except mysql.connector.Error as err:

        messagebox.showerror(
            "Error",
            f"No se pudo actualizar:\n{err}"
        )

    finally:

        cursor.close()
        conexion.close()


# INTERFAZ GRÁFICA

ventana = tk.Tk()

ventana.title("Sistema de Gestión de Fauna y Flora")
ventana.geometry("850x600")
ventana.configure(bg="#ecfdf5")


# TÍTULO

titulo = tk.Label(
    ventana,
    text="Gestión de Fauna y Flora",
    font=("Arial", 20, "bold"),
    bg="#ecfdf5",
    fg="#14532d"
)

titulo.pack(pady=15)



# FRAME FORMULARIO


frame_formulario = tk.LabelFrame(
    ventana,
    text=" Información de Especies ",
    bg="white",
    padx=20,
    pady=15,
    font=("Arial", 10, "bold")
)

frame_formulario.pack(
    padx=20,
    pady=10,
    fill="x"
)


# CAMPOS

campos = [
    ("Código:", 0),
    ("Nombre Científico:", 1),
    ("Hábitat:", 2),
    ("Estado de Conservación:", 3),
    ("Región Geográfica:", 4)
]

for texto, fila in campos:

    tk.Label(
        frame_formulario,
        text=texto,
        bg="white",
        font=("Arial", 10)
    ).grid(
        row=fila,
        column=0,
        sticky="w",
        pady=5
    )


entry_codigo = tk.Entry(frame_formulario, width=40)
entry_codigo.grid(row=0, column=1)

entry_nombre = tk.Entry(frame_formulario, width=40)
entry_nombre.grid(row=1, column=1)

entry_habitat = tk.Entry(frame_formulario, width=40)
entry_habitat.grid(row=2, column=1)

entry_estado = tk.Entry(frame_formulario, width=40)
entry_estado.grid(row=3, column=1)

entry_region = tk.Entry(frame_formulario, width=40)
entry_region.grid(row=4, column=1)


# BOTONES

frame_botones = tk.Frame(
    ventana,
    bg="#ecfdf5"
)

frame_botones.pack(pady=15)


tk.Button(
    frame_botones,
    text="Agregar",
    command=agregar_registro,
    bg="#15803d",
    fg="white",
    width=15
).pack(side="left", padx=5)


tk.Button(
    frame_botones,
    text="Actualizar",
    command=actualizar_registro,
    bg="#2563eb",
    fg="white",
    width=15
).pack(side="left", padx=5)


tk.Button(
    frame_botones,
    text="Eliminar",
    command=eliminar_registro,
    bg="#dc2626",
    fg="white",
    width=15
).pack(side="left", padx=5)


tk.Button(
    frame_botones,
    text="Limpiar",
    command=limpiar_campos,
    bg="#6b7280",
    fg="white",
    width=15
).pack(side="left", padx=5)


# LISTA DE REGISTROS

frame_lista = tk.LabelFrame(
    ventana,
    text=" Registros almacenados ",
    bg="white",
    padx=10,
    pady=10,
    font=("Arial", 10, "bold")
)

frame_lista.pack(
    padx=20,
    pady=10,
    fill="both",
    expand=True
)


lista = tk.Listbox(
    frame_lista,
    width=100,
    height=12,
    font=("Arial", 10)
)

lista.pack(
    side="left",
    fill="both",
    expand=True
)


scroll = tk.Scrollbar(frame_lista)

scroll.pack(
    side="right",
    fill="y"
)

lista.config(yscrollcommand=scroll.set)
scroll.config(command=lista.yview)

lista.bind(
    "<<ListboxSelect>>",
    cargar_campos
)


# MOSTRAR DATOS AL INICIO


mostrar_registros()


# EJECUTAR VENTANA
ventana.mainloop()