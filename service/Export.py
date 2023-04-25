from interface.IExport import IExport

class Export(IExport):
    def __init__(self, export_content :IExport) -> None:
        self._export_content = export_content


    def export(self, table, path, page_name) -> bool:
        return self._export_content.export(table, path, page_name)