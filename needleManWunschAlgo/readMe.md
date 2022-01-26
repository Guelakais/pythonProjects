#Explanation needleManWunschAlgo

"

def needlemanWunsch(lista, listb, rowLen, colLen):
    levensteinTable = full([rowLen, colLen],0)

    for j in range(0,colLen):       #Fill out the first row
        levensteinTable[0][j] = j

    for i in range(0,rowLen):       #Fill out the first column
        levensteinTable[i][0] = i

    for i in range(1,rowLen):       #Fill out the rest of the Board in dependency of several cases
        for j in range (1,colLen):  #traversing with a nested loop
            levensteinTable[i][j]=min(  #every Levenstein Score has to be the Minimum of three cases
                (levensteinTable[i-1][j-1]+(0 if listb[j-1] == lista[i-1] else 1)), #in this part, the Delta of the two strings will be detected 
                (levensteinTable[i][j-1] +1), #The score of the left cell
                (levensteinTable[i-1][j] +1)    #The Score of the upper cell
                )

    return levensteinTable #the finished levenstein Table will be returned

"
