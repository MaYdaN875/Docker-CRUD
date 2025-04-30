from factory import ContenedorFactory
from crud import iniciar_menu_crud
from utils import obtener_puerto_mysql


def main():
    nombre = input(
        "Ingresa el nombre del contenedor (ContenedorA, B, etc.): ").strip().lower()

    try:
        contenedor = ContenedorFactory.crear(nombre)
        instancia = contenedor.crear_contenedor(nombre)
        puerto = obtener_puerto_mysql(instancia)
        print(f"Contenedor listo en puerto local {puerto}")
        iniciar_menu_crud(puerto)
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
