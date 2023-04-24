from interface.IFormatterStrategy import IForamtterStrategy
import Asset.Regex as Regex
import json

class DSCCFormatter (IForamtterStrategy):
    def format(content):
        content = json.loads(content)
        result = {}
        titles = ["Document", "Description","URL","File size", "More Info"]
        url_re = Regex.URL_RE
        current_title = None
        for line in content.split("\n"):
            match_title = False
            for title in titles:
                if line.lower().startswith(title.lower()):
                    text = line[len(title)+2:]
                    current_title = title
                    match_title = True
            if not match_title:

                if url_re.match(text):
                    text = text.replace(" ", "")
                result[current_title] = text
                
        return result
        