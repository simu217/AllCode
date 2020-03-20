"""This code will be helpful to assign vendor ID
  It will assign if:
 # Counter Party of one name existing in other counter party names, then one family will be assigned to them.
 # Two words will match in counter party names then one family will be assigned to them. For single word matching it wont work.
 Requirements:
 # concatenate two columns of counter party and additional party.
 # remove "." , ","  and party extensions from them.
#======================================================================================================================================================================
 #

 """
import pyodbc
import difflib
import pandas as pd
from difflib import SequenceMatcher
import re

def dif(word,cp):
    final=re.search(word.replace(" ",""), cp.replace(" ",""))
    final1=re.search(cp.replace(" ",""), word.replace(" ",""))
    if final:
        return True
    elif final1:
        return True
    else:
        return False

def diff(word,cp,num1):
    final=re.search(word.replace(" ",""), cp.replace(" ",""))
    final1=re.search(cp.replace(" ",""), word.replace(" ",""))
    if final:
        num1=num1+1
        return num1
    elif final1:
        num1 = num1 + 1
        return num1
    else:
        return num1

def foroneCP(dualist,additionalcp1):
    ID = 1001
    vendorID = 1001
    #----------------------------------------------------------------------------------------------------------------------------------------------
    """here we are iterating thru additional party list and checking in which counterparty it exist then we are matching that counterparty words with all parties 
    and assigning it a vendor ID"""
    addfinal={}
    singleID = []
    addParty=set(additionalcp1)
    for items in addParty:
        similardualist = list(dualist)
        for val in similardualist:
            if items.replace(" ","") in val.replace(" ",""):
                addfinal[val]=vendorID
                val1 = val.split()
                for cp in similardualist:
                    num = 0
                    num1 = 0
                    for word in val1:
                        ratio = diff(word, cp, num1)
                        if word in cp:
                            num = num + 1
                            if (num > 1):
                                addfinal[cp] = vendorID
                        elif (ratio >= 1):
                            addfinal[cp] = vendorID
        vendorID = vendorID + 1
    #-----------------------------------------------------------------------------------------------------------------------------------------------
    """we are subtracting list assigned list elements of ADDFINAL variable with dualist, so that we can get less elements to iterate"""
    for elms in addfinal.keys():
        singleID.append(elms)
    leftParty=set(dualist)-set(singleID)
    LeftPartyList=list(leftParty)
    similardualist=list(LeftPartyList)
    #-----------------------------------------------------------------------------------------------------------------------------------------------
    """here we are assigning vendor id for that counter parties which are of one word """
    final,container,similardualist,temp= {},{},[],[]
    for item in LeftPartyList:
        val = item.split()
        for cp in LeftPartyList:
            if len(val) == len(cp.split()) == 1:
                if val[0] in cp:
                    final[cp] = vendorID
                    for cp1 in similardualist:
                        ratio = dif(val[0], cp1)
                        if val[0] in cp1:
                            if cp != val[0]:
                                final[cp1] = vendorID
                        elif (ratio == True) & (cp1 != val[0]):
                            final[cp1] = vendorID
                    for x, y in final.items():
                        temp.append(x)
                    similardualist = [i for i in similardualist + temp if i not in similardualist or i not in temp]
                    if len(similardualist) == 0:
                        break
                    else:
                        pass
        vendorID += 1
    for x, y in final.items():
        for itm in dualist:
            if x.replace(" ", "") in itm.replace(" ", ""):
                container[itm] = y
    #---------------------------------------------------------------------------------------------------------------------------------------------------
    """we are subtracting list assigned list elements of CONTAINER variable with dualist, so that we can get less elements to iterate"""
    leftParty.clear()
    LeftPartyList.clear()
    for elms in container.keys():
        singleID.append(elms)
    leftParty=set(dualist)-set(singleID)
    LeftPartyList=sorted(list(leftParty))
    similardualist=sorted(list(LeftPartyList))

    #---------------------------------------------------------------------------------------------------------------------------------------------------------
    """here we are assigning vendor id for remaining elements"""
    container1,final1 = {}, {}
    for item in LeftPartyList:
        val = item.split()
        for cp in similardualist:
            num = 0
            num1 = 0
            for word in val:
                ratio = diff(word, cp, num1)
                if word in cp:
                    num = num + 1
                    if (num > 1):
                        container1[cp] = vendorID
                elif (ratio >= 1):
                    container1[cp] = vendorID
        vendorID = vendorID + 1
    #---------------------------------------------------------------------------------------------------------------------
    """Container is the dictionary which contains all data of different dictionaries as ADDFINAL AND CONTAINER 1 both are updated with it."""
    container1.update(container)
    container1.update(addfinal)
    """for every vendor, Id assignment number is not of number sequence so that we are rectifying this here"""
    vendor = []
    for x, y in container1.items():
        vendor.append(y)
    uniID = set(vendor)
    for items in uniID:
        for x, y in container1.items():
            if items == y:
                final1[x] = ID
        ID += 1
    return final1

def listmodify(list1):
    merged,finalist=[],[]
    cplist=set(list1)
    for iem in cplist:
        if len(iem.split()) == 1:
            merged.append(iem)
        else:
            pass
    res = [i for i in cplist if i not in merged]
    finalist=merged+res
    return finalist

def main():
    final=[]
    # cplist=["North Haven Expansion Capital LP","LG EuropeLimited ","Liberty Global EuropeLimited  ","Liberty GlobalEurope Limited LGE ltd","LGE ltd "]
    # cplist = ["North Haven Expansion Capital","K foundation HP", "Kaiser FHP", "Kaiser foundation Health P", " ABC KFHP ltd","LG EuropeLimited ",
    #           "Liberty Global EuropeLimited  ","Liberty GlobalEurope Limited LGE ltd","LGE ltd "   ,                                                                                                                                                           'intelcorporation ',
    #           "intel ", 'intel corporation ']
    cplist = ['hp', 'kfh plan',"kaiser foundation health plan","kfh plan"]
    # data = pd.read_excel("D:\\VendorID Output.xlsx", encoding="utf-8") #VendorID Output #vendorIDsample
    # data["VendorID"]=""
    # data["Updated"] = ((((data["Counter Party"].str.replace(",","")).str.replace(".","")).str.replace("-","")).str.lower()).str.replace("inc","")
    # cplist =data["Updated"].values.tolist()
    # additionalcp=(data["Additional Party"].str.lower()).values.tolist()
    # additionalcp1=[x for x in additionalcp if str(x) != 'nan']
    additionalcp1=[]
    setlist1=listmodify(cplist)
    if setlist1:
        final=foroneCP(list(setlist1),additionalcp1)
    print(final)
    # for x,y in final.items():
    #     for ind in data.index:
    #         if data['Updated'][ind]== x:
    #             data['VendorID'][ind]= y
    # data.to_csv('D:\\IntergratedOutput2.csv')
        # conn = pyodbc.connect(
    #     'Driver={SQL Server};Server=database.sumatilegal.loc;Database=dno_context_dev;Trusted_Connection=yes;')
    # cursor = conn.cursor()
    # # all=cursor.execute(
    # #                 "SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'PREOUTLIN_CONTRACTS_QA'")
    # # print(all.fetchall())
    # for row in cursor.execute(
    #                 # "SELECT FOLDERPATH,FILENAME,COUNTERPARTYNAME,AdditionalNameOfCP FROM PREOUTLIN_CONTRACTS_QA WHERE DBA_FFA_AKA='' ;"):
    #          # "SELECT FOLDERPATH,FILENAME,COUNTERPARTYNAME,AdditionalNameOfCP FROM PREOUTLIN_CONTRACTS_QA WHERE DBA_FFA_AKA='' ;"):
    #          "SELECT FOLDERPATH,FILENAME,COUNTERPARTYNAME,AdditionalNameOfCP FROM PREOUTLIN_CONTRACTS_QA;"):
    #             list1.append(row)
    #             print(row)
    #             cplist.append(row.COUNTERPARTYNAME)

    # -----------------------------------------------------------------------------------------------------


if __name__ == '__main__':
        # dif("IntelCorporation","Intel")
        main()



