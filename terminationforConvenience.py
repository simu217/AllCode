#---------------------------------------------------#
# AUTHOR: Simarjit Kaur                             #
# CODE:   ExpiryDatePartners                        #
#---------------------------------------------------#

import os
import csv
import re
import time
import datetime

def strip_non_ascii(string):
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)

def ForOptions(date2):
    FindOption=[]
    list1=[]
    if "day" in date2:
        var1=date2
        FindOption=re.findall('((\(([\d\d?)]+)\)|\d\d?|1st|first|2nd|3rd|4rth|5th|fifth|one|two|three|four|five|sixt?h?|sevent?h?|eighth?|ninet?h?|tent?h?|elevent?h?|twelvet?h?|thirteent?h?|fourteent?h?|fifteent?h?|sixteent?h?|seventeent?h?|eighteent?h?|nineteent?h?|twenty|twentieth)\s?(-?days?|-weeks?))', var1)
    for i in range(0, len(FindOption)):
        if (i < len(FindOption)):
            list1.append(FindOption[i][0])
        else:
            list1="no match"
        i = i + 1
    return list1

def ORFile():
    # Opening the csv file so that we can append the changes to it.

    f = open("D:\MainData\csv files\Flircsv\Phase V TXT Files\TerminationForConvenience1.csv", 'w+', encoding="utf8",errors="ignore",newline="")
    w = csv.writer(f, quoting=csv.QUOTE_ALL, delimiter=',')
    w.writerow(['Path & File Name', 'Output_String', 'Keywords', 'Termination for conveience'])
    count = 0
# Walking through the directories
    for root, dir, files in os.walk("D:\MainData\Phase V TXT Files"):
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
                keywords = ['(either party((.*?).{400}))',
                            '(with or without cause((.*?).{400}))',
                            '(may terminate((.*?).{400}))',
                            '(right to terminate((.*?).{400}))'
                            ]
            # Getting expiration date
                date, date1, foundOptions, dateObj,date3 = '', "", "", "",""
                for i in keywords:
                    dateObj = re.search(i, str2, re.I | re.M)
                    if dateObj:
                        date2 = dateObj.group()
                        index = str2.index(date2)
                        date3 = str2[index - 50:index]
                        date1 = date3 + date2
                        date = i
                        foundOptions = ForOptions(date1.lower())
                        break
                w.writerow([newPath,date3, date1,  date,foundOptions])
                print(count, " files scanned !")

            # Writing changes to the csv
                file1.close()
                print("Scanned :" + count1 + " Files" + "\tFile Name: " + singFile)

#===========================================================================================#

def RemainingBatch():
    # Opening the csv file so that we can append the changes to it.
    f = open("D:\MainData\csv files\Brightstar\Brighstar 3231.63/Brightstar_TerminationForConvenience1.csv", 'w+', encoding="utf8",errors="ignore",newline="")
    WritingCSV = csv.writer(f, quoting=csv.QUOTE_ALL, delimiter=',')
    WritingCSV.writerow(['Path & File Name', 'Output String', 'Keywords', 'Expiry Date'])
    FNlist = []
    count = 0
    f1 = open('D:\MainData/remainingbatch.csv', 'r+', encoding="utf8",errors="ignore")
    reading = csv.reader(f1)
    for row in reading:
        try:
            file1 = open(row[0], 'r+', encoding="utf8",errors="ignore")
            content = file1.read()
            count = count+1
            count1 = str(count)
            text = content.split()
            str1 = ' '.join(str(e) for e in text)
            keywords = ['(may terminate this((.*?).{400}))']
            # keywords = ['(with or without cause upon five (5) days prior written notice((.*?).{400}))','(at any time, upon reasonable notice((.*?).{400}))',
            # '(SGEN reserves the right to terminate your advisory services and this Letter Agreement at any time((.*?).{400}))','(with or without cause upon((.*?).{400}))']


            # keywords = ['(this agreement shall remain in effect from the((.*?).{500}))',
            # '(the term of this agreement shall be for a.? period,? of((.*?).{500}))',
            # '(the term for disclosure of confidential information under((.*?).{500}))','(this agreement shall come into force on the earlier of((.*?).{500}))'
            #             ]
          #   keywords = ['(estimated destruction will be completed within((.*?).{500}))',
          # '(shall continue through the end of the last expiring or terminating subscription order((.*?).{500}))',
          #               '(this agreement shall come into force on the earlier of((.*?).{500}))']
          #   keywords = ['(Agreement duration: scheduled end date:((.*?).{500}))',
          #   '(evaluation timeline:((.*?).{500}))',
          #   '(the total project would take approximately((.*?).{500}))''(agreement duration:((.*?).{500}))',
          #   '(final results:((.*?).{500}))',
          #   '(renewal target date((.*?).{500}))',

            date, date2, foundOptions = "", "", ""
            for i in keywords:
                dateObj = re.search(i, str1, re.M)
                if dateObj:
                    date3 = dateObj.group()
                    date2 = strip_non_ascii(date3)
                    date = i
                    foundOptions = ForOptions(date2)
                    break
            WritingCSV.writerow([row[0], date2, date, foundOptions])
            file1.close()
            print(count1 + " " + "\tFile Name: " + row[0])
        except:
            pass

def main():
    # ORFile()
    RemainingBatch()

if __name__ == '__main__':
    main()


