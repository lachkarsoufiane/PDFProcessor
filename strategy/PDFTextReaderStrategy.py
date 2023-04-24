from interface.IReaderStrategy import IReaderStrategy

class PDFTextReaderStrategy(IReaderStrategy):
    def read_file(file, page) -> str:
        content = file.pages[page -1].extract_text()
        return content
