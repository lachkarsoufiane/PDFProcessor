from abc import ABC, abstractstaticmethod

class ISplitterStrategy(ABC):
    @abstractstaticmethod
    def split_content(content, splitter):
        pass