from interface.ISplitterStrategy import ISplitterStrategy
import json

class ParagraphKeywordSplitterStrategy(ISplitterStrategy):
    
    def split_content(content, start_keyword, end_keyword = None):
        end_keyword = start_keyword if end_keyword is None else end_keyword
        paragraphs = []
        paragraph = ""
        current_title = None
        content_list = content.split("\n")
        
        for i, line in enumerate(content_list):
            
            if(line.find(end_keyword) >= 0 and line != current_title and current_title ):
                paragraphs.append(paragraph)
                paragraph = ""
                current_title = line
            
            if(line.find(start_keyword) >= 0):
                paragraph += line + " \n"
                current_title = line
            
            if(current_title and line.find(start_keyword) < 0):
                paragraph += line + " \n"
            
            if(i == len(content_list)-1):
                paragraphs.append(paragraph)
        
        return paragraphs