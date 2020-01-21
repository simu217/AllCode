# from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
# from pdfminer.converter import TextConverter
# from pdfminer.layout import LAParams
# from pdfminer.pdfpage import PDFPage
# from io import StringIO
import PyPDF2
import os
import csv

def convert_pdf_to_txt(path,singFile,count):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = open(path, 'rb')

    interpreter = PDFPageInterpreter(rsrcmgr, device)
    # print(interpreter)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()

    # try to open your pdf here - do not raise the error yourself!
    # if it happens, catch and handle it as well
    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password, caching=caching,
                                  check_extractable=True):
        interpreter.process_page(page)
        print(interpreter.process_page(page))

    text = retstr.getvalue()
    files = "D:/test/" + singFile.replace(".pdf", ".txt")
    print(files)
    ReadingCSV = open(files, 'w+', encoding="utf-8",
                      errors="ignore", newline="")
    WritingCSV = csv.writer(ReadingCSV, quoting=csv.QUOTE_ALL, delimiter=',')
    WritingCSV.writerow([text])
    print(count + 1, "files processed")
    fp.close()
    device.close()
    retstr.close()
    return

def PyPdf2(path,singFile,count,root):
    # creating a pdf file object
    print(path)
    pdfFileObj = open(path, 'rb')
    # creating a pdf reader object
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    # creating a page object
    fullstring,fullList="",[]
    for i in range(0,pdfReader.numPages):
        pageObj = pdfReader.getPage(i)
        halfstring = pageObj.extractText()
        fullList.append(halfstring)
    text=fullstring.join(fullList)
    root1 = root.replace("D:\PDFS", "D:\PDFS")
    try:
        os.makedirs(root1)
    except:
        os.chdir(root1)

    file1 = singFile.replace(".pdf", ".txt")
    completeName = os.path.join(root1, file1 )
    ReadingCSV = open(completeName, 'w+', encoding="utf-8",errors="ignore", newline="")
    WritingCSV = csv.writer(ReadingCSV, quoting=csv.QUOTE_ALL, delimiter=',')
    WritingCSV.writerow([text])
    print(count , completeName ,"files processed")
    # closing the pdf file object
    pdfFileObj.close()
    return

def Converter():
    ReadingCSV = open("D:/RemainingFiles.csv", 'w+', encoding="utf8", errors="ignore", newline="")
    WritingCSV = csv.writer(ReadingCSV, quoting=csv.QUOTE_ALL, delimiter=',')
    WritingCSV.writerow(['Path & File Name'])
    count=0
    for root, dir, files in os.walk("D:\PDFS\\"):
            for singFile in files:
                if ".pdf"  in singFile :
                    count = count + 1
                    newPath = (root +"\\" +singFile)
                    try:
                        PyPdf2(newPath,singFile,count,root)
                    except:
                        WritingCSV.writerow([newPath])

Converter()