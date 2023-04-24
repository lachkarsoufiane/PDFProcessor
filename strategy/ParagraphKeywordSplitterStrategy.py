from interface.ISplitterStrategy import ISplitterStrategy
import json

class ParagraphKeywordSplitterStrategy(ISplitterStrategy):
    
    def split_content(content, start_keyword, end_keyword = None):
        end_keyword = start_keyword if end_keyword is None else end_keyword
        result = {}
        paragraph = ""
        current_title = None
        content_list = content.split("\n")
        index = 0
        for i, line in enumerate(content_list):
            
            # si llegamos al final del parrafo, guardomos
            if(line.find(end_keyword) >= 0 and line != current_title and current_title ):
                result[index] = paragraph
                paragraph = ""
                current_title = line
            
            if(line.find(start_keyword) >= 0):
                index += 1
                result[index] = ""
                paragraph += line + " \n"
                current_title = line
            
            if(current_title and line.find(start_keyword) < 0):
                paragraph += line + " \n"
            
            if(i == len(content_list)-1):
                result[index] = paragraph
            
        result = json.dumps(result)
        
        return result