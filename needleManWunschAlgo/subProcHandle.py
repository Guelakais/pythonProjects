#!/usr/bin/env python
import subprocess
import os

def NCBIQueryCall(file):
    print('START')
    subprocess.call(f"{os.getcwd()}/{file}")
    print('END')
#NCBIQueryCall(NCBIQuery.sh)

def getApiKeyString(fileName):
    apiKey =''
    currentDir = os.getcwd()
    os.chdir(os.environ.get('OLDPWD'))
    with open(f"{os.getcwd()}/{fileName}", 'r') as apiKeyFile: 
        apiKey +="".join([s for s in (apiKeyFile.read()).strip().splitlines(True) if s.strip()])
    os.chdir(currentDir)
    return apiKey
#apiKey = getApiKeyString('NCBIAPIKEY.txt')

from itertools import groupby

def fileProcessing2(fileE):
    with open(f'{os.getcwd()}/{fileE}', 'r') as fh:
        faiter = (x[1] for x in groupby(fh, lambda line: line[0] ==">"))
        for header in faiter:
            header = header.__next__()[1:].strip()
            seq = "".join(s.strip() for s in faiter.__next__())
            long_name = headerStr.strip().replace('>', '')
            name = long_name.split()[0]
            #with open(f'{os.getcwd()}/sequences/{header}.fasta', w) as outFile:
            #    outFile.write(seq)
            yield (headerStr, seq, name)


for ff in fileProcessing2('/s_sclerot.fa'):
    header, sequence, name = ff
