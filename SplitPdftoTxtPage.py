from PyPDF2 import PdfFileReader, PdfFileWriter
import os
import csv
import textract


def extractSignature():
    MainPath = "D:\DemoPDFs\\"
    SavePath = "D:\Demo\\"
    count = 0
    for root, dir, files in os.walk(MainPath):
        # Fetching a single file\
        for singFile in files:
            # Getting only pdf files
            if ".pdf" in singFile:
                newPath = os.path.join(root, singFile)
                newPath1=newPath.replace(".pdf","")
                Path=newPath1.replace(MainPath,SavePath)+"SplitPages"
                try:
                    pdfReader = PdfFileReader(newPath, strict=False)
                    os.makedirs(Path)
                    pages = pdfReader.getNumPages()
                    for i in range(0, pages):
                        output = PdfFileWriter()
                        pageObj = pdfReader.getPage(i)
                        text = pageObj.extractText()
                        TxtFile = Path+"\\"+singFile.replace(".pdf", "_" + str(i)) + ".txt"
                        PDFFile = Path+"\\"+singFile.replace(".pdf", "_" + str(i)) + ".pdf"
                        PDFFileOpen = open(PDFFile, "wb")
                        output.addPage(pdfReader.getPage(i))
                        output.write(PDFFileOpen)
                        TxtFileOpen = open(TxtFile, "w+")
                        TxtFileOpen.write(text)

                except:
                    os.chdir(Path)
                    pdfReader = PdfFileReader(newPath, strict=False)
                    pages = pdfReader.getNumPages()
                    for i in range(0, pages):
                        output = PdfFileWriter()
                        pageObj = pdfReader.getPage(i)
                        text = pageObj.extractText()
                        TxtFile = Path + "\\" + singFile.replace(".pdf", "_" + str(i)) + ".txt"
                        PDFFile = Path + "\\" + singFile.replace(".pdf", "_" + str(i)) + ".pdf"
                        PDFFileOpen = open(PDFFile, "wb")
                        output.addPage(pdfReader.getPage(i))
                        output.write(PDFFileOpen)
                        TxtFileOpen = open(TxtFile, "w+",encoding="utf-8")
                        TxtFileOpen.write(text)
                # print( "File : " + newPath + " Processed")

def main():
    extractSignature()


if __name__ == '__main__':
    main()