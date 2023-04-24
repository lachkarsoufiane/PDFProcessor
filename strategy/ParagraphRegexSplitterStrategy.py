from interface.ISplitterStrategy import ISplitterStrategy
import json

class ParagraphRegexSplitterStrategy(ISplitterStrategy):
    def split_content(content, start, end = None):
        end = start if end is None else end 
        paragraphs = {}
        paragraph = ""
        current_title = None
        content_list = content.split("\n")
        
        for i, line in enumerate(content_list):
            
            if(i == len(content_list)-1 or end.match(line)):
                paragraphs[current_title] = paragraph
                break

            if(start.match(line) and line != current_title and current_title ):
                paragraphs[current_title] = paragraph
                paragraph = ""
                current_title = line
            
            if(start.match(line)):
                current_title = line.replace(":", "")
                paragraphs[current_title] = {}
            
            if(current_title and not start.match(line)):
                paragraph += line + " \n"

        result = json.dumps(paragraphs)
        
        return result