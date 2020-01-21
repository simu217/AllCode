#---------------------------------------------------#
# AUTHOR: Simarjit Kaur                             #
# CODE:   RenewalPartners                             #
#---------------------------------------------------#
import os
import csv
import re
import time


def ORFile():
    # Opening the csv file so that we can append the changes to it.
    f = open("D:\MainData\csv files\kohl's csv//Kohl'sAllFeilds.csv", 'w+', encoding="utf8",errors="ignore")
    w = csv.writer(f, quoting=csv.QUOTE_ALL, delimiter=',')
    w.writerow(['Path', 'File Name', 'Governing Law & Venue', 'Indemnification','Intellectual Property Rights','License Grant','Limitation of Liability','Warranty'])
    count = 0
# Walking through the directories
    for root, dir, files in os.walk("D:\MainData\Kohl's 1-7-2019\TXT"):
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
            # Getting expiration date
                dateObj1 = re.search(r'((choice of law|venue)(.*?)state of ((.*?).{50}))', str2, re.I | re.M)
                dateObj2=re.search(r'(indemnification((.*?).{500}))', str2, re.I | re.M)
                dateObj3 = re.search(r'(intellectual property (rights|owned)|property rights|ownership & title|((.*?).{500}))', str2, re.I | re.M)
                dateObj4 = re.search(r'(license grant|licensed materials((.*?).{500}))',str2, re.I | re.M)
                dateObj5 = re.search(r'(limitation of liability|liability|((.*?).{500}))',str2, re.I | re.M)
                dateObj6 = re.search(r'(warranty((.*?).{500}))',str2, re.I | re.M)
                if ((dateObj1 or dateObj2 or dateObj3 or dateObj4 or dateObj5 or dateObj6) != None):
                    if dateObj1:
                        date1 = dateObj1.group(1)
                    else:
                        date1= "no match"
                    if dateObj2:
                        date2 = dateObj2.group(1)
                    else:
                        date2= "no match"
                    if dateObj3:
                        date3 = dateObj3.group(1)
                    else:
                        date3= "no match"
                    if dateObj4:
                        date4 = dateObj4.group(1)
                    else:
                        date4= "no match"
                    if dateObj5:
                        date5 = dateObj5.group(1)
                    else:
                        date5= "no match"
                    if dateObj6:
                        date6 = dateObj6.group(1)
                    else:
                        date6="no match"
                else:
                    date1=date2=date3=date4=date5=date6="No Match"
            # Writing changes to the csv
                w.writerow([root, singFile, date1, date2,date3,date4,date5,date6])
                file1.close()
                print("Scanned :" + count1 + " Files" + "\tFile Name: " + singFile)
#===========================================================================================#
def RemainingBatch():
    # Opening the csv file so that we can append the changes to it.
    f = open('D:\MainData\csv files\googlecsv//11kKRenewalremaining.csv', 'w+', encoding="utf8",errors="ignore")
    w = csv.writer(f, quoting=csv.QUOTE_ALL, delimiter=',')
    w.writerow(['Path', 'File Name', 'Output_String', 'Keywords'])
    FNlist = []
    count = 0
    f1 = open('D:\MainData//remainingbatch.csv', 'r+', encoding="utf8",errors="ignore")
    reading = csv.reader(f1)
    for row in reading:
        singfile = row[0] + row[1]
        #print(singfile)
        for root, dir, files in os.walk("D:\MainData\GoogleMoca12192017"):
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
            dateObj9 = re.search(r'(renew.*?(renew))',str2, re.I | re.M)
            if dateObj9:
                date3 = dateObj9.group(1)
                #print(date3)
                #Variable1= Searchmonth(date3)
                date = "renew"
            else:
                date3 = "No Match"
                #Variable1="N/A"
                date = "1/1/1900"
            w.writerow([singfile,row[1],date3, date])
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

