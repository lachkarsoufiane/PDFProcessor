from strategy.PDFOpenerStrategy import PDFOpenerStrategy
from strategy.PDFReaderStrategy import PDFReaderStrategy
from strategy.ParagraphSplitterStrategy import ParagraphSplitterStrategy
from service.Checker import Checker
from strategy.CheckerESCCStrategy import CheckerESCCStrategy
import json
import re


file_path = "./files/esccrpqpl005iss235.pdf"
title_re = re.compile(r'[A-Z][a-zA-Z -]+(?=:$)')
extra_re = re.compile(r'(Extension|Revision): [a-zA-Z. ]+')


open_file = PDFOpenerStrategy.open_file(file_path)
content = PDFReaderStrategy.read_file(open_file, 3)
paragraphs = ParagraphSplitterStrategy.split_content(content, title_re, extra_re)

checker = Checker(CheckerESCCStrategy)


if checker.check(paragraphs):
    print("ok")
else:
    print("bad")

# p_dict = json.loads(paragraphs)
# for p in p_dict:
#     print(p)
