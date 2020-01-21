#---------------------------------------------------#
# AUTHOR: Simarjit Kaur                             #
# CODE:   RenewalPartners                           #
#---------------------------------------------------#
import os
import csv
import re
import time

def ORFile():
    PathForCSV = "D:\MainData\csv files\Elevate Contract Extraction_Internal\Elevate_Renewal.csv"
    MainPathtext = "D:\Elevate Contract Extraction_Internal\TXT"

    f = open(PathForCSV , 'w+', encoding="utf8",errors="ignore",newline="")
    w = csv.writer(f, quoting=csv.QUOTE_ALL, delimiter=',')
    w.writerow([ "Txt Path" ,'File Name', 'Output String' ,'Keywords'])
    count = 0
# Walking through the directories
    for root, dir, files in os.walk(MainPathtext):
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
                keywords = ['(automatically( be)? renew((.*?).{300}))',
                            '(renewi?n?g? automatically((.*?).{300}))',
                            '(auto-?matically extend for((.*?).{300}))',
                            '(renewable annual((.*?).{300}))',
                            '((shall|will)( be)? renew((.*?).{500}))',
                            '(auto-renewal.?\s?at the end of each((.*?).{500}))',
                            '(auto-?\s?renew((.*?).{500}))',
                            '(renewal-? term((.*?).{500}))',
                            '(renew((.*?).{500}))']
                i = 0
                date, date2, foundOptions = "", "", ""
                for i in keywords:
                    dateObj = re.search(i, str2, re.I | re.M)
                    if dateObj:
                        date1 = dateObj.group()
                        index = str2.index(date1)
                        date3 = str2[index - 100:index]
                        date2 = date3 + date1
                        date = i
                        break
            # Writing changes to the csv
                w.writerow([newPath, singFile, date2, date])
                file1.close()
                print("Scanned :" + count1 + " Files" + "\tFile Name: " + singFile)


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

def RemainingBatch():
    # Opening the csv file so that we can append the changes to it.
    f = open("D:\MainData\csv files\Brightstar\Brighstar 3231.63\Brightstar_Renewal_7K.csv", 'w+',
             encoding="utf8",errors="ignore", newline="")
    w = csv.writer(f, quoting=csv.QUOTE_ALL, delimiter=',')
    w.writerow(['Path & File Name', 'Keyword String', 'Initial String','Keyword','days'])
    FNlist = []
    count = 0
    f1 = open('D:\MainData/remainingbatch.csv', 'r+', encoding="utf8",errors="ignore")
    reading = csv.reader(f1)
    # for root, dir, files in os.walk("D:\MainData\SeaGenTXTFiles"):
    for row in reading:
        try:
            file1 = open(row[0], 'r+', encoding="utf8",errors="ignore")
            content = file1.read()
            count = count+1
            filename=strip_non_ascii(row[0])
            count1 = str(count)
            text = content.split()
            str1 = ' '.join(str(e) for e in text)
            str2=strip_non_ascii(str1)
            String=str2[:1000]
            keywords = ['(((.*?).{300}))',
                        ]
            i = 0
            date, date3,date2, foundOptions = "", "", "",""
            for i in keywords:
                dateObj = re.search(i, str2, re.I | re.M)
                if dateObj:
                    date1 = dateObj.group()
                    index = str2.index(date1)
                    date3 = str2[index - 100:index]
                    date2 = date3 + date1
                    foundOptions = ForOptions(date2)
                    date = i
                    break
            # Writing changes to the csv
            w.writerow([row[0],filename, date2, String, date,foundOptions])
            file1.close()
            print("Scanned :" + count1 + " Files" + "\tFile Name: " + row[0])
        except:
            pass
def main():

    ORFile()
    # RemainingBatch()

if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time() - start_time
    hours, rem = divmod(end_time - start_time, 3600)
    minutes, seconds = divmod(rem, 60)
    print("-------------TIME TAKEN-----------------")
    print("{:0>2}:{:0>2}:{:05.2f}".format(int(hours), int(minutes), seconds))

