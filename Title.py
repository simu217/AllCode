
#---------------------------------------------------#
# AUTHOR: Lakshay Saini                             #
# CODE:   TitlePartners                             #
# WORK:   We are extracting titles from GOOGLE Docs #
#---------------------------------------------------#

import os
import sys
import csv
import re
import time


def ORFile():
    # Opening the csv file so that we can append the changes to it.

    f = open('D:\MainData\csv files\googlecsv/Google_Title_20K.csv', 'w+')
    w = csv.writer(f, quoting=csv.QUOTE_ALL, delimiter=',')
    w.writerow(['Path', 'File Name', 'Title'])

    count = 0

    # Walking through the directories

    for root, dir, files in os.walk("D:\Brightstar"):

        # Fetching a single file

        for singFile in files:

            # Getting only text files

            if ".txt" in singFile:
                newPath = os.path.join(root, singFile)

            count = count + 1
            count1 = str(count)

            # For getting common share path
            newRoot = root.replace("D:/Data/Google/130000", "//192.168.1.2/Google Data/Phase 2 - More Than 5 Pages - 132024")
            newFile = singFile.replace("txt", "pdf")

            pdfPath = newRoot + "/" + newFile

            if "/" in pdfPath:
                newpdfPath = pdfPath.replace("/", "\\")

            else:
                newpdfPath = pdfPath

            # Opening single file for editing and detecting language

            file1 = open(newPath, 'r+')

            content = file1.read()

            # Extracting Parties from txt files (300 words)

            loweredContent = content.lower()

            str2 = content[:500]

            # Getting expiration title

            titleObj = re.search(r'((.*)this)((.*?).{60})', str2, re.I | re.M)

            titleObj1 = re.search(r'((.*)addendum)((.*?).{60})', str2, re.I | re.M)

            titleObj2 = re.search(r'((.*)amendment)((.*?).{60})', str2, re.I | re.M)

            titleObj3 = re.search(r'((.*)summary)((.*?).{60})', str2, re.I | re.M)

            titleObj4 = re.search(r'((.*)dear)((.*?).{60})', str2, re.I | re.M)

            titleObj5 = re.search(r'(.*)re:((.*?).{60})', str2, re.I | re.M)

            titleObj6 = re.search(r'((.*)form(.*?).{60})', str2, re.I | re.M)

            titleObj7 = re.search(r'((.*)order(.*?).{60})', str2, re.I | re.M)

            titleObj8 = re.search(r'((.*)exhibit(.*?).{60})', str2, re.I | re.M)

            titleObj9 = re.search(r'((.*)agreement)((.*?).{60})', str2, re.I | re.M)

            titleObj10 = re.search(r'((.*)statement of work)((.*?).{60})', str2, re.I | re.M)

            titleObj11 = re.search(r'((.*)contract)((.*?).{60})', str2, re.I | re.M)

            if titleObj:
                title = titleObj.group()

            elif titleObj1:
                title = titleObj1.group()

            elif titleObj2:
                title = titleObj2.group()

            elif titleObj3:
                title = titleObj3.group()

            elif titleObj4:
                title = titleObj4.group()

            elif titleObj5:
                title = titleObj5.group()

            elif titleObj6:
                title = titleObj6.group()

            elif titleObj7:
                title = titleObj7.group()

            elif titleObj8:
                title = titleObj8.group()

            elif titleObj9:
                title = titleObj9.group()

            elif titleObj10:
                title = titleObj10.group()

            elif titleObj11:
                title = titleObj11.group()

            else:
                title = "No Match"

            # Writing changes to the csv
            w.writerow([newpdfPath, newFile, title])

            file1.close()

            print("Scanned :" + count1 + " Files" + "\tFile Name: " + singFile)


# ===========================================================================================#

def main():
    ORFile()


if __name__ == '__main__':
    # Set encoding so that complier can detect language

    reload(sys)
    sys.setdefaultencoding('utf-8')

    '''
        CALCULATE THE EXECUTION TIME OF THE PROGRAM
        '''

    start_time = time.time()

    main()

    end_time = time.time() - start_time
    hours, rem = divmod(end_time - start_time, 3600)
    minutes, seconds = divmod(rem, 60)
    print ("-------------TIME TAKEN-----------------")
    print("{:0>2}:{:0>2}:{:05.2f}".format(int(hours), int(minutes), seconds))
