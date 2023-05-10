from interface.ICheckStrategy import ICheckStrategy
import json

class CheckerDSCCStrategy(ICheckStrategy):
    def check(content) -> bool:
        titles = ["Document", "Description", "URL", "File size", "More info"]
        try:
            # Comprobar si el contenido esta en Json
            content = json.loads(content)
        except Exception as e:
            print(e)
            return False
        
        # Verificamos los titulos
        for paragraph in content:
            for title in paragraph:
                if title not in titles:
                    return False
        return True
