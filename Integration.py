import pyodbc
import csv
import pandas as pd

def dif(cp,word,instance1):
    final = list(set(word) & set(cp))
    if final:
        instance1+=1

    return instance1

def foroneCP(dualist):
    vendor = []
    final,final1 = {},{}
    ID = 1001
    vendorID = 1001
    for item in dualist:
        val = item.split()
        for cp in dualist:
            num = 0
            instance1 = 0
            for word in val:
                instance1 = dif(cp, word, instance1)
                if len(cp.split()) == 1:
                    if word in cp:
                        final[cp] = vendorID
                        pass
                if word in cp:
                    num += 1
                if (num > 1 and instance1 == 2):
                    final[cp] = vendorID
        vendorID += 1

    for x, y in final.items():
        vendor.append(y)
    uniID = set(vendor)
    for items in uniID:
        for x, y in final.items():
            if items == y:
                final1[x] = ID
        ID += 1
    return final1

def listmodify(list1):
    cplist1,merged,finalist=[],[],[]
    for item in list1:
        val = item.replace(",", "")
        val1 = val.replace(".", "")
        cplist1.append(val1)
    cplist=set(cplist1)
    cplist1.clear()
    for iem in cplist:
        if len(iem.split()) == 1:
            merged.append(iem)
    res = [i for i in cplist if i not in merged]
    finalist=merged+res
    return finalist

def main():
    final=[]
    final1={}
    list1=[]
    data = pd.read_excel("D:\Input File.xlsx", encoding="utf-8")
    cplist = data["Updated"].values.tolist()
    file = open("D:\\IntergratedOutput1.csv", 'w+', encoding="utf8", errors="ignore", newline="")
    setlist1=listmodify(cplist)
    if setlist1:
        final=foroneCP(list(setlist1))
    # for y in final.values():
    #     list1.append(y)
    # list2=sorted(set(list1))
    # list1.clear()
    # for item in list2:
    #     list3 = []
    #     for x,y in final.items():
    #         if y == item:
    #             list3.append(x)
    #     final1[item] = list3
    # print(data)
    for x,y in final.items():
        for ind in data.index:
            if data['Updated'][ind]== x:
                data['VendorID'][ind]= y
    data.to_csv('D:\\IntergratedOutput1.csv')










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
    # file=open("D:\\IntergratedOutput1.csv", 'w+', encoding="utf8",errors="ignore",newline=   "")
    # WritingCSV = csv.writer(file, quoting=csv.QUOTE_ALL, delimiter=',')
    # WritingCSV.writerow(["Output CP","Additional CP","VendorID"]\\\\\\\
    # setlist1=listmodify(cplist)
    # setlist2=listmodify(cplist1)
    # dualist=list(setlist2)+list(setlist1)
    # if dualist:
    #     foroneCP(list(dualist),WritingCSV)
    #     print("executed")


if __name__ == '__main__':
        main()




