#!/usr/bin/env python

#%%
DNABases = ["A", "T", "C", "G"]
dimerList = []
trimerList = []
###########################
def cDimerList(base, dList):
    for x in base:
        for y in base:
            dList.append(x + y)
    return dList
###########################
def cTrimerList(base, tList):
    for x in base:
        for y in base:
            for z in base:
                tList.append(x + y + z)
    return tList
###########################
def read_file(path):
    with open(path, mode="r", encoding="utf8") as infile:
        seq = ''.join([line.strip("\n\r").replace("N", "").replace(",", "")
                       .replace(" ", "") for line in infile if not line.startswith(">")])
    return seq
###########################
