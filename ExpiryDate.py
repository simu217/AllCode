#---------------------------------------------------#
# AUTHOR: Simarjit Kaur                             #
# CODE:   ExpiryDatePartners                        #
#---------------------------------------------------#

import os
import csv
import re
import datetime



from EffectiveDateTypeTrial import *

def strip_non_ascii(string):
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)

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

def findDate(date2):
    list1=[]
    if ("renew" or "renewal")  in date2:
        str3 = re.search(r'(.*)(renew|renewal)', date2, re.I | re.M)
        var1=str3.group()
        FindOption=re.findall('((\(([\d\d?)]+)\)|\d\d?|1st|first|third|fourth|second|2nd|3rd|4rth|5th|fifth|one|two|three|four|five|sixt?h?|sevent?h''?|eighth?|ninet?h?|tent?h?|elevent?h?|twelvet?h?|thirteent?h?|fourteent?h?|'
                              'fifteent?h?|sixteent?h?|seventeent?h?|eighteent?h?|nineteent?h?|twenty|twentieth'
                              '|twelfth)\s?(-?(calendar)?\s?months?(\s?anniversary)?|-?(calendar)?\s?years?(\s?anniversary)?|(calendar)?\s?weeks?|-?(calendar)?\s?months?|-?(calendar)?\s?days?|-?(calendar)?\s?anniversary)|'
                    '(\d\d?(?:(st|nd|rd|th))?\s?,?\s?-?(january|february|mar|march|april|apr|may|june|jun|jul|july|august|october|november|september|december|jan|feb|aug|sept|sep|oct|nov|dec)-?,?\s?\d{2}\d?\d?)|'
                    '(\d?\d?\d{2}\s?,?\s?-?(january|february|mar|march|jun|jul|sep|april|apr|may|june|july|august|october|november|september|december|jan|feb|aug|sept|oct|nov|dec)-?,?\s?\d\d?(?:(st|nd|rd|th))?)|'
                 '((january|february|mar|march|april|apr|may|june|jun|jul|sep|july|august|october|november|september|december|jan|feb|aug|sept|oct|nov|dec)\s?-?,?\s?\d\d?(?:(st|nd|rd|th))?\s?,?-?\s?,?\s?\d{2}\d?\d?)|'
                   '(\d\d?[.\/-]\d\d?[.\/-]\d{4})|(\d{4}[.\/-]\d\d?[.\/-]\d{2})|(\d{2}[.\/-]\d\d?[.\/-]\d\d?))',
                              var1,re.I | re.M)

    else:
        FindOption=re.findall('((\(([\d\d?)]+)\)|\d\d?|1st|first|third|fourth|second|2nd|3rd|4rth|5th|fifth|one|two|three|four|five|sixt?h?|sevent?h''?|eighth?|ninet?h?|tent?h?|elevent?h?|twelvet?h?|thirteent?h?|fourteent?h?|'
                              'fifteent?h?|sixteent?h?|seventeent?h?|eighteent?h?|nineteent?h?|twenty|twentieth'
                              '|twelfth)\s?(-?(calendar)?\s?months?(\s?anniversary)?|-?(calendar)?\s?years?(\s?anniversary)?|(calendar)?\s?weeks?|-?(calendar)?\s?months?|-?(calendar)?\s?days?|-?(calendar)?\s?anniversary)|'
                    '(\d\d?(?:(st|nd|rd|th))?\s?,?\s?-?(january|february|mar|march|april|apr|may|june|jun|jul|july|august|october|november|september|december|jan|feb|aug|sept|sep|oct|nov|dec)-?,?\s?\d{2}\d?\d?)|'
                    '(\d?\d?\d{2}\s?,?\s?-?(january|february|mar|march|jun|jul|sep|april|apr|may|june|july|august|october|november|september|december|jan|feb|aug|sept|oct|nov|dec)-?,?\s?\d\d?(?:(st|nd|rd|th))?)|'
                 '((january|february|mar|march|april|apr|may|june|jun|jul|sep|july|august|october|november|september|december|jan|feb|aug|sept|oct|nov|dec)\s?-?,?\s?\d\d?(?:(st|nd|rd|th))?\s?,?-?\s?,?\s?\d{2}\d?\d?)|'
                   '(\d\d?[.\/-]\d\d?[.\/-]\d{4})|(\d{4}[.\/-]\d\d?[.\/-]\d{2})|(\d{2}[.\/-]\d\d?[.\/-]\d\d?))',
                              date2, re.I | re.M)
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

def extractExpiryDate():
    PathForCSV = "D:\MainData\csv files\FLIR 11.1\FLIR Phase 8 TXT/FLIR_P8_Territory.csv"
    MainPathtext = "D:\MainData\FLIR Phase 8 TXT"
    ReadingCSV= open(PathForCSV, 'w+', encoding="utf8",errors="ignore",newline="")
    WritingCSV = csv.writer(ReadingCSV, quoting=csv.QUOTE_ALL, delimiter=',')
    WritingCSV.writerow([ "Txt Path & File Name", "file name",'Output_String', 'Keywords', 'Expiry Date'])
    count = 0
# Walking through the directories
    for root, dir, files in os.walk(MainPathtext):
    #Fetching a single file\
        for singFile in files:
     #Getting only text files
            if ".txt" in singFile:
                newPath = os.path.join(root, singFile)
                count = count + 1
                count1 = str(count)
                filename=strip_non_ascii(newPath)
            # Opening single file for editing and detecting language
                file1 = open(newPath, 'r+',encoding="utf8",errors="ignore")
                content = file1.read()
                text = content.split()
                str1 = ' '.join(str(e) for e in text)
                str2 = strip_non_ascii(str1)
                # keywords = ['([“"”]initial term[”"“]((.*?).{200}))',
                #                 '(term[,;] termination.?((.*?).{300}))',
                #                 '([“"”]term[”"“] means?((.*?).{200}))',
                #                 '((\d?\d.?,?\d?.\s?)\s?term and termination((.*?).{250}))',
                #                 '(term[:.-]\s?((.*?).{300}))'
                #                 '((\d?\d.?,?\d?.\s?)\s?terms of agreement\s?-?;?:?((.*?).{250}))',
                #                 '(initial term\s?:\s?((.*?).{200}))',
                #                 '((\d?\d.?,?\d?.\s?)\s?term\s?;?:?-?((.*?).{250}))',
                #                 '((\d?\d.?,?\d?.\s?)\s?program period((.*?).{250}))',
                #                 '(company hereby extend the term of the de contracts through((.*?).{150}))',
                #                 '(agreement (shall|will) begin on the effective date and (end on|expire)((.*?).{200}))',
                #                 '(current term length (in whole months) for renewed services((.*?).{150}))',
                #                 '(current term length (in whole months) for additional purchased units((.*?).{150}))',
                #                 '(shall become effective from the last date of signature for a period of((.*?).{500}))',
                #                 '(orderterm/auftragdauer((.*?).{200}))',
                #                 '(date of substantial completion((.*?).{200}))',
                #                 '(initial purchase period is extended and continue((.*?).{200}))',
                #                 '(the agreement is terminated((.*?).{300}))',
                #                 '(order term\s?:((.*?).{200}))',
                #                 '(\(([“quotation”)]+)\) is valid for((.*?).{100}))',
                #                 '(quote expire((.*?).{150}))',
                #                 '(the following words in the term section on page 1 shall be deleted((.*?).{150}))',
                #                 '(order form is hereby amended to be in effect through((.*?).{200}))',
                #                 '(with respect to the period commencing ((.*?).{200}))',
                #                 '(the term of the dcb master agreement, and the term of each dcb accession agreement,? is extended to((.*?).{150}))',
                #                 '(term of this cross connect order form\s?:\s?((.*?).{200}))',
                #                 '(term:\s?from the order form effective date((.*?).{200}))',
                #                 '(the term of the agreement shall commence on the effective date and continue until((.*?).{300}))',
                #                 '(the period from the effective date until((.*?).{200}))',
                #                 '(initial term of this agreement will be((.*?).{150}))',
                #                 '(this order form is subject to and incorporates by reference the terms and conditions of the google apps for enterprise agreement((.*?).{200}))',
                #                 '(agreement shall expire(.*?).{200})',
                #                 '(effect from through((.*?).{150}))',
                #                 '(the term of this agreement shall be for((.*?).{200}))',
                #                 '(above mentioned effective date and expire((.*?).{200}))',
                #                 '(but for a period not to exceed((.*?).{200}))',
                #                 '(duration of the ambulant care services is extended until((.*?).{300}))',
                #                 '(company’s disclosure of the confidential information to each other((.*?).{200}))',
                #                 '(products and support services\s?:((.*?).{200}))',
                #                 '(the end date of the agreement((.*?).{200}))',
                #                 '(valid only through((.*?).{150}))',
                #                 '(from the effective date to((.*?).{200}))',
                #                 '(term commencing on the date of this agreement((.*?).{200}))',
                #                 '(continue in full force for((.*?).{200}))',
                #                 '(effective during a period of((.*?).{200}))',
                #                 '(remain in effect for((.*?).{200}))',
                #                 '(survive and continue for((.*?).{200}))',
                #                 '(continue for the later of((.*?).{200}))',
                #                 "(automatically terminate((.*?).{100}))",
                #                 '(new termination date((.*?).{200}))',
                #                 '(term of this order form((.*?).{200}))',
                #                 '(extended so that it expires on((.*?).{200}))',
                #                 '(effective date and continuing through((.*?).{200}))',
                #                 '((\d?\d{1}[.]?\d?)\s?extending the term(.*?).{200})',
                #                 '(this agreement will commence on the effective date and will continue((.*?).{200}))',
                #                 "((?:will|shall) (?:end|expire) on((.*?).{200}))",
                #                 "((?:will|shall) (?:end|expire) upon the ((.*?).{200}))",
                #                 '(and end upon the completion of((.*?).{200}))',
                #                 '(the effective date and will continue until((.*?).{300}))',
                #                 '(extended through((.*?).{200}))',
                #                 '((?:authorization|this agreement)(?: will| shall) remain in (effect until|effective)((.*?).{300}))',
                #                 '((the term of )?the agreement is (hereby )?extended((.*?).{200}))',
                #                 '(are hereby extended for a period of((.*?).{300}))',
                #                 '(effective date of termination of the service((.*?).{200}))',
                #                 '(term\s?:\s?starting on ((.*?).{200}))',
                #                 '([“"”]term[“"”] a period of((.*?).{200}))',
                #                 '(the renewed services shall be renewed pursuant((.*?).{200}))',
                #                 "((?:shall|will) terminate((.*?).{300}))",
                #                 '(and expiring( on)?((.*?).{300}))',
                #                 '(term will begin on the effective date and continue for((.*?).{300}))',
                #                 '(will expire pursuant to its terms on((.*?).{200}))',
                #                 '(agreed? to extend the term ((.*?).{200}))',
                #                 '(term duration in months((.*?).{150}))',
                #                 '(to take effect at the end of((.*?).{300}))',
                #                 '(shall continue until the expiration of the((.*?).{300}))',
                #                 '(completion date of services:((.*?).{300}))',
                #                 '(order is due to be completed on((.*?).{300}))',
                #                 '(the term of this service order will be((.*?).{300}))',
                #                 '(initial order term length committed((.*?).{300}))',
                #                 "(services shall terminate((.*?).{200}))",
                #                 '(term \(([in months)]+)\)((.*?).{150}))',
                #                 '(close date\s?:(.*?).{200})',
                #                 "(chromebook\s?[:;-]((.*?).{100}))",
                #                 '(initial services? term\s?[-;:]((.*?).{300}))',
                #                 '(am term[-;:]((.*?).{200}))',
                #                 '(dfp term[-;:]((.*?).{200}))',
                #                 '(dart adapt term[-;:]((.*?).{200}))',
                #                 '(special term[-;:]((.*?).{200}))',
                #                 '(services? term[:;-]((.*?).{300}))',
                #                 '(updated term[:;-]((.*?).{300}))',
                #                 '(expiration date[:;-]((.*?).{200}))',
                #                 '(promotion period\s?[:;-](.*?).{200})',
                #                 '(contract period\s?[:;-](.*?).{200})',
                #                 '(contract terms?\s?[:;-](.*?).{300})',
                #                 '(service term\s?\(([months)]+)\):((.*?).{300}))',
                #                 '(minimum\s?term\s?\(([months)]+)\)((.*?).{300}))',
                #                 '(initial agreement period \(([in months)]+)\)((.*?).{200}))',
                #                 '(campaign end date:((.*?).{200}))',
                #                 "((commencing from( the)? Effective Date|begins? from( the)? effective date| commences? from( the)? effective date)((.*?).{50}))",
                #                 '((\d?\d{1}.?,?\d?\s?.)\s?extension(.*?).{250})',
                #                 "(and concluding on ((.*?).{100}))",
                #                 "(valid until((.*?).{100}))",
                #                 '(circuit term length((.*?).{150}))',
                #                 '(contract term in months((.*?).{150}))',
                #                 "(current services? term((.*?).{300}))",
                #                 "(expire on(.*?).{200})",
                #                 '(sow end date((.*?).{300}))',
                #                 '(contract minimum service term(.*?).{200})',
                #                 '(end date((.*?).{100}))',
                #                 '(term of sow ((.*?).{300}))',
                #                 '(licen(?:c|s)e term((.*?).{500}))',
                #                 "(support period(.*?).{300})",
                #                 '(minimum contract term((.*?).{300}))',
                #                 '(term commitment((.*?).{300}))',
                #                 '(support term date((.*?).{300}))',
                #                 '(initial contract term((.*?).{300}))',
                #                 '(initial lease term((.*?).{300}))',
                #                 '(min.? contract period(.*?).{200})',
                #                 '(service type contract period((.*?).{300}))',
                #                 '(term of contract((.*?).{300}))'
                #                 ]
                # keywords = ['([“”"]initial term[”“"]((.*?).{200}))',"([']expiration date((.*?).{10}))","(and ending((.*?).{40}))","(Due Date((.*?).{40}))"
                #     , "(This agreement cannot be terminated((.*?).{10}))"
                #     , "(^(payment) Terms:((.*?).{100}))",
                #             '((\d?\d.?,?\d?.\s?)\s?term and termination((.*?).{250}))',
                #             '(valid until((.*?).{100}))',
                # '(and will remain in effect until(.*?).{100})',
                # '(Agreement will expire(.*?).{100})',
                # '(expires on(.*?).{100})']
                # keywords = ['((\d?\d.?,?\d?[.]\s?)\s?Indemnification((.*?).{2000}))']
                keywords = [
                    # 'place of business at(.*?)(place of business at(.*?).{250})',
                    # 'located at(.*?)(located at(.*?).{350})'
                            '(Territory:(.*?).{550})','(Territory(.*?).{350})'
                            ]
                date,date1,date2,foundOptions,dateObj='',"","","",""
                for i in keywords:
                    dateObj = re.search(i, str2, re.I | re.M)
                    if dateObj:
                        date1 = dateObj.group()
                        index = str2.index(date1)
                        date3=str2[index-40:index]
                        date2=date3+date1
                        date = i
                        foundOptions = findDate(date2)
                        break
                    else:
                        date2 = "No Match"
                        date = "No Match"
                        foundOptions = "No Match"
                WritingCSV.writerow([newPath, singFile,date2,foundOptions, date ])
                print( count1, singFile)

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

    return String,date

#===============================================================================================#

def remainingBatch():
    PathForCSV = 'D:\MainData\csv files\Elevate Contract Extraction_Internal\Acceptance_Criteria.csv'
    RemainingfilesList='D:\MainData/remainingbatch.csv'
    RemainingFiles = open(RemainingfilesList, 'r+', encoding="utf8", errors="ignore")
    reading = csv.reader(RemainingFiles)
    ReadingCSV = open(PathForCSV, 'w+', encoding="utf8",errors="ignore", newline="")
    WritingCSV = csv.writer(ReadingCSV, quoting=csv.QUOTE_ALL, delimiter=',')
    WritingCSV.writerow(['Path & File Name','Output String','effective',"keyword"])
    count = 0
    for row in reading:
        try:
            print(row[0])
            file1 = open(row[0], 'r+', encoding="utf8",errors="ignore")
            count=count+1
            content = file1.read()
            text = content.split()
            str1= ' '.join(str(e) for e in text)
            str2 = strip_non_ascii(str1)
            did=""
            date, date2, foundOptions, dateObj = '', "", "", ""
            keywords = ['((\d?\d.?,?\d?.\s?)\s?Acceptance Criteria(.*?).{1000})']
            date, date1, foundOptions, dateObj,foundOptions = '','', "", "", ""
            for i in keywords:
                dateObj = re.search(i, str2, re.I | re.M)
                if dateObj:
                    date2 = dateObj.group(1)
                    index = str2.index(date2)
                    date3 = str2[index - 0:index]
                    date1 =date3+" "+date2
                    foundOptions = findDate(date1)
                    date = i
                    break
            WritingCSV.writerow([row[0],date1,foundOptions,date])
            # WritingCSV.writerow([row[0],str3])
            print(count, " files scanned !")
        except:
            pass

def main():
    extractExpiryDate()
    # remainingBatch()
    print("Execution completed !..")

if __name__ == '__main__':
    main()
