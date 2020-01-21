
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

def check(ele, ele1, str1):

    if ele1 != "":
        ind = str1.index(ele1)
        String = str1[ind - 100:ind + 100]
        lowredString = String.lower()

        if ("program" in lowredString) or ("project" in lowredString) or ("product" in lowredString):
            date = "Other"

        else:
            date = "N/A"
    else:
        ind = str1.index(ele)
        String = str1[ind - 100:ind + 100]
        lowredString = String.lower()

        if ("program" in lowredString) or ("project" in lowredString) or ("product" in lowredString):
            date = ele

        else:
            date = "N/A"

    return date, String

def conditions(str1):

    dateObj = re.search(r'(SGN|SEA|TGIT|ASG)-[0-9A-Z]+', str1, re.I | re.M)

    dateObj1 = re.search(r'((SGN|SEA|TGIT|ASG)-[0-9A-Z]+-[0-9A-Z]+)', str1, re.I | re.M)

    dateObj2 = re.search(r'((SGN|SEA|TGIT|ASG)(|\s)\((SGN|SEA|TGIT|ASG)-[0-9A-Z]+\))', str1, re.I | re.M)

    lis = ["ASG-2FF", "2FF", "Adcetris", "ASG-15ME", "ASG-22", "ASG5", "SGN30", "SGN33",
           "SGN-35", "SGN40", "SGN70", "SGN75", "SGN-CD19B", "SGN-CD33A", "SGN-CD352A", "SGN-CD40",
           "SGN-CD48A", "SGN-CD70A", "SGN-LIV1A", "SGN-TV", "SGN-CD47M", "SGNBCMA", "Tucatinib", "TIGIT",
           "SGN-CD123A", "SGN-CD19A", "TIGIT (CASC-674)"]

    for ele in lis:

        if ele in str1:
            date1 = check(ele=ele, ele1="", str1=str1)
            date = date1[0]
            String = date1[1]
            break

        elif dateObj:
            ele = dateObj.group()
            date1 = check(ele="", ele1=ele, str1=str1)
            date = date1[0]
            String = date1[1]
            break

        elif dateObj1:
            ele = dateObj1.group()
            date1 = check(ele="", ele1=ele, str1=str1)
            date = date1[0]
            String = date1[1]
            break

        elif dateObj2:
            ele = dateObj2.group()
            date1 = check(ele="", ele1=ele, str1=str1)
            date = date1[0]
            String = date1[1]
            break

        else:
            date1 = ["No match", "No match"]
            date = date1[0]
            String = date1[1]

    return date, String

def ORFile():
    # Opening the csv file so that we can append the changes to it.

    f = open('D:\MainData\csv files\seagencsv\Seagen new files\Seagen_Program.csv', 'w+',encoding="utf8",errors="ignore", newline="")
    w = csv.writer(f, quoting=csv.QUOTE_ALL, delimiter=',')
    w.writerow(['Path & File Name', 'Program', 'String'])

    count = 0

    # Walking through the directories

    f1 = open("D:\MainData\csv files\SeaGen_Listing/Seagen_List2.csv", "r+")
    reader = csv.reader(f1)

    for row in reader:
            count = count + 1
            count1 = str(count)

            file1 = open(row[0], 'r+',encoding="utf8",errors="ignore")

            content = file1.read()

            text = content.lower()
            str1 = content

            if "product name:" in content.lower():
                ind = text.index("product name:")
                String = content[ind-10:ind+100]
                date1 = conditions(String)
                date = date1[0]
                StringL = date1[1]

            elif "product:" in content.lower():
                ind = text.index("product:")
                String = content[ind - 10:ind + 100]
                date1 = conditions(String)
                date = date1[0]
                StringL = date1[1]

            else:
                date1 = conditions(str1)
                date = date1[0]
                StringL = date1[1]

            # Writing changes to the csv
            w.writerow([row[0], date, StringL])

            file1.close()

            print("Scanned :" + count1 + " Files" + "\tFile Name: " + row[0])


# ===========================================================================================#

def main():
    ORFile()


if __name__ == '__main__':
    # Set encoding so that complier can detect language

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

