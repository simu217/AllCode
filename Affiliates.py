
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

def conditions(str1):

    dateObj = re.search(r'(Yeah)', str1, re.I | re.M)

    dateObj1 = re.search(r'((SGN|SEA|TGIT|ASG)-[0-9A-Z]+-[0-9A-Z]+)', str1, re.I | re.M)

    dateObj2 = re.search(r'((SGN|SEA|TGIT|ASG)(|\s)\((SGN|SEA|TGIT|ASG)-[0-9A-Z]+\))', str1, re.I | re.M)

    if "ASG-2FF" in str1:
        date = "ASG-2FF"

    elif "2FF" in str1:
        date = "2FF"

    elif "Adcetris" in str1:
        date = "Adcetris"

    elif "ASG-15ME" in str1:
        date = "ASG-15ME"

    elif "ASG-22" in str1:
        date = "ASG-22"

    elif "ASG5" in str1:
        date = "ASG5"

    elif "SGN30" in str1:
        date = "SGN30"

    elif "SGN33" in str1:
        date = "SGN33"

    elif "SGN-35" in str1:
        date = "SGN-35"

    elif "SGN40" in str1:
        date = "SGN40"

    elif "SGN70" in str1:
        date = "SGN70"

    elif "SGN75" in str1:
        date = "SGN75"

    elif "SGN-CD19B" in str1:
        date = "SGN-CD19B"

    elif "SGN-CD33A" in str1:
        date = "SGN-CD33A"

    elif "SGN-CD352A" in str1:
        date = "SGN-CD352A"

    elif "SGN-CD40" in str1:
        date = "SGN-CD40"

    elif "SGN-CD48A" in str1:
        date = "SGN-CD48A"

    elif "SGN-CD70A" in str1:
        date = "SGN-CD70A"

    elif "SGN-LIV1A" in str1:
        date = "SGN-LIV1A"

    elif "SGN-TV" in str1:
        date = "SGN-TV"

    elif "SGN-CD47M" in str1:
        date = "SGN-CD47M"

    elif "SGNBCMA" in str1:
        date = "SGNBCMA"

    elif "Tucatinib" in str1:
        date = "Tucatinib"

    elif "TIGIT" in str1:
        date = "TIGIT"

    elif "TIGIT (CASC-674)" in str1:
        date = "TIGIT (CASC-674)"

    elif "SGN-CD123A" in str1:
        date = "SGN-CD123A"

    elif "SGN-CD19A" in str1:
        date = "SGN-CD19A"

    elif dateObj:
        date = "Other"

    elif dateObj1:
        date = "Other"

    elif dateObj2:
        date = "Other"

    else:
        date = "No Match"

    return date

def ORFile():
    # Opening the csv file so that we can append the changes to it.

    f = open('D:\MainData\csv files\seagencsv\Seagen new files/Seagen_Affiliates.csv', 'w+',encoding="utf8",errors="ignore", newline="")
    w = csv.writer(f, quoting=csv.QUOTE_ALL, delimiter=',')
    w.writerow(['Path&File Name', 'Program'])

    # File name list
    # Walking through the directories

    f1 = open("D:\MainData\csv files\SeaGen_Listing/Seagen_List2.csv", "r+")
    reader = csv.reader(f1)
    for row in reader:
            nda=''
            file1 = open(row[0], 'r+',encoding="utf8",errors="ignore")
            content = file1.read()
            text = content.lower()
            if row[1].lower() == "this":
                if ('and affiliates (collectively, "seagen"),' in text) or ('and it\'s affiliates (collectively, "seagen"),' in text) \
                        or ("seagen and it's affiliates" in text)or ("seagen or it's affiliates" in text):
                    nda = "Yes, to any affiliate"

                elif ("listed affiliates" in text) or ("affiliates mentioned below" in text):
                    nda = "Yes, to listed affiliate"

                else:
                    nda = "No/No Relevant Provision"

            elif row[1].lower() == "nda":
                if "each party agrees not to disclose any information of the other party to third parties or to such party's affiliates" in text:
                    nda = "No/No Relevant Provision"

                elif "the party receiving confidential information will limit disclosure to its directors, officers, employees, consultants, agents and those of its affiliates" in text:
                    nda = "Yes, to any affiliate"

                elif ("may disclose confidential information to any of its affiliates" in text)\
                        or ("may disclose confidential information of the disclosing party to its affiliates" in text)\
                        or ('and affiliates (collectively, "seagen"),' in text):
                    nda = "Yes, to any affiliate"

                else:
                    nda = "No/No Relevant Provision"

            # Writing changes to the csv
            w.writerow([row[0], nda])

            file1.close()

            print("\tFile Name: " + row[0])


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

