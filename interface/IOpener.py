from abc import ABC, abstractstaticmethod

class IOpener(ABC):
    @abstractstaticmethod
    def open_file(file_path):
        pass
