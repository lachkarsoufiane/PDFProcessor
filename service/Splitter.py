from interface.ISplitter import ISplitter
from interface.ISplitterStrategy import ISplitterStrategy

class Splitter(ISplitter):
    
    def __init__(self, split_strategy :ISplitterStrategy) -> None:
        self._split_strategy = split_strategy
    
    def read_file(self, content, start, end):
        return self._split_strategy.split_content(content, start, end) 