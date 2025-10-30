from abc import ABC, abstractmethod

class IExportadorPerfil(ABC):
    @abstractmethod
    def exportar(self, perfil_usuario):
        pass
