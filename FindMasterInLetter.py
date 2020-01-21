
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

    f = open('D:/Results/Seagen/05_March_2019/Seagen_Master.csv', 'w+')
    w = csv.writer(f, quoting=csv.QUOTE_ALL, delimiter=',')
    w.writerow(['Path', 'File Name', 'Master', "Clinical Trial", "Confidentiality", "Collaboration",
                "Agreement", "Re:", "Regarding:", "Persuant to Master"])

    f1 = open("D:\Data\Error Files CSV\Seagen\FindMaster.csv")
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

            if ' re:' in lowredContent[:1000]:
                ind = lowredContent.index("re:")
                re = content[ind:ind+200]
                reg = "No"

            elif 'regarding:' in lowredContent[:1000]:
                ind = lowredContent.index("regarding:")
                reg = content[ind:ind+200]
                re = "No"

            else:
                re = "No"
                reg = "No"

            if ('clinical trial agreement' in lowredContent) or ('clinical trial' in lowredContent):
                cta = "Yes"
                conf = "No"
                col = "No"
                agree = "No"
                ptm = "No"
                msa = "No"

            elif 'confidentiality' in lowredContent:
                conf = "Yes"
                col = "No"
                agree = "No"
                ptm = "No"
                msa = "No"
                cta = "No"

            elif 'collaboration' in lowredContent:
                col = "Yes"
                msa = "No"
                cta = "No"
                conf = "No"
                agree = "No"
                ptm = "No"

            elif 'persuant to master' in lowredContent:
                ptm = "Yes"
                msa = "No"
                cta = "No"
                conf = "No"
                col = "No"
                agree = "No"

            elif 'master services agreement' in lowredContent:
                msa = "Yes"
                cta = "No"
                conf = "No"
                col = "No"
                agree = "No"
                ptm = "No"

            elif 'master service agreement' in lowredContent:
                msa = "Yes"
                cta = "No"
                conf = "No"
                col = "No"
                agree = "No"
                ptm = "No"

            elif 'Agreement' in content:
                agree = "Yes"
                ptm = "No"
                msa = "No"
                cta = "No"
                conf = "No"
                col = "No"

            else:
                msa = "No"
                cta = "No"
                conf = "No"
                col = "No"
                agree = "No"
                ptm = "No"

            # Writing changes to the csv
            w.writerow([newpdfPath, newFile, msa, cta, conf, col, agree, re, reg, ptm])

            file1.close()

            print("Scanned :" + count1 + " Files" + "\tFile Name: " + singFile)


# ===========================================================================================#

def main():
    ORFile()


if __name__ == '__main__':

    main()
