import os
import sys
import csv
import re
import time
def file_name_cp(singFile):
    matchObj = re.search(r'-(.*?)\(', singFile, re.I|re.M)

    matchObj1 = re.search(r'-(.*?)\(f', singFile, re.I|re.M)

    matchObj2 = re.search(r'-(.*?)\(c', singFile, re.I|re.M)

    matchObj3 = re.search(r'-(.*?)\(n', singFile, re.I|re.M)

    if matchObj1:
        cp = matchObj1.group(1)

        if "__" in cp:
            cp1 = cp.replace("__", " ")

        elif "_" in cp:
            cp1 = cp.replace('_',' ')

        else:
            cp1 = cp

    elif matchObj2:
        cp = matchObj2.group(1)

        if "__" in cp:
            cp1 = cp.replace("__", " ")

        elif "_" in cp:
            cp1 = cp.replace('_',' ')

        else:
            cp1 = cp

    elif matchObj3:
        cp = matchObj3.group(1)

        if "__" in cp:
            cp1 = cp.replace("__", " ")

        elif "_" in cp:
            cp1 = cp.replace('_',' ')

        else:
            cp1 = cp

    elif matchObj:
        cp = matchObj.group(1)

        if "__" in cp:
            cp1 = cp.replace("__", " ")

        elif "_" in cp:
            cp1 = cp.replace('_',' ')

        else:
            cp1 = cp

    else:
        cp1 = "No Match"
    return cp1

def file_name_cp1(singFile):
        cp2,cp3,cp4 = "","",""
        matchObj = re.search(r'-(.*?)\(', singFile, re.I | re.M)

        matchObj1 = re.search(r'-(.*?)\(f', singFile, re.I | re.M)

        matchObj2 = re.search(r'-(.*?)\(c', singFile, re.I | re.M)

        matchObj3 = re.search(r'-(.*?)\(n', singFile, re.I | re.M)

        if matchObj1:
            cp = matchObj1.group(1)

            if "__" in cp:
                cp1 = cp.replace("__", " ")
                if "_" in cp:
                    cp1 = cp.replace("_", " ")

            elif "_" in cp:
                cp1 = cp.replace('_', ' ')

            else:
                cp1 = cp

        elif matchObj2:
            cp = matchObj2.group(1)

            if "__" in cp:
                cp1 = cp.replace("__", " ")
                if "_" in cp:
                    cp1 = cp.replace("_", " ")

            elif "_" in cp:
                cp1 = cp.replace('_', ' ')

            else:
                cp1 = cp

        elif matchObj3:
            cp = matchObj3.group(1)

            if "__" in cp:
                cp1 = cp.replace("__", " ")

            elif "_" in cp:
                cp1 = cp.replace('_', ' ')

            else:
                cp1 = cp

        elif matchObj:
            cp = matchObj.group(1)

            if "__" in cp:
                cp1 = cp.replace("__", " ")

            elif "_" in cp:
                cp1 = cp.replace('_', ' ')

            else:
                cp1 = cp

        else:
            cp1 = "No Match"
        cp2 = cp1.split()
        if len(cp2) > 0:
            cp3 = cp2[0]
        if len(cp2) > 1:
            cp4= cp2[0]+" "+cp2[1]
        return cp3,cp4

def file_name_cp2(singFile):
        cp2,cp3,cp4 = "","",""
        matchObj = re.search(r'(.*?)-', singFile, re.I | re.M)

        if matchObj:
            cp = matchObj.group(1)

            if "__" in cp:
                cp1 = cp.replace("__", " ")
                if "_" in cp:
                    cp1 = cp.replace("_", " ")

            elif "_" in cp:
                cp1 = cp.replace('_', ' ')

            else:
                cp1 = cp

        else:
            cp1 = "No Match"
        cp2 = cp1.split()
        if len(cp2) > 0:
            cp3 = cp2[0]
        if len(cp2) > 1:
            cp4= cp2[0]+" "+cp2[1]
        return cp3,cp4

def string_search_CP(fcp, content, text):

    fcpLower = fcp.lower()
    fcpLen = len(fcp)

    if fcpLower in text:
        ind = text.index(fcpLower)

        # Extracting CP
        cp = content[ind:(ind+(fcpLen+30))]

    else:
        cp = "No Match"

    return cp

def strip_non_ascii(string):
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)

def CP_Cleanup_Code(str1, entities):
    str2 = str1.lower()

    for ent in entities:
        if str(ent.lower()) in str2:
            loweredEnt = ent.lower()
            entLen = len(loweredEnt)
            entIndex = str2.index(loweredEnt)
            entity = str1[entIndex:(entIndex + entLen)]
            newString = str1[:(entIndex)] + str1[(entIndex + entLen):]
            break
        else:
            newString = str1

    return newString

def reverse_string(str1):
    revList = []
    str2 = str1.split()

    for i in (reversed(str2)):
        revList.append(i)

    revString = ' '.join(str(e) for e in revList)
    # print revString
    return revString

def CP_Extractor(lis, str1, revString):
    for i in lis:
        keyLen = len(i)
        if i in revString.lower():
            ind = str1.lower().index(i)
            newString = str1[:(ind + keyLen)]
            break
        else:
            newString = "No Match"
    return newString

def last_sign_date(content1):
    content = content1.lower()
    lis = ["with kind regards", "acknowledged, agreed and confirmed", "signed:", 'agreed and accepted by grantee:',"provider and google hereby agree to this agreement", "in witness whereof", "signed by the parties",
           "agreed and accepted", 'accepted and agreed', "supplier:", 'accepted on', 'sincerely', "kindly regards", "very truly yours",
           "agreed by the parties on the dates stated below", "agreed by the parties using echosign on the dates stated below", "title:", "title"]
    contentLen = len(content)
    String=""
    for element in lis:
        key = element
        if element in content:
            elementIndex = content.index(key)
            String = content1[(elementIndex - 200):(elementIndex + 600)]
            break
        else:
            String = "No Match"


    return String

def ORFile():
    # Opening the csv file so that we can write the changes to it.
    f = open('D:\MainData\csv files\FLIR 11.1\FLIR Phase 8 TXT/FLIR_P8_CP.csv', 'w+',
             newline='', encoding="utf8", errors="ignore")
    w = csv.writer(f, quoting=csv.QUOTE_ALL, delimiter=',')
    # w.writerow(['File Name', 'CP from File Name', 'CP_String', 'Signature block', 'CP Search in Doc',"One word from filename","One word search","Two words from filename","Two words search"])
    w.writerow(['File Name', 'NSCfilename' ,'CP from File Name', 'CP_String', 'Signature block', 'CP Search in Doc',
                'Initial String'])
    # w.writerow(['Path & File Name', 'CP from File Name string combined','words from filename'])
    entities = ["ITA Software Inc.'s", 'ITA Software Inc.', 'ITA Software Inc', 'Teracent Corporation', 'Google Ireland United',
                'TX VIA, INC.', 'Google Australia Pty Ltd.', 'GOOGLE INTERNATIONAL, LLC TAIWAN BRANCH', 'Google Fiber, Inc.', 'Google UK, Ltd', 'Grand Central Communications, Inc.', 'Google UK, Ltd.', 'CSquared Ghana Ltd.', 'Google Inc.', 'Google Ireland Limited', 'Google, LLC', 'Google Google Denmark ApS', 'GOOGLE FIBER, INC.', 'Google, Inc.', 'Google Asia Pacific Pte. Ltd.', 'Google Ireland Ltd', 'Mahataa Information India Private Limited', 'Google Netherlands B.V.', 'Terra Bella Technologies Inc.', 'Google Germany GmbH', 'Google Payment Corp.', 'Google Japan GK.', 'Google Ireland Ltd.', 'Nest Labs Inc.', 'Google Brasil Internet Ltda.', 'Google Argentina S.R.L.', 'Google Advertising (Shanghai) Co., Ltd.', 'Google Asia Pacific Pte Ltd', 'Google Asia Pacific Pte. Limited', 'Google Fiber Inc.', 'Nest Labs, Inc.', 'Google Ireland Limited.', 'Google Japan Inc.', 'Google Switzerland GmBH', 'Google India Pvt Ltd.', 'AdMob, Inc.', 'Google Inc.', 'Google Asia Pacific Pte Ltd.', 'Google Spain, S.L.', 'Google Peru S.R.L', 'GOOGLE OPERACIONES DE M\xc3\x89XICO, S. DE R.L. DE C.V.', 'Google Infrastructure Bermuda Limited', 'Google Ireland, Ltd', 'DailyDeal GmbH', 'Google India Private Limited', 'Google Infraestrutura Brasil Ltda.', 'Crystal Computing SPRL', 'Google Argentina SRL', 'Google OOO', 'Google lreland Limited', 'Google Colombia Ltda.', 'Nest Labs (Europe) Limited', 'GOOGLE CHILE LTDA.', 'GOOGLE INDIA PRIVATE LTD.', 'Admeld, LLC.', 'Admeld, LLC', 'Google Japan, Inc.', 'Google India Pvt. Ltd.', 'GOOGLE TECHNOLOGY INC.', 'Google Australia Pty Ltd', 'GU Holdings Inc.', 'AdMeld Inc.', 'BeatThatQuote.com Limited', 'Google, Inc', 'Google Cable Japan G.K.', 'Google India Pvt.Ltd.', 'Google Singapore Pte. Ltd.', 'GOOGLE OPERACIONES DE MEXICO, S. DE R.L. DE C.V.', 'Google Spain S.L.', 'Google Denmark ApS', 'Google Poland sp. z o.o.', 'Google Brasil lnternet Ltda.', 'GOOGLE COLOMBIA LIMITADA', 'Google Commerce Limited', 'Google France SARL', 'GU Holdings, Inc.', 'Inversiones y Servicios Dataluna Limitada', 'Google Access LLC', 'CHANNEL INTELLIGENCE, INC.', 'CRYSTAL COMPUTING SPRL OU', 'Google Netherlands BV', 'Google Belgium NV', 'Google Asia Pacific Pte, Ltd.', 'GOOGLE SERVICES MALAYSlA SDN. BHD', 'NEST LABS Europe Limited', 'Google lnc.', 'Volo GmbH vertreten durch WOLF THEISS Rechtsanw\xc3\xa4lte GmbH', 'Google Australia Pty Ltd.', 'Google Fiber', 'Postini Inc.', 'Google, Inc/YouTube', 'Orbitera, Inc.', 'GOOGLE INTERNATIONAL LLC TAIWAN BRANCH', 'Google Technology, Inc.', 'Google Singapore Pte. Limited.', 'Google Operaciones de  M\xc3\xa9xico S. de R.L. de C.V.', 'GOOGLE MEXICO, S. DE R.L. DE C.V.', 'Google Chile Limitada', 'Google Italy s.r.l.', 'DOUBLECLICK INC.', 'Google UK Ltd', 'Grand Central Communications, Inc', 'Google Norway AS', 'GOOGLE INFORMATION TECHNOLOGY (SHANGHAI) CO., LTD.', 'Google Australia Pty Limited', 'bruNET GmbH', 'Rotarua Limited', 'Google Sweden AB', 'Google Hrvatska D.o.o', 'GOOGLE KOREA LLC', 'Skybox Imaging, Inc.', 'Google Advertising (Shanghai) Company Limited', 'Anvato, Inc.', 'Anvato, Inc', 'Anvato Inc.', 'Anvato Inc', 'Google SJC Bermuda Limited', 'Volo GmbH', 'SAYNOW CORPORATION', 'Google Belgium', 'Green Box Computing B.V.', 'Google, LLC', 'Bear-Line GmbH', 'Google Asia Pacific Pte. Ltd', 'Google UK Ltd.', 'GRANDCENTRAL COMMUNICATIONS, INC.', 'CSquared Ghana Ltd', 'GOOGLE INFRAESTRUTURA BRASIL, LTDA.', 'TX VIA, INC', 'GOOGLE (FR)', 'Google Network Circuit Provider', 'DailyDeal CH GmbH', 'Google Infrastructure Bermuda Ltd.', 'Google Merchant Center Partner', 'GOOGLE INFORMATION TECHNOLOGY (CHINA) COMPANY LIMITED', 'Google Spain', 'Google International LLC', 'Google Services Malaysia Sdn. Bhd.', 'Apigee Corporation', 'Google Germany GmbH.', 'Google Argentina LLC', 'DOUBLECLICK, INC.', 'YOUTUBE, LLC', 'YOUTUBE LLC', 'YOUTUBE LLC,', 'YOUTUBE LLC.', 'YOUTUBE, LLC.', 'YOUTUBE, INC.', 'YOUTUBE, INC', 'YOUTUBE INC.', 'allPAY GmbH', 'GRANDCENTRAL VENTURES, INC.', 'GOOGLE OPERACIONES DE MEXICO S DE RL DE CV', 'Google India Pvt Limited.', 'Google LLC.', 'Eyetower LLC', 'Blue Path Technology Unlimited Company', 'Google Japan G.K.', 'Nest, Labs Inc.', 'Google Peru S.R.L.', 'Green Box Computing B.V', 'Gu Holdings, Inc', 'Zynamics GmbH.', 'Google Cable Bermuda Ltd.', 'Google, Inc. (Brasil)', 'Google Inc. (Brasil)', 'POSTINI UK LIMITED', 'ITA Software, LLC.', 'ITA Software, LLC', 'ITA Software LLC.', 'ITA SOFTWARE, INC.', 'Google Brasil Internet, Ltda.', 'Google Ireland, Ltd.', 'Google (Ireland) Limited', 'Google Israel Ltd.', 'SONOA SYSTEMS, INC.', 'SONOA SYSTEMS INC.', 'Jibe Mobile, Inc.', 'Google Canada, Corporation', 'Google Singapore Pte., Ltd.', 'Google Singapore Pte., Ltd', 'Google Singapore Pte.', 'Google Ireland Ltd.', 'Google Ireland Ltd,', 'Postini, Inc.', 'APIGEE CORP.', 'Channel Intelligence, Inc.', 'Channel Intelligence, Inc', 'Google International, LLC.', 'Meebo, Inc.', 'Tx Via Philippines, Inc.', 'Google India Private, Ltd.', 'Google India Private Ltd.', 'Google India Private Ltd', 'GU Holdings Inc.', 'GU Holdings Inc', 'Google Affiliate Network, Inc.', 'Google Poland SP. z.o.o.', 'Admeld, LLC', 'AdMeld, Inc.', 'Google Voice, Inc.', 'Crystal Computing S.P.R.L.', 'TxVia Inc.', 'Meebo Inc.', 'Google Slovakia s.r.o.', 'Google Australia Pty. Ltd.', 'Nest Labs (Europe) Ltd.', 'GOOGLE INDIA PVT.LTD', 'SayNow, Inc.', 'Google India Pvt .Ltd.', 'Google Cable Bermuda, Ltd.', 'Google Cable Bermuda, Ltd', 'Technology Infrastructure Italy, Srl.', 'Technology Infrastructure Italy, Srl', 'Google Compare Credit Cards Inc.', 'GU Holdings, LLC.', 'GU Holdings, LLC', 'Google Access Inc.', 'Google India PVT. Ltd.', 'Google India PVT. Ltd', 'Google Belgium.', 'Google Could Japan G.K.', 'Google Poland Sp z.o.o', 'Google Ireland, Limited', 'Level 3 Communications SA.', 'ON2 TECHNOLOGIES, LLC', 'Google Belgium N.V./ SA', 'Google Singapore Pte. Ltd', 'Virus Total S.L.', 'Google Enterprise', 'Google Brasil Internet Limitada', 'GOOGLE AKWAN INTERNET LTDA.', 'Google India Digital Services PVT, Limited.', 'Google India Digital Services PVT. Limited.', 'Google India Digital Services PVT Limited', 'NIANTIC, INC.', 'Ireland and Google Commerce, Limited.', 'Ireland and Google Commerce Limited.', 'Google Spain SL.', 'Performics, Inc.', 'Google India Pvt Ltd', 'DailyDeal GmbH', 'Google Infraestrutura Brasil Ltda', 'Crystal Computing SPRL', 'Google Argentina SRL', 'Google OOO', 'Google Colombia Ltda', 'Nest Labs (Europe) Limited', 'NEST LABS Europe Limited', 'Volo GmbH vertreten durch WOLF THEISS Rechtsanw\xc3\xa4lte GmbH', 'Google Australia Pty Ltd', 'Google Fiber', 'Postini Inc', 'Orbitera, Inc', 'Google France', 'GOOGLE INTERNATIONAL LLC TAIWAN BRANCH', 'Raiden Limited', 'Google Technology, Inc', 'Google Singapore Pte Limited', 'Google Operaciones de  M\xc3\xa9xico S de RL de CV', 'GOOGLE MEXICO, S DE RL DE CV', 'GOOGLE (DE)', 'Google Chile Limitada', 'Google Italy srl', 'Google Fiber, Inc', 'DOUBLECLICK INC', 'Google UK Ltd', 'Grand Central Communications, Inc', 'Google Norway AS', 'GOOGLE INFORMATION TECHNOLOGY (SHANGHAI) CO, LTD', 'Google Australia Pty Limited', 'bruNET GmbH', 'Rotarua Limited', 'Google Sweden AB', 'Google Hrvatska Doo', 'GOOGLE KOREA LLC', 'Skybox Imaging, Inc', 'Google Advertising (Shanghai) Company Limited', 'Google SJC Bermuda Limited', 'Volo GmbH', 'SAYNOW CORPORATION', 'Google Belgium', 'Green Box Computing BV', 'Google, LLC', 'Bear-Line GmbH', 'Google Asia Pacific Pte. Ltd', 'Google Asia Pacific Pte Ltd', 'Google Asia Pacific Pte. Ltd.', 'Google UK Ltd', 'Grand Central', 'GRANDCENTRAL COMMUNICATIONS, INC', 'CSquared Ghana Ltd', 'GOOGLE INFRAESTRUTURA BRASIL, LTDA', 'TX VIA, INC', 'GOOGLE (FR)', 'Google Network Circuit Provider', 'DailyDeal CH GmbH', 'Google Infrastructure Bermuda Ltd', 'Google Merchant Center Partner', 'GOOGLE INFORMATION TECHNOLOGY (CHINA) COMPANY LIMITED', 'Google Spain', 'Google International LLC', 'Google Services Malaysia Sdn Bhd', 'Apigee Corporation', 'Google Germany GmbH', 'Google Argentina LLC', 'DOUBLECLICK, INC', 'YOUTUBE, LLC', 'allPAY GmbH', 'GRANDCENTRAL VENTURES, INC', 'GOOGLE OPERACIONES DE MEXICO S DE RL DE CV', 'Google India Pvt Limited', 'Google LLC', 'Eyetower LLC', 'Blue Path Technology Unlimited Company', 'Google Japan GK', 'Nest, Labs Inc', 'Google Peru SRL', 'GOOGLE COLOMBIA LTDA', 'Green Box Computing BV', 'NEST LABS', 'Gu Holdings, Inc', 'Zynamics GmbH', 'Fionnuala Meehan', 'Google Cable Bermuda Limited', 'Google Inc (Brasil)', 'POSTINI UK LIMITED', 'ITA Software LLC', 'ITA SOFTWARE, INC', 'Google Brasil Internet, Ltda', 'Google Ireland', 'Google (Ireland) Limited', 'Google Israel Ltd', 'SONOA SYSTEMS INC', 'Jibe Mobile, Inc', 'Google Canada Corporation', 'Google Singapore Pte Ltd', 'Dapsi International ApS', 'Google Ireland Ltd', 'Postini, Inc', 'APIGEE CORP', 'Channel Intelligence, Inc', 'Google International, LLC', 'Meebo, Inc', 'Tx Via Philippines, Inc', 'Google India Private Ltd', 'GU Holdings Inc', 'Google Affiliate Network, Inc (f/k/a Performics, Inc)', 'GOOGLE FIBER INC', 'Google Poland SP zoo', 'Google Voice, Inc', 'Tuike Finland Oy', 'Crystal Computing SPRL', 'Google Germany', 'Charter Investments Limited', 'TxVia Inc', 'Meebo Inc', 'Google Singapore Pte', 'Widevine Technologies', 'Google Slovakia sro', 'Google Australia Pty Ltd', 'Channel Intelligence', 'Nest Labs (Europe) Ltd', 'GOOGLE INDIA PVTLTD', 'SayNow, Inc', 'Google Japan Inc', 'SPRL CRYSTAL-COMPUTING', 'Green Box Computing BV', 'Google India Pvt Ltd', 'Google Cable Bermuda Ltd', 'Technology Infrastructure Italy Srl', 'Google Compare Credit Cards Inc', 'GU Holdings, LLC', 'Google Access Inc', 'Google UK', 'Google India PVT Ltd', 'Google Belgium', 'Raiden Unlimted Company', 'Google Could Japan GK', 'Google Poland Sp zoo', 'Google Ireland, Limited', 'Level 3 Communications SA', 'ON2 TECHNOLOGIES, LLC', 'Google Belgium NV/ SA', 'Green Box Computing', 'Google Singapore Pte Ltd', 'Virus Total SL', 'Google Brasil Internet Limitada', 'GOOGLE AKWAN INTERNET LTDA', 'Google India Digital Services PVT Limited', 'NIANTIC, INC', 'Cameron Fisher', 'Ireland and Google Commerce Limited', 'Google Spain SL', 'Google Affiliate Network, Inc', 'Google LLC', 'Google Denmark ApS', 'GOOGLE FIBER, INC', 'Google, Inc', 'Google Asia Pacific Pte Ltd', 'Google Ireland Ltd', 'Google Cable Bermuda Ltd', 'Mahataa Information India Private Limited', 'Google Netherlands BV', 'Terra Bella Technologies Inc', 'Google Germany GmbH', 'Google Payment Corp', 'Google Japan GK', 'Nest Labs Inc', 'Raiden', 'Google Brasil Internet Ltda', 'Google Argentina SRL', 'Google Advertising (Shanghai) Co, Ltd', 'Google Asia Pacific Pte Ltd', 'Google Asia Pacific Pte Limited', 'Google Fiber Inc', 'Nest Labs, Inc', 'Endoxon AG', 'Google Japan Inc', 'Google Switzerland GmBH', 'Google Inc', 'Google Asia Pacific Pte Ltd', 'Google Spain, SL', 'Google Peru SRL', 'GOOGLE OPERACIONES DE M\xc3\x89XICO, S DE RL DE CV', 'Google Infrastructure Bermuda Limited', 'Google Ireland, Ltd', 'Google lreland Limited', 'Google India Private Limited', 'GOOGLE CHILE LTDA', 'GOOGLE INDIA PRIVATE LTD', 'Admeld LLC', 'Google Japan, Inc', 'Google India Pvt Ltd', 'GOOGLE TECHNOLOGY INC', 'Google Australia Pty Ltd', 'GU Holdings Inc', 'AdMeld Inc', 'BeatThatQuotecom Limited', 'Google, Inc', 'Google Cable Japan GK', 'Google India PvtLtd', 'Google UK Limited', 'Google Singapore Pte Ltd', 'GOOGLE OPERACIONES DE MEXICO, S DE RL DE CV', 'Google Spain SL', 'Google Denmark ApS', 'Google Poland sp z oo', 'Google Brasil lnternet Ltda', 'GOOGLE COLOMBIA LIMITADA', 'Google Commerce Limited', 'Google France SARL', 'Google Korea', 'GU Holdings, Inc', 'Inversiones y Servicios Dataluna Limitada', 'Google Access LLC', 'CHANNEL INTELLIGENCE, INC', 'CRYSTAL COMPUTING SPRL OU', 'Google Netherlands BV', 'Google Belgium NV', 'Google Asia Pacific Pte, Ltd', 'BeatThatQuote', 'Google Commerce Limited', 'Adometry, Inc', 'Click Forensics, Inc', 'GOOGLE SERVICES MALAYSlA SDN BHD', 'Google lnc', 'Google', 'Google Inc', 'AdMeld', 'Google, Inc/YouTube', 'AdMob, Inc', 'Admob Inc.', ' YouTube', 'Admob']

    lis = ['s.p.a', ' sa ', ' bv ', ' srl ', ' sa. ', ' s.a. ', ' bv. ', ' srl. ', ' s.r.l', ' srl ', ' sarl ',
           ' s.a.r.l', ' sl ',
           ' sl. ', ' s.l', ' se ', ' sprl ', ' asa ', ' aps ', ' a.p.s', ' ohg ', ' o.h.g', ' spa ', ' sas ', ' rjo ',
           ' pvt', ' llc ', 'llc.', 'llp', ' corporate services ', ' inc.', ' inc ', ' inc',
           '.inc ', ' nv ', ' n.v ', ' gmbh', ' co ', ' co.', ' projects',
           ' incorporation', ' incorporated', ' corporation ', ' companies', ' ltd.', ' ltd', ' ltda' ' bhd ', ' oy ',
           ' limited', ' company',
           ' technolog', ' foundation', ' private ', 'labs', ' laboratories', '\s']

    count = 0

    for root, dir, files in os.walk("D:\MainData\FLIR Phase 8 TXT  "):
        # Fetching a single file
        for singFile in files:
            # Getting only text files
            if ".txt" in singFile:
                newPath = os.path.join(root, singFile)
                newPath1 = strip_non_ascii(newPath)
                file1 = open(newPath, 'r+',  encoding="utf8", errors="ignore")
                count = count + 1
                count1 = str(count)
                # # Opening single file for editing and detecting language
                str2 = file1.read()
                text = str2.split()
                str1 = ' '.join(str(e) for e in text)
                content = strip_non_ascii(str1)
                lowredContent = content.lower()
                fcp = file_name_cp(singFile)
                IntialString=content[:1500]
                # String search for cp in document
                ss = string_search_CP(fcp, content, lowredContent)

                if "background information" in lowredContent[:500]:
                    CPObj = re.search("(Contracting entity:(.*?).{200})", content, re.I | re.M)
                    if CPObj:
                        CP = CPObj.group()
                        print(CP)
                        index = content.index(CP)
                        CP2 = content[index - 100:index]
                        Party1 = CP + " " + CP2

                elif "company name:" in lowredContent[:500]:
                    ind = lowredContent.index("company name:")
                    Party1 = content[ind:ind + 100]

                elif "full legal name:" in lowredContent:
                    ind = lowredContent.index("full legal name:")
                    Party1 = content[ind:ind + 200]

                elif "name of grantee" in lowredContent:
                    ind = lowredContent.index("name of grantee")
                    Party1 = content[ind:ind + 100]

                elif '"company"' in lowredContent:
                    ind = lowredContent.index('"company"')
                    Party1 = content[ind:ind + 100]

                elif "company:" in lowredContent[:500]:
                    ind = lowredContent.index("company:")
                    Party1 = content[ind:ind + 100]

                elif "name of customer:" in lowredContent:
                    ind = lowredContent.index("name of customer:")
                    Party1 = content[ind:ind + 100]

                elif "name of advertiser:" in lowredContent:
                    ind = lowredContent.index("name of advertiser:")
                    Party1 = content[ind:ind + 100]

                elif "name of customer " in lowredContent:
                    ind = lowredContent.index("name of customer ")
                    Party1 = content[ind:ind + 100]

                elif "name of advertiser " in lowredContent:
                    ind = lowredContent.index("name of advertiser ")
                    Party1 = content[ind:ind + 100]

                elif '"customer":' in lowredContent:
                    ind = lowredContent.index('"customer":')
                    Party1 = content[ind:ind + 100]

                elif 'customer:' in lowredContent:
                    ind = lowredContent.index('customer:')
                    if ind < 100:
                        Party1 = content[:ind + 200]
                    else:
                        Party1 = content[ind - 100:ind + 200]

                elif 'customer' in lowredContent[:600]:
                    ind = lowredContent.index('customer')
                    Party1 = content[:ind + 100]

                elif "advertiser:" in lowredContent:
                    ind = lowredContent.index("advertiser:")
                    Party1 = content[ind:ind + 100]

                elif 'distributor:' in lowredContent:
                    ind = lowredContent.index('distributor:')
                    Party1 = content[ind:ind + 100]

                elif 'publisher:' in lowredContent:
                    ind = lowredContent.index('publisher:')
                    Party1 = content[ind:ind + 100]

                elif 'partner:' in lowredContent:
                    ind = lowredContent.index('partner:')
                    Party1 = content[ind:ind + 100]

                elif 'reseller:' in lowredContent:
                    ind = lowredContent.index('reseller:')
                    Party1 = content[ind:ind + 100]

                elif 'customer' in lowredContent[:600]:
                    ind = lowredContent.index('customer')
                    Party1 = content[:ind + 100]

                elif "order form" in lowredContent[:300]:
                    Party1 = content[:800]

                elif "participant:" in lowredContent[:300]:
                    ind = lowredContent.index('participant:')
                    Party1 = content[ind - 100:ind + 100]

                elif "party:" in lowredContent[:300]:
                    ind = lowredContent.index('party:')
                    Party1 = content[ind - 100:ind + 100]

                elif "party1:" in lowredContent[:300]:
                    ind = lowredContent.index('party1:')
                    Party1 = content[ind - 100:ind + 100]

                elif "trainer:" in lowredContent[:300]:
                    ind = lowredContent.index('trainer:')
                    Party1 = content[ind:ind + 100]

                elif "you:" in lowredContent:
                    ind = lowredContent.index('you:')
                    Party1 = content[ind:ind + 100]

                else:

                    str4 = content[:1000]
                    str5 = content[1000:1500]

                    matchObj = re.search(r'\("customer"\) between google((.*?)and((.*?).{100}))', str4, re.M | re.I)

                    matchObj5 = re.search(r'between double((.*?)and((.*?).{100}))', str4,
                                          re.M | re.I)

                    matchObj7 = re.search(r'\(the "effective date"\) between google((.*)and((.*?).{100}))', str4,
                                          re.M | re.I)

                    matchObj9 = re.search(r'\("effective date"\) between google((.*?)and((.*?).{100}))', str4,
                                          re.M | re.I)

                    matchObj8 = re.search(r'between google((.*?)and((.*?).{100}))', str4, re.M | re.I)

                    matchObj2 = re.search(r'by and between((.*?)and((.*?).{100}))', str4, re.M | re.I)

                    matchObj4 = re.search(r'between((.*?)and((.*?).{200}))', str4, re.M | re.I)

                    matchObj1 = re.search(r'by and among((.*?)and((.*?).{100}))', str4, re.M | re.I)

                    matchObj3 = re.search(r'among((.*?)and((.*?).{100}))', str4, re.M | re.I)

                    matchObj6 = re.search(r'( parties:((.*?).{100}))', str4, re.M | re.I)

                    matchObj15 = re.search(r'between and among((.*?)and((.*?).{100}))', str4, re.M | re.I)

                    matchObj17 = re.search(r'full legal name((.*?).{100})', str4, re.M | re.I)

                    matchObj18 = re.search(r'(full legal entity((.*?).{100}))', str4, re.M | re.I)

                    matchObj19 = re.search(r'(\(1\)((.*?)\(2\)(.*?).{150}))', str4, re.M | re.I)

                    if matchObj7:
                        Party1 = matchObj7.group()

                    elif matchObj9:
                        Party1 = matchObj9.group()

                    elif matchObj8:
                        Party1 = matchObj8.group()

                    elif matchObj5:
                        Party1 = matchObj5.group()

                    elif matchObj:
                        Party1 = matchObj.group()

                    elif matchObj2:
                        Party1 = matchObj2.group()

                    elif matchObj1:
                        Party1 = matchObj1.group()

                    elif matchObj19:
                        Party1 = matchObj19.group()

                    elif matchObj3:
                        Party1 = matchObj3.group()

                    elif matchObj15:
                        Party1 = matchObj5.group()

                    elif matchObj4:
                        Party1 = matchObj4.group()

                    elif matchObj6:
                        Party1 = matchObj6.group()

                    elif matchObj17:
                        Party1 = matchObj17.group()

                    elif matchObj18:
                        Party1 = matchObj18.group()

                    elif 'customer:' in lowredContent:
                        ind = lowredContent.index('customer:')
                        Party1 = content[ind:ind + 100]

                    elif 'reseller name:' in lowredContent:
                        ind = lowredContent.index('reseller name:')
                        Party1 = content[ind:ind + 500]

                    elif 'customer' in lowredContent[:300]:
                        ind = lowredContent.index('customer')
                        Party1 = content[:ind + 100]

                    else:
                        matchObj = re.search(r'\("customer"\) between google((.*?)and((.*?).{100}))', str5, re.M | re.I)

                        matchObj5 = re.search(r'between double((.*?)and((.*?).{100}))', str5,
                                              re.M | re.I)

                        matchObj7 = re.search(r'\(the "effective date"\) between google((.*?)and((.*?).{100}))', str5,
                                              re.M | re.I)

                        matchObj9 = re.search(r'\("effective date"\) between google((.*?)and((.*?).{100}))', str5,
                                              re.M | re.I)

                        matchObj8 = re.search(r'between google((.*?)and((.*?).{100}))', str5, re.M | re.I)

                        matchObj2 = re.search(r'by and between((.*?)and((.*?).{100}))', str5, re.M | re.I)

                        matchObj4 = re.search(r'between((.*?)and((.*?).{220}))', str5, re.M | re.I)

                        matchObj1 = re.search(r'by and among((.*?)and((.*?).{100}))', str5, re.M | re.I)

                        matchObj3 = re.search(r'among((.*?)and((.*?).{100}))', str5, re.M | re.I)

                        matchObj6 = re.search(r'( parties:((.*?).{100}))', str5, re.M | re.I)

                        matchObj15 = re.search(r'between and among((.*?)and((.*?).{100}))', str5, re.M | re.I)

                        matchObj17 = re.search(r'full legal name((.*?).{200})', str5, re.M | re.I)

                        matchObj18 = re.search(r'(full legal entity((.*?).{100}))', str5, re.M | re.I)

                        matchObj19 = re.search(r'(\(1\)((.*?)\(2\)(.*?).{150}))', str5, re.M | re.I)

                        if matchObj7:
                            Party1 = matchObj7.group()

                        elif matchObj9:
                            Party1 = matchObj9.group()

                        elif matchObj8:
                            Party1 = matchObj8.group()

                        elif matchObj5:
                            Party1 = matchObj5.group()

                        elif matchObj:
                            Party1 = matchObj.group()

                        elif matchObj2:
                            Party1 = matchObj2.group()

                        elif matchObj1:
                            Party1 = matchObj1.group()

                        elif matchObj19:
                            Party1 = matchObj19.group()

                        elif matchObj3:
                            Party1 = matchObj3.group()

                        elif matchObj15:
                            Party1 = matchObj5.group()

                        elif matchObj4:
                            Party1 = matchObj4.group()

                        elif matchObj6:
                            Party1 = matchObj6.group()

                        elif matchObj17:
                            Party1 = matchObj17.group()

                        elif matchObj18:
                            Party1 = matchObj18.group()

                        elif 'customer:' in lowredContent:
                            ind = lowredContent.index('customer:')
                            Party1 = content[ind:ind + 100]

                        elif 'customer :' in lowredContent:
                            ind = lowredContent.index('customer :')
                            Party1 = content[ind:ind + 100]

                        elif 'name of grantee' in lowredContent:
                            ind = lowredContent.index('name of grantee')
                            Party1 = content[ind:ind + 100]

                        elif "dear" in lowredContent[:1000] or "attn" in lowredContent[
                                                                         :1000] or "attention" in lowredContent[:1000]:
                            Party1 = content[:500]

                        else:
                            Party1 = "No Match"

                if '"contractor"' in lowredContent:
                    ind = lowredContent.index('"contractor"')

                    if ind < 200:
                        Party2 = content[ind - 200:ind + 100]
                    else:
                        Party2 = content[ind - 200:ind + 100]

                elif '"provider"' in lowredContent:
                    ind = lowredContent.index('"provider"')
                    if ind < 200:
                        Party2 = content[ind - 200:ind + 100]
                    else:
                        Party2 = content[ind - 200:ind + 100]

                elif '"reseller"' in lowredContent:
                    ind = lowredContent.index('"reseller"')

                    if ind < 200:
                        Party2 = content[ind - 200:ind + 100]
                    else:
                        Party2 = content[ind - 200:ind + 100]

                elif '"customer"' in lowredContent:
                    ind = lowredContent.index('"customer"')

                    if ind < 200:
                        Party2 = content[ind - 200:ind + 100]
                    else:
                        Party2 = content[ind - 200:ind + 100]
                else:
                    Party2 = "No Match"
                fcp1 = file_name_cp2(singFile)
                fstword = fcp1[0]
                scndword = fcp1[1]
                print(fstword, " ,", scndword)
                signature= last_sign_date(content)
                try:
                    fstword = fcp1[0]
                    scndword = fcp1[1]
                    print(fstword, " ,", scndword)
                    index=(content.lower()).index(fstword.lower())
                    index1=(content.lower()).index(scndword.lower())
                    if index:
                        beforeword1= content[index - 100:index]
                        afterword1=content[index:index+150]
                        fstString=beforeword1+" "+afterword1
                        word = fstword
                    else:
                        fstString="No Match"
                        word=fstword
                    if index1:
                        beforeword= content[index1 - 100:index1]
                        afterword=content[index1:index1+150]
                        scndString=beforeword+" "+afterword
                        word1= scndword
                    else:
                        scndString="No Match"
                        word1=scndword
                except:
                    fstString = "No Match"
                    word = fstword
                    scndString = "No Match"
                    word1 = scndword
                final,final1="",""
                matchObj2 = re.search(r'([“"”]holder[“"”](.*?).{100})', str1, re.M | re.I)
                matchObj3 = re.search(r'(lender(.*?).{100})', str1, re.M | re.I)
                if matchObj2:
                        date1 = matchObj2.group()
                        index = str1.index(date1)
                        date3 = str1[index - 150:index]
                        final = date3 + date1
                if matchObj3:
                        date1 = matchObj3.group()
                        index = str1.index(date1)
                        date3 = str1[index - 150:index]
                        final1 = date3 + date1
                w.writerow([newPath1,newPath, fcp, Party1, signature, ss,IntialString])

                print([newPath1, fcp, Party1, signature, ss,final,final1])
                file1.close()
                print("Scanned :" + count1 + " Files" + "\tFile Name: " + singFile)
# ===========================================================================================#

def RemainingBatch():
    PathForCSV = "D:\MainData\csv files\Search Project 1 (non-compete)/Norcal_ExpiryRemaining.csv"
    RemainingfilesList='D:\MainData/remainingbatch1.csv'
    RemainingFiles = open(RemainingfilesList, 'r+', encoding="utf8", errors="ignore")
    reading = csv.reader(RemainingFiles)
    ReadingCSV = open(PathForCSV, 'w+', encoding="utf8",errors="ignore", newline="")
    WritingCSV = csv.writer(ReadingCSV, quoting=csv.QUOTE_ALL, delimiter=',')
    WritingCSV.writerow(['Path & File Name','Output String', 'Keywords'])
    count = 0
    for row in reading:
            file1 = open(row[0], 'r+', encoding="utf8",errors="ignore")
            count=count+1
            content = file1.read()
            text = content.split()
            str1 = ' '.join(str(e) for e in text)
            str2 = strip_non_ascii(str1)
            date, date2, dateObj = '', "", ""
            # signature=last_sign_date(str2)
            keywords=['(by(.*?)between(.*?).{400})']
            # keywords=["(Full legal name:(.*?).{300})","(Contractor:(.*?).{300})"]
            for i in keywords:
                dateObj = re.search(i, str2, re.I | re.M)
                if dateObj:
                    date1 = dateObj.group()
                    index = str2.index(date1)
                    date3 = str2[index - 1:index]
                    date2 = date3 + date1
                    date = i
                    break

                else:
                    date2 = "No Match"
                    date = "No Match"
            WritingCSV.writerow([row[0], date2, date])
            # WritingCSV.writerow([row[0],signature])
            file1.close()
            print(count, row[0])

def main():

    ORFile()
    # RemainingBatch()

if __name__ == '__main__':
    main()

