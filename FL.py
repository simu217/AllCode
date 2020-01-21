from polyglot.detect import Detector
from langdetect import detect
import os
import sys
import csv
import time

def strip_non_ascii(string):
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)

def ORFilePolyglot():
    # Opening the csv file so that we can append the changes to it.
    f = open('D:\MainData\csv files\FLIR 11.1\FLIR Phase 8 TXT/FLIR_P8_FL.csv', 'w+', encoding="utf8",errors="ignore",newline="")
    w = csv.writer(f, quoting=csv.QUOTE_ALL, delimiter=',')
    w.writerow(['Path', 'File Name', 'Ployglot', 'Langdetect'])
    count = 0
    # Walking through the directories
    for root, dir, files in os.walk("D:\MainData\FLIR Phase 8 TXT"):

        # Fetching a single file

        for singFile in files:

            # Getting only text files

            if ".txt" in singFile:
                newPath = os.path.join(root, singFile)

                count = count + 1
                count1 = str(count)

                # For getting common share path
                newRoot = root.replace("D:\MainData\Phase2AsOfDec172019-4648_txt", "\\192.168.1.2\Google Data\Phase2AsOfDec172019 (4648)")
                # newFile = singFile.replace("txt", "pdf")

                pdfPath = newRoot + "/" + singFile

                if "/" in pdfPath:
                    newpdfPath = pdfPath.replace("/", "\\")

                else:
                    newpdfPath = pdfPath

                # Opening single file for editing and detecting language

                file1 = open(newPath, 'r+', encoding="utf8",errors="ignore",newline="")


                str1 = file1.read()
                text = str1.split()
                str2 = ' '.join(str(e) for e in text)
                content = strip_non_ascii(str2)
                try:
                    Ployglot = Detector(u""+content)

                    lang = Ployglot.language

                    language = lang.name
                    Langdetect = detect(content)

                except Exception:
                    language = "No Match"
                    Langdetect="No Match"

                # Writing changes to the csv
                w.writerow([newpdfPath, singFile, language, Langdetect])

                file1.close()

                print("Scanned :" + count1 + " Files" + "\tFile Name: " + singFile)

# ===========================================================================================#

def main():

    ORFilePolyglot()


if __name__ == '__main__':

    main()
