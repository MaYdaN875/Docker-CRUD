from crud import iniciar_menu_crud_completo, iniciar_menu_crud_usuario


class CRUDInterface:
    def ejecutar_menu(self, puerto):
        raise NotImplementedError("Debe implementarse en una subclase.")


class CRUDAdminAdapter(CRUDInterface):
    def ejecutar_menu(self, puerto):
        iniciar_menu_crud_completo(puerto)


class CRUDUsuarioAdapter(CRUDInterface):
    def ejecutar_menu(self, puerto):
        iniciar_menu_crud_usuario(puerto)
