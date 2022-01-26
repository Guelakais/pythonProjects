#!/usr/bin/env python
import pandas as pd #to create data frames
from numpy import full #to build the arrays
import subprocess
import os
from itertools import groupby

def needlemanWunsch(lista, listb, rowLen, colLen):
    levensteinTable = full([rowLen, colLen],0)

    for j in range(0,colLen):       #Fill out the first row
        levensteinTable[0, j] = j

    for i in range(0,rowLen):       #Fill out the first column
        levensteinTable[i, 0] = i

    for i in range(1,rowLen):       #Fill out the rest of the Board in dependency of several cases
        for j in range (1,colLen):  #traversing with a nested loop
            levensteinTable[i,j]=min(  #every Levenstein Score has to be the Minimum of three cases
                (levensteinTable[i-1, j-1]+(0 if listb[j-1] == lista[i-1] else 1)), #in this part, the Delta of the two strings will be detected 
                (levensteinTable[i, j-1] +1), #The score of the left cell
                (levensteinTable[i-1, j] +1)    #The Score of the upper cell
                )

    return levensteinTable #the finished levenstein Table will be returned

upArrow = "\u2191"
right_arrow = "\u2192"
down_arrow = "\u2193"
leftArrow = "\u2190"
down_right_arrow = "\u2198"
upLeftArrow = "\u2196"

def needlemanWunschTraceBack(listx,listy,rows,columns, gapPenalty = -1, matchBonus = 1, mismatchPenalty = -1):
    #This algorithm will fill out the Penalty Scoreboard and the Arrow Score board
    penaltyArray = full([rows, columns],0)  #build up the penalty score Array
    tracerArray = full([rows, columns],"-") #build up the Array for the traceback arrows
    
    for row in range(rows):         #filling the two arrays
        for col in range(columns):
            if row==0 and col==0:   #the first cell
                score = 0           #the first Cell doesn't have any alignment
                arrow = "-"         #no Alignment, no arrow
            elif row==0 and col!=0:            #the first Row
                score = penaltyArray[row, col -1]+gapPenalty #every Cell in this row need his score
                arrow = leftArrow   #every Arrow in this row has to look up to the start of the array
            elif row!=0 and col == 0:  #the first column
                score = penaltyArray[row-1, col]+gapPenalty #every Cell in this column need his score
                arrow = upArrow     #every Arrow in this row has to look up to the start of the array
            else: #in this case, every other cell will be processed
                fromLeftScore = penaltyArray[row,col-1] + gapPenalty #The score of the former left cell + gapPenalty
                fromAboveScore = penaltyArray[row-1,col] + gapPenalty #The score of the former Above cell
                diagonalLeftCellScore = penaltyArray[row-1,col-1] +(
                    matchBonus if(listx[row -1]==listy[col-1])else mismatchPenalty) #if the alighment matches with the former diagonal left cell, it gets a match bonus, else a mismatchPenalty
                score = max([fromLeftScore, fromAboveScore, diagonalLeftCellScore]) #The score of our Cell has to be the maximum of the three given scores
                arrow =(leftArrow if score==fromLeftScore else upArrow if score==fromAboveScore else\
                     upLeftArrow if score==diagonalLeftCellScore else 0)
                #the right arrow of every cell will be seperately detected
            tracerArray[row, col]=arrow #the tracerArray gets the arrows
            penaltyArray[row, col]=score #the penaltyArray gets the scores

    return tracerArray, penaltyArray

def traceback_alignment(traceback_array,listC,listD,up_arrow = upArrow ,\
                        left_arrow=leftArrow,up_left_arrow=upLeftArrow,stop="-"):
    
    row = len(listC)
    col = len(listD)
    arrow = traceback_array[row,col]
    alignedSeq1 = ""
    alignedSeq2 = ""
    alignmentIndicator = ""
    while arrow != "-":
            arrow = traceback_array[row,col]
            print(f"Currently on row: {row} and col: {col}; Arrow: {arrow}")
            
            if arrow == up_arrow: 
                alignedSeq2 = "-"+alignedSeq2 
                alignedSeq1 = listC[row-1] + alignedSeq1
                alignmentIndicator = " "+alignmentIndicator
                row -=1
                            
            elif arrow == up_left_arrow:
                alignedSeq1 = listC[row-1] + alignedSeq1
                alignedSeq2 = listD[col-1] + alignedSeq2
                if listC[row-1] == listD[col-1]:
                    alignmentIndicator = "|"+alignmentIndicator
                else:
                    alignmentIndicator = " "+alignmentIndicator
                row -=1
                col -=1
                
            elif arrow == left_arrow:
                alignedSeq1 = "-"+alignedSeq1
                alignedSeq2 = listD[col-1] + alignedSeq2
                alignmentIndicator = " "+alignmentIndicator
                col -=1
                
            elif arrow == stop:
                break
            else:
                raise ValueError(f"Traceback array entry at {row},{col}: {arrow}" \
                f"is not recognized as an up arrow ({up_arrow}),left_arrow ({left_arrow}), "\
                f"up_left_arrow ({up_left_arrow}), or a stop ({stop}).")
            
    return f"{alignedSeq1}\n{alignmentIndicator}\n{alignedSeq2}"

def seqHandle(seq1, seq2):
    columnLabels = [label for label in "-"+seq1]
    rowLabels = [label for label in "-"+seq2]
    nRows = len("-"+seq1)
    nColumns = len("-"+seq2)
    levensteinBoard = needlemanWunsch(seq1, seq2,nRows,nColumns)
    arrowArray, zuchtArray, = needlemanWunschTraceBack(seq1, seq2,nRows, nColumns)
    return (f"This is our ScoreBoard with all the important distanzes\n"
    f"{pd.DataFrame(levensteinBoard, index=columnLabels, columns= rowLabels)}\n"\
    f"The Levenstein Distanz of{seq1} and {seq2} is {levensteinBoard[len(seq1)][len(seq2)]}.\n"\
    f"The trace back arrow board:\n{pd.DataFrame(arrowArray, index=columnLabels, columns= rowLabels)}\n"\
    f"The Penalty Score Board:\n{pd.DataFrame(zuchtArray, index=columnLabels, columns= rowLabels)}\n"\
    f"{traceback_alignment(arrowArray,seq1,seq2)}")


#Asserts
#print(seqHandle("ATTACA","ATGCT"))
#print(seqHandle("BURN THE ART OR BLACK SUN DIES","BURNT HEART ORB LACKS UNDIES"))
#print(seqHandle("I LOVE MY LARGE LOOPS","I LOVE MYLAR GEL OOPS"))
#print(seqHandle("I AM SINKING","I AM SIN KING"))
#print(seqHandle("CANTELOPE","CANT ELOPE"))

def fileProcessing2(fileE):
    with open(f'{os.getcwd()}/{fileE}', 'r') as fh:
        faiter = (x[1] for x in groupby(fh, lambda line: line[0] ==">"))
        for header in faiter:
            headerStr = header.__next__()[1:].strip()
            yield (
                headerStr.strip().replace('>', '').split()[0],  #name 
                ''.join(s.strip() for s in faiter.__next__()))  #sequence

def sequenceAnalyzer(fileName, OutputPath):

    print(f"\n\n Warning: I'll proceed really a lot of Sequence combinations Sequences.\n\n This will take Time! Please stay patient")
    totalOverKillAnalysisisstring = ""
    processnumber = 0
    for ff in fileProcessing2(fileName):
        for fo in fileProcessing2(fileName):
            if ff != fo:

                name, seqOne, = ff
                namel, seqTwo, = fo
                print(f"processing for {name} and {namel} -Process Nr.{processnumber}")
                processnumber += 1
                with open(f"{OutputPath}/For_{name}_and_{namel}.txt", 'w') as bitch:
                    bitch.write(f"Analysis for {name} and {namel}: \n{seqHandle(seqOne, seqTwo)}")
    print("Ich habe fertig")

sequenceAnalyzer('/s_sclerot.fa', 'AnalysedFiles')

