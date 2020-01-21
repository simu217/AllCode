#---------------------------------------------------#
# AUTHOR: Simarjit Kaur                             #
# CODE:   RenewalPartners                             #
#---------------------------------------------------#
import os
import csv
import re
import time
def Searchdays(date3):
    SearchdaysVar = ""
    if ("refund" or "repay" or "give back" or "re-pay" or "giveback") in date3:
        SearchdaysVar="true"
    else:
        SearchdaysVar = "false"
    return SearchdaysVar

def ORFile():
    # Opening the csv file so that we can append the changes to it.
    f = open("D:\MainData\csv files\kohl's csv//Kohl'sRefundtoKohl1.csv", 'w+', encoding="utf8",errors="ignore")
    w = csv.writer(f, quoting=csv.QUOTE_ALL, delimiter=',')
    w.writerow(['Path', 'File Name', 'Contractual Notice', "2nd String", 'Keywords'])
    count = 0
# Walking through the directories
    for root, dir, files in os.walk("D:\MainData\Kohl's 1-7-2019\TXT\ContractsForSumati"):
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
                date4 = ""
            # Getting expiration date
                dateObj86 = re.search(r'( (\d?\d{1}.?,?\d?\s?.)\s?termination\s?((.*?).{1000}))', str2, re.I | re.M)
                dateObj87 = re.search(r'( (\d?\d{1}.?,?\d?\s?.)\s?term\s?[.:;,-]((.*?).{1000}))', str2, re.I | re.M)
                if dateObj86:
                    date3 = dateObj86.group(1)
                    date = "termination clause"
                    date4 = Searchdays(date3)
                elif dateObj87:
                    date3 = dateObj87.group(1)
                    date = "term clause"
                    date4 = Searchdays(date3)
                else:
                    date3="No Match"
                    date="1/1/1900"
            # Writing changes to the csv
                w.writerow([root, singFile, date3, date4,date])
                file1.close()
                print("Scanned :" + count1 + " Files" + "\tFile Name: " + singFile)
#===========================================================================================#
def RemainingBatch():
    # Opening the csv file so that we can append the changes to it.
    f = open('D:\MainData\csv files\intelcsv//intelRenewalremaining.csv', 'w+', encoding="utf8",errors="ignore")
    w = csv.writer(f, quoting=csv.QUOTE_ALL, delimiter=',')
    w.writerow(['Path', 'File Name', 'Output_String', 'Keywords'])
    FNlist = []
    count = 0
    f1 = open('D:\MainData//remainingbatch2.csv', 'r+', encoding="utf8",errors="ignore")
    reading = csv.reader(f1)
    for root, dir, files in os.walk("D:\MainData\intel132019\TXT"):
        for row in reading:
            singfile = row[0]
            file1 = open(singfile, 'r+', encoding="utf8",errors="ignore")
            content = file1.read()
            count = count+1
            count1 = str(count)
            text = content.split()
            str1 = ' '.join(str(e) for e in text)
            str2 = str1.lower()
            #print(str2)
            # Variable1=[]
            # dateObj91 = re.search(r'((?:\S+\s)(?:\S+\s)(?:\S+\s)(?:\S+\s)(?:\S+\s)(?:\S+\s)(?:\S+\s)(?:\S+\s)(?:\S+\s)(?:\S+\s)(?:\S+\s)(?:\S+\s)(?:\S+\s)(?:\S+\s)(?:\S+\s)renew ((.*?).{500}))',
            #     str2, re.I | re.M)
            dateObj9 = re.search(r'((?:\S+\s)(?:\S+\s)(?:\S+\s)(?:\S+\s)(?:\S+\s)(?:\S+\s)this agreement may be renewed for((.*?).{500}))',str2, re.I | re.M)
            #dateObj10 = re.search(r'(renew.*?(renew))',str2, re.I | re.M)
            if dateObj9:
                date3 = dateObj9.group(1)
                date="this Agreement may be renewed for"
            # elif dateObj10:
            #     date3 = dateObj10.group(1)
            #     date = "renew"
            else:
                date3 = "No Match"
                #Variable1="N/A"
                date = "1/1/1900"
            w.writerow([singfile,date3, date])
            file1.close()
            print("Scanned  Files :"  + count1  + "\tFile Name: " + singfile)

def main():
    ORFile()
    #RemainingBatch()

if __name__ == '__main__':

    start_time = time.time()
    main()
    end_time = time.time() - start_time
    hours, rem = divmod(end_time - start_time, 3600)
    minutes, seconds = divmod(rem, 60)
    print("-------------TIME TAKEN-----------------")
    print("{:0>2}:{:0>2}:{:05.2f}".format(int(hours), int(minutes), seconds))

