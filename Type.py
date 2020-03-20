#---------------------------------------------------#
# AUTHOR: SIMARJIT KAUR                             #
# CODE:   TitlePartners                             #
# WORK:   We are extracting titles from GOOGLE Docs #
#---------------------------------------------------#
import os
import sys
import csv
import re
import time
# from tqdm import tqdm
def extractType(text, title): #text= lower string, title= normal striong
    dateObj,titleType="",[]
    if ((" dear" in text) or (" re:" in text)or (" re :" in text) or (" subject:" in text) or (" sub:" in text) or (
            "fw:" in text)  or (" ref:" in text) or (" regarding:" in text) or (" attn:" in text
    ) or (" attention:" in text) or (" subject :" in text) or (" sub :" in text) or (
            "fw :" in text)  or ("ref :" in text) or ("regarding :" in text) or ("attn :" in text) or (" attention :" in text)or (" letter " in text)):
        print("inside dear" , "---" , title)
        OrderFormList = {'AMENDMENT/ADDENDUM': '((amendment\s?(and|/|\|&)?\s?addendum)(.*?).{50}|(addendum\s?(and|/|\|&)?\s?amendment(.*?).{50}))',
                            'AMENDMENT ': '((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?amendment(.*?)(to)(.*?)addendum(.*?).{60})',
                            'ADDENDUM ': '((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?addendum(.*?)(to)(.*?)amendment(.*?).{60})',
                            'AMENDMENT': '((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?amendment(.*?).{60})',
                            'ADDENDUM': '((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?addendum(.*?).{60})',
            "AGREEMENT": '(letter agreement(.*?).{50})',
            "LETTER":'( re\s?:(.*?).{70}|subject\s?:(.*?).{70}|sub\s?:(.*?).{70}|fw\s?:(.*?).{70}|fwd\s?:(.*?).{70}|ref\s?:(.*?).{70}|regarding\s:(.*?).{70}'
                          '|attn:(.*?).{70}|letter (of )?agreement(.*?).{20}|(.*?)letter of intent|(.*?)letter(.*?).{10})',
            "TERMINATION": '(dear(.*?)termination(.*?).{30})',
            "LETTER ": '(dear(.*?).{50})'
            }
        for key, value in OrderFormList.items():
            dateObj = re.search(value, title, re.I | re.M)
            if dateObj:
                titleType.append(dateObj.group())
                titleType.append(key)
                break
        if not dateObj:
            titleType.append(title)
            titleType.append("LETTER")
        return titleType

    elif (("disclosure agreement" in text) or ("confidentiality agreement" in text) or (" nda " in text) ):
        print("inside nda" , "---" , title)
        text1 = (re.search('((.*?)(agreement| nda )(.*?))', title, re.I | re.M)).group()
        print(text1)
        if text1:
            OrderFormList = {'AMENDMENT/ADDENDUM': '((amendment\s?(and|/|\|&)?\s?addendum)(.*?).{50}|(addendum\s?(and|/|\|&)?\s?amendment(.*?).{50}))',
                            'AMENDMENT ': '((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?amendment(.*?)(to)(.*?)addendum('
                                          '.*?).{60})',
                            'ADDENDUM ': '((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?addendum(.*?)(to)(.*?)amendment('
                                         '.*?).{60})',
                            'AMENDMENT': '((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?amendment(.*?).{60})',
                            'ADDENDUM': '((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?addendum(.*?).{10})',
                            'REVOCATION': '(revocation(.*)to(.*?).{60})',
                            'NOTICE': "((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?notice( of| to)(.*?).{60})",
                            'SCHEDULE': "(schedule(.*?).{60})",
                            'RATIFICATION, EXTENSION, AND AMENDMENT ': "(RATIFICATION, EXTENSION,? AND AMENDMENT(.*?).{60})"}
            for key, value in OrderFormList.items():
                dateObj = re.search(value, text1, re.I | re.M)
                if dateObj:
                    titleType.append(dateObj.group())
                    titleType.append(key)
                    break
            if not dateObj:
                titleType.append(text1)
                titleType.append("NDA")
            return titleType

    elif "agreement" in text:
        print("inside agreement" , "---" , title)
        OrderFormList = {
            'AMENDMENT/ADDENDUM': '((amendment\s?(and|/|\|&)?\s?addendum)(.*?).{50}|(addendum\s?(and|/|\|&)?\s?amendment(.*?).{50}))',
            'AMENDMENT ': '((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?amendment(.*?)(to)(.*?)addendum('
                          '.*?).{60})',
            'ADDENDUM ': '((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?addendum(.*?)(to)(.*?)amendment('
                         '.*?).{60})',
            'AMENDMENT': '((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?amendment(.*?).{60})',
            'ADDENDUM': '((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?addendum(.*?).{60})',
            "ORDER FORM": "((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?order form(.*?).{20})",
            "ORDER": "((.*?)order agreement(.*?).{10}|(.*?)order(.*)(to|of|for)("
                     ".*?).{10}|(.*?)order(.*?).{10}|(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?change order(.*?).{60})",
            "PERMISSION": "(permission(.*?).{50}|permission(.*)to(.*?).{50})",
            'RELEASE': '((.*?)release agreement(.*?).{30})',
            'RATIFICATION, EXTENSION AND AMENDMENT ': "(RATIFICATION, EXTENSION,? AND AMENDMENT(.*?).{60})",
            'RATIFICATION': '(ratification(.*?).{60})',
            'SOW': '((.*?)statement of work(.*?).{20})',
            'FORM': '((.*?) form (.*?).{20}|(.*?) agreement form (.*?).{10})',
            "CONSENT": "(consent to(.*?).{10})",
            "APPENDIX": "((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?appendix(.*)to(.*?).{50})",
            "ASSIGNMENT/ASSUMPTION": "(assignment\s?(and|/|\|&)?\s?assumption(.*?).{40})",
            "ASSIGNMENT/CONSENT": "(assignment\s?[and|/|&|of]\s?consent(.*?).{40})",
            "ATTACHMENT": "((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?attachment( of| to)(.*?).{60})",
            "AGREEMENT": "((.*?)contract (.*?) agreement)",
            "DEED": "((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?deed (.*)of(.*?).{10})",
            "EXTENSION": "((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?extension(.*?).{60})",
            "TERMINATION": "(termination of(.*?).{60})",
            "SUPPLEMENT": "((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?supplement(.*?).{60})",
            "SCHEDULE": "((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?schedule(.*?).{60})",
            "NOTICE": "(notice of(.*?).{60})",
            "EXHIBIT": "((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?exhibit to(.*?).{60})",
            'TERMS AND CONDITIONS': "((.*?)terms and conditions(.*?).{20})",
            'TEMPLATE': "((.*?)template)"
            }
        for key, value in OrderFormList.items():
            dateObj = re.search(value, title, re.I | re.M)
            if dateObj:
                titleType.append(dateObj.group())
                titleType.append(key)
                break
        if not dateObj:
            text1=re.search(r'((.*?)agreement)', title, re.I | re.M)
            if text1:
                titleType.append(text1.group())
                titleType.append("AGREEMENT")
            else:
                titleType.append(title)
                titleType.append("AGREEMENT")
        return titleType

    elif "order form" in text:
        print("inside orderform", "---" , title)
        text1 = (re.search('((.*?)order form((.){10})?)', title, re.I | re.M)).group()

        if text1:

            OrderFormList = {'AMENDMENT/ADDENDUM': '((amendment\s?(and|/|\|&)?\s?addendum)(.*?).{50}|(addendum\s?(and|/|\|&)?\s?amendment(.*?).{50}))',
                                'AMENDMENT ': '((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?amendment(.*?)(to)(.*?)addendum('
                                              '.*?).{60})',
                                'ADDENDUM ': '((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?addendum(.*?)(to)(.*?)amendment('
                                             '.*?).{60})',
                                'AMENDMENT': '((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?amendment(.*?).{60})',
                                'ADDENDUM': '((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?addendum(.*?).{60})',
                                "ORDER": "(order agreement(.*?).{60}|order(.*)(to|of|for)(.*?).{60}|change order(.*)to(.*?).{60}|order(.*?).{60})",
                                'CONSENT': "(consent( of| to)(.*?) assignment(.*?).{60})",
                                'ASSIGNMENT ': "(assignment( of| to)(.*?).{60})",
                             'RATIFICATION, EXTENSION, AND AMENDMENT ': "(RATIFICATION, EXTENSION,? AND AMENDMENT(.*?).{60})",
                                'RATIFICATION': '(ratification(.*?).{60})',
                                 'SOW': '((.*?)statement of work(.*?).{20})',
                                'FORM': '((.*?) form (.*?).{20}|(.*?) agreement form (.*?).{10})',
                                "CONSENT ": "(consent (.*)to(.*?).{10})",
                                "APPENDIX": "((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?appendix(.*)to(.*?).{50})",
                                "ASSIGNMENT/ASSUMPTION": "((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?assignment\s?(and|/|\|&)?\s?assumption(.*?).{40})",
                                "ASSIGNMENT/CONSENT": "((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?assignment\s?("
                                                "and|/|\|&)?\s?consent(.*?).{40})",
                                "ATTACHMENT": "((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?attachment( of| to)(.*?).{60})",
                                "DEED": "((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?deed (.*)of(.*?).{10})",
                                "EXTENSION": "((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?extension(.*?).{60})",
                                "TERMINATION": "(termination of(.*?).{60})",
                                "SUPPLEMENT": "((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?supplement(.*?).{60})",
                                "SCHEDULE": "((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?schedule(.*?).{60})",
                                "NOTICE": "(notice of(.*?).{60})",
                                "EXHIBIT": "((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?exhibit(.*)to(.*?).{60})",
                                'TERMS AND CONDITIONS': "((.*?)terms and conditions(.*?).{20})",
                                'TEMPLATE': "((.*?)template)"
                             }
            for key, value in OrderFormList.items():
                dateObj = re.search(value, text1, re.I | re.M)
                if dateObj:
                    titleType.append(dateObj.group())
                    titleType.append(key)
                    break
            if not dateObj:
                titleType.append(text1)
                titleType.append("ORDER FORM")
            return titleType

    elif (("scope of work" in text) or ( "statement of work" in text)):
        print("inside sow", "---" , title)
        text1 = (re.search('((.*?)(statement|scope) of work((.){25})?)', title, re.I | re.M)).group()

        if text1:

            OrderFormList = {   'AMENDMENT/ADDENDUM': '((amendment\s?(and|/|\|&)?\s?addendum)(.*?).{50}|(addendum\s?(and|/|\|&)?\s?amendment(.*?).{50}))',
                                'AMENDMENT ': '((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?amendment(.*?)(to)(.*?)addendum('
                                              '.*?).{60})',
                                'ADDENDUM ': '((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?addendum(.*?)(to)(.*?)amendment('
                                             '.*?).{60})',
                                'AMENDMENT': '((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?amendment(.*?).{50})',
                                'ADDENDUM': '((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?addendum(.*?).{60})',
                                "ORDER": "(order agreement(.*?).{60}|order(.*)(to|of|for)(.*?).{60}|change order(.*)to(.*?).{60}|order(.*?).{60})",
                                'REQUEST':"((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?request (.*?).{30})",
                                "TERMINATION": "(termination of(.*?).{60})",
                                'RATIFICATION, EXTENSION, AND AMENDMENT ': "(RATIFICATION, EXTENSION,? AND AMENDMENT(.*?).{60})",
                                 'RATIFICATION': '(ratification(.*?).{60})',
                                 "SCHEDULE": "((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?schedule(.*?).{60})",
                                 "NOTICE": "(notice of(.*?).{60})",
                                 "EXHIBIT": "((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?exhibit(.*)to(.*?).{60})",
                                 'TERMS AND CONDITIONS': "((.*?)terms and conditions(.*?).{20})"
                             }
            for key, value in OrderFormList.items():
                dateObj = re.search(value, text1, re.I | re.M)
                if dateObj:
                    titleType.append(dateObj.group())
                    titleType.append(key)
                    break
            if not dateObj:
                titleType.append(text1)
                titleType.append("SOW")
            return titleType

    elif " order" in text:
        print("inside order", "---" , title)
        text1 = (re.search('((.*?) order((.){15})?)', title, re.I | re.M)).group()

        if text1:

            OrderFormList = {'AMENDMENT/ADDENDUM': '((amendment\s?(and|/|\|&)?\s?addendum)(.*?).{50}|(addendum\s?(and|/|\|&)?\s?amendment(.*?).{50}))',
                                'AMENDMENT ': '((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?amendment(.*?)(to)(.*?)addendum('
                                              '.*?).{60})',
                                'ADDENDUM ': '((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?addendum(.*?)(to)(.*?)amendment('
                                             '.*?).{60})',
                                'AMENDMENT': '((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?amendment(.*?).{60})',
                                'ADDENDUM': '((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?addendum(.*?).{60})',
                                'CONFIRMATION': "((.*?)confirmation(.*?).{15})",
                                'ATTACHMENT':"((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?attachment( of| to)(.*?).{60})",
                                'SCHEDULE':"((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?schedule(.*?).{60})",
                                'REQUEST':"((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?request (.*?).{30})"
                             }
            for key, value in OrderFormList.items():
                dateObj = re.search(value, text1, re.I | re.M)
                if dateObj:
                    titleType.append(dateObj.group())
                    titleType.append(key)
                    break
            if not dateObj:
                titleType.append(text1)
                titleType.append("ORDER")
            return titleType

    elif "confirmation" in text:
        print("inside confirmation", "---" , title)
        titleType.append(text)
        titleType.append("CONFIRMATION")
        return titleType

    elif "attachment" in text:
        print("inside attachment", "---" , title)
        text1 = (re.search('((.*?)attachment((.){16})?)', title, re.I | re.M)).group()

        if text1:

            OrderFormList = {'AMENDMENT/ADDENDUM': '((amendment\s?(and|/|\|&)?\s?addendum)(.*?).{50}|(addendum\s?(and|/|\|&)?\s?amendment(.*?).{50}))',
                                'AMENDMENT ': '((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?amendment(.*?)(to)(.*?)addendum('
                                              '.*?).{60})',
                                'ADDENDUM ': '((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?addendum(.*?)(to)(.*?)amendment('
                                             '.*?).{60})',
                                'AMENDMENT': '((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?amendment(.*?).{60})',
                                'ADDENDUM': '((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?addendum(.*?).{60})',
                                'SUPPLEMENT':"((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?supplement(.*?).{60})",
                                'TERMS AND CONDITIONS': "((.*?)terms and conditions(.*?).{20})"
                             }
            for key, value in OrderFormList.items():
                dateObj = re.search(value, text1, re.I | re.M)
                if dateObj:
                    titleType.append(dateObj.group())
                    titleType.append(key)
                    break
            if not dateObj:
                titleType.append(text1)
                titleType.append("ATTACHMENT")
            return titleType

    elif "addendum" in text:
        print("inside addendum", "---" , title)
        text1 = (re.search('((.*?)addendum((.){15})?)', title, re.I | re.M)).group()

        if text1:

            OrderFormList = {'AMENDMENT/ADDENDUM': '((amendment\s?(and|/|\|&)?\s?addendum)(.*?).{50}|(addendum\s?(and|/|\|&)?\s?amendment(.*?).{50}))',
                                'AMENDMENT ': '((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?amendment(.*?)(to)(.*?)addendum('
                                              '.*?).{60})',
                                'ADDENDUM ': '((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?addendum(.*?)(to)(.*?)amendment('
                                             '.*?).{60})',
                                'AMENDMENT': '((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?amendment(.*?).{60})',
                                'ADDENDUM': '((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?addendum(.*?).{60})',
                                 'REQUEST':"((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?request (.*?).{30})",
                                 "TERMINATION": "(termination of(.*?).{60})"
                             }
            for key, value in OrderFormList.items():
                dateObj = re.search(value, text1, re.I | re.M)
                if dateObj:
                    titleType.append(dateObj.group())
                    titleType.append(key)
                    break
            if not dateObj:
                titleType.append(text1)
                titleType.append("ADDENDUM")
            return titleType

    elif "amendment" in text:
        print("inside amendment", "---" , title)
        text1 = (re.search('((.*?)amendment((.){60})?)', title, re.I | re.M)).group()

        if text1:

            OrderFormList = {'AMENDMENT/ADDENDUM': '((amendment\s?(and|/|\|&)?\s?addendum)(.*?).{50}|(addendum\s?(and|/|\|&)?\s?amendment(.*?).{50}))',
                                'AMENDMENT ': '((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?amendment(.*?)(to)(.*?)addendum('
                                              '.*?).{60})',
                                'ADDENDUM ': '((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?addendum(.*?)(to)(.*?)amendment('
                                             '.*?).{60})',
                                'AMENDMENT': '((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?amendment(.*?).{60})',
                                'ADDENDUM': '((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?addendum(.*?).{60})'}
            for key, value in OrderFormList.items():
                dateObj = re.search(value, text1, re.I | re.M)
                if dateObj:
                    titleType.append(dateObj.group())
                    titleType.append(key)
                    break
            if not dateObj:
                titleType.append(text1)
                titleType.append("AMENDMENT")
            return titleType

    elif "release" in text:
        print("inside release", "---" , title)
        text1 = (re.search('((.*?)release((.*?).{15})?)', title, re.I | re.M)).group()

        if text1:
            OrderFormList = {'AMENDMENT': '((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?amendment(.*?).{60})',
                                "DEED": "((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?deed (.*)of(.*?).{10})",
                                'FORM': '((.*?)release form(.*?).{20})'
                             }

            for key, value in OrderFormList.items():
                dateObj = re.search(value, text1, re.I | re.M)
                if dateObj:
                    titleType.append(dateObj.group())
                    titleType.append(key)
                    break
            if not dateObj:
                titleType.append(text1)
                titleType.append("RELEASE")
            return titleType

    elif "contract " in text:
        print("inside contract", "---" , title)
        text1 = (re.search('((.*?)contract ((.){40})?)', title, re.I | re.M)).group()

        if text1:

            OrderFormList = {'AMENDMENT/ADDENDUM': '((amendment\s?(and|/|\|&)?\s?addendum)(.*?).{50}|(addendum\s?(and|/|\|&)?\s?amendment(.*?).{50}))',
                                'AMENDMENT ': '((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?amendment(.*?)(to)(.*?)addendum('
                                              '.*?).{60})',
                                'ADDENDUM ': '((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?addendum(.*?)(to)(.*?)amendment('
                                             '.*?).{60})',
                                'AMENDMENT': '((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?amendment(.*?).{60})',
                                'ADDENDUM': '((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?addendum(.*?).{60})',
                                 "REQUEST":"((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?request (.*?).{30})",
                                 "FORM":"(contract form(.*?).{30})",
                                'APPENDIX': "(appendix(.*?).{60})",
                                'ASSIGNMENT/ASSUMPTION': "((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?assignment\s?(and|/|\|&)?\s?assumption(.*?).{60})",
                                'ASSIGNMENT/CONSENT': "((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?assignment\s?(and|/|\|&)?\s?consent(.*?).{60})",
                                'CERTIFICATE': "(certificate of(.*?).{60})",
                                'NOTICE': "(notice(.*?).{60})",
                                'NOTIFICATION': "(notification(.*?).{60})",
                                'RESIGNATION AND TERMINATION ': "(resignation and termination(.*?).{60})",
                                "TERMINATION": "(termination of(.*?).{60})",
                                "EXHIBIT": "((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?exhibit(.*)to(.*?).{60})",
                                "SCHEDULE": "((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?schedule(.*?).{60})"
                             }
            for key, value in OrderFormList.items():
                dateObj = re.search(value, text1, re.I | re.M)
                if dateObj:
                    titleType.append(dateObj.group())
                    titleType.append(key)
                    break
            if not dateObj:
                titleType.append(text1)
                titleType.append("CONTRACT")
            return titleType

    elif " form " in text:
        print("inside form", "---" , title)
        text1 = (re.search('((.*?) form ((.){15})?)', title, re.I | re.M)).group()

        if text1:

            OrderFormList = {'AMENDMENT ': '((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?amendment(.*?)(to)(.*?)addendum('
                                              '.*?).{60})',
                                'ADDENDUM ': '((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?addendum(.*?)(to)(.*?)amendment('
                                             '.*?).{60})',
                                'AMENDMENT': '((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?amendment(.*?).{60})',
                                'ADDENDUM': '((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?addendum(.*?).{60})',
                                 'REQUEST':"((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?request (.*?).{30})",
                                'ATTACHMENT':"((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?attachment( of| to)(.*?).{60})",
                                'APPENDIX' :"(appendix(.*?).{60})"
                             }

            for key, value in OrderFormList.items():
                dateObj = re.search(value, text1, re.I | re.M)
                if dateObj:
                    titleType.append(dateObj.group())
                    titleType.append(key)
                    break
            if not dateObj:
                titleType.append(text1)
                titleType.append("FORM")
            return titleType

    elif "assignment" in text:
        print("inside assignment", "---" , title)
        text1 = (re.search('((.*?)assignment((.){40})?)', title, re.I | re.M)).group()
        OrderFormList = {'AMENDMENT ': '((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?amendment(.*?)(to)(.*?)addendum('
                                          '.*?).{60})',
                            'ADDENDUM ': '((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?addendum(.*?)(to)(.*?)amendment('
                                         '.*?).{60})',
                            'AMENDMENT': '((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?amendment(.*?).{60})',
                            'ADDENDUM': '((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?addendum(.*?).{60})',
                         'ASSIGNMENT/ASSUMPTION':"((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?assignment\s?(and|/|\|&)?\s?assumption(.*?).{60})",
                         'ASSIGNMENT/CONSENT':"((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?assignment\s?(and|/|\|&)?\s?consent(.*?).{60})",
                         'BILL':"((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?bill(.*?).{60})",
                         'CONSENT': "(consent( of| to)(.*?) assignment(.*?).{60})",
                                'ASSIGNMENT ': "(assignment( of| to)(.*?).{60})",
                                'CONSENT  ': "(consent( of| to)(.*?).{60})",
                         'NOTICE':"(notice(.*?).{60})"
                         }
        for key, value in OrderFormList.items():
            dateObj = re.search(value, text1, re.I | re.M)
            if dateObj:
                titleType.append(dateObj.group())
                titleType.append(key)
                break
        if not dateObj:
            titleType.append(text1)
            titleType.append("ASSIGNMENT")
        return titleType

    elif "termination" in text:
        print("inside termination", "---" , title)
        text1 = (re.search('((.*?)termination((.){15})?)', title, re.I | re.M)).group()
        OrderFormList = {'AMENDMENT ': '((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?amendment(.*?)(to)(.*?)addendum('
                                              '.*?).{60})',
                            'ADDENDUM ': '((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?addendum(.*?)(to)(.*?)amendment('
                                             '.*?).{60})',
                            'AMENDMENT': '((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?amendment(.*?).{60})',
                            'ADDENDUM': '((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?addendum(.*?).{60})',
                            'REVOCATION': '(revocation(.*?).{60})',
                         'REQUEST':"((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?request (.*?).{30})"
                                 }
        for key, value in OrderFormList.items():
            dateObj = re.search(value, text1, re.I | re.M)
            if dateObj:
                titleType.append(dateObj.group())
                titleType.append(key)
                break
        if not dateObj:
            titleType.append(text1)
            titleType.append("TERMINATION")
        return titleType

    elif "schedule" in text:
        print("inside schedule", "---" , title)
        text1 = (re.search('((.*?)schedule((.){15})?)', title, re.I | re.M)).group()
        OrderFormList = {'AMENDMENT ': '((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?amendment(.*?)(to)(.*?)addendum('
                                              '.*?).{60})',
                                'ADDENDUM ': '((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?addendum(.*?)(to)(.*?)amendment('
                                             '.*?).{60})',
                                'AMENDMENT': '((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?amendment(.*?).{60})',
                                'ADDENDUM': '((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?addendum(.*?).{60})'}
        for key, value in OrderFormList.items():
            dateObj = re.search(value, text1, re.I | re.M)
            if dateObj:
                titleType.append(dateObj.group())
                titleType.append(key)
                break
        if not dateObj:
            titleType.append(text1)
            titleType.append("SCHEDULE")
        return titleType

    elif "sheet" in text:
        print("inside sheet", "---" , title)
        text1 = (re.search('((.*?)sheet((.){15})?)', title, re.I | re.M)).group()
        OrderFormList = {'AMENDMENT ': '((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?amendment(.*?)(to)(.*?)addendum('
                                              '.*?).{60})',
                                'ADDENDUM ': '((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?addendum(.*?)(to)(.*?)amendment('
                                             '.*?).{60})',
                                'AMENDMENT': '((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?amendment(.*?).{60})',
                                'ADDENDUM': '((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?addendum(.*?).{60})'}
        for key, value in OrderFormList.items():
            dateObj = re.search(value, text1, re.I | re.M)
            if dateObj:
                titleType.append(dateObj.group())
                titleType.append(key)
                break
        if not dateObj:
            titleType.append(text1)
            titleType.append("SHEET")
        return titleType

    elif "notice" in text:
        print("inside notice", "---" , title)
        text1 = (re.search('((.*?)notice((.){15})?)', title, re.I | re.M)).group()
        OrderFormList = {'AMENDMENT ': '((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?amendment(.*?)(to)(.*?)addendum('
                                              '.*?).{60})',
                            'ADDENDUM ': '((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?addendum(.*?)(to)(.*?)amendment('
                                             '.*?).{60})',
                            'AMENDMENT': '((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?amendment(.*?).{60})',
                            'ADDENDUM': '((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?addendum(.*?).{60})',
                            'REVOCATION': '(revocation(.*?).{60})'}
        for key, value in OrderFormList.items():
            dateObj = re.search(value, text1, re.I | re.M)
            if dateObj:
                titleType.append(dateObj.group())
                titleType.append(key)
                break
        if not dateObj:
            titleType.append(text1)
            titleType.append("NOTICE")
        return titleType

    elif "exhibit" in text:
        print("inside exhibit", "---" , title)
        text1 = (re.search('((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?exhibit((.){50})?)', title, re.I | re.M)).group()
        OrderFormList = {'AMENDMENT ': '((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?amendment(.*?)(to)(.*?)addendum('
                                              '.*?).{60})',
                            'ADDENDUM ': '((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?addendum(.*?)(to)(.*?)amendment('
                                             '.*?).{60})',
                            'AMENDMENT': '((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?amendment(.*?).{60})',
                            'ADDENDUM': '((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?addendum(.*?).{60})',
                            'SUPPLEMENT': "((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?supplement(.*?).{60})",
                         'TERMS AND CONDITIONS':"((.*?)terms and conditions(.*?).{20})"
                         }
        for key, value in OrderFormList.items():
            dateObj = re.search(value, text1, re.I | re.M)
            if dateObj:
                titleType.append(dateObj.group())
                titleType.append(key)
                break
        if not dateObj:
            titleType.append(text1)
            titleType.append("EXHIBIT")
        return titleType

    elif "appendix" in text:
        print("inside appendix", "---" , title)
        text1 = (re.search('((.*?)appendix((.){20})?)', title, re.I | re.M)).group()
        OrderFormList = {'APPENDIX ': '((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?appendix(.*?)to agreement('
                                       '.*?).{10})'
                         }
        for key, value in OrderFormList.items():
            dateObj = re.search(value, text1, re.I | re.M)
            if dateObj:
                titleType.append(dateObj.group())
                titleType.append(key)
                break
        if not dateObj:
            titleType.append(text1)
            titleType.append("SOW")
        return titleType

    elif "consent" in text:
        print("inside consent", "---" , title)
        text1 = (re.search('((.*?)consent((.){15})?)', title, re.I | re.M)).group()
        OrderFormList = {'AMENDMENT ': '((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?amendment(.*?)(to)(.*?)addendum('
                                          '.*?).{60})',
                            'ADDENDUM ': '((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?addendum(.*?)(to)(.*?)amendment('
                                         '.*?).{60})',
                            'AMENDMENT': '((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?amendment(.*?).{60})',
                            'ADDENDUM': '((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?addendum(.*?).{60})'}
        for key, value in OrderFormList.items():
            dateObj = re.search(value, text1, re.I | re.M)
            if dateObj:
                titleType.append(dateObj.group())
                titleType.append(key)
                break
        if not dateObj:
            titleType.append(text1)
            titleType.append("CONSENT")
        return titleType

    elif "supplement" in text:
        print("inside supplement", "---" , title)
        text1 = (re.search('((.*?)supplement((.){60})?)', title, re.I | re.M)).group()
        OrderFormList = {'AMENDMENT': '((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?amendment(.*?).{60})',
                         'TERMS AND CONDITIONS': "((.*?)terms and conditions(.*?).{20})"}
        for key, value in OrderFormList.items():
            dateObj = re.search(value, text1, re.I | re.M)
            if dateObj:
                titleType.append(dateObj.group())
                titleType.append(key)
                break
        if not dateObj:
            titleType.append(text1)
            titleType.append("SUPPLEMENT")
        return titleType

    elif "certificate" in text:
        print("inside certificate", "---" , title)
        text1 = (re.search('((.*?)certificate((.){40})?)', title, re.I | re.M)).group()
        OrderFormList = {'AMENDMENT': '((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?amendment(.*?).{60})',
                         'APPICATION': '((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?application(.*?).{30})',
                         'REQUEST':"((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?request (.*?).{30})",
                                                  }
        for key, value in OrderFormList.items():
            dateObj = re.search(value, text1, re.I | re.M)
            if dateObj:
                titleType.append(dateObj.group())
                titleType.append(key)
                break
        if not dateObj:
            titleType.append(text1)
            titleType.append("CERTIFICATE")
        return titleType

    elif (("memorandum of understanding" in text) or ( " mou " in text) ):
        print("inside mou", "---" , title)
        text1 = (re.search('(memorandum of understanding| mou ((.*?){15})?)', title, re.I | re.M)).group()
        OrderFormList = {'AMENDMENT': '((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?amendment(.*?).{60})',
                         'EXTENSION': '((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?extension(.*?).{60})'}
        for key, value in OrderFormList.items():
            dateObj = re.search(value, text1, re.I | re.M)
            if dateObj:
                titleType.append(dateObj.group())
                titleType.append(key)
                break
        if not dateObj:
            titleType.append(text1)
            titleType.append("MOU")
        return titleType

    elif "terms and condition" in text:
        print("inside t&c", "---" , title)
        text1 = (re.search('((.*?)terms and conditions((.*?).{20})?)', title, re.I | re.M)).group()
        OrderFormList = {'AMENDMENT/ADDENDUM': '((amendment\s?(and|/|\|&)?\s?addendum)(.*?).{50}|(addendum\s?(and|/|\|&)?\s?amendment(.*?).{50}))',
                                'AMENDMENT ': '((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?amendment(.*?)(to)(.*?)addendum('
                                              '.*?).{60})',
                                'ADDENDUM ': '((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?addendum(.*?)(to)(.*?)amendment('
                                             '.*?).{60})',
                                'AMENDMENT': '((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?amendment(.*?).{60})',
                                'ADDENDUM': '((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?addendum(.*?).{60})',
                         'LETTER': "((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?letter(.*?).{40})"}
        for key, value in OrderFormList.items():
            dateObj = re.search(value, text1, re.I | re.M)
            if dateObj:
                titleType.append(dateObj.group())
                titleType.append(key)
                break
        if not dateObj:
            titleType.append(text1)
            titleType.append("TERMS AND CONDITIONS")
        return titleType

    elif "permission" in text:
        print("inside permission", "---" , title)
        text1 = (re.search('((.*?)permission((.*?).{60})?)', title, re.I | re.M)).group()
        OrderFormList = {'GRANT': '((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?grant(.*?).{40})'}
        for key, value in OrderFormList.items():
            dateObj = re.search(value, text1, re.I | re.M)
            if dateObj:
                titleType.append(dateObj.group())
                titleType.append(key)
                break
        if not dateObj:
            titleType.append(text1)
            titleType.append("PERMISSION")
        return titleType

    elif "extension" in text:
        print("inside extension", "---" , title)
        text1 = (re.search('((.*?)extension((.){15})?)', title, re.I | re.M)).group()
        OrderFormList = {'AMENDMENT/ADDENDUM': '((amendment\s?(and|/|\|&)?\s?addendum)(.*?).{50}|(addendum\s?(and|/|\|&)?\s?amendment(.*?).{50}))',
                                'AMENDMENT ': '((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?amendment(.*?)(to)(.*?)addendum('
                                              '.*?).{60})',
                                'ADDENDUM ': '((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?addendum(.*?)(to)(.*?)amendment('
                                             '.*?).{60})',
                                'AMENDMENT': '((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?amendment(.*?).{60})',
                                'ADDENDUM': '((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?addendum(.*?).{60})',
                         'EXTENSION AND AMENDMENT': '((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?extension and amendment(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?)'}
        for key, value in OrderFormList.items():
            dateObj = re.search(value, text1, re.I | re.M)
            if dateObj:
                titleType.append(dateObj.group())
                titleType.append(key)
                break
        if not dateObj:
            titleType.append(text1)
            titleType.append("EXTENSION")
        return titleType

    elif "summary" in text:
        print("inside summary", "---" , title)
        text1 = (re.search('((.*?)summary((.){15})?)', title, re.I | re.M)).group()
        OrderFormList = {'AMENDMENT': '((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?amendment(.*?).{60})',
                         'EXTENSION': '((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?extension(.*?).{60})',
                         'QUOTE':'((.*?)quote((.){15})?)'}
        for key, value in OrderFormList.items():
            dateObj = re.search(value, text1, re.I | re.M)
            if dateObj:
                titleType.append(dateObj.group())
                titleType.append(key)
                break
        if not dateObj:
            titleType.append(text1)
            titleType.append("SUMMARY")
        return titleType

    elif "release" in text:
        print("inside work release", "---" , title)
        text1 = (re.search('((.*?)release((.){40})?)', title, re.I | re.M)).group()
        titleType.append(text1)
        titleType.append("RELEASE")
        return titleType

    elif "quote" in text:
        print("inside quote", "---" , title)
        text1 = (re.search('((.*?)quote((.){15})?)', title, re.I | re.M)).group()
        titleType.append(text1)
        titleType.append("QUOTE")
        return titleType

    elif "memorandum" in text:
        print("inside memorandum", "---" , title)
        text1 = (re.search('((.*?)memorandum((.){15})?)', title, re.I | re.M)).group()
        OrderFormList = {'AMENDMENT': '((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?amendment(.*?).{60})',
                         'EXTENSION': '((?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?(?:\S+\s)?extension(.*?).{60})'}
        for key, value in OrderFormList.items():
            dateObj = re.search(value, text1, re.I | re.M)
            if dateObj:
                titleType.append(dateObj.group())
                titleType.append(key)
                break
        if not dateObj:
            titleType.append(text1)
            titleType.append("MEMORANDUM")
        return titleType

    elif "work plan" in text:
        print("inside work plan", "---" , title)
        text1 = (re.search('((.*?)work plan((.){15})?)', title, re.I | re.M)).group()
        titleType.append(text1)
        titleType.append("PLAN")
        return titleType

    else:
        titleType= ["No Match","NO MATCH"]
        return titleType

def strip_non_ascii(string):
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)

def ORFile():
    # Opening the csv file so that we can append the changes to it.
    f = open('D:\MainData\csv files\Carndinal\Cardinal_Title_Type.csv', 'w+',
             newline='', encoding="utf8", errors="ignore")
    w = csv.writer(f, quoting=csv.QUOTE_ALL, delimiter=',')
    w.writerow(['Path & File Name', 'String' ,"Title",'Type' ])
    count=0
    for root, dir, files in os.walk("D:\MainData\TXT"):
        # Fetching a single file
        for singFile in files:
            # Getting only text files
            if ".txt" in singFile:
                newPath = os.path.join(root, singFile)
                file1 = open(newPath, 'r+',  encoding="utf8", errors="ignore")
                content = file1.read()
                # Extracting Parties from txt files (300 words)
                text = content.split()
                str1 = ' '.join(str(e) for e in text)
                str3 =str1[:2500]
                str2 = strip_non_ascii(str3)
                count=count+1
                # Getting expiration title
                titleList = ['((.*)this)((.*?).{69})','((.*)addendum)((.*?).{60})','((.*)amendment)((.*?).{60})',
                             '((.*)summary)((.*?).{60})','((.*)dear)((.*?).{60})','(.*)re:((.*?).{60})','((.*)form(.*?).{60})', '((.*)order(.*?).{60})',
                            '((.*)exhibit(.*?).{60})','((.*)agreement)((.*?).{60})','((.*)statement of work)((.*?).{'
                                                                                    '60})','((.*)contract )((.*?).{'
                                                                                           '60})']

                dateObj=''
                type,titleString,titleKey=[],[],[]
                for i in titleList:
                    dateObj = re.search(i, str2, re.I | re.M)
                    if dateObj:
                        titleString = dateObj.group()
                        type = extractType(titleString.lower(),titleString)

                        break
                    if not dateObj:
                        titleString= "No Match"
                        type= ["No Match","NO MATCH"]
                print(count, "---", singFile, " Files Processed ..!")
                # Writing changes to the csv
                w.writerow([newPath,singFile, titleString ,type[0] ,type[1],str3])
                file1.close()

def remainingBatch():
    PathForCSV = 'D:\MainData\csv files\Carndinal\Cardinal_Title_Type.csv'
    RemainingfilesList='D:\\remainingbatch.csv'
    RemainingFiles = open(RemainingfilesList, 'r+', encoding="utf8", errors="ignore")
    reading = csv.reader(RemainingFiles)
    ReadingCSV = open(PathForCSV, 'w+', encoding="utf8",errors="ignore", newline="")
    WritingCSV = csv.writer(ReadingCSV, quoting=csv.QUOTE_ALL, delimiter=',')
    WritingCSV.writerow(['Path & File Name','Output String','title','type'])
    count = 0
    for row in reading:
            file1 = open(row[0], 'r+', encoding="utf8",errors="ignore")
            count=count+1
            content = file1.read()
            text = content.split()
            str1= ' '.join(str(e) for e in text)

            # row1 = strip_non_ascii(row[0])
            str3= str1[:500]
            str2 = strip_non_ascii(str3)
            did=""
            date, date2, foundOptions, dateObj = '', "", "", ""
            titleList = ['((.*)this)((.*?).{69})', '((.*)addendum)((.*?).{60})', '((.*)amendment)((.*?).{60})',
                         '((.*)summary)((.*?).{60})', '((.*)dear)((.*?).{60})', '(.*)re:((.*?).{60})',
                         '((.*)form(.*?).{60})', '((.*)order(.*?).{60})','((.*)exhibit(.*?).{60})',
                         '((.*)agreement)((.*?).{60})', '((.*)statement of work)((.*?).{60})', '((.*)contract )((.*?).{60})']
            dateObj = ''
            type, titleString, titleKey = [], [], []
            for i in titleList:
                dateObj = re.search(i, str2, re.I | re.M)
                if dateObj:
                    titleString = dateObj.group()
                    type = extractType(titleString.lower(), titleString)
                    print(type)
                    break
                if not dateObj:
                    titleString = "No Match"
                    type = ["No Match", "NO MATCH"]
            print(count, "---", row[0], " Files Processed ..!")
            # Writing changes to the csv
            WritingCSV.writerow([row[0],  titleString, type[0], type[1]])


# ===========================================================================================#

def main():
    remainingBatch()

if __name__ == '__main__':
    start_time = time.time()
    main()
