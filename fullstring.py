#---------------------------------------------------#
# AUTHOR: Simarjit Kaur                             #
# CODE:   ExpiryDatePartners                        #
#---------------------------------------------------#

import os
import csv
import re
import time
def strip_non_ascii(string):
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)

def ForOptions(date2):
    list1=[]
    if "automatically"  in date2:
        str3 = re.search(r'((.*)automatically|automatically renew|renew automatically|renew|auto)', date2, re.I | re.M)
        var1=str3.group(1)
        FindOption=re.findall('((\(([\d\d?)]+)\)|\d\d?|1st|first|2nd|3rd|4rth|5th|fifth|one|two|three|four|five|sixt?h?|sevent?h?|eighth?|ninet?h?|tent?h?|elevent?h?|twelvet?h?|thirteent?h?|fourteent?h?|fifteent?h?|sixteent?h?|seventeent?h?|eighteent?h?|nineteent?h?|twenty|twentieth)\s?(anniversary|-?months?|-?days?|-?years?( anniversary)?)|'
                    '(\d\d?(?:(st|nd|rd|th))?\s?,?\s?-?(january|february|mar|march|april|apr|may|june|jun|jul|july|august|october|november|september|december|jan|feb|aug|sept|sep|oct|nov|dec)-?,?\s?\d{2}\d?\d?)|'
                    '(\d?\d?\d{2}\s?,?\s?-?(january|february|mar|march|jun|jul|sep|april|apr|may|june|july|august|october|november|september|december|jan|feb|aug|sept|oct|nov|dec)-?,?\s?\d\d?(?:(st|nd|rd|th))?)|'
                 '((january|february|mar|march|april|apr|may|june|jun|jul|sep|july|august|october|november|september|december|jan|feb|aug|sept|oct|nov|dec)\s?-?,?\s?\d\d?(?:(st|nd|rd|th))?\s?,?-?\s?,?\s?\d{2}\d?\d?)|'
                   '(\d\d?[.\/-]\d\d?[.\/-]\d{4})|(\d\d?[.\/-]\d\d?[.\/-]\d{2})|(\d{2}[.\/-]\d\d?[.\/-]\d\d?))', var1)
    else:
        FindOption=re.findall('((\(([\d\d?)]+)\)|\d\d?|1st|first|2nd|3rd|4rth|5th|fifth|one|two|three|four|five|sixt?h?|sevent?h?|eighth?|ninet?h?|tent?h?|elevent?h?|twelvet?h?|thirteent?h?|fourteent?h?|fifteent?h?|sixteent?h?|seventeent?h?|eighteent?h?|nineteent?h?|twenty|twentieth)\s?(anniversary|-?months?|-?days?|-?years?( anniversary)?)|'
                    '(\d\d?(?:(st|nd|rd|th))?\s?,?\s?-?(january|february|mar|march|april|apr|may|june|july|jun|jul|sep|august|october|november|september|december|jan|feb|aug|sept|oct|nov|dec)-?,?\s?\d{2}\d?\d?)|'
                    '(\d?\d?\d{2}\s?,?\s?-?(january|february|mar|march|april|apr|may|june|jun|jul|sep|july|august|october|november|september|december|jan|feb|aug|sept|oct|nov|dec)-?,?\s?\d\d?(?:(st|nd|rd|th))?)|'
                 '((january|february|mar|march|april|apr|may|june|july|august|october|jun|jul|sep|november|september|december|jan|feb|aug|sept|oct|nov|dec)\s?-?,?\s?\d\d?(?:(st|nd|rd|th))?\s?,?-?\s?,?\s?\d{2}\d?\d?)|'
                   '(\d\d?[.\/-]\d\d?[.\/-]\d{4})|(\d\d?[.\/-]\d\d?[.\/-]\d{2})|(\d{2}[.\/-]\d\d?[.\/-]\d\d?))', date2)
    for i in range(0, len(FindOption)):
        if (i < len(FindOption)):
            list1.append(FindOption[i][0])
            i = i + 1
    return list1

def ORFile():
    # Opening the csv file so that we can append the changes to it.
    f = open("D:\MainData\csv files\googlecsv\google45K'1-16-19'/fullstring45K.csv", 'w+', encoding="utf8",errors="ignore")

    w = csv.writer(f, quoting=csv.QUOTE_ALL, delimiter=',')
    w.writerow(['Path', 'File Name', 'Output_String'])
    count = 0
# Walking through the directories
    for root, dir, files in os.walk("D:\MainData\Google50knew'1-16-19'"):
    #Fetching a single file
        for singFile in files:
    # Getting only text files
            if ".txt" in singFile:
                newPath = os.path.join(root, singFile)
                count = count + 1
                count1 = str(count)
            # Opening single file for editing and detecting language
                file1 = open(newPath, 'r+',encoding="utf8",errors="ignore")
                content = file1.read()
            # Extracting Parties from txt files (300 words)
                text = content.split()
                str1 = ' '.join(str(e) for e in text)
                str2 = str1.lower()



            # Writing changes to the csv
                w.writerow([root, singFile, str2])
                file1.close()
                print("Scanned :" + count1 + " Files" + "\tFile Name: " + singFile)
#===========================================================================================#



def main():
    ORFile()


if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time() - start_time
    hours, rem = divmod(end_time - start_time, 3600)
    minutes, seconds = divmod(rem, 60)
    print( ("-------------TIME TAKEN-----------------")
    print("{:0>2}:{:0>2}:{:05.2f}".format(int(hours), int(minutes), seconds))

