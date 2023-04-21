from abc import ABC, abstractstaticmethod

class ICheckStrategy(ABC):
    @abstractstaticmethod
    def check(json :str) ->bool:
        pass