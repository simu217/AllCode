from PyPDF2 import PdfFileReader,PdfFileWriter
import os
import csv
import textract

def extractSignature():
    MainPath="D:\Demo\\"
    PDffile=open('D:\PDFS/PDFRemaining.csv', 'w+', encoding="utf8",errors="ignore",newline="")
    WritingCSV = csv.writer(PDffile, quoting=csv.QUOTE_ALL, delimiter=',')
    searchList = ['Agreed and AccePted:', 'Title','IN WITNESS WHEREOF','Agreed and accepted:']
    count=0
    for root, dir, files in os.walk(MainPath):
        # Fetching a single file\
        for singFile in files:
            # Getting only text files
            if ".pdf" in singFile:
                directory=""
                newPath = os.path.join(root, singFile)
                count = count + 1
                count1 = str(count)
                pdfReader = PdfFileReader(newPath, strict=False)
                output=PdfFileWriter()
                try:
                    pages=pdfReader.getNumPages()
                    print(pages)
                    for i in range(0,pages):
                        pageObj = pdfReader.getPage(i)
                        text = pageObj.extractText().encode('utf-8')
                        TxtFile=newPath.replace(".pdf","_"+str(i))+".txt"
                        TxtFileOpen=open(TxtFile,"w+")
                        str2=text.decode('utf-8')
                        str1 = str2.split('\n')
                        stringtext = ''.join(str(e) for e in str1)
                        print(stringtext)
                        for element in searchList:
                            if stringtext.find(element)>=0:
                                output.addPage(pageObj)
                                directory="D:\PDFS_Signature\\"
                                try:
                                    os.makedirs(directory)
                                    out_f= open(directory+singFile, "wb")
                                    output.write(out_f)
                                except:
                                    os.chdir(directory)
                                    out_f = open(directory+singFile, "wb")
                                    output.write(out_f)
                            else:
                                WritingCSV.writerow([newPath])
                                pass
                    print("File: ",count1 , newPath)
                except:
                    WritingCSV.writerow([newPath])

def main():
    extractSignature()

if __name__ == '__main__':
    main()