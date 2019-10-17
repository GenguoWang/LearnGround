#!/usr/bin/env python
# -*- coding: cp936 -*-
import csv
import re
import argparse
from datetime import datetime
parser = argparse.ArgumentParser(description='Convert bank exported csv to sui csv file.')
parser.add_argument('filenames', nargs='+', help='The filenames of bank exported csvs')
parser.add_argument('-o', '--output', default = 'out.csv', help='Output file name')
parser.add_argument('--after', help='only convert items after curtain date e.g 05/18/1990')
args = parser.parse_args()
head = open('head.txt').read()
foot = open('foot.txt').read()
outFile = open(args.output,'w')
outFile.write(head)

lineTmp = ',,%s,%s,%s,,,,"%s",%s,%s,,,,"%s",,\n'

afterDateStr = args.after
afterDate = datetime.strptime(afterDateStr, '%m/%d/%Y') if afterDateStr else None

def getDiscoverCredit(row):
    date = datetime.strptime(row['Trans. Date'],'%m/%d/%Y')
    amount = float(row['Amount'])
    name = row['Description'].replace('"','""')
    memo = row['Category'].replace('"','""')
    return [date, -amount, name, memo]

def getDiscoverSaving(row):
    date = datetime.strptime(row['Transaction Date'],'%m/%d/%Y')
    amount = float(row['Credit']) - float(row['Debit'])
    memo = ''
    name = ''
    return [date, amount, name, memo]

def getBoaCheck(row):
    amountStr = row['Summary Amt.']
    noneStr = row.get(None)
    if not noneStr or not amountStr or not re.match('[0-9.-]+', amountStr):
        return None
    date = datetime.strptime(row['Description'],'%m/%d/%Y')
    amount = float(amountStr)
    name = row.get('')
    memo = ''
    return [date, amount, name, memo]

def getBoaCredit(row):
    date = datetime.strptime(row['Posted Date'],'%m/%d/%Y')
    amount = float(row['Amount'])
    name = row['Payee'].replace('"','""')
    memo = ''
    return [date, amount, name, memo]

def getChaseCheck(row):
    date = datetime.strptime(row['Posting Date'],'%m/%d/%Y')
    amount = float(row['Amount'])
    name = row['Description'].replace('"','""')
    memo = row['Details'].replace('"','""')
    return [date, amount, name, memo]

def getChaseCredit(row):
    date = datetime.strptime(row['Trans Date'],'%m/%d/%Y')
    amount = float(row['Amount'])
    name = row['Description'].replace('"','""')
    memo = row['Type'].replace('"','""')
    return [date, amount, name, memo]
    

cnt = 0
for filename in args.filenames:
    with open(filename,'rb') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
        rowReader = None
        if 'Transaction Date' in reader.fieldnames:
            print "Discover Bank"
            rowReader = getDiscoverSaving
        elif 'Trans. Date' in reader.fieldnames:
            print "Discover Credit"
            rowReader = getDiscoverCredit
        elif 'Summary Amt.' in reader.fieldnames:
            print "BOA Bank"
            rowReader = getBoaCheck
        elif 'Reference Number' in reader.fieldnames:
            print "BOA Credit"
            rowReader = getBoaCredit
        elif 'Details' in reader.fieldnames:
            print "Chase Bank"
            rowReader = getChaseCheck
        elif 'Post Date' in reader.fieldnames:
            print "Chase Credit"
            rowReader = getChaseCredit
        else:
            raise ValueError('No reader matched!')
        for row in reader:
            items = rowReader(row)
            if items == None:
                continue
            dateOrg, amount, name, memo = items
            if afterDate and dateOrg < afterDate:
                continue
            date = dateOrg.strftime('%Y-%m-%d')
            line = lineTmp%(date,date,date,name,abs(amount),'收入' if amount > 0 else'支出',memo)
            outFile.write(line)
            cnt += 1
            print date,amount, name
outFile.write(foot)
outFile.close()
print "Done", cnt
