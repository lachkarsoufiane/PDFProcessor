from interface.IChecker import IChecker
from interface.ICheckStrategy import ICheckStrategy

class Checker(IChecker):
    
    def __init__(self, check_strategy :ICheckStrategy) -> None:
        self._check_strategy = check_strategy
    
    def check(self, json :str) -> bool:
        return self._check_strategy.check(json) 