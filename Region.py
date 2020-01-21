
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

def CRO(cntry):
    croString=cntry

    if 'cro' in croString:
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
        cro = "No Match"

    return cro


def ORFile():
    # Opening the csv file so that we can append the changes to it.
    f = open('D:\MainData\csv files\seagencsv\Seagen new files/Seagen_Region.csv', 'w+',encoding="utf8",errors="ignore", newline="")
    w = csv.writer(f, quoting=csv.QUOTE_ALL, delimiter=',')
    w.writerow(['Path&File Name', 'Country', 'CRO'])

    count = 0

    countryList = []

    # Walking through the directories

    f1 = open("D:\MainData\csv files\SeaGen_Listing/Seagen_List2.csv", "r+",encoding="utf8",errors="ignore")
    reader = csv.reader(f1)

    # f2 = open("D:\MainData\csv files\SeaGen_Listing/countries of the world (1).csv", "r+",encoding="utf8",errors="ignore")
    # reader1 = csv.DictReader(f2)
    #
    # for row in reader1:
    #     countryList.append(str(row["Country"]))

    for row in reader:
            cntry=""
            f = open(row[0], "r+",encoding="utf8",errors="ignore")
            content = f.read()
            text = content.split()
            str1 = ' '.join(str(e) for e in text)
            lowredContent = str1.lower()
            count = count + 1
            count1 = str(count)

            if "cro at the following address" in lowredContent:
                ind = lowredContent.index("cro at the following address")
                cntry = content[ind:ind+200].lower()
                cro=CRO(cntry)

            elif "if to cro:" in lowredContent:
                ind = lowredContent.index("if to cro:")
                cntry = content[ind:ind+200].lower()
                cro = CRO(cntry)

            elif "wire transfer" in lowredContent:
                ind = lowredContent.index("wire transfer")
                cntry = content[ind:ind+200].lower()
                cro = CRO(cntry)

            elif "invoice to:" in lowredContent:
                ind = lowredContent.index("invoice to:")
                cntry = content[ind:ind+200].lower()
                cro = CRO(cntry)

            elif "addressed to the following:" in lowredContent:
                ind = lowredContent.index("addressed to the following:")
                cntry = content[ind:ind+200].lower()
                cro = CRO(cntry)

            elif "following address:" in lowredContent:
                ind = lowredContent.index("following address:")
                cntry = content[ind:ind+200].lower()
                cro = CRO(cntry)

            elif "cro mailing address" in lowredContent:
                ind = lowredContent.index("cro mailing address")
                cntry = content[ind:ind+200].lower()
                cro = CRO(cntry)

            elif "pra mailing address" in lowredContent:
                ind = lowredContent.index("pra mailing address")
                cntry = content[ind:ind+200].lower()
                cro = CRO(cntry)

            elif "payments via wire transfer shall be made to:" in lowredContent:
                ind = lowredContent.index("payments via wire transfer shall be made to:")
                cntry = content[ind:ind+200].lower()
                cro = CRO(cntry)

            elif "address/anschrift:" in lowredContent:
                ind = lowredContent.index("address/anschrift:")
                cntry = content[ind:ind+200].lower()
                cro = CRO(cntry)

            elif "invoices shall be sent to" in lowredContent:
                ind = lowredContent.index("invoices shall be sent to")
                cntry = content[ind:ind+200].lower()
                cro = CRO(cntry)

            elif "invoices should be sent for payment to:" in lowredContent:
                ind = lowredContent.index("invoices should be sent for payment to:")
                cntry = content[ind:ind+200].lower()
                cro = CRO(cntry)

            elif "in witness whereof" in lowredContent:
                ind = lowredContent.index("in witness whereof")
                string = content[ind:ind+500].lower()
                cro = CRO(cntry)

                if "address:" in string:
                    ind = string.index("address:")
                    cntry = content[ind:ind+200].lower()
                    cro = CRO(cntry)

                else:
                    cntry = "No Match"
                    cro="No Match"

            elif "the parties hereto have caused" in lowredContent:
                ind = lowredContent.index("the parties hereto have caused")
                string = content[ind:ind+500].lower()

                if "address:" in string:
                    ind = string.index("address:")
                    cntry = content[ind:ind+200].lower()
                    cro = CRO(cntry)

                else:
                    cntry = "No Match"
                    cro = "No Match"
            else:
                cntry ="No Match"
                cro = "No Match"


            # Writing changes to the csv
            w.writerow([row[0],cntry,cro ])

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

