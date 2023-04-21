from abc import ABC,abstractstaticmethod

class IOpenerStrategy(ABC):
    @abstractstaticmethod
    def open_file(file_path):
        pass