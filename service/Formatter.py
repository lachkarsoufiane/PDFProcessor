from interface.IFormatter import IFormatter
from interface.IFormatterStrategy import IForamtterStrategy

class Formatter(IFormatter):
    
    def __init__(self, formatter_strategy :IForamtterStrategy) -> None:
        self._formatter_strategy = formatter_strategy
    
    def format(self, content:str):
        return self._formatter_strategy.format(content) 