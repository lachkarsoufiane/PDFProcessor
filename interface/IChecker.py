from abc import ABC, abstractstaticmethod
from interface.ICheckStrategy import ICheckStrategy

class IChecker(ABC):
    @abstractstaticmethod
    def check(json :str)->bool:
        pass