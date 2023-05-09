from strategy.PDFOpenerStrategy import PDFOpenerStrategy
from strategy.PDFTableReaderStrategy import PDFTableReaderStrategy
from strategy.ParagraphRegexSplitterStrategy import ParagraphRegexSplitterStrategy
from strategy.ESCCFormatter import ESCCFormatter
from strategy.TableESCCFormatterStrategy import TableESCCFormatterStrategy
from strategy.JsonCheckerStrategy import JsonCheckerStrategy
from strategy.ExcelExportStrategy import ExcelExportStrategy
from strategy.CheckerESCCStrategy import CheckerESCCStrategy
from service.Checker import Checker
from service.Opener import Opener
from service.Reader import Reader
from service.Splitter import Splitter
from service.Formatter import Formatter
from service.Export import Export


import Asset.Regex as Regex


title_re = Regex.TITLE_RE
extra_re = Regex.EXTRA_RE

file_path = "./files/esccrpqpl005iss234_jan_23.pdf"
export_path = "./export/result.xlsx"
sheet_name = "ESCC"
page = 3


opener = Opener(PDFOpenerStrategy)
reader = Reader(PDFTableReaderStrategy)
splitter = Splitter(ParagraphRegexSplitterStrategy)
json_checker = Checker(JsonCheckerStrategy)
ESCCchecker = Checker(CheckerESCCStrategy)
formatter = Formatter(ESCCFormatter)
table_formatter = Formatter(TableESCCFormatterStrategy)
exporter = Export(ExcelExportStrategy)



def run():

    # Abrir el fichero
    open_file = opener.open_file(file_path)
    
    # Leer el contenido
    content = reader.read_file(open_file, page)

    paragraphs = splitter.split_content(content, title_re, extra_re)
    # Formatear los parrafos si estan en el formato requerido 

    if ESCCchecker.check(paragraphs) and json_checker.check(paragraphs):
        print("Formateando el contenido...")
        formated = formatter.format(paragraphs)
        print("Creado la tabla...")
        table = table_formatter.format(formated)
        print("Exportando la tabla...")
        
        if exporter.export(table, export_path, sheet_name) :
            print("Se ha exportado la tabla correctamente.")
        else :
            print("No se ha podido exportar la tabla!")
    else:
        print("Bad format!")


