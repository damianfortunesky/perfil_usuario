from user_profile import PerfilUsuario
from exportador_json import ExportadorJSON
from exportador_xml import ExportadorXML

# Crear usuario 
usuario = PerfilUsuario("damian_87", "damian@email.com", "xdseefeD21s123")

# Mostrar en consola
usuario.mostrar_perfil()

# Exportar a JSON
print("\nExportando en formato JSON:")
exportador_json = ExportadorJSON()
exportador_json.exportar(usuario)

# Exportar a XML
print("\nExportando en formato XML:")
exportador_xml = ExportadorXML()
exportador_xml.exportar(usuario)
