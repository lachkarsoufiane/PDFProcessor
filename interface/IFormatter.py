from abc import ABC, abstractstaticmethod

class IFormatter(ABC):
    @abstractstaticmethod
    def format(content :str)->bool:
        pass