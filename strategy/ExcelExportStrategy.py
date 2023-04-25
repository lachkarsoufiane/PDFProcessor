from interface.IExport import IExport
from pathlib import Path
import pandas as pd


class ExcelExportStrategy(IExport):
    def export(table, path, page_name) -> bool:
        mode_type = 'w'
        sheet = None
        # comprobar si el fichero existe, para usar el append
        path = Path(path)
        if path.is_file():
            mode_type = 'a'
            sheet = 'new'
        try:
            with pd.ExcelWriter(path, mode = mode_type, if_sheet_exists = sheet ) as writer:
                df = pd.DataFrame(table)
                df.to_excel(writer, sheet_name=page_name)
        except Exception as e:
            print(e)
            return False
        return True