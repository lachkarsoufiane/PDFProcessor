from abc import ABC, abstractstaticmethod

class IForamtterStrategy(ABC):
    @abstractstaticmethod
    def format(content):
        pass