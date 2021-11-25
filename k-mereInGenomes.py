#!/usr/bin/env python

from Bio import SeqIO
from pathlib import Path
import os
import pandas as pd
#%% #Special sign to uses this part of the code in vscode as one block
DNABases = ["A", "T", "C", "G"]     #List with all current DNA Bases
dimerList = [x+y for x in DNABases for y in DNABases]   #List comprehension to deliver a list with all possible dimers
trimerList = [x+y+z for x in DNABases for y in DNABases for z in DNABases]  #List comprehension to deliver all possible trimers
###########################
#def read_file(path):    #useless right now
#    with open(path, mode="r", encoding="utf8") as infile:
#        seq = ''.join([line.strip("\n\r").replace("N", "").replace(",", "")
#                       .replace(" ", "") for line in infile if not line.startswith(">")])
#    return seq
###########################

#%%
def directoryIterator(directory, outputfile):   #to iterate over a whole given directory

    for filename in os.listdir(directory): #uses listdir from os package to generate al list from the files of a given folder
        fileDirectory = str(directory+filename) #produces a string
        dataParser(fileDirectory, outputfile) #Acquise the features of every File in given folder
    outputfile.close()

def headLine(dirk):
    outPutFile = open(dirk,'w')
    headLineString = str("Gene\tlength")
    for Base in DNABases:
        headLineString +=str("\t"+Base+"%")

    for dimer in dimerList:
        headLineString +=str("\t"+dimer+"%")

    for trimer in trimerList:
        headLineString +=str("\t"+trimer+"%")
    headLineString += "\n"
    outPutFile.write(headLineString)
    print(headLineString)
    return outPutFile
    
def dataParser(SequenceInput, path): #Acquise the features of a given file in folder
    
    outPutLine = '' #references the outPutLine
    for curRecord in SeqIO.parse(SequenceInput, "fasta"):
        outPutLine += '%s\t' % curRecord.id #every outPutline does start with the id of the record
        length = len(curRecord) #
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
    while 1:
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
    while 1:
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