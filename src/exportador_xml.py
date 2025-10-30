from i_exportador import IExportadorPerfil

class ExportadorXML(IExportadorPerfil):
    def exportar(self, perfil_usuario):
        print("<PerfilUsuario>")
        print(f"  <usuario>{perfil_usuario.get_nombre_usuario()}</usuario>")
        print(f"  <correo>{perfil_usuario.get_correo()}</correo>")
        print("</PerfilUsuario>")
