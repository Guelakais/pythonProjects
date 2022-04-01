from numpy import full #to build the arrays
import numpy as np


def needlemanWunsch(lista, listb, rowLen, colLen): #o(n*m)
    levensteinTable = np.zeros((rowLen+1, colLen+1))
    levensteinTable[:,0]=np.linspace(0, rowLen, rowLen+1)
    levensteinTable[0,:]=np.linspace(0, colLen, colLen+1)

    for i in range(1,rowLen+1):       #Fill out the rest of the Board in dependency of several cases
        for j in range (1,colLen+1):  #traversing with a nested loop
            levensteinTable[i,j]=min(  #every Levenstein Score has to be the Minimum of three cases
                (levensteinTable[i-1, j-1]+(0 if listb[j-1] == lista[i-1] else 1)), #in this part, the Delta of the two strings will be detected 
                (levensteinTable[i, j-1] +1), #The score of the left cell
                (levensteinTable[i-1, j] +1)    #The Score of the upper cell
                )

    return levensteinTable #the finished levenstein Table will be returned


seq1, seq2= "ATTACA","ATGCT"
nRows, nColumns = len("-"+seq1), len("-"+seq2)
print(needlemanWunsch(seq1, seq2, nRows-1, nColumns-1))
