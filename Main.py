from strategy.PDFOpenerStrategy import PDFOpenerStrategy
from strategy.PDFTableReaderStrategy import PDFTableReaderStrategy
from strategy.ParagraphRegexSplitterStrategy import ParagraphRegexSplitterStrategy
from strategy.ParagraphKeywordSplitterStrategy import ParagraphKeywordSplitterStrategy
from strategy.ESCCFormatter import ESCCFormatter
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
title_re = re.compile(r'[A-Z][a-zA-Z -]+(?=:$)')
extra_re = re.compile(r'(Extension|Revision): [a-zA-Z. ]+')
page = 3

# Inicializar las strategias
opener = Opener(PDFOpenerStrategy)
reader = Reader(PDFTableReaderStrategy)
splitter = Splitter(ParagraphRegexSplitterStrategy)
json_checker = Checker(JsonCheckerStrategy)
ESCCchecker = Checker(CheckerESCCStrategy)
formatter = Formatter(ESCCFormatter)


def runESCC():

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


if __name__ == "__main__":
    runESCC()