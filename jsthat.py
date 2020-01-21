from flask import Flask, jsonify
app = Flask(__name__)
import json
import os
import csv
import spacy
import turicreate as tc
#import sframe
from polyglot.text import Text
from spacy.matcher import Matcher
from polyglot.detect import Detector
import re


sf1 = tc.SFrame()
sf = tc.SFrame.read_csv(('/root/flrrs.csv'), header=True)
#sf.export_csv('/root/out.csv')
len(sf)
print(len(sf))
print(sf)
sf_text = sf['title']

nlp = spacy.load('en_core_web_md')
sf_test_doc = sf_text[0]

print(sf_test_doc)

orgs = []
doctype=[]
fd = tc.SFrame()
fd['complete path'] = sf['complete path'][0:8811]
fd['filename'] = sf['filename'][0:8811]
fd['title'] = sf['title'][0:8811]
#fd.add_column(tc.SArray(orgs), 'Title', inplace=True)
#fd.print_rows(num_rows=100)

fd_text=sf['title']



for i in range(0,8811):
    #text = fd_text[i]
    #print("text",text)
    doc = fd_text[i]
    #print(sf_text[i])
    #text = "EMPLOYER JOB POSTING Agreement This Job Posting Agreement "
    text=doc[0:250]
    while True:

        if "Amendment" in text:
            doctype.append("AMENDMENT")

            break
        if "AMENDMENT" in text:
            doctype.append("AMENDMENT")

            break
        if "Addendum" in text:
            doctype.append("ADDENDUM")

            break
        if "ADDENDUM" in text:
            doctype.append("ADDENDUM")

            break

        if "AGREEMENT" in text:
            doctype.append("MASTER")
            break

        if "Work" in text:
            doctype.append("Work Order")
            break

        if "Agreement" in text:
            doctype.append("MASTER")
            break

        if "" in text:
            print ("un")
            #orgs.append("un")
            doctype.append("un")
            break

fd.add_column(tc.SArray(doctype), 'type', inplace=True)
fd.print_rows(num_rows=100)
fd.export_csv('/root/flr.csv')
l = []
for x in range(0, len(fd)):
     #print contracts[x]
    data = json.dumps(fd[x])
    data1 = json.loads(data)
    print(data1)
    l.append(data1)
#print(l)


@app.route("/FLR")
def MergeSFrame():
    return jsonify(l)


if __name__ == "__main__":
    app.run(host='192.168.1.58', port=8003)

