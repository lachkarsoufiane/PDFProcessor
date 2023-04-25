from abc import ABC, abstractstaticmethod

class IGenerator(ABC):
    @abstractstaticmethod
    def generate(original):
        pass