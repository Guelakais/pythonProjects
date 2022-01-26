#!/usr/bin/env python
import eutils

#print(f"{getApiKeyString('NCBIAPIKEY.txt')}")
ec = eutils.Client(cache=False, api_key=f"{getApiKeyString('NCBIAPIKEY.txt')}")
#
esr = ec.esearch(db='gene',term='tumor necrosis factor')
egs = ec.efetch(db='gene', id=7157)
eg = egs.entrezgenes[0]

esz = ec.efetch(db='gene', id=7157)
print(esz)