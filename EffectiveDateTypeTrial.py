import sys
import csv
import re
import time
import datetime

def convert_month_to_num(mm):
    if (mm == 'jan') or (mm == 'january'):
        new_mm = '01'

    elif (mm == 'feb') or (mm == 'february'):
        new_mm = '02'

    elif (mm == 'mar') or (mm == 'march'):
        new_mm = '03'

    elif (mm == 'apr') or (mm == 'april'):
        new_mm = '04'

    elif mm == 'may':
        new_mm = '05'

    elif (mm == 'jun') or (mm == 'june'):
        new_mm = '06'

    elif (mm == 'jul') or (mm == 'july'):
        new_mm = '07'

    elif (mm == 'aug') or (mm == 'august'):
        new_mm = '08'

    elif (mm == 'sep') or (mm == 'sept') or (mm == 'september'):
        new_mm = '09'

    elif (mm == 'oct') or (mm == 'october'):
        new_mm = '10'

    elif (mm == 'nov') or (mm == 'november'):
        new_mm = '11'

    elif (mm == 'dec') or (mm == 'december'):
        new_mm = '12'

    else:
        new_mm = mm

    return new_mm


def dateCleanUp(rawdate):
    if ("month" or "year" or "days") in rawdate:
        return rawdate
    else:
        for fmt in ["%m/%d/%Y", "%m /%d /%Y", "%d/%m/%Y", "%d /%m /%Y", "%Y/%m/%d",
                    "%m/%d/%y","%m /%d/ %y","%d/%m/%y","%d /%m /%y",
                    "%B %d, %Y", "%B %d,%Y", "%B%d, %Y", "%B%d,%Y", "%B %d %Y", "%B%d%Y",
                    "%b %d, %Y", "%b %d, %Y", "%b%d, %Y", "%b%d,%Y", "%b %d %Y", "%b%d%Y",
                    "%d %B, %Y", "%d %B %Y","%d %b, %Y", "%d %b %Y","%d-%m-%Y", "%d - %m - %Y", "%Y-%m-%d"]:
            try:
                formatdate=datetime.datetime.strptime(rawdate, fmt).date()
                rawdate1=formatdate.strftime("%m-%d-%Y")
                return rawdate1
            except ValueError:
                continue

# For extracting date only from the string
def cleanup_func(DateString):
    list1 = []
    if ('1201' in DateString):
        new_DateString = DateString.replace('1201', '1 201')

    elif '1200' in DateString:
        new_DateString = DateString.replace('1200', '1 200')

    elif '2201' in DateString:
        new_DateString = DateString.replace('2201', '2 201')

    elif '2200' in DateString:
        new_DateString = DateString.replace('2200', '2 200')

    else:
        new_DateString = DateString

    FindOption = re.findall(
        '((\(([\d\d?)]+)\)|\d\d?|1st|first|third|fourth|second|2nd|3rd|4rth|5th|fifth|one|two|three|four|five|sixt?h?|sevent?h''?|eighth?|ninet?h?|tent?h?|elevent?h?|twelvet?h?|thirteent?h?|fourteent?h?|'
        'fifteent?h?|sixteent?h?|seventeent?h?|eighteent?h?|nineteent?h?|twenty|twentieth'
        '|twelfth)\s?(-?(calendar)?\s?months?(\s?anniversary)?|-?(calendar)?\s?years?(\s?anniversary)?|(calendar)?\s?weeks?|-?(calendar)?\s?months?|-?(calendar)?\s?days?|-?(calendar)?\s?anniversary)|'
        '(\d\d?(?:(st|nd|rd|th))?\s?,?\s?-?(january|february|mar|march|april|apr|may|june|jun|jul|july|august|october|november|september|december|jan|feb|aug|sept|sep|oct|nov|dec)-?,?\s?\d{2}\d?\d?)|'
        '(\d?\d?\d{2}\s?,?\s?-?(january|february|mar|march|jun|jul|sep|april|apr|may|june|july|august|october|november|september|december|jan|feb|aug|sept|oct|nov|dec)-?,?\s?\d\d?(?:(st|nd|rd|th))?)|'
        '((january|february|mar|march|april|apr|may|june|jun|jul|sep|july|august|october|november|september|december|jan|feb|aug|sept|oct|nov|dec)\s?-?,?\s?\d\d?(?:(st|nd|rd|th))?\s?,?-?\s?,?\s?\d{2}\d?\d?)|'
        '(\d\d?[.\/-]\d\d?[.\/-]\d{4})|(\d{4}[.\/-]\d\d?[.\/-]\d{2})|(\d{2}[.\/-]\d\d?[.\/-]\d\d?))',
        new_DateString, re.I | re.M)
    for i in range(0, len(FindOption)):
        if (i < len(FindOption)):
            rawdate = FindOption[i][0]
            properDate = dateCleanUp(rawdate)
            if properDate == None:
                list1.append(rawdate)
            else:
                list1.append(properDate)
                i = i + 1
    return list1

# Function for getting signature block and also includes conditions for signature block
# noinspection PyUnboundLocalVariable
# For getting Date from the Signature.
def last_sign_date(content1):
    text = content1.split()
    str1 = ' '.join(str(e) for e in text)
    content = str1.lower()
    lis = ["title:",'for acknowledgement and acceptance', "signed:", 'agreed and accepted by grantee:',
           "provider and google hereby agree to this agreement", "in witness whereof", "signed by the parties", "agreed and accepted",
           'accepted and agreed', "supplier:", 'accepted on', 'sincerely', "kindly regards", "very truly yours",
           "agreed by the parties using echosign on the dates stated below", "agreed by the parties on the dates stated below",  "title",
           "prepared by:", "on behalf of:", "signed on behalf of the:", "the parties hereto have caused this", "last party to subscribe below"]
    contentLen = len(content)

    for element in lis:

        if element in content:

            if element == "sincerely":
                elementIndex = content.index(element)
                String = content[(elementIndex):(elementIndex + 600)]
                break

            else:
                elementIndex = content.index(element)
                String = content[(elementIndex - 200):(elementIndex + 600)]
                break

        else:
            String = content[(contentLen - 350):contentLen]

    String1 = String.replace(' ','')
    date = cleanup_func(String1)

    return String, date

# A function for searching all the keywords in a document and checking if a date exists nearby or not
# noinspection PyUnboundLocalVariable
def keyword_process(key, content, length = 0):
    result = [m.start() for m in re.finditer(key, content)]

    key_len = len(key)
    contentLen = len(content)

    for ind in result:
        if ind <= 100:
            Index = 0

        else:
            Index = ind - 100

        Index1 = ind + (key_len + 3)
        Index2 = ind + 120 + length

        String = content[Index:Index2]  # used for checking if any date exists nearby 'effective' keyword.
        String2 = content[ind:Index1]  # Used for checking if tab exists after 'effective' or any other keyword.

        if key == "effective":

            if "\t" in String2:
                CSV_Col = "No Match"
                break

            # elif "last sign" in String:
            #     Conlength = len(content)
            #     prevLen = content[(Conlength - 100):Conlength]
            #     dateObj = re.search(
            #         '(?:Jan(?:u)(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)',
            #         prevLen, re.M | re.I)
            #     dateObj2 = re.search(
            #         '[\d][\d][\s^./-]?[\d][\d]',
            #         prevLen,
            #         re.M | re.I)
            #
            #     if dateObj:
            #         CSV_Col = prevLen
            #         break
            #
            #     elif dateObj2:
            #         CSV_Col = prevLen
            #         break
            #
            #     else:
            #         CSV_Col = "No Match"

            else:
                dateObj = re.search(
                    '(?:Jan(?:u)(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)',
                    String, re.M | re.I)
                dateObj2 = re.search(
                    '([\d][\d][\s^./-]?[\d][\d])', String,
                    re.M | re.I)

                if dateObj:
                    CSV_Col = String
                    CSV_Col1 = dateObj.group()
                    break

                elif dateObj2:
                    CSV_Col = String
                    CSV_Col1 = dateObj2.group()
                    break

                else:
                    CSV_Col = "No Match"
                    CSV_Col1 = "No Match"

        # elif "last sign" in String:
        #     Conlength = len(content)
        #     prevLen = content[(Conlength-100):Conlength]
        #     dateObj = re.search(
        #         '(?:Jan(?:u)(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)',
        #         prevLen, re.M | re.I)
        #     dateObj2 = re.search(
        #         '([\d][\d][\s^./-]?[\d][\d])',
        #         prevLen,
        #         re.M | re.I)
        #
        #     if dateObj:
        #         CSV_Col = prevLen
        #         break
        #
        #     elif dateObj2:
        #         CSV_Col = prevLen
        #         break
        #
        #     else:
        #         CSV_Col = "No Match"

        else:
            dateObj = re.search(
                '(?:Jan(?:u)(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)',
                String, re.M | re.I)
            dateObj2 = re.search(
                '([\d][\d][\s^./-]?[\d][\d])',
                String,
                re.M | re.I)

            if dateObj:
                CSV_Col = String
                CSV_Col1 = dateObj.group()
                break

            elif dateObj2:
                CSV_Col = String
                CSV_Col1 = dateObj2.group()
                break

            else:
                CSV_Col = "No Match"
                CSV_Col1 = "No Match"
    # returns date
    return CSV_Col


def processing(lis, str1, content, lowredContent):

    if "insertion order" in lowredContent[:100]:
        total = last_sign_date(content)
        dateString = total[0]
        date = total[1]
        edOption = "Later of the two signatures"

    elif "order id#" in lowredContent[:200]:
        dateString = lowredContent[:300]
        date = cleanup_func(dateString)
        edOption = "Specific Date"

    else:
        # For each keyword in list
        for element in lis:
            # Checking every keyword present in the list
            if element in str1:
                if (element == 'dear') or (element == ' re:'):
                    key = str1.index(element)
                    dateString = str1[:key]
                    # date = cleanup_func(dateString)
                    # break

                elif element == 'this':
                    key = str1.index(element)
                    dateString = str1[:(key + 200)]
                    # date = cleanup_func(dateString)
                    # break

                else:
                    key = str1.index(element)
                    if key < 100:
                        dateString = str1[:(key + 180)]

                    else:
                        dateString = str1[(key - 100): (key + 110)]

                    # Getting signature block to determine Effective Date
                    if ("first day of the month in which the last party signs" in dateString) \
                            or ("first day of the calendar month in which this agreement is fully executed" in dateString) \
                            or ("1st day of the calendar month in which this agreement is fully executed" in dateString) \
                            or ("1st day of the calendar month" in dateString):
                        edOption = "first day of the month in which the last party signs"
                        lastSign = last_sign_date(content)
                        dateString = lastSign[0]
                        date = lastSign[1]
                        break

                    elif ("first day of the immediately following calendar month" in dateString):
                        edOption = "first day of the immediately following calendar month"
                        lastSign = last_sign_date(content)
                        dateString = lastSign[0]
                        date = lastSign[1]
                        break

                    elif ("last signed" in dateString) \
                            or ("as of the date of the last party's signature" in dateString) \
                            or ("signature block" in dateString) \
                            or ("last signature" in dateString) \
                            or ("signed below" in dateString) \
                            or ("last party signs" in dateString) \
                            or ("final signature" in dateString) \
                            or ("party identified below" in dateString) \
                            or ("sincerely" in dateString) \
                            or ("kind regards" in dateString) \
                            or ("owner's signature below" in dateString) \
                            or ("executed by both partner and google" in dateString) \
                            or ("agreed by the parties using echosign on the dates stated below" in dateString) \
                            or ("date signed by the supplier" in dateString) \
                            or ("last date of execution" in dateString) \
                            or ("date that this order form is signed by" in dateString) \
                            or ("date that both parties have signed the contract" in dateString) \
                            or ("latest of the signature dates below" in dateString) \
                            or ("date signed by the last party below" in dateString) \
                            or ("association's signature below" in dateString) \
                            or ("the parties hereto have caused this" in dateString) \
                            or ("last party to subscribe below" in dateString):
                        edOption = "Later of the two signatures"
                        lastSign = last_sign_date(content)
                        dateString = lastSign[0]
                        date = lastSign[1]
                        break

                        # Getting signature block to determine Effective Date

                    elif ("signed by google" in dateString) \
                            or ("google sign" in dateString) \
                            or ("google signature" in dateString) \
                            or ("google's signature below" in dateString) \
                            or ("the date this agreement is signed by google" in dateString):
                        edOption = "Google Sign Date"
                        lastSign = last_sign_date(content)
                        dateString = lastSign[0]
                        date = lastSign[1]
                        break

                    else:
                        if (element == "effective date") \
                                or (element == "amendement effective date") \
                                or (element == "sow effective date") \
                                or (element == "order form effective date") \
                                or (element == "this") \
                                or (element == "entered into as of ") \
                                or (element == "entered into") \
                                or (element == "made as of") \
                                or (element == "made on") \
                                or (element == "made into") \
                                or (element == "effective as of")\
                                or (element == '(the "effective date")')\
                                or (element == '"effective date"')\
                                or (element == "effective")\
                                or (element == '(the "amendment date")')\
                                or (element == '(the "statement of work")')\
                                or (element == '"pilot effective date"')\
                                or (element == 'dear')\
                                or (element == 'date of work statement')\
                                or (element == 'date of request:')\
                                or (element == 'addendum effective date')\
                                or (element == 'this addendum')\
                                or (element == 'this statement of work')\
                                or (element == 'this amendment')\
                                or (element == 'this agreement')\
                                or (element == 'amendment three effective date')\
                                or (element == 'sow effective')\
                                or (element == '(the "addendum")')\
                                or (element == '"effective date" means')\
                                or (element == 'start date:')\
                                or (element == 'attn:')\
                                or (element == 'scheduled start date'):
                            result = keyword_process(element, str1)

                        else:
                            try:
                                result = keyword_process(element, dateString)

                            except Exception:
                                result = "skip"

                        if result == "No Match":
                            edOption = "Later of two"
                            date = result

                        elif result == "skip":
                            date = "skip"

                        else:
                            edOption = "Specific Date"
                            dateString = result
                            date = cleanup_func(result)
                            break

            else:
                dateString = 'No Match'
                date = 'No Match'
                edOption = "No Match"



    return dateString, date, edOption
# noinspection PyUnboundLocalVariable
def strip_non_ascii(string):
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)

def ORFile():
    # Opening the csv file so that we can append the changes to it.
    f = open('D:\MainData\csv files\FLIR 11.1\FLIR Phase 8 TXT\Flir_P8_EffectiveDate.csv', 'w+',
             encoding="utf8",errors="ignore",
             newline="")
    w = csv.writer(f, quoting=csv.QUOTE_ALL, delimiter=',')
    w.writerow(['Path& File Name', "filename without special char",'Date String', 'Date', 'ED Option', 'Signature Block String', 'Signature Block Date'])
# this is for writing tha names of those files which have ascii/special chars in their file names and cant be open from listing
    f1 = open('D:\MainData\Brightstar_SpecialCharRemainingFileListing.csv', 'w+',
              encoding="utf8", errors="ignore", newline="")
    w1 = csv.writer(f1, quoting=csv.QUOTE_ALL, delimiter=',')
    w1.writerow(['Path & File Name'])
    # List which contains all the keywords for the desired field.
    lis= ['"effective date"','made and entered', 'dear', 'date of work statement','p.o. no.', 'ref:', ' re:','date of request:', 'addendum effective date',
           'this addendum','effective as of', '(the "amendment date")','amendment one effective date','amendment two effective date','amendment three effective date',
           'amendment four effective date', 'amendment effective date', '(the "statement of work")', 'sow effective date', 'sow effective', '(the "addendum")', 'order form effective date',
           "pilot effective date",'"effective date" means', '(the "effective date")', 'effective date', 'this statement of work', 'this amendment', 'this agreement'
           'this', 'entered into as of ', 'entered into', 'made as of', 'made into', 'made on', 'commencement date', 'effective as of',
           'effective', 'contract date:','start date:', 'attn:', 'scheduled start date', 'for acknowledgement and acceptance', "signed:", 'agreed and accepted by grantee:',
           "provider and google hereby agree to this agreement", "in witness whereof", "signed by the parties", "agreed and accepted",
           'accepted and agreed', "supplier:", 'accepted on', 'sincerely', "kindly regards", "very truly yours",
           "agreed by the parties using echosign on the dates stated below", "agreed by the parties on the dates stated below", "title:", "title",
           "prepared by:", "on behalf of:", "signed on behalf of the:", "the parties hereto have caused this", "last party to subscribe below"]

    # Keywords for Amendment
    amendment =['"effective date"','made and entered', 'effective as of','(the "amendment date")', "amendment effective date", 'amendment four effective date',
                'amendment three effective date', 'amendment two effective date', 'amendment one effective date', 'is effective from', 'this amendment'
                'this', 'entered into this','entered into as of ', 'entered into', 'made as of', 'made into', 'made on', '"effective date" means',
                'for acknowledgement and acceptance', "signed:", 'agreed and accepted by grantee:',
                "provider and google hereby agree to this agreement", "in witness whereof", "signed by the parties",
                "agreed and accepted",
                'accepted and agreed', "supplier:", 'accepted on', 'sincerely', "kindly regards", "very truly yours",
                "agreed by the parties using echosign on the dates stated below",
                "agreed by the parties on the dates stated below", "title:", "title",
                "prepared by:", "on behalf of:", "signed on behalf of the:",  'commencement date', "the parties hereto have caused this",
                "last party to subscribe below"
                ]

    # Keywords for Addendum
    addendum = ['"effective date"', 'made and entered','effective as of', '(the "effective date")', '(the "addendum")', 'entered into this', 'entered into as of ',
                'entered into', 'made as of', 'made into', 'made on', 'is effective from', '"effective date" means', 'this addendum', 'dated',
                'for acknowledgement and acceptance', "signed:", 'agreed and accepted by grantee:',
               "provider and google hereby agree to this agreement", "in witness whereof", "signed by the parties", "agreed and accepted",
               'accepted and agreed', "supplier:", 'accepted on', 'sincerely', "kindly regards", "very truly yours",
               "agreed by the parties using echosign on the dates stated below", "agreed by the parties on the dates stated below", "title:", "title",
               "prepared by:", "on behalf of:", "signed on behalf of the:", 'commencement date', "the parties hereto have caused this", "last party to subscribe below"]

    # Keywords for SOW
    sow = ['(the "statement of work")','made and entered', 'sow effective date', 'sow effective', '"effective date"', 'effective as of', '(the "effective date")',
                'effective', 'is effective from', 'this', 'dated', 'for acknowledgement and acceptance', "signed:", 'agreed and accepted by grantee:',
                "provider and google hereby agree to this agreement", "in witness whereof", "signed by the parties",
                "agreed and accepted",
                'accepted and agreed', "supplier:", 'accepted on', 'sincerely', "kindly regards", "very truly yours",
                "agreed by the parties using echosign on the dates stated below",
                "agreed by the parties on the dates stated below", "title:", "title", "last party to subscribe below",
                "prepared by:", "on behalf of:", "signed on behalf of the:", 'commencement date', "the parties hereto have caused this"
                ]

    # Keywords for Letter
    letter = ['"effective date"', 'effective as of', '(the "effective date")', 'effective date', 'effective', 'dear', 'attn:',
              'sent via', ' re:','for acknowledgement and acceptance', "signed:", 'agreed and accepted by grantee:',
              "provider and google hereby agree to this agreement", "in witness whereof", "signed by the parties",
              "agreed and accepted",
              'accepted and agreed', "supplier:", 'accepted on', 'sincerely', "kindly regards", "very truly yours",
              "agreed by the parties using echosign on the dates stated below",
              "agreed by the parties on the dates stated below", "title:", "title",
              "prepared by:", "on behalf of:", "signed on behalf of the:", "customer signature",'commencement date',
              "the parties hereto have caused this", "last party to subscribe below"
              ]

    # Keywords for Order Form
    orderForm = ["order form effective date", 'made and entered',"order effective date:", "effective date of order", "order effective", '"edo"',
                 '"effective date"', 'effective as of', '(the "effective date")', 'effective date', 'effective', 'this',
                 'for acknowledgement and acceptance', "signed:", 'agreed and accepted by grantee:',
                  "provider and google hereby agree to this agreement", "in witness whereof", "signed by the parties",
                  "agreed and accepted",
                  'accepted and agreed', "supplier:", 'accepted on', 'sincerely', "kindly regards", "very truly yours",
                  "agreed by the parties using echosign on the dates stated below",
                  "agreed by the parties on the dates stated below", "title:", "title",
                  "prepared by:", "on behalf of:", "signed on behalf of the:", "customer signature",'commencement date', "customer signature", "last party to subscribe below"]

    # Keywords for Agreement
    agreement = ['"effective date"', 'made and entered','effective as of', '(the "effective date")', 'effective date', 'effective', '(hereinafter the "effective date")',
                 'entered into as of ', 'entered into', 'made as of', 'made into', 'made on', 'commencement date','(the "agreement")',
                 'this agreement','this', 'is effective from', 'agreement dated', 'dated', 'for acknowledgement and acceptance', "signed:", 'agreed and accepted by grantee:',
                  "provider and google hereby agree to this agreement", "in witness whereof", "signed by the parties",
                  "agreed and accepted", 'accepted and agreed', "supplier:", 'accepted on', 'sincerely', "kindly regards", "very truly yours",
                  "agreed by the parties using echosign on the dates stated below", "agreed by the parties on the dates stated below", "title:", "title",
                  "prepared by:", "on behalf of:", "signed on behalf of the:", "customer signature",'commencement date', "customer signature", "last party to subscribe below"]

    # Keywords for Quotes
    quotes = ['"effective date"','made and entered', 'effective as of', '(the "effective date")', 'effective date', 'effective', '(hereinafter the "effective date")',
                 'entered into as of ', 'entered into', 'made as of', 'made into', 'made on', 'commencement date', " ref:", "last party to subscribe below"]


    # File which contains listing of files on which code has to run.
    f = open("D:\MainData/remainingbatch.csv","r+",errors="ignore")
    reader = csv.DictReader(f)

    count = 0
    for row in reader:
        try:
            # Opening single file for editing and detecting language
            file1 = open(row["File Name"], 'r+',errors="ignore")
            type = str(row["Type"]).lower()
            str2 = file1.read()
            text=str2.split()
            content = ' '.join(str(e) for e in text)
            lowredContent = content.lower()
            filename=strip_non_ascii(row["File Name"])
            # print("THIS IS LOWERED CONTENT",lowredContent)
            count = count + 1
            if "this legal contract" in lowredContent:
                ind = lowredContent.index("this legal contract")
                newContent = content[ind+80:]
                newLowredContent = newContent.lower()
                if "this legal contract" in newLowredContent:
                    ind = newLowredContent.index("this legal contract")
                    newContent1 = newContent[ind + 80:]
                    newLowredContent1 = newContent1.lower()

                    if "if contract is already approved or signed" in newLowredContent1:
                        ind = newLowredContent1.index("if contract is already approved or signed")
                        newContent2 = newContent1[ind + 100:]
                        str1 = newContent2.lower()
                    else:
                        str1 = newContent1.lower()

                elif "if contract is already approved or signed" in newLowredContent:
                    ind = newLowredContent.index("if contract is already approved or signed")
                    newContent1 = newContent[ind + 100:]
                    newLowredContent1 = newContent1.lower()

                    if "if contract is already approved or signed" in newLowredContent1:
                        ind = newLowredContent.index("if contract is already approved or signed")
                        newContent2 = newContent1[ind + 100:]
                        newLowredContent2 = newContent1.lower()

                        if "this legal contract" in newLowredContent2:
                            ind = newLowredContent2.index("this legal contract")
                            newContent3 = newContent2[ind + 100:]
                            str1 = newContent3.lower()

                        else:
                            str1 = newContent1.lower()
                    else:
                        str1 = newContent1.lower()

                else:
                    str1 = newContent.lower()

            elif "if contract is already approved or signed" in lowredContent:
                ind = lowredContent.index("if contract is already approved or signed")
                newContent = content[ind+80:]
                newLowredContent = newContent.lower()
                if "if contract is already approved or signed" in newLowredContent:
                    ind = newLowredContent.index("this legal contract")
                    newContent1 = newContent[ind + 80:]
                    newLowredContent1 = newContent1.lower()

                    if "this legal contract" in newLowredContent1:
                        ind = newLowredContent1.index("if contract is already approved or signed")
                        newContent2 = newContent1[ind + 100:]
                        str1 = newContent2.lower()

                    else:
                        str1 = newContent1.lower()

                elif "this legal contract" in newLowredContent:
                    ind = newLowredContent.index("this legal contract")
                    newContent1 = newContent[ind + 100:]
                    newLowredContent1 = newContent1.lower()

                    if "this legal contract" in newLowredContent1:
                        ind = newLowredContent.index("this legal contract")
                        newContent2 = newContent1[ind + 100:]
                        newLowredContent2 = newContent1.lower()

                        if "if contract is already approved or signed" in newLowredContent2:
                            ind = newLowredContent2.index("this legal contract")
                            newContent3 = newContent2[ind + 100:]
                            str1 = newContent3.lower()

                        else:
                            str1 = newContent1.lower()
                    else:
                        str1 = newContent1.lower()

                else:
                    str1 = newContent.lower()

            else:
                str1 = content.lower()

            # For changing path

            if type == "amendment":

                    result = processing(amendment, str1, content, lowredContent)

            elif type == "addendum":

                    result = processing(addendum, str1, content, lowredContent)

            elif type == "sow":

                    result = processing(sow, str1, content, lowredContent)

            elif type == "order form":
                    result = processing(orderForm, str1, content, lowredContent)

            elif type == "letter":
                    if "dear" in str1:
                        newString = str1[:2000]

                        result = processing(letter, newString, content, lowredContent)

                    elif " re:" in str1:
                        result = processing(letter, newString, content, lowredContent)

                    else:
                        result = processing(letter, str1, content, lowredContent)

            elif (type == "agreement") or (type == "nda"):

                    result = processing(agreement, str1, content, lowredContent)

            elif "quot" in type:

                    result = processing(quotes, str1, content, lowredContent)

            else:
                    result = processing(lis, str1, content, lowredContent)

            dateString = result[0]
            date = result[1]
            edOption = result[2]

            lastDate = last_sign_date(lowredContent)
            dateString1 = lastDate[0]
            date1 = lastDate[1]

            w.writerow([row["File Name"], filename,dateString, date, edOption, dateString1, date1])

            file1.close()

            print("Scanned :" + str(count) + "\tFile Name: " + row["File Name"])

        except:
            w1.writerow([row["File Name"]])

# ===========================================================================================#

def main():
    ORFile()

if __name__ == '__main__':
    main()
