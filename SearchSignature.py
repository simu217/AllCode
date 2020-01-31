from PyPDF2 import PdfFileReader,PdfFileWriter
import os
import csv
import textract
import shutil

def extractSignature():
    MainPath="D:\Signature_Search_Project\splitPages\\"
    SavePath="D:\Signature_Search_Project\DemoOutput\\"
    PathForCSV = 'D:\\SearchSignature.csv'
    ReadingCSV = open(PathForCSV, 'w+', encoding="utf8", errors="ignore", newline="")
    WritingCSV = csv.writer(ReadingCSV, quoting=csv.QUOTE_ALL, delimiter=',')
    WritingCSV.writerow(['Path & File Name', 'keyword'])
    count=1
    for root, dir, files in os.walk(MainPath):
        # Fetching a single file\
        for singFile in files:
            # Getting only text files
            if ".txt" in singFile:
                newPath = os.path.join(root, singFile)
                count = count + 1
                count1 = str(count)
                file1 = open(newPath, 'r+', encoding="utf8", errors="ignore")
                content = file1.read()
                text = content.split()
                str1 = ' '.join(str(e) for e in text).lower()
                keywords = ["with kind regards", "acknowledged", "agreed and confirmed", "signed:",
                       'agreed and accepted by grantee:', "provider and google hereby agree to this agreement",
                       "in witness whereof", "signed by the parties",
                       "agreed and accepted", 'accepted and agreed', "supplier:", 'accepted on', 'sincerely',
                       "kindly regards", "very truly yours",
                       "agreed by the parties on the dates stated below",
                       "agreed by the parties using echosign on the dates stated below", "title:","signature:","Signed on behalf of"]
                directory=SavePath+root.replace("D:\Signature_Search_Project\splitPages\\","")
                for i in keywords:
                    if str1.find(i) >= 0:
                        try:
                            os.makedirs(directory)
                            shutil.copy(newPath.replace(".txt",".pdf"), directory)
                        except:
                            os.chdir(directory)
                            shutil.copy(newPath.replace(".txt", ".pdf"), directory)
                        WritingCSV.writerow([newPath.replace(".txt", ".pdf"), i])
                        print(newPath.replace(".txt", ".pdf"), i)
                        break
                    else:
                        pass

def main():
    extractSignature()

if __name__ == '__main__':
    main()