from interface.IFormatterStrategy import IForamtterStrategy
import Asset.Regex as Regex
import json

class DSCCFormatter (IForamtterStrategy):
    def format(content):
        content = json.loads(content)
        result = []
        url_re = Regex.URL_RE
        for index in content:
            data = {}
            current_title = None
            titles = Regex.DSCC_TITLES_RE.findall(content[index])
            
            for line in content[index].split("\n"):
                match_title = False
                
                for title in titles:
                    if line.lower().startswith(title.lower()):
                        current_title = title
                        data[current_title] = line[len(title)+2:]
                        match_title = True
                

                if not match_title and current_title:
                    data[current_title] += line
                    #Quitar los espacios en blancos, en el caso de ser enlace
                    if url_re.match(data[current_title]):
                        data[current_title] = data[current_title].replace(" ", "")
            
            result.append(data)
        result = json.dumps(result)
        return result
        