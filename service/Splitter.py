from interface.ISplitter import ISplitter
from interface.ISplitterStrategy import ISplitterStrategy

class Splitter(ISplitter):
    
    def __init__(self, split_strategy :ISplitterStrategy) -> None:
        self._split_strategy = split_strategy
    
    def split_content(self, content, start, end = None):
        return self._split_strategy.split_content(content, start, end) 