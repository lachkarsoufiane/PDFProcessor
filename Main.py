from strategy.PDFOpenerStrategy import PDFOpenerStrategy
from strategy.PDFTableReaderStrategy import PDFTableReaderStrategy
from strategy.PDFTextReaderStrategy import PDFTextReaderStrategy
from strategy.ParagraphRegexSplitterStrategy import ParagraphRegexSplitterStrategy
from strategy.ParagraphKeywordSplitterStrategy import ParagraphKeywordSplitterStrategy
from strategy.ESCCFormatter import ESCCFormatter
from strategy.DSCCFormatter import DSCCFormatter
from strategy.JsonCheckerStrategy import JsonCheckerStrategy
from service.Checker import Checker
from service.Opener import Opener
from service.Reader import Reader
from service.Splitter import Splitter
from service.Formatter import Formatter
from strategy.CheckerESCCStrategy import CheckerESCCStrategy
import json
import re

file_path = "./files/esccrpqpl005iss235.pdf"
file_path_2 = "./files/DSCCFile.pdf"
title_re = re.compile(r'[A-Z][a-zA-Z -]+(?=:$)')
extra_re = re.compile(r'(Extension|Revision): [a-zA-Z. ]+')
page = 3




def runESCC():

    # Inicializar las strategias
    opener = Opener(PDFOpenerStrategy)
    reader = Reader(PDFTableReaderStrategy)
    splitter = Splitter(ParagraphRegexSplitterStrategy)
    json_checker = Checker(JsonCheckerStrategy)
    ESCCchecker = Checker(CheckerESCCStrategy)
    formatter = Formatter(ESCCFormatter)
    
    
    # Abrir el fichero
    open_file = opener.open_file(file_path)

    # Leer el contenido
    content = reader.read_file(open_file, page)

    paragraphs = splitter.split_content(content, title_re, extra_re)


    # Formatear los parrafos si estan en el formato requerido 

    if ESCCchecker.check(paragraphs) and json_checker.check(paragraphs):
        print(formatter.format(paragraphs))
    else:
        print("bad")

    # p_dict = json.loads(paragraphs)
    # for p in p_dict:
    #     print(p)

def runDSCC():
    opener = Opener(PDFOpenerStrategy)
    reader = Reader(PDFTextReaderStrategy)
    splitter = Splitter(ParagraphKeywordSplitterStrategy)
    json_checker = Checker(JsonCheckerStrategy)
    formatter = Formatter(DSCCFormatter)



    open_file = opener.open_file(file_path_2)
    content = reader.read_file(open_file, 1)
    paragraphs = splitter.split_content(content, "Document:")

    if json_checker.check(paragraphs):
        print("kjdf")
    else:
        print("Something went wrong!")

if __name__ == "__main__":
    runDSCC()