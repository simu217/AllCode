
#---------------------------------------------------#
# AUTHOR: Lakshay Saini                             #
# CODE:   TitleAclaris                              #
# WORK:   We are extracting titles from GOOGLE Docs #
#---------------------------------------------------#

import os
import sys
import csv
import re
import time
import subprocess

def ORFile():
    # Opening the csv file so that we can append the changes to it.

    f = open('D:/Results/Seagen/05_March_2019/Seagen_Master_Service(s).csv', 'w+')
    w = csv.writer(f, quoting=csv.QUOTE_ALL, delimiter=',')
    w.writerow(['Path', 'File Name', 'Master', "Key"])

    f1 = open("D:\Data\Error Files CSV\Seagen\FindMaster1.csv")
    reader = csv.DictReader(f1)

    count = 0

    # Walking through the directories

    for row in reader:

            newPath = row["Path"] + "/" + row["File Name"]

            root = row["Path"]
            singFile = row["File Name"]

            count = count + 1
            count1 = str(count)

            newRoot = root.replace("D:/Data/SeaGen/TXT", "//192.168.1.2/Seagen")
            newFile = singFile.replace("txt", "pdf")

            pdfPath = newRoot + "/" + newFile

            if "/" in pdfPath:
                newpdfPath = pdfPath.replace("/", "\\")

            else:
                newpdfPath = pdfPath

            # Opening single file for editing and detecting language

            file1 = open(newPath, 'r+')

            content = file1.read()

            lowredContent = content.lower()

            if "this legal contract" in lowredContent:
                ind = lowredContent.index("this legal contract")
                newContent = content[ind+80:]
                newLowredContent = newContent.lower()
                if "this legal contract" in newLowredContent:
                    ind = newLowredContent.index("this legal contract")
                    newContent1 = newContent[ind + 80:]
                    newLowredContent1 = newContent1.lower()

                    if "if contract is already approved or signed" in newLowredContent1:
                        ind = newLowredContent1.index("if contract is already approved or signed")
                        newContent2 = newContent1[ind + 100:]
                        str1 = newContent2[:1000]

                    else:
                        str1 = newContent1[:1000]

                elif "if contract is already approved or signed" in newLowredContent:
                    ind = newLowredContent.index("if contract is already approved or signed")
                    newContent1 = newContent[ind + 100:]
                    newLowredContent1 = newContent1.lower()

                    if "if contract is already approved or signed" in newLowredContent1:
                        ind = newLowredContent.index("if contract is already approved or signed")
                        newContent2 = newContent1[ind + 100:]
                        newLowredContent2 = newContent1.lower()

                        if "this legal contract" in newLowredContent2:
                            ind = newLowredContent2.index("this legal contract")
                            newContent3 = newContent2[ind + 100:]
                            str1 = newContent3[:1000]

                        else:
                            str1 = newContent1[:1000]
                    else:
                        str1 = newContent1[:1000]

                else:
                    str1 = newContent[:1000]

            elif "if contract is already approved or signed" in lowredContent:
                ind = lowredContent.index("if contract is already approved or signed")
                newContent = content[ind+80:]
                newLowredContent = newContent.lower()
                if "if contract is already approved or signed" in newLowredContent:
                    ind = newLowredContent.index("this legal contract")
                    newContent1 = newContent[ind + 80:]
                    newLowredContent1 = newContent1.lower()

                    if "this legal contract" in newLowredContent1:
                        ind = newLowredContent1.index("if contract is already approved or signed")
                        newContent2 = newContent1[ind + 100:]
                        str1 = newContent2[:1000]

                    else:
                        str1 = newContent1[:1000]

                elif "this legal contract" in newLowredContent:
                    ind = newLowredContent.index("this legal contract")
                    newContent1 = newContent[ind + 100:]
                    newLowredContent1 = newContent1.lower()

                    if "this legal contract" in newLowredContent1:
                        ind = newLowredContent.index("this legal contract")
                        newContent2 = newContent1[ind + 100:]
                        newLowredContent2 = newContent1.lower()

                        if "if contract is already approved or signed" in newLowredContent2:
                            ind = newLowredContent2.index("this legal contract")
                            newContent3 = newContent2[ind + 100:]
                            str1 = newContent3[:1000]

                        else:
                            str1 = newContent1[:1000]
                    else:
                        str1 = newContent1[:1000]

                else:
                    str1 = newContent[:1000]

            # elif "if contract is already approved or signed" in lowredContent:
            #     ind = lowredContent.index("if contract is already approved or signed")
            #     newContent = content[ind+100:]
            #     newLowredContent = newContent.lower()
            #
            #     if "this legal contract" in newLowredContent:
            #         ind = newLowredContent.index("this legal contract")
            #         newContent1 = newContent[ind + 80:]
            #         str1 = newContent1[:1000]
            #
            #     elif "if contract is already approved or signed" in newLowredContent:
            #         ind = newLowredContent.index("if contract is already approved or signed")
            #         newContent1 = newContent[ind + 100:]
            #         str1 = newContent1[:1000]
            #
            #     else:
            #         str1 = newContent[:1000]

            else:
                print("else")
                str1 = content[:1000]

            lowredString = str1.lower()

            # if 'the("agreement")' in lowredString:
            #     key = "Yes"
            #
            # elif 'persuant to master' in lowredString:
            #     key = "Yes"
            #
            # elif 'master service(s) agreement' in lowredString:
            #     key = "Yes"
            #
            # elif 'master service agreement' in lowredString:
            #     key = "Yes"
            #
            # elif 'agreement' in lowredString:
            #     key = "Yes"
            #
            # else:
            #     key = "No"

            # if 'the("agreement")' in lowredContent:
            #     date = "Yes"
            #
            if 'persuant to master' in lowredContent:
                 date = "Yes"

            elif 'master service agreement' in lowredContent:
                date = "Yes"
            #
            elif 'master services agreement' in lowredContent:
                 date = "Yes"
            #
            # elif 'agreement' in lowredContent:
            #     date = "Yes"

            else:
                date = "No"

            # Writing changes to the csv
            w.writerow([newpdfPath, newFile, date])

            file1.close()

            print("Scanned :" + count1 + " Files" + "\tFile Name: " + singFile)


# ===========================================================================================#

def main():
    ORFile()


if __name__ == '__main__':
    # Set encoding so that complier can detect language
    main()

