from interface.IOpener import IOpener
from interface.IOpenerStrategy import IOpenerStrategy

class Opener(IOpener):
    
    def __init__(self, opener_strategy :IOpenerStrategy) -> None:
        self._opener_strategy = opener_strategy
    
    def open_file(self, file_path:str):
        return self._opener_strategy.open_file(file_path) 