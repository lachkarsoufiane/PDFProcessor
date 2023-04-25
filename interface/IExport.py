from abc import ABC, abstractstaticmethod

class IExport(ABC):
    @abstractstaticmethod
    def export(table, path, page_name):
        pass
