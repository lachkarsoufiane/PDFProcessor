import pdfplumber
from interface.IOpenerStrategy import IOpenerStrategy

class PDFOpenerStrategy(IOpenerStrategy):
    def open_file(file_path):
        file = pdfplumber.open(file_path)
        return file