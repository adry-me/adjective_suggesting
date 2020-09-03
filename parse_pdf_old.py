import PyPDF2


def extract(filename):
    lines = []

    with open(f'{filename}.txt', 'rb') as f:
        reader = PyPDF2.PdfFileReader(f)
        reader.getPageMode()
        reader.getDocumentInfo()

        for page_num in range(reader.numPages):
            page = reader.getPage(page_num)
            page_text = page.extractText()
            for line in page_text.split('\n'):
              lines.append(line)
    #TODO: use code below to put all the text into lines
    #[line2, line3, line4]

    return lines


if __name__ == '__main__':
    result = extract('M_P')

    for line in result:
        print(line)

