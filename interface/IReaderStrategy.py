from abc import ABC, abstractclassmethod

class IReaderStrategy(ABC):
    @abstractclassmethod
    def read_file(file, page):
        pass