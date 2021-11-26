#!/usr/bin/env python

from Bio import SeqIO
from pathlib import Path
import os
import pandas as pd
#%% #Special sign to uses this part of the code in vscode as one block
def headLine():
    headLineString = str("Gene,length")
    for Base in DNABases:
        headLineString +=str(","+Base+"%")

    for dimer in dimerList:
        headLineString +=str(","+dimer+"%")

    for trimer in trimerList:
        headLineString +=str(","+trimer+"%")
    headLineString += "\n"
    return headLineString

DNABases = ["A", "T", "C", "G"]     #List with all current DNA Bases
dimerList = [x+y for x in DNABases for y in DNABases]   #List comprehension to deliver a list with all possible dimers
trimerList = [x+y+z for x in DNABases for y in DNABases for z in DNABases]  #List comprehension to deliver all possible trimers
#%%
def directoryIterator(directory):   #to iterate over a whole given directory
    featureOutPut = ""
    for filename in os.listdir(directory): #uses listdir from os package to generate al list from the files of a given folder
        fileDirectory = str(directory+filename) #produces a string
        featureOutPut += dataParser(fileDirectory) #Acquise the features of every File in given folder
    return featureOutPut
    
def dataParser(SequenceInput): #Acquise the features of a given file in folder
    featureOutPutLine = '' #references the featureOutPutLine
    for curRecord in SeqIO.parse(SequenceInput, "fasta"):
        featureOutPutLine += '%s,' % curRecord.id #every outPutline does start with the id of the record
        length = len(curRecord.seq) #
        featureOutPutLine += '%i,' % (length)
        lengthstr = str(length)
        print("Current iterated sequence length: "+lengthstr)
        for Base in DNABases:
            pCount = curRecord.seq.count(Base)
            pBasePercentage = float(pCount)/length
            featureOutPutLine += '%f,' % (pBasePercentage)
        print("Percentage of Bases in current sequence are done")
        
        for dimer in dimerList:
            dCount = curRecord.seq.count(dimer)
            bBasePercentage = float(dCount)/length
            featureOutPutLine += '%f,' % (bBasePercentage)

        print("Percentage of dimer in current sequence are done")

        for trimer in trimerList:
            tCount = curRecord.seq.count(trimer)
            tBasePercentage = float(tCount)/length
            featureOutPutLine += '%f,' % (tBasePercentage)
        
        print("Percentage of trimers in current sequence are done")
        featureOutPutLine += '\n'
    return featureOutPutLine

def cheatSheet(fileName ,strOne, strTwo):
    with open(fileName, 'w') as notice:
        fileInput = str(strOne +strTwo)
        fileName.write(fileInput)

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