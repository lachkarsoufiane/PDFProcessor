from interface.IFormatterStrategy import IForamtterStrategy
from service.ServiceESCC import ServiceESCC
import Asset.Regex as Regex
import json

class ESCCFormatter (IForamtterStrategy):
    def format(content) -> str:
        content = json.loads(content)
        result = {}
        for title in content:
            certificates =  ServiceESCC.get_certificate(content[title], title, Regex.CERTIFICATE_RE)
            for title in certificates:
                description = ""
                for certificate in certificates[title]:
                    revision = ""
                    manifacturer = ServiceESCC.get_by_regex_from_line(content[title], certificate, Regex.MANUFACTURE_RE)
                    description = ServiceESCC.get_certificate_description(content[title], certificate, Regex.EXTRA_RE) 

                    if(certificate.find("rev") >= 0):
                        revision = certificate[certificate.find("rev"):]
                        certificate = certificate[:-4]
                    result[certificate] = {}
                    
                    result[certificate]["Title"] = title
                    result[certificate]["Revision"] = revision
                    result[certificate]["Manufacturer"] = manifacturer
                    result[certificate]["Description"] = description

        result = json.dumps(result)
        return result
        