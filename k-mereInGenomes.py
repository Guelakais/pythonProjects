#!/usr/bin/env python

from Bio import SeqIO
from pathlib import Path
import os
import pandas as pd
#%% #Special sign to uses this part of the code in vscode as one block
def headLine(singleChar, doubleChar, tribleChar):
    return "Gene,length"+(
        ''.join(f",{Base}%" for Base in singleChar
        ))+(
            ''.join(f",{dimer}%" for dimer in doubleChar
            ))+(
                ''.join(f",{trimer}%" for trimer in tribleChar
                ))+"\n"

DNABases = ["A", "T", "C", "G"]     #List with all current DNA Bases
dimerList = [x+y for x in DNABases for y in DNABases]   #List comprehension to deliver a list with all possible dimers
trimerList = [x+y+z for x in DNABases for y in DNABases for z in DNABases]  #List comprehension to deliver all possible trimers
strHeadLine = headLine(DNABases, dimerList, trimerList)
#%%
def directoryIterator(directory):   #to iterate over a whole given directory
    return ''.join(
        f'{dataParser(str(directory+filename))}'for filename in os.listdir(directory)
        )

def dataParser(SequenceInput): #Acquise the features of a given file in folder
    featureOutPutLine = '' #references the featureOutPutLine
    for curRecord in SeqIO.parse(SequenceInput, "fasta"):
        featureOutPutLine += '%s,' % curRecord.id #every outPutline does start with the id of the record
        length = len(curRecord.seq) #
        featureOutPutLine += '%i,' % (length)
        lengthstr = str(length)
        print(f"Current iterated sequence length: {lengthstr}")
        for Base in DNABases:
            featureOutPutLine += '%f,' % (
                float(
                    curRecord.seq.count(Base)
                    )/length)
        print("Percentage of Bases in current sequence are done")
        
        for dimer in dimerList:
            featureOutPutLine += '%f,' % (
                float(curRecord.seq.count(dimer)
                )/length)
        print("Percentage of dimer in current sequence are done")

        for trimer in trimerList: 
            featureOutPutLine += '%f,' % (
                float(curRecord.seq.count(trimer)
                )/length)
        print("Percentage of trimers in current sequence are done")
        featureOutPutLine += '\n'
    return featureOutPutLine

def cheatSheet(fileName ,strOne, strTwo):
    with open(fileName, 'w') as notice:
        fileName.write(str(strOne +strTwo))

def thirdTask(file):
    print("yo")

def secondTask(file):
    print("do you wanna see the results?")
    while 1:
        sTInput = input("[y/n]")
        if sTInput == "y":
            df = pd.read_csv(file,index_col = 0,)
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
                print("\nok, we'll proceed. Please keep patient while the process\n")
                outPutFileString = str(userInput+"features.csv")
                output = directoryIterator(userInput)
                cheatSheet(outPutFileString , strHeadLine, output)
                secondTask(outPutFileString)    
                break
            elif inputTwo == "y":
                print("ok")

        else:
            print("Given input is not a directory. Please again")


inputManager()
# %%
