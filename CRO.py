
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

    f = open('D:\MainData\csv files\seagencsv\Seagen new files/Seagen_CRO.csv', 'w+',encoding="utf8",errors="ignore", newline="")
    w = csv.writer(f, quoting=csv.QUOTE_ALL, delimiter=',')
    w.writerow(['Path&File Name', 'CRO String','CRO'])

    count = 0

    # Walking through the directories

    f1 = open("D:\MainData\csv files\SeaGen_Listing/Seagen_List2.csv", "r+", encoding="utf8",errors="ignore")
    reader = csv.reader(f1)
    for row in reader:
            file1 = open(row[0], 'r+', encoding="utf8",errors="ignore")
            content = file1.read()
            text = content
            str1 = text.lower()
            count1=count+1
            if '"cro"' in str1:
                ind = str1.index('"cro"')
                if ind < 500:
                    croString = str1[:ind + 4]
                else:
                    croString = str1[ind-500:ind+4]
                if ('"pra"' in croString) or (' pra ' in croString) or ("pharmaceutical research associat" in croString):
                    cro = "PRA"

                elif "parexel" in croString:
                    cro = "Parexel"

                elif "psi" in croString:
                    cro = "PSI"

                elif "quintiles" in croString:
                    cro = "Quintiles"

                elif "novella" in croString:
                    cro = "Novella"

                elif "precision oncology" in croString:
                    cro = "Precision Oncology"

                elif "covance clinical" in croString:
                    cro = "Covance Clinical"

                else:
                    cro = "N/A"

            else:
                croString = "No Match"
                cro = "No Match"

            # Writing changes to the csv
            w.writerow([row[0], croString, cro])

            file1.close()

            print("Scanned :" ,count1, " Files" + "\tFile Name: " + row[0])

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

