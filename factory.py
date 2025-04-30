import docker

# Cliente Docker
docker_client = docker.from_env()

# Base del producto


class ServicioContenedor:
    def crear_contenedor(self, nombre):
        raise NotImplementedError()

# Producto concreto: todos usan MySQL, pero con distinto nombre


class MySQLContenedor(ServicioContenedor):
    def crear_contenedor(self, nombre):
        return docker_client.containers.run(
            "mysql",
            detach=True,
            name=nombre,
            environment={"MYSQL_ROOT_PASSWORD": "root"},
            # Puerto aleatorio local para evitar conflictos
            ports={'3306/tcp': None},
            restart_policy={"Name": "always"}
        )

# Fábrica: puedes extender para más tipos si lo deseas en el futuro


class ContenedorFactory:
    @staticmethod
    def crear(nombre):
        if nombre.lower() in ["contenedora", "contenedorb", "contenedorc", "contenedord"]:
            return MySQLContenedor()
        else:
            raise ValueError("Nombre de contenedor no reconocido")

# Cliente


def main():
    nombre_contenedor = input(
        "Ingresa el nombre del contenedor (ContenedorA, ContenedorB, etc.): ").strip()
    try:
        contenedor = ContenedorFactory.crear(nombre_contenedor)
        instancia = contenedor.crear_contenedor(nombre_contenedor.lower())
        print(f"Contenedor '{instancia.name}' creado con éxito.")
        print(f"ID del contenedor: {instancia.short_id}")
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
