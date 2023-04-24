from strategy.PDFOpenerStrategy import PDFOpenerStrategy
from strategy.PDFReaderStrategy import PDFReaderStrategy
from strategy.ParagraphRegexSplitterStrategy import ParagraphRegexSplitterStrategy
from strategy.ParagraphKeywordSplitterStrategy import ParagraphKeywordSplitterStrategy
from service.Checker import Checker
from service.Opener import Opener
from service.Reader import Reader
from service.Splitter import Splitter
from strategy.CheckerESCCStrategy import CheckerESCCStrategy
import json
import re

file_path = "./files/esccrpqpl005iss235.pdf"
title_re = re.compile(r'[A-Z][a-zA-Z -]+(?=:$)')
extra_re = re.compile(r'(Extension|Revision): [a-zA-Z. ]+')
page = 3

# Inicializar las strategias
opener = Opener(PDFOpenerStrategy)
reader = Reader(PDFReaderStrategy)
splitter = Splitter(ParagraphRegexSplitterStrategy)
checker = Checker(CheckerESCCStrategy)


def runESCC():

    # Abrir el fichero
    open_file = opener.open_file(file_path)

    # Leer el contenido
    content = reader.read_file(open_file, page)

    paragraphs = splitter.split_content(content, title_re, extra_re)

    # Checkear el resultado 

    if checker.check(paragraphs):
        print("ok")
    else:
        print("bad")

    # p_dict = json.loads(paragraphs)
    # for p in p_dict:
    #     print(p)


if __name__ == "__main__":
    runESCC()