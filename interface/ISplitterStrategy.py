from abc import ABC, abstractstaticmethod

class ISplitterStrategy(ABC):
    @abstractstaticmethod
    def split_content(content, start, end = None):
        pass