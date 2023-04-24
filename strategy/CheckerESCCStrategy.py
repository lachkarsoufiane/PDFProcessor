from interface.ICheckStrategy import ICheckStrategy
import json

class CheckerESCCStrategy(ICheckStrategy):
    
    def check(json_content :str) -> bool:
        # Deserializar el contenido json
        titles = ["Extension", "Extension with new Remark", "Extension with re-scope", "Editorial", "Removal"]
        try:
            content = json.loads(json_content)
        except:
            print("El contenido no es de tipo json.")
            return False
        
        for title in content:
            if title not in titles:
                print(title)
                return False
        
        return True
