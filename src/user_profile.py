class PerfilUsuario:
    def __init__(self, nombre_usuario, correo, password):
        self._nombre_usuario = nombre_usuario
        self._correo = None
        self._password = None

        self.set_correo(correo)
        self.set_password(password)

    def get_nombre_usuario(self):
        return self._nombre_usuario

    def get_correo(self):
        return self._correo

    def get_password(self):
        return "*" * len(self._password)

    def set_correo(self, nuevo_correo):
        if "@" in nuevo_correo:
            self._correo = nuevo_correo
        else:
            print("Error: El correo electrónico no es válido.")

    def set_password(self, nueva_password):
        if len(nueva_password) > 8:
            self._password = nueva_password
        else:
            print("Error: La password debe tener más de 8 caracteres.")

    def mostrar_perfil(self):
        print("Nombre de usuario:", self._nombre_usuario)
        print("Correo:", self._correo)
