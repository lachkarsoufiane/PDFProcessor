from interface.IExport import IExport
import pandas as pd

class ExcelExportStrategy(IExport):
    def export(table, path, page_name):
        try:
            with pd.ExcelWriter(path) as writer:
                df = pd.DataFrame(table)
                df.to_excel(writer, sheet_name=page_name)
        except:
            return False
        return True