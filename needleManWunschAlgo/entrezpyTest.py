#!/usr/bin/env python
from functools import lru_cache
import entrezpy.conduit
from io import StringIO
import sys

w = entrezpy.conduit.Conduit('koroyeldiores@gmail.com')

fetch_influenza = w.new_pipeline()
sid = fetch_influenza.add_search({'db' : 'nucleotide', 'term' : 'H3N2 [organism] AND HA', 'rettype':'count', 'sort' : 'Date Released', 'mindate': 2000, 'maxdate':2019, 'datetype' : 'pdat'})
fid = fetch_influenza.add_fetch({'retmax' : 10, 'retmode' : 'text', 'rettype': 'fasta'}, dependency=sid)
#w.run(fetch_influenza)

fetchTest=w.new_pipeline()
fetchTest.add_fetch({'retmax' : 10, 'retmode' : 'text', 'rettype':'fasta'}, dependency=fetchTest.add_search({'db' : 'nuccore', 'term':'SS1G_01676 [GENE]'}))
old_stdout = sys.stdout

def getResult():
    return w.run(fetchTest)

results = getResult()
result = StringIO()
normalString = result.getvalue()
