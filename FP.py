import os
import sys
import csv
import re
import time

def by_and_between(text, txtContent2, content):
    googleEntities = []

    for entities in txtContent2:

        loweredEntity = entities.lower()

        # Find Entities
        if loweredEntity in text:
            googleEntities.append(entities)

    try:
        ele = googleEntities[0]

        if googleEntities[0] == '':
            ele = googleEntities[1]
            if ele != "No Match":
                lowEnt = googleEntities[1].lower()
                entLen = len(lowEnt)
                entInd = text.index(lowEnt)
                newEnt = content[entInd:(entInd + entLen)]

            else:
                newEnt = "No Match"

        else:
            if googleEntities[0] != "No Match":
                lowEnt = googleEntities[0].lower()
                entLen = len(lowEnt)
                entInd = text.index(lowEnt)
                newEnt = content[entInd:(entInd + entLen)]

            else:
                newEnt = "No Match"

    except Exception:
        googleEntities.append("No Match")

    # Logic for extracting exact FP as present in text file
    if googleEntities[0] != "No Match":
        lowEnt = googleEntities[0].lower()
        entLen = len(lowEnt)
        entInd = text.index(lowEnt)
        newEnt = content[entInd:(entInd + entLen)]

    else:
        newEnt = "No Match"

    return newEnt, googleEntities

def ORFile():
    # Opening the csv file so that we can append the changes to it.

    f = open('D:\MainData\csv files\Carndinal\Cardinal_FP.csv', 'w+', encoding="utf8",
             errors="ignore",
             newline="")
    w = csv.writer(f, quoting=csv.QUOTE_ALL, delimiter=',')
    w.writerow(['Path & File Name', 'First party', 'By and Between'])

    # Used for getting all the google entities.
    f1 = open('D:\MainData\csv files\Flir_Listing/FLIR_Entities.txt', 'r')
    txtContent = f1.read()
    txtContent2 = txtContent.split(":")
    print(txtContent2)

    # Keeping file count
    count = 0
    nmCount = 0

    # Walking through the directories
    for root, dir, files in os.walk("D:\MainData\FLIR Phase 8 TXT"):

        # Fetching a single file
        for singFile in files:

            # Getting only text files
            if ".txt" in singFile:
                newPath = os.path.join(root, singFile)

                count = count + 1
                count1 = str(count)

                # Opening single file
                file1 = open(newPath, 'r+', encoding="utf8",errors="ignore")

                content = file1.read()
                text = content.lower()
                str4 = content

                # List of Google Entities
                googleEntities = []

                # by and between
                matchObj = re.search(r'by and between((.*) and((.*).{100}))', str4, re.M | re.I)

                matchObj1 = re.search(r'between((.*?) and((.*).{100}))', str4, re.M | re.I)

                matchObj2 = re.search(r'by and among((.*) and((.*).{100}))', str4, re.M | re.I)

                matchObj5 = re.search(r'(by (google|doubleclick)(.*?) and((.*).{100}))', str4, re.M | re.I)

                matchObj4 = re.search(r'into by((.*?) and((.*).{100}))', str4, re.M | re.I)

                matchObj6 = re.search(r'between (google|doubleclick)((.*?) and((.*).{100}))', str4, re.M | re.I)

                if matchObj6:
                    Party1 = matchObj6.group()

                elif matchObj1:
                    Party1 = matchObj1.group()

                elif matchObj:
                    Party1 = matchObj.group()

                elif matchObj2:
                    Party1 = matchObj2.group()

                elif matchObj4:
                    Party1 = matchObj4.group()

                elif matchObj5:
                    Party1 = matchObj5.group()

                else:
                    Party1 = "No Match"

                for entities in txtContent2:

                    loweredEntity = entities.lower()

                    # Find Entities
                    if loweredEntity in text:
                        googleEntities.append(entities)

                try:
                    ele = googleEntities[0]

                    if googleEntities[0] == '':
                        ele = googleEntities[1]
                        if ele != "No Match":
                            lowEnt = googleEntities[1].lower()
                            entLen = len(lowEnt)
                            entInd = text.index(lowEnt)
                            newEnt = content[entInd:(entInd + entLen)]

                        else:
                            newEnt = "No Match"

                    else:
                        if googleEntities[0] != "No Match":
                            lowEnt = googleEntities[0].lower()
                            entLen = len(lowEnt)
                            entInd = text.index(lowEnt)
                            newEnt = content[entInd:(entInd + entLen)]

                        else:
                            newEnt = "No Match"

                except Exception:
                    googleEntities.append("No Match")

                # Logic for extracting exact FP as present in text file
                if googleEntities[0] != "No Match":
                    lowEnt = googleEntities[0].lower()
                    entLen = len(lowEnt)
                    entInd = text.index(lowEnt)
                    newEnt = content[entInd:(entInd + entLen)]

                else:
                    newEnt = "No Match"
                list1=checkList(txtContent2,str4)


                bnb = by_and_between(Party1.lower(), txtContent2, Party1)

                w.writerow([newPath, newEnt, bnb[0],list1])

                if bnb[0] == "No Match":
                    nmCount = nmCount + 1

                print ("No Match = " + str(nmCount))

                file1.close()

                print("Scanned :" + count1 + " Files" + "\tFile Name: " + singFile)

                # w.writerow([newPath, list1])

def checkList(txtContent2,str4):
    list1=[]
    for element in txtContent2:
        try:
            element1=str4.find(element)
            if element1>=0:
                list1.append(element)
        except:
            pass
    return list1

def remainingBatch():
    PathForCSV = 'D:\MainData\csv files\Carndinal\Cardinal_FP.csv'
    RemainingfilesList='D:/remainingbatch.csv'
    RemainingFiles = open(RemainingfilesList, 'r+', encoding="utf8", errors="ignore")
    reading = csv.reader(RemainingFiles)
    ReadingCSV = open(PathForCSV, 'w+', encoding="utf8",errors="ignore", newline="")
    WritingCSV = csv.writer(ReadingCSV, quoting=csv.QUOTE_ALL, delimiter=',')
    WritingCSV.writerow(['Path & File Name', 'First party', 'By and Between'])
    count = 0

    f1 = open('D:\MainData\csv files\Carndinal\CardinalSubsidiaries.txt', 'r',errors="ignore")
    txtContent = f1.read()

    txtContent2 = txtContent.split(":")

    for row in reading:
            file1 = open(row[0], 'r+', encoding="utf8",errors="ignore")
            count=count+1
            content = file1.read()
            text = content.split()
            str4= ' '.join(str(e) for e in text).lower()
            # str4=strip_non_ascii(str1)
            # List of Google Entities
            googleEntities = []
            #
            # # by and between
            matchObj = re.search(r'by and between((.*) and((.*).{100}))', str4, re.M | re.I)

            matchObj1 = re.search(r'between((.*?) and((.*).{100}))', str4, re.M | re.I)

            matchObj2 = re.search(r'by and among((.*) and((.*).{100}))', str4, re.M | re.I)

            matchObj5 = re.search(r'(by (google|doubleclick)(.*?) and((.*).{100}))', str4, re.M | re.I)

            matchObj4 = re.search(r'into by((.*?) and((.*).{100}))', str4, re.M | re.I)

            matchObj6 = re.search(r'between (google|doubleclick)((.*?) and((.*).{100}))', str4, re.M | re.I)

            if matchObj6:
                Party1 = matchObj6.group()

            elif matchObj1:
                Party1 = matchObj1.group()

            elif matchObj:
                Party1 = matchObj.group()

            elif matchObj2:
                Party1 = matchObj2.group()

            elif matchObj4:
                Party1 = matchObj4.group()

            elif matchObj5:
                Party1 = matchObj5.group()

            else:
                Party1 = "No Match"

            for entities in txtContent2:

                loweredEntity = entities.lower()

                # Find Entities
                if loweredEntity in text:
                    googleEntities.append(entities)

            try:
                ele = googleEntities[0]

                if googleEntities[0] == '':
                    ele = googleEntities[1]
                    if ele != "No Match":
                        lowEnt = googleEntities[1].lower()
                        entLen = len(lowEnt)
                        entInd = text.index(lowEnt)
                        newEnt = content[entInd:(entInd + entLen)]

                    else:
                        newEnt = "No Match"

                else:
                    if googleEntities[0] != "No Match":
                        lowEnt = googleEntities[0].lower()
                        entLen = len(lowEnt)
                        entInd = text.index(lowEnt)
                        newEnt = content[entInd:(entInd + entLen)]

                    else:
                        newEnt = "No Match"

            except Exception:
                googleEntities.append("No Match")

            # Logic for extracting exact FP as present in text file
            if googleEntities[0] != "No Match":
                lowEnt = googleEntities[0].lower()
                entLen = len(lowEnt)
                entInd = text.index(lowEnt)
                newEnt = content[entInd:(entInd + entLen)]

            else:
                newEnt = "No Match"

            list1 = checkList(txtContent2, str4)

            bnb = by_and_between(Party1.lower(), txtContent2, Party1)

            WritingCSV.writerow([row[0], newEnt, bnb[0],list1])

            print("Scanned :" + str(count) + " Files" + "\tFile Name: " + row[0])


# ===========================================================================================#

def main():
    # ORFile()
    remainingBatch()

if __name__ == '__main__':

    start_time = time.time()

    main()

    end_time = time.time()
    print ("-------------TIME TAKEN-----------------")
    print(start_time)
    print(end_time)
