from interface.ICheckStrategy import ICheckStrategy
import json

class CheckerESCCStrategy(ICheckStrategy):
    
    def check(json_content :str) -> bool:
        titles = ["Extension", "Extension with new Remark", "Extension with re-scope", "Editorial", "Removal", "Revision"]
        try:
            # Comprobar si el contenido esta en Json
            content = json.loads(json_content)
        except:
            print("El contenido no es de tipo json.")
            return False
        
        # Verficiar los titulos
        for title in content:
            if title not in titles:
                print(title)
                return False
        
        return True
