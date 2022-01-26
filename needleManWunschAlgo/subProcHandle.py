#!/usr/bin/env python
import subprocess
import os

def NCBIQueryCall(file):
    print('START')
    subprocess.call(f"{os.getcwd()}/{file}")
    print('END')
#NCBIQueryCall(NCBIQuery.sh)

def getApiKeyString(fileName, path):
    with open(f"{path}/{fileName}", 'r') as apiKeyFile: 
        return ''.join([s for s in (apiKeyFile.read()).strip().splitlines(True) if s.strip()]) #ApikeyString
   
apiKey = getApiKeyString('NCBIAPIKEY.txt','/home/stevenhgf')
#print(apiKey)
from itertools import groupby

def fileProcessing2(fileE):
    with open(f'{os.getcwd()}/{fileE}', 'r') as fh:
        faiter = (x[1] for x in groupby(fh, lambda line: line[0] ==">"))
        for header in faiter:
            headerStr = header.__next__()[1:].strip()
            yield (
                headerStr, 
                headerStr.strip().replace('>', '').split()[0],  #name 
                ''.join(s.strip() for s in faiter.__next__()))  #sequence


for ff in fileProcessing2('/s_sclerot.fa'):
    header, sequence, name = ff
    print(header, name, sequence)