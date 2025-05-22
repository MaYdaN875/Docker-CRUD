import mysql.connector
import time


def iniciar_menu_crud_completo(puerto):
    conexion, cursor = preparar_bd(puerto)

    while True:
        print("\n=== Menú CRUD (Admin) ===")
        print("1. Crear usuario")
        print("2. Ver usuarios")
        print("3. Actualizar usuario")
        print("4. Eliminar usuario")
        print("5. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            crear(cursor)
        elif opcion == "2":
            leer(cursor)
        elif opcion == "3":
            actualizar(cursor)
        elif opcion == "4":
            eliminar(cursor)
        elif opcion == "5":
            break

        conexion.commit()

    cursor.close()
    conexion.close()


def iniciar_menu_crud_usuario(puerto):
    conexion, cursor = preparar_bd(puerto)

    while True:
        print("\n=== Menú CRUD (Usuario) ===")
        print("1. Ver usuarios")
        print("2. Actualizar usuario")
        print("3. Crear usuario (requiere contraseña)")
        print("4. Eliminar usuario (requiere contraseña)")
        print("5. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            leer(cursor)
        elif opcion == "2":
            actualizar(cursor)
        elif opcion == "3":
            if verificar_password():
                crear(cursor)
            else:
                print("Contraseña incorrecta.")
        elif opcion == "4":
            if verificar_password():
                eliminar(cursor)
            else:
                print("Contraseña incorrecta.")
        elif opcion == "5":
            break

        conexion.commit()

    cursor.close()
    conexion.close()

# --- funciones auxiliares reutilizables ---


def preparar_bd(puerto):
    import mysql.connector
    import time
    time.sleep(5)
    conexion = mysql.connector.connect(
        host="localhost",
        port=int(puerto),
        user="root",
        password="root"
    )
    cursor = conexion.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS testdb")
    cursor.execute("USE testdb")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(100),
            correo VARCHAR(100)
        )
    """)
    return conexion, cursor


def crear(cursor):
    nombre = input("Nombre: ")
    correo = input("Correo: ")
    cursor.execute(
        "INSERT INTO usuarios (nombre, correo) VALUES (%s, %s)", (nombre, correo))


def leer(cursor):
    cursor.execute("SELECT * FROM usuarios")
    for row in cursor.fetchall():
        print(row)


def actualizar(cursor):
    id_ = input("ID del usuario a actualizar: ")
    correo = input("Nuevo correo: ")
    cursor.execute(
        "UPDATE usuarios SET correo = %s WHERE id = %s", (correo, id_))


def eliminar(cursor):
    id_ = input("ID del usuario a eliminar: ")
    cursor.execute("DELETE FROM usuarios WHERE id = %s", (id_,))


def verificar_password():
    pwd = input("Contraseña de root: ")
    return pwd == "admin123"  # puedes cambiarla o usar variables de entorno
