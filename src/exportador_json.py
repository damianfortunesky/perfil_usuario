import json
from i_exportador import IExportadorPerfil

class ExportadorJSON(IExportadorPerfil):
    def exportar(self, perfil_usuario):
        datos = {
            "usuario": perfil_usuario.get_nombre_usuario(),
            "correo": perfil_usuario.get_correo()
        }
        print(json.dumps(datos, indent=4))
