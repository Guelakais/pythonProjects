#!/usr/bin/env python
import pandas as pd #to create data frames
from numpy import full #to build the arrays
import numpy as np
import subprocess
import os
from itertools import groupby

upArrow = "\u2191"
upLeftArrow = "\u2196"
leftArrow = "\u2190"

def needlemanWunsch(lista, listb, rowLen, colLen): #o(n*m)
    levensteinTable = np.zeros((rowLen+1, colLen+1))
    levensteinTable[:,0]=np.linspace(0, rowLen, rowLen+1)
    levensteinTable[0,:]=np.linspace(0, colLen, colLen+1)

    for i in range(1,rowLen):       #Fill out the rest of the Board in dependency of several cases
        for j in range (1,colLen):  #traversing with a nested loop
            levensteinTable[i,j]=min(  #every Levenstein Score has to be the Minimum of three cases
                (levensteinTable[i-1, j-1]+(0 if listb[j-1] == lista[i-1] else 1)), #in this part, the Delta of the two strings will be detected 
                (levensteinTable[i, j-1] +1), #The score of the left cell
                (levensteinTable[i-1, j] +1)    #The Score of the upper cell
                )

    return levensteinTable #the finished levenstein Table will be returned

def needlemanWunschTraceBack(listx,listy,rows,columns, gapPenalty = -1, matchBonus = 1, mismatchPenalty = -1): #o(n*m)
    #This algorithm will fill out the Penalty Scoreboard and the Arrow Score board
    penaltyArray = np.zeros((rows+1, columns+1))  #build up the penalty score Array
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
                    matchBonus if(listx[row -1]==listy[col-1])else mismatchPenalty
                    ) #if the alighment matches with the former diagonal left cell, it gets a match bonus, else a mismatchPenalty
                score = max([fromLeftScore, fromAboveScore, diagonalLeftCellScore]) #The score of our Cell has to be the maximum of the three given scores
                arrow =(leftArrow if score==fromLeftScore else upArrow if score==fromAboveScore else\
                     upLeftArrow if score==diagonalLeftCellScore else 0)
                #the right arrow of every cell will be seperately detected
            tracerArray[row, col]=arrow #the tracerArray gets the arrows
            penaltyArray[row, col]=score #the penaltyArray gets the scores

    return tracerArray, penaltyArray

def traceback_alignment(traceback_array,listC,listD,lenRow, lenCol,up_arrow = upArrow ,\
                        left_arrow=leftArrow,up_left_arrow=upLeftArrow,stop="-"): #o(n)
    
    row = len(listC)    #The Traceback Algo needs the sequences anyway
    col = len(listD)
    arrow = traceback_array[row,col]    #to get the right arrow for the current position
    alignedSeq1 = ""    #to initiate the produced alignment upper line
    alignedSeq2 = ""    #to initiate the produced alignment under line
    alignmentIndicator = "" #to indicate the alighment
    while arrow != "-":     #No Arrow, no interes
            arrow = traceback_array[row,col]    #the current position in the array inside the loop
            print(f"Currently on row: {row} and col: {col}; Arrow: {arrow}")    #Because you could get bored without visual process indication
            
            if arrow == up_arrow: #up_arrow shows a gap in under sequence
                alignedSeq2 = "-"+alignedSeq2 
                alignedSeq1 = listC[row-1] + alignedSeq1
                alignmentIndicator = " "+alignmentIndicator #to show that here is no alignment
                row -=1
                            
            elif arrow == up_left_arrow: #up_left_arrow shows that here is accordance between the sequences
                alignedSeq1 = listC[row-1] + alignedSeq1
                alignedSeq2 = listD[col-1] + alignedSeq2
                if listC[row-1] == listD[col-1]:
                    alignmentIndicator = "|"+alignmentIndicator #visual indicator for accordance
                else:
                    alignmentIndicator = " "+alignmentIndicator #visual indicator for no accordance
                row -=1
                col -=1
                
            elif arrow == left_arrow:
                alignedSeq1 = "-"+alignedSeq1
                alignedSeq2 = listD[col-1] + alignedSeq2
                alignmentIndicator = " "+alignmentIndicator #visual indicator for no accordance
                col -=1
                
            elif arrow == stop:
                break
            else:
                raise ValueError(
                    f"Traceback array entry at {row},{col}: {arrow}" \
                    f"is not recognized as an up arrow ({up_arrow}),left_arrow ({left_arrow}), "\
                    f"up_left_arrow ({up_left_arrow}), or a stop ({stop})."
                    )
            
    return f"{alignedSeq1}\n{alignmentIndicator}\n{alignedSeq2}"

def seqHandle(seq1, seq2):  #to handle a two given Sequences o(n*m)
    columnLabels = [label for label in "-"+seq1] #for the later buildet Dataframes
    rowLabels = [label for label in "-"+seq2]   ##for the later buildet Dataframes
    nRows = len(seq1)       #Count of all rows
    nColumns = len(seq2)    #Count of all columns
    levensteinBoard = needlemanWunsch(seq1, seq2,nRows,nColumns)    #to build the Board with the levensteinDistances
    arrowArray, zuchtArray, = needlemanWunschTraceBack(seq1, seq2,nRows, nColumns)  #Important for the traceback
    levensteinDistance = levensteinBoard[nRows][nColumns]  #I'll explain the Levenstein Distance in the Readme
    return (
        f"This is our ScoreBoard with all the important distances\n"\
        f"{pd.DataFrame(levensteinBoard, index=columnLabels, columns= rowLabels)}\n"\
        f"The Levenstein Distance of{seq1} and {seq2} is {levensteinDistance}.\n"\
        f"The trace back arrow board:\n{pd.DataFrame(arrowArray, index=columnLabels, columns= rowLabels)}\n"\
        f"The Penalty Score Board:\n{pd.DataFrame(zuchtArray, index=columnLabels, columns= rowLabels)}\n"\
        f"{traceback_alignment(arrowArray,seq1,seq2, nRows, nColumns)}"), levensteinDistance

def fileProcessGenerator(fileE):    #to iterate over a SequenceSummaryFile o(n)
    with open(f'{os.getcwd()}/{fileE}', 'r') as fh: #to savely work with the given file
        faiter = (x[1] for x in groupby(fh, lambda line: line[0] ==">"))    #to group the single sequences to their related header Line
        for header in faiter:
            headerStr = header.__next__()[1:].strip() #to fetch the header line from the group
            yield (
                headerStr.strip().replace('>', '').split()[0],  #name of the sequence
                ''.join(s.strip() for s in faiter.__next__()))  #sequence

def FileOfSequencesAnalisis(fileName, OutputPath): #to analyse a SequenceSummaryFile o(n*m*a*b)

    print(f"\n\n Warning: I'll proceed really a lot of Sequence combinations Sequences.\n\n This will take Time! Please stay patient")
    processnumber = 1 #We want to know, in which process we are
    levensteinDistanceCounter= 0 #To count all Levenstein distances so far
    LevensteinDistancesAverage = 0 #to calculate the average of all levenstein distances so far
    try:    #because someone could try shit
        for ff in fileProcessGenerator(fileName):   #the main loop devines the sequence in the line
            for fo in fileProcessGenerator(fileName):   #the main loop devines the sequence in the column
                if ff != fo:    #nobody wants to know the levenstein Distance of two identical sequences
                    name, seqOne, = ff  #to get the important stuff from the generator
                    namel, seqTwo, = fo
                    print(
                        f"processing for {name} and {namel} -Process Nr.{processnumber}\n"\
                        f"current average Levenstein Distances is {LevensteinDistancesAverage}")    #to show, that the process works well
                    seqHandling, currentLevensteinDistance = seqHandle(seqOne, seqTwo) #to get the struff from seqHandle
                    with open(f"{OutputPath}/For_{name}_and_{namel}.txt", 'w') as bitch:    #to savely save our Output to a file
                        bitch.write(f"Analysis for {name} and {namel}: \n{seqHandling}")
                    levensteinDistanceCounter += currentLevensteinDistance
                    LevensteinDistancesAverage = levensteinDistanceCounter/processnumber
                    processnumber += 1
    except RuntimeError:
        print("invalid File. Use a File with inherited fasta Sequences with a Header Line and Sequences")
    print(f"I'm done. Here is the average Levenstein Distance of the analysed File:\n{LevensteinDistancesAverage}")

