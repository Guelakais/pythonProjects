#!/usr/bin/env python
import eutils
import os

def getApiKeyString(fileName):
    currentDir = os.getcwd()
    apiKey =''
    os.chdir(os.environ.get('OLDPWD'))
    with open(f"{os.getcwd()}/{fileName}", 'r') as apiKeyFile: 
        apiKey += "".join([s for s in (apiKeyFile.read()).strip().splitlines(True) if s.strip()])
    os.chdir(currentDir)
    return apiKey

#print(f"{getApiKeyString('NCBIAPIKEY.txt')}")
ec = eutils.Client(cache=False, api_key=f"{getApiKeyString('NCBIAPIKEY.txt')}")
#
esr = ec.esearch(db='gene',term='tumor necrosis factor')
egs = ec.efetch(db='gene', id=7157)
eg = egs.entrezgenes[0]

esz = ec.efetch(db='gene', id=7157)
print(esz)