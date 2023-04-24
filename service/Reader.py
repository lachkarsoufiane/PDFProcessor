from interface.IReader import IReader
from interface.IReaderStrategy import IReaderStrategy

class Reader(IReader):
    
    def __init__(self, reader_strategy :IReaderStrategy) -> None:
        self._reader_strategy = reader_strategy
    
    def read_file(self, file, page :int):
        return self._reader_strategy.read_file(file, page) 