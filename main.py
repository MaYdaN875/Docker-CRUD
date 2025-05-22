from factory import ContenedorFactory
from utils import obtener_puerto_mysql
from crud_adapter import CRUDAdminAdapter, CRUDUsuarioAdapter


def main():
    nombre = input(
        "Ingresa el nombre del contenedor (ContenedorA, B, etc.): ").strip().lower()
    rol = input("¿Eres 'admin' o 'usuario'?: ").strip().lower()

    try:
        contenedor = ContenedorFactory.crear(nombre)
        instancia = contenedor.crear_contenedor(nombre)
        puerto = obtener_puerto_mysql(instancia)

        if rol == "admin":
            menu = CRUDAdminAdapter()
        elif rol == "usuario":
            menu = CRUDUsuarioAdapter()
        else:
            print("Rol inválido.")
            return

        menu.ejecutar_menu(puerto)

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
