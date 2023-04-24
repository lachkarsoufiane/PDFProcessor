from abc import ABC, abstractstaticmethod

class IReader(ABC):
    @abstractstaticmethod
    def read_file(file, page :int):
        pass
