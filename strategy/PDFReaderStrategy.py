from interface.IReaderStrategy import IReaderStrategy

class PDFReaderStrategy(IReaderStrategy):
    def read_file(file, page) -> str:
        content = file.pages[page -1].extract_table()[1][1]
        return content
