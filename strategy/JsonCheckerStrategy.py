from interface.ICheckStrategy import ICheckStrategy
import json

class JsonCheckerStrategy(ICheckStrategy):
    def check(json_content :str) -> bool:
        try:
            json.loads(json_content)
        except:
            print("El contenido no es de formato Json!")
            return False
        return True