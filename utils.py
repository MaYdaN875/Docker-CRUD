def obtener_puerto_mysql(instancia):
    try:
        return instancia.attrs['NetworkSettings']['Ports']['3306/tcp'][0]['HostPort']
    except (KeyError, IndexError, TypeError):
        raise RuntimeError(
            "No se pudo obtener el puerto del contenedor MySQL.")
