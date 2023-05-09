from strategy.PDFOpenerStrategy import PDFOpenerStrategy
from strategy.PDFTextReaderStrategy import PDFTextReaderStrategy
from strategy.JsonCheckerStrategy import JsonCheckerStrategy
from strategy.ParagraphKeywordSplitterStrategy import ParagraphKeywordSplitterStrategy
from strategy.DSCCFormatter import DSCCFormatter
from strategy.TableDSCCFormatterStrategy import TableDSCCFormatterStrategy
from strategy.ExcelExportStrategy import ExcelExportStrategy
from strategy.CheckerDSCCStrategy import CheckerDSCCStrategy

from service.Opener import Opener
from service.Reader import Reader
from service.Checker import Checker
from service.Splitter import Splitter
from service.Formatter import Formatter
from service.Export import Export
from service.NameGenerator import NameGenerator


file_path = "./files/DSCCFile.pdf"
export_path = "./export/DSCCresult.xlsx"
sheet_name = "DSCC"
split_keyword = "Document:"
page = 1

# Inicializar las strategias
opener = Opener(PDFOpenerStrategy)
reader = Reader(PDFTextReaderStrategy)
splitter = Splitter(ParagraphKeywordSplitterStrategy)
json_checker = Checker(JsonCheckerStrategy)
checker = Checker(CheckerDSCCStrategy)
formatter = Formatter(DSCCFormatter)
table_formatter = Formatter(TableDSCCFormatterStrategy)
exporter = Export(ExcelExportStrategy)
name_generator = NameGenerator

def run():
    open_file = opener.open_file(file_path)
    content = reader.read_file(open_file, page)
    paragraphs = splitter.split_content(content, split_keyword)
    sheet_name = name_generator.generate(file_path)

    if json_checker.check(paragraphs):
        formated = formatter.format(paragraphs)
        if  checker.check(formated):    
            table = table_formatter.format(formated)

            if exporter.export(table, export_path, sheet_name):
                print("Se ha exportado la tabla correctamente")
            else:
                print("No se ha podido guardar el fichero")
        else:
            print("Se ha ocurrido un erro en la hora de formatear el contenido")
    else: 
        print("El formato del contenido no es Json!")


