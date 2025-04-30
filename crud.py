import mysql.connector
import time


def iniciar_menu_crud(puerto):
    time.sleep(10)

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

    while True:
        print("\n=== Menú CRUD ===")
        print("1. Crear usuario")
        print("2. Ver usuarios")
        print("3. Actualizar usuario")
        print("4. Eliminar usuario")
        print("5. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            correo = input("Correo: ")
            cursor.execute(
                "INSERT INTO usuarios (nombre, correo) VALUES (%s, %s)", (nombre, correo))
            conexion.commit()
        elif opcion == "2":
            cursor.execute("SELECT * FROM usuarios")
            for row in cursor.fetchall():
                print(row)
        elif opcion == "3":
            id_ = input("ID del usuario a actualizar: ")
            correo = input("Nuevo correo: ")
            cursor.execute(
                "UPDATE usuarios SET correo = %s WHERE id = %s", (correo, id_))
            conexion.commit()
        elif opcion == "4":
            id_ = input("ID del usuario a eliminar: ")
            cursor.execute("DELETE FROM usuarios WHERE id = %s", (id_,))
            conexion.commit()
        elif opcion == "5":
            print("Saliendo del menú.")
            break
        else:
            print("Opción no válida.")

    cursor.close()
    conexion.close()
