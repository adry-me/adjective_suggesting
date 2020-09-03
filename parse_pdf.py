from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.layout import LAParams
from pdfminer.converter import TextConverter
from pdfminer.pdfpage import PDFPage
from io import StringIO


def extract(filename, exclude=()):
    with open(f'{filename}.txt', 'rb') as f:
        parser = PDFParser(f)
        document = PDFDocument(parser)
        res_mgr = PDFResourceManager()
        output = StringIO()
        params = LAParams()

        converter = TextConverter(res_mgr, output, laparams=params)
        interpreter = PDFPageInterpreter(res_mgr, converter)

        i = 0
        for i, page in enumerate(PDFPage.create_pages(document)):
            if i not in exclude:
                interpreter.process_page(page)

        lines = list(output.getvalue().splitlines())

    with open(f'{filename}.txt', 'w') as f:
        for line in lines:
            f.write(f'{line}\n')
    return lines


if __name__ == '__main__':
    #0, 243~248
    exclude = [0]
    exclude.extend(range(243, 249))
    contents = extract('M_P', exclude=exclude)
    for line in contents:
        print(line)