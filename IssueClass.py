import os
import sys
import csv
import re
import time

def ORFile():
    # Opening the csv file so that we can append the changes to it.
    f = open('D:\MainData\csv files\FLIR Phase 6 TXT/Google_IssueClassifier16k.csv', 'w+',newline="", errors="ignore")
    w = csv.writer(f, quoting=csv.QUOTE_ALL, delimiter=',')
    w.writerow(['Path', 'File Name', 'Issue Classification'])

    count = 0

    f1 = open("D:/MainData/remainingbatch1.csv", "r+", encoding="utf8", errors="ignore")
    reader = csv.reader(f1)

    # Used for getting all the google entities.
    f1 = open('D:\MainData\csv files\Google_Entities\Google entities_1.txt', 'r', encoding="utf8", errors="ignore")
    txtContent = f1.read()
    googleEntities = txtContent.split(":")

    # Walking through the directories
    for row in reader:
            count = count + 1
            count1 = str(count)

            # Opening single file for editing and detecting language

            file1 = open(row[0], 'r+', encoding="utf8", errors="ignore")

            content = file1.read()

            # Extracting Parties from txt files (300 words)

            loweredContent = content.lower()

            text = loweredContent[:400]

            matchObj = re.search(r'to:(.*?)@google.com', text, re.I|re.M)

            for entity in googleEntities:
                loweredEntity = entity.lower()

                if matchObj:
                    classification = "Miscellaneous"

                elif loweredEntity in loweredContent:
                    classification = "One Way Signatures- External Customer Only"
                    break

                else:
                    classification = "One Way Signatures- Google only"

            # Writing changes to the csv
            w.writerow([row[0], classification])

            file1.close()

            print("Scanned :" + count1 + " Files" + "\tFile Name: " + row[0])


# ===========================================================================================#

def main():
    ORFile()


if __name__ == '__main__':

    main()
