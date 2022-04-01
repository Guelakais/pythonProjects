**Explanations to the needleManWunschAlgo Stuff**  
**Please make sure, you use the Python 3.8.8.8 64-bit('base':conda) Environment or lower, so the inheratidet Algorithms can work properly**
**chapters of this ReadMe.txt**  
> **_interrupt: If you're unsure how to play with the codesheet, go straight to 3.7 on line 98 on this File to follow the instructions_**  
1. .vscode
> this order is here, because i use vscodium it contains a settings file to set the right environment.
2. NCBIQuery.sh
> this file contains a e-utilities query in bash to fetch the used  's_sclerot.fa'
### 3. NeedlemanWunsch2.py
> contains the important algorithms  
**introduction:**
> the needleman Wunsch algorithm is like a classical dynamic programmic algorithm to solve the Problem of detection the similarity of two sequences without run in a wall of a overly complicatet brute force algorithm and speed up the process. Here the needleman Wunsch algorithm as child of his kind isn't the most efficient way to solve the problem. He is one of the most known Solutions.

**3.1 Imports**  
> all imports are properly explaned inside 'needlemanWunsch2.py'

**3.1.1 The Numpy Array**
> I use for all my two dimensional arrays the full function from numpy, but you can do it the same in plain python with: Matrix = [[0 for x in range(rowlen)] for y in range(collen)]

**3.2 def needlemanWunsch**
#introduction:
this definition is a rebuild of a classical needleman Wunsch algorithm. it works almost the same, as if you would see this kind of algorithm in a textbook for algorithms and data structures.
#an Example of What the Algorithm does:
#   -  A  T  G  C  T
#-  0  1  2  3  4  5
#A  1  0  1  2  3  4
#T  2  1  0  1  2  3
#T  3  2  1  1  2  2
#A  4  3  2  2  2  3
#C  5  4  3  3  2  3
#A  6  5  4  4  3  3
#The last number in the Cell right down is the levenstein Distance of this two sequences.
#the algorithms fills with the two first seen for loops the first line and the first column. The after comming nested for loop fills the other cells.
#It hardly follows the rules of a needleman Wunsch algorithm:
#For every Cell, you need to enter the score of the difference of  the comparised Strings.
#   -  A  T  G  C  T
#-  0  1  2  3  4  5
#For exampe the differences of  '-ATGCT' and '-' is 5, because you need this amount of  operations to one of the strings into another.
#All the Columns and rows up to first follow this mindset, while they consider the formerly filled cells.
#the algorithm does look into formerly filled cells and fill the current cell with the minimum of them.
#This is, what the nested loop does. 
#this definition will be called with two sequences, the rowlength and the column length.
#it does return an numpy array with the levenstein scores

#3.3 The Arrows
#Because it is fancy, we use several Arrows for this Algorithm. The Arrows will be seen in the analysed files.
#3.4 def needlemanWunschTraceBack
#Introduction: This Algorithm does build up parallel two numpy arrays. One full of Arrows. The second full of a more modern styled board.
#This algorithm will be called with two sequences, the rowhlenth, the columnlenght and three different kind of scores.
#first it'll build up the two arrays, that'll be filled parallel.
#because this algorithm is a little bit different in his style of function, it only uses two nested for loops. This speed ups the process in comparission to a classical Needleman Wunsch algorithm, simultanously we need this speedup for the two arrays.
The Levenstein Distance ofATTACA and ATGCT is 3.
The trace back arrow board:
#   -  A  T  G  C  T
#-  -  ←  ←  ←  ←  ←
#A  ↑  ↖  ←  ←  ←  ←
#T  ↑  ↑  ↖  ←  ←  ←
#T  ↑  ↑  ↑  ↖  ←  ↖
#A  ↑  ↑  ↑  ↑  ↖  ↑
#C  ↑  ↑  ↑  ↑  ↖  ←
#A  ↑  ↑  ↑  ↑  ↑  ↖
#The Penalty Score Board:
#   -  A  T  G  C  T
#-  0 -1 -2 -3 -4 -5
#A -1  1  0 -1 -2 -3
#T -2  0  2  1  0 -1
#T -3 -1  1  1  0  1
#A -4 -2  0  0  0  0
#C -5 -3 -1 -1  1  0
#A -6 -4 -2 -2  0  0
#Here we see an example of what this algorithm does.
#As we can see, it produces on the one hand a normal modern expected board of a Needleman Wunsch algorithm. On the other hand we see a Board full of Arrows, which is the justification of why need this algorithm this way.
#The process of filling the arrow board is a little complicated. It does rebuild the process of filling other score Board, besides it can't use the max function, because arrows are no number.
#at the end it returns the modern score board (penaltyArray) and the Array with the Arrows.

#3.5 def traceback_alignment
#Introduction: This algorithm only returns one possible alighnment. Although the Needleman Wunsch algorithm opens up for several tracebacks, it will be to complicatet for me to show you this process, so here only one possibility is shown.
#the definition will be called with the arrow Array, the two sequences, several Arrows and a stop sign.
#first it defines the length of rows and columns and several explained varables
#It only need one while loop to iterate over the whole array in comparision of the two given sequences. it does follows the arrows to build up an alighnment between the two sequences.
#It returns a string with the alighnment.

#3.6 def seqHandle
#This algorithm summons the results of all the other algorithms and extract some features from them. It is used to call them and does lay the parameters of how they have to be called.
#It returns a string of all current features and the levenstein Distance, which it calculates on his own.

#3.7 Examples for seqHandle
#here are some examples at line 123 which you can use to play with the seqhandle algorithm. because seqhandle does return two things, you need first uncomment an example and than the print line in line 129

#3.8 def fileProcessGenerator
#This Generator opens a file with a summary of several sequences from the NCBI, to yield the name of the sequences and the sequence itself.

#3.9 FileOfSequencesAnalisis
#This Algorithm does use a generator to iterates over all the sequences of a summary file to extract a lot of features
#It can need a while to process the whole File. ;)
#As a Metafeature it extracts the average levenstein distance of the whole file and shows the current averages as statusreport.
#because i don't know how extract the right error from the given file, it does stop, if the generator can't be called properly.
#at the end, it will tell you