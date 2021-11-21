#!/usr/bin/env python

from Bio import SeqIO
from pathlib import Path
import os
import pandas as pd

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

cDimerList(DNABases, dimerList)
cTrimerList(DNABases, trimerList)

def directoryIterator(directory, outputfile):

    for filename in os.listdir(directory):
        fileDirectory = str(directory+filename)
        dataParser(fileDirectory, outputfile)
    outputfile.close()

def headLine(dirk):
    outPutFile = open(dirk,'w')
    headLineString = str("Gene\tlength")
    for Base in DNABases:
        primeString =str("\t"+Base+"%")
        headLineString +=primeString

    for dimer in dimerList:
        dString =str("\t"+dimer+"%")
        headLineString +=dString

    for trimer in trimerList:
        tString =str("\t"+trimer+"%")
        headLineString +=tString
    headLineString += "\n"
    outPutFile.write(headLineString)
    print(headLineString)
    return outPutFile
    
def dataParser(SequenceInput, path):
    outPutLine = '%s\t' % (SequenceInput)
    for curRecord in SeqIO.parse(SequenceInput, "fasta"):
        length = len(curRecord.name)
        outPutLine += '%i\t' % (length)
        lengthstr = str(length)
        print("Current iterated sequence length: "+lengthstr)
        for Base in DNABases:
            pCount = curRecord.seq.count(Base)
            pBasePercentage = float(pCount)/length
            outPutLine += '%f\t' % (pBasePercentage)
        print("Percentage of Bases in current sequence are done")

        for dimer in dimerList:
            dCount = curRecord.seq.count(dimer)
            bBasePercentage = float(dCount)/length
            outPutLine += '%f\t' % (bBasePercentage)

        print("Percentage of dimer in current sequence are done")

        for trimer in trimerList:
            tCount = curRecord.seq.count(trimer)
            tBasePercentage = float(tCount)/length
            outPutLine += '%f\t' % (tBasePercentage)
        
        print("Percentage of trimers in current sequence are done")
        outPutLine += '\n'
        path.write(outPutLine)

def thirdTask(file):
    print("yo")

def secondTask(file):
    print("do you wanna see the results?")
    while True:
        sTInput = input("[y/n]")
        if sTInput == "y":
            df = pd.read_csv(file,index_col = 0, delimiter='\t')
            print(df)
            thirdTask(df)
            break
        elif sTInput == "n":
            print("good bye")
            break
        else:
            print("please again.")


def inputManager():
    print("Hello, I'm here to help you Acquire Data from your given Fasta files.\n")
    while True:
        userInput = input("Please insert the path of your Folder: ")
        isdir = os.path.isdir(userInput)
        if isdir == True:
            inputTwo = input("Warning: Please make sure your given Directory does only contain .fasta files.\n \n Do you wanna change? [y;n]")
            if inputTwo == "n":
                print("\nok, we'll proceed. Please keep patient while the process")
                outPutFileString = str(userInput+"features.txt")
                outPut = headLine(outPutFileString)
                directoryIterator(userInput, outPut)
                secondTask(outPutFileString)    
                break
            elif inputTwo == "y":
                print("ok")

        else:
            print("Given input is not a directory. Please again")


inputManager()


# %%
