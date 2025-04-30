import docker
from docker.errors import APIError

docker_client = docker.from_env()


class ServicioContenedor:
    def crear_contenedor(self, nombre):
        raise NotImplementedError()


class MySQLContenedor(ServicioContenedor):
    def crear_contenedor(self, nombre):
        try:
            return docker_client.containers.run(
                "mysql",
                detach=True,
                name=nombre,
                environment={"MYSQL_ROOT_PASSWORD": "root"},
                ports={'3306/tcp': None},
                restart_policy={"Name": "always"}
            )
        except APIError as e:
            if e.status_code == 409:
                print(
                    f"Contenedor '{nombre}' ya existe. Recuperando instancia...")
                return docker_client.containers.get(nombre)
            else:
                raise


class ContenedorFactory:
    @staticmethod
    def crear(nombre):
        if nombre.lower() in ["contenedora", "contenedorb", "contenedorc"]:
            return MySQLContenedor()
        else:
            raise ValueError("Nombre de contenedor no válido o no soportado")
