from abc import ABC, abstractstaticmethod

class IChecker(ABC):
    @abstractstaticmethod
    def check(json :str)->bool:
        pass