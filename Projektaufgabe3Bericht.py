#!/usr/bin/env python
# coding: utf-8

# In[29]:


from Bio import SeqIO
SequenceInput = open('/media/steven/3e435451-bd40-4af1-844c-494c5d0eb5412/THM/Grundbionformatik/project 3/HomoSapiensChromosome21_GRCh38p13PrimaryAssemblyAccessionNC_000021.fasta', 'r')
output_file = open('/media/steven/3e435451-bd40-4af1-844c-494c5d0eb5412/THM/Grundbionformatik/project 3/nucleotide_counts.txt','w')
output_file.write('Gene\tLength\tCG%\n')
for cur_record in SeqIO.parse(SequenceInput, "fasta") : SequenceInput = cur_record.name
C_count = cur_record.seq.count('C')
G_count = cur_record.seq.count('G')
length = len(cur_record.seq)
cg_percentage = float(C_count + G_count) / length
output_line = '%s\t%i\t%f\n' % (SequenceInput, length, cg_percentage)
output_file.write(output_line)
output_file.close()


# In[31]:


from Bio import SeqIO
SequenceInput = open('/media/steven/3e435451-bd40-4af1-844c-494c5d0eb5412/THM/Grundbionformatik/project 3/ChinchillalanigeraisolateChin_1UnplacedGenomicScaffoldChiLan1Scaffold00001WholeGenomeShotgunSequenceAccessionNW004955402.fasta', 'r')
output_file = open('/media/steven/3e435451-bd40-4af1-844c-494c5d0eb5412/THM/Grundbionformatik/project 3/nucleotide_counts.txt','a')
for cur_record in SeqIO.parse(SequenceInput, "fasta") : SequenceInput = cur_record.name
C_count = cur_record.seq.count('C')
G_count = cur_record.seq.count('G')
length = len(cur_record.seq)
cg_percentage = float(C_count + G_count) / length
output_line = '%s\t%i\t%f\n' % (SequenceInput, length, cg_percentage)
output_file.write(output_line)
output_file.close()


# In[32]:


from Bio import SeqIO
SequenceInput = open('/media/steven/3e435451-bd40-4af1-844c-494c5d0eb5412/THM/Grundbionformatik/project 3/EscherichiaColiStrainST2747CompleteGenomeAccessionNZ_CP007393.fasta', 'r')
output_file = open('/media/steven/3e435451-bd40-4af1-844c-494c5d0eb5412/THM/Grundbionformatik/project 3/nucleotide_counts.txt','a')
#output_file.write('Gene\tA\tC\tG\tT\tLength\tCG%\n')
for cur_record in SeqIO.parse(SequenceInput, "fasta") : SequenceInput = cur_record.name
C_count = cur_record.seq.count('C')
G_count = cur_record.seq.count('G')
length = len(cur_record.seq)
cg_percentage = float(C_count + G_count) / length
output_line = '%s\t%i\t%f\n' % (SequenceInput, length, cg_percentage)
output_file.write(output_line)
output_file.close()


# In[33]:


from Bio import SeqIO
SequenceInput = open('/media/steven/3e435451-bd40-4af1-844c-494c5d0eb5412/THM/Grundbionformatik/project 3/FelisCatusIsolateCinnamonBreedAbyssinianChromosomeD4Felis_catus_9.0WholeGenomeShotgunSequenceAccessionNC_018735.fasta', 'r')
output_file = open('/media/steven/3e435451-bd40-4af1-844c-494c5d0eb5412/THM/Grundbionformatik/project 3/nucleotide_counts.txt','a')
#output_file.write('Gene\tA\tC\tG\tT\tLength\tCG%\n')
for cur_record in SeqIO.parse(SequenceInput, "fasta") : SequenceInput = cur_record.name
A_count = cur_record.seq.count('A')
C_count = cur_record.seq.count('C')
G_count = cur_record.seq.count('G')
T_count = cur_record.seq.count('T')
length = len(cur_record.seq)
cg_percentage = float(C_count + G_count) / length
output_line = '%s\t%i\t%f\n' % (SequenceInput, length, cg_percentage)
output_file.write(output_line)
output_file.close()


# In[34]:


from Bio import SeqIO
SequenceInput = open('/media/steven/3e435451-bd40-4af1-844c-494c5d0eb5412/THM/Grundbionformatik/project 3/MusMusculusStrainChromosome19AccessionNC_000085.fasta', 'r')
output_file = open('/media/steven/3e435451-bd40-4af1-844c-494c5d0eb5412/THM/Grundbionformatik/project 3/nucleotide_counts.txt','a')
#output_file.write('Gene\tA\tC\tG\tT\tLength\tCG%\n')
for cur_record in SeqIO.parse(SequenceInput, "fasta") : SequenceInput = cur_record.name
A_count = cur_record.seq.count('A')
C_count = cur_record.seq.count('C')
G_count = cur_record.seq.count('G')
T_count = cur_record.seq.count('T')
length = len(cur_record.seq)
cg_percentage = float(C_count + G_count) / length
output_line = '%s\t%i\t%f\n' % (SequenceInput, length, cg_percentage)
output_file.write(output_line)
output_file.close()


# In[35]:


from Bio import SeqIO
SequenceInput = open('/media/steven/3e435451-bd40-4af1-844c-494c5d0eb5412/THM/Grundbionformatik/project 3/SevereAcuteRespiratorySyndromeCoronavirus2IsolateWuhan-Hu-1CompleteGenomeAccessionNC_045512.fasta', 'r')
output_file = open('/media/steven/3e435451-bd40-4af1-844c-494c5d0eb5412/THM/Grundbionformatik/project 3/nucleotide_counts.txt','a')
#output_file.write('Gene\tA\tC\tG\tT\tLength\tCG%\n')
for cur_record in SeqIO.parse(SequenceInput, "fasta") : SequenceInput = cur_record.name
A_count = cur_record.seq.count('A')
C_count = cur_record.seq.count('C')
G_count = cur_record.seq.count('G')
T_count = cur_record.seq.count('T')
length = len(cur_record.seq)
cg_percentage = float(C_count + G_count) / length
output_line = '%s\t%i\t%f\n' % (SequenceInput, length, cg_percentage)
output_file.write(output_line)
output_file.close()


# In[10]:


from Bio import SeqIO
SequenceInput = open('/media/steven/3e435451-bd40-4af1-844c-494c5d0eb5412/THM/Grundbionformatik/project 3/HomoSapiensChromosome21_GRCh38p13PrimaryAssemblyAccessionNC_000021.fasta', 'r')
output_file = open('/media/steven/3e435451-bd40-4af1-844c-494c5d0eb5412/THM/Grundbionformatik/project 3/dinucleotide_counts.txt','w')
output_file.write('Gene\tAA\tAC\tAG\tAT\tCA\tCC\tCG\tGG\tGA\tGC\tTA\n')
for cur_record in SeqIO.parse(SequenceInput, "fasta") : SequenceInput = cur_record.name
AA_count = cur_record.seq.count('AA')
AC_count = cur_record.seq.count('AC')
AG_count = cur_record.seq.count('AG')
AT_count = cur_record.seq.count('AT')
CA_count = cur_record.seq.count('CA')
CC_count = cur_record.seq.count('CC')
CG_count = cur_record.seq.count('CG')
GG_count = cur_record.seq.count('GG')
GA_count = cur_record.seq.count('GA')
GC_count = cur_record.seq.count('GC')
TA_count = cur_record.seq.count('TA')
output_line = '%s\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\n' % (SequenceInput, AA_count, AC_count, AG_count, AT_count, CA_count, CC_count, CG_count, GG_count, GA_count, GC_count, TA_count)
output_file.write(output_line)
output_file.close()


# In[30]:


from Bio import SeqIO
SequenceInput = open('/media/steven/3e435451-bd40-4af1-844c-494c5d0eb5412/THM/Grundbionformatik/project 3/ChinchillalanigeraisolateChin_1UnplacedGenomicScaffoldChiLan1Scaffold00001WholeGenomeShotgunSequenceAccessionNW004955402.fasta', 'r')
output_file = open('/media/steven/3e435451-bd40-4af1-844c-494c5d0eb5412/THM/Grundbionformatik/project 3/trinucleotide_counts.txt','w')
output_file.write('Gene\tAAA\tAAC\tAAG\tAAT\tACA\tACC\tACG\tACT\tAGA\tAGC\tAGG\tATA\tATC\tATG\tCAA\tCAC\tCAG\tCCA\tCCC\tCCG\tCGA\tCGC\tCTA\tCTC\tGAA\tGAC\tGCA\tGCC\tGGA\tGTA\tTAA\tTCA\n')
for cur_record in SeqIO.parse(SequenceInput, "fasta") : SequenceInput = cur_record.name
AAA_count = cur_record.seq.count('AAA')
AAC_count = cur_record.seq.count('AAC')
AAG_count = cur_record.seq.count('AAG')
AAT_count = cur_record.seq.count('AAT')
ACA_count = cur_record.seq.count('ACA')
ACC_count = cur_record.seq.count('ACC')
ACG_count = cur_record.seq.count('ACG')
ACT_count = cur_record.seq.count('ACT')
AGA_count = cur_record.seq.count('AGA')
AGC_count = cur_record.seq.count('AGC')
AGG_count = cur_record.seq.count('AGG')
ATA_count = cur_record.seq.count('ATA')
ATC_count = cur_record.seq.count('ATC')
ATG_count = cur_record.seq.count('ATG')
CAA_count = cur_record.seq.count('CAA')
CAC_count = cur_record.seq.count('CAC')
CAG_count = cur_record.seq.count('CAG')
CCA_count = cur_record.seq.count('CCA')
CCC_count = cur_record.seq.count('CCC')
CCG_count = cur_record.seq.count('CCG')
CGA_count = cur_record.seq.count('CGA')
CGC_count = cur_record.seq.count('CGC')
CTA_count = cur_record.seq.count('CTA')
CTC_count = cur_record.seq.count('CTC')
GAA_count = cur_record.seq.count('GAA')
GAC_count = cur_record.seq.count('GAC')
GCA_count = cur_record.seq.count('GCA')
GCC_count = cur_record.seq.count('GCC')
GGA_count = cur_record.seq.count('GGA')
GTA_count = cur_record.seq.count('GTA')
TAA_count = cur_record.seq.count('TAA')
TCA_count = cur_record.seq.count('TCA')
output_line = '%s\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\n' % (SequenceInput, AAA_count, AAC_count, AAG_count, AAT_count, ACA_count, ACC_count, ACG_count, ACT_count, AGA_count, AGC_count, AGG_count, ATA_count, ATC_count, ATG_count, CAA_count, CAC_count, CAG_count, CCA_count, CCC_count, CCG_count, CGA_count, CGC_count, CTA_count, CTC_count, GAA_count, GAC_count, GCA_count, GCC_count, GGA_count, GTA_count, TAA_count, TCA_count)
output_file.write(output_line)
output_file.close()


# In[31]:


from Bio import SeqIO
SequenceInput = open('/media/steven/3e435451-bd40-4af1-844c-494c5d0eb5412/THM/Grundbionformatik/project 3/EscherichiaColiStrainST2747CompleteGenomeAccessionNZ_CP007393.fasta', 'r')
output_file = open('/media/steven/3e435451-bd40-4af1-844c-494c5d0eb5412/THM/Grundbionformatik/project 3/trinucleotide_counts.txt','a')
for cur_record in SeqIO.parse(SequenceInput, "fasta") : SequenceInput = cur_record.name
AAA_count = cur_record.seq.count('AAA')
AAC_count = cur_record.seq.count('AAC')
AAG_count = cur_record.seq.count('AAG')
AAT_count = cur_record.seq.count('AAT')
ACA_count = cur_record.seq.count('ACA')
ACC_count = cur_record.seq.count('ACC')
ACG_count = cur_record.seq.count('ACG')
ACT_count = cur_record.seq.count('ACT')
AGA_count = cur_record.seq.count('AGA')
AGC_count = cur_record.seq.count('AGC')
AGG_count = cur_record.seq.count('AGG')
ATA_count = cur_record.seq.count('ATA')
ATC_count = cur_record.seq.count('ATC')
ATG_count = cur_record.seq.count('ATG')
CAA_count = cur_record.seq.count('CAA')
CAC_count = cur_record.seq.count('CAC')
CAG_count = cur_record.seq.count('CAG')
CCA_count = cur_record.seq.count('CCA')
CCC_count = cur_record.seq.count('CCC')
CCG_count = cur_record.seq.count('CCG')
CGA_count = cur_record.seq.count('CGA')
CGC_count = cur_record.seq.count('CGC')
CTA_count = cur_record.seq.count('CTA')
CTC_count = cur_record.seq.count('CTC')
GAA_count = cur_record.seq.count('GAA')
GAC_count = cur_record.seq.count('GAC')
GCA_count = cur_record.seq.count('GCA')
GCC_count = cur_record.seq.count('GCC')
GGA_count = cur_record.seq.count('GGA')
GTA_count = cur_record.seq.count('GTA')
TAA_count = cur_record.seq.count('TAA')
TCA_count = cur_record.seq.count('TCA')
output_line = '%s\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\n' % (SequenceInput, AAA_count, AAC_count, AAG_count, AAT_count, ACA_count, ACC_count, ACG_count, ACT_count, AGA_count, AGC_count, AGG_count, ATA_count, ATC_count, ATG_count, CAA_count, CAC_count, CAG_count, CCA_count, CCC_count, CCG_count, CGA_count, CGC_count, CTA_count, CTC_count, GAA_count, GAC_count, GCA_count, GCC_count, GGA_count, GTA_count, TAA_count, TCA_count)
output_file.write(output_line)
output_file.close()


# In[32]:


from Bio import SeqIO
SequenceInput = open('/media/steven/3e435451-bd40-4af1-844c-494c5d0eb5412/THM/Grundbionformatik/project 3/FelisCatusIsolateCinnamonBreedAbyssinianChromosomeD4Felis_catus_9.0WholeGenomeShotgunSequenceAccessionNC_018735.fasta', 'r')
output_file = open('/media/steven/3e435451-bd40-4af1-844c-494c5d0eb5412/THM/Grundbionformatik/project 3/trinucleotide_counts.txt','a')
for cur_record in SeqIO.parse(SequenceInput, "fasta") : SequenceInput = cur_record.name
AAA_count = cur_record.seq.count('AAA')
AAC_count = cur_record.seq.count('AAC')
AAG_count = cur_record.seq.count('AAG')
AAT_count = cur_record.seq.count('AAT')
ACA_count = cur_record.seq.count('ACA')
ACC_count = cur_record.seq.count('ACC')
ACG_count = cur_record.seq.count('ACG')
ACT_count = cur_record.seq.count('ACT')
AGA_count = cur_record.seq.count('AGA')
AGC_count = cur_record.seq.count('AGC')
AGG_count = cur_record.seq.count('AGG')
ATA_count = cur_record.seq.count('ATA')
ATC_count = cur_record.seq.count('ATC')
ATG_count = cur_record.seq.count('ATG')
CAA_count = cur_record.seq.count('CAA')
CAC_count = cur_record.seq.count('CAC')
CAG_count = cur_record.seq.count('CAG')
CCA_count = cur_record.seq.count('CCA')
CCC_count = cur_record.seq.count('CCC')
CCG_count = cur_record.seq.count('CCG')
CGA_count = cur_record.seq.count('CGA')
CGC_count = cur_record.seq.count('CGC')
CTA_count = cur_record.seq.count('CTA')
CTC_count = cur_record.seq.count('CTC')
GAA_count = cur_record.seq.count('GAA')
GAC_count = cur_record.seq.count('GAC')
GCA_count = cur_record.seq.count('GCA')
GCC_count = cur_record.seq.count('GCC')
GGA_count = cur_record.seq.count('GGA')
GTA_count = cur_record.seq.count('GTA')
TAA_count = cur_record.seq.count('TAA')
TCA_count = cur_record.seq.count('TCA')
output_line = '%s\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\n' % (SequenceInput, AAA_count, AAC_count, AAG_count, AAT_count, ACA_count, ACC_count, ACG_count, ACT_count, AGA_count, AGC_count, AGG_count, ATA_count, ATC_count, ATG_count, CAA_count, CAC_count, CAG_count, CCA_count, CCC_count, CCG_count, CGA_count, CGC_count, CTA_count, CTC_count, GAA_count, GAC_count, GCA_count, GCC_count, GGA_count, GTA_count, TAA_count, TCA_count)
output_file.write(output_line)
output_file.close()


# In[33]:


from Bio import SeqIO
SequenceInput = open('/media/steven/3e435451-bd40-4af1-844c-494c5d0eb5412/THM/Grundbionformatik/project 3/HomoSapiensChromosome21_GRCh38p13PrimaryAssemblyAccessionNC_000021.fasta', 'r')
output_file = open('/media/steven/3e435451-bd40-4af1-844c-494c5d0eb5412/THM/Grundbionformatik/project 3/trinucleotide_counts.txt','a')
for cur_record in SeqIO.parse(SequenceInput, "fasta") : SequenceInput = cur_record.name
AAA_count = cur_record.seq.count('AAA')
AAC_count = cur_record.seq.count('AAC')
AAG_count = cur_record.seq.count('AAG')
AAT_count = cur_record.seq.count('AAT')
ACA_count = cur_record.seq.count('ACA')
ACC_count = cur_record.seq.count('ACC')
ACG_count = cur_record.seq.count('ACG')
ACT_count = cur_record.seq.count('ACT')
AGA_count = cur_record.seq.count('AGA')
AGC_count = cur_record.seq.count('AGC')
AGG_count = cur_record.seq.count('AGG')
ATA_count = cur_record.seq.count('ATA')
ATC_count = cur_record.seq.count('ATC')
ATG_count = cur_record.seq.count('ATG')
CAA_count = cur_record.seq.count('CAA')
CAC_count = cur_record.seq.count('CAC')
CAG_count = cur_record.seq.count('CAG')
CCA_count = cur_record.seq.count('CCA')
CCC_count = cur_record.seq.count('CCC')
CCG_count = cur_record.seq.count('CCG')
CGA_count = cur_record.seq.count('CGA')
CGC_count = cur_record.seq.count('CGC')
CTA_count = cur_record.seq.count('CTA')
CTC_count = cur_record.seq.count('CTC')
GAA_count = cur_record.seq.count('GAA')
GAC_count = cur_record.seq.count('GAC')
GCA_count = cur_record.seq.count('GCA')
GCC_count = cur_record.seq.count('GCC')
GGA_count = cur_record.seq.count('GGA')
GTA_count = cur_record.seq.count('GTA')
TAA_count = cur_record.seq.count('TAA')
TCA_count = cur_record.seq.count('TCA')
output_line = '%s\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\n' % (SequenceInput, AAA_count, AAC_count, AAG_count, AAT_count, ACA_count, ACC_count, ACG_count, ACT_count, AGA_count, AGC_count, AGG_count, ATA_count, ATC_count, ATG_count, CAA_count, CAC_count, CAG_count, CCA_count, CCC_count, CCG_count, CGA_count, CGC_count, CTA_count, CTC_count, GAA_count, GAC_count, GCA_count, GCC_count, GGA_count, GTA_count, TAA_count, TCA_count)
output_file.write(output_line)
output_file.close()


# In[34]:


from Bio import SeqIO
SequenceInput = open('/media/steven/3e435451-bd40-4af1-844c-494c5d0eb5412/THM/Grundbionformatik/project 3/MusMusculusStrainChromosome19AccessionNC_000085.fasta', 'r')
output_file = open('/media/steven/3e435451-bd40-4af1-844c-494c5d0eb5412/THM/Grundbionformatik/project 3/trinucleotide_counts.txt','a')
for cur_record in SeqIO.parse(SequenceInput, "fasta") : SequenceInput = cur_record.name
AAA_count = cur_record.seq.count('AAA')
AAC_count = cur_record.seq.count('AAC')
AAG_count = cur_record.seq.count('AAG')
AAT_count = cur_record.seq.count('AAT')
ACA_count = cur_record.seq.count('ACA')
ACC_count = cur_record.seq.count('ACC')
ACG_count = cur_record.seq.count('ACG')
ACT_count = cur_record.seq.count('ACT')
AGA_count = cur_record.seq.count('AGA')
AGC_count = cur_record.seq.count('AGC')
AGG_count = cur_record.seq.count('AGG')
ATA_count = cur_record.seq.count('ATA')
ATC_count = cur_record.seq.count('ATC')
ATG_count = cur_record.seq.count('ATG')
CAA_count = cur_record.seq.count('CAA')
CAC_count = cur_record.seq.count('CAC')
CAG_count = cur_record.seq.count('CAG')
CCA_count = cur_record.seq.count('CCA')
CCC_count = cur_record.seq.count('CCC')
CCG_count = cur_record.seq.count('CCG')
CGA_count = cur_record.seq.count('CGA')
CGC_count = cur_record.seq.count('CGC')
CTA_count = cur_record.seq.count('CTA')
CTC_count = cur_record.seq.count('CTC')
GAA_count = cur_record.seq.count('GAA')
GAC_count = cur_record.seq.count('GAC')
GCA_count = cur_record.seq.count('GCA')
GCC_count = cur_record.seq.count('GCC')
GGA_count = cur_record.seq.count('GGA')
GTA_count = cur_record.seq.count('GTA')
TAA_count = cur_record.seq.count('TAA')
TCA_count = cur_record.seq.count('TCA')
output_line = '%s\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\n' % (SequenceInput, AAA_count, AAC_count, AAG_count, AAT_count, ACA_count, ACC_count, ACG_count, ACT_count, AGA_count, AGC_count, AGG_count, ATA_count, ATC_count, ATG_count, CAA_count, CAC_count, CAG_count, CCA_count, CCC_count, CCG_count, CGA_count, CGC_count, CTA_count, CTC_count, GAA_count, GAC_count, GCA_count, GCC_count, GGA_count, GTA_count, TAA_count, TCA_count)
output_file.write(output_line)
output_file.close()


# In[35]:


from Bio import SeqIO
SequenceInput = open('/media/steven/3e435451-bd40-4af1-844c-494c5d0eb5412/THM/Grundbionformatik/project 3/SevereAcuteRespiratorySyndromeCoronavirus2IsolateWuhan-Hu-1CompleteGenomeAccessionNC_045512.fasta', 'r')
output_file = open('/media/steven/3e435451-bd40-4af1-844c-494c5d0eb5412/THM/Grundbionformatik/project 3/trinucleotide_counts.txt','a')
for cur_record in SeqIO.parse(SequenceInput, "fasta") : SequenceInput = cur_record.name
AAA_count = cur_record.seq.count('AAA')
AAC_count = cur_record.seq.count('AAC')
AAG_count = cur_record.seq.count('AAG')
AAT_count = cur_record.seq.count('AAT')
ACA_count = cur_record.seq.count('ACA')
ACC_count = cur_record.seq.count('ACC')
ACG_count = cur_record.seq.count('ACG')
ACT_count = cur_record.seq.count('ACT')
AGA_count = cur_record.seq.count('AGA')
AGC_count = cur_record.seq.count('AGC')
AGG_count = cur_record.seq.count('AGG')
ATA_count = cur_record.seq.count('ATA')
ATC_count = cur_record.seq.count('ATC')
ATG_count = cur_record.seq.count('ATG')
CAA_count = cur_record.seq.count('CAA')
CAC_count = cur_record.seq.count('CAC')
CAG_count = cur_record.seq.count('CAG')
CCA_count = cur_record.seq.count('CCA')
CCC_count = cur_record.seq.count('CCC')
CCG_count = cur_record.seq.count('CCG')
CGA_count = cur_record.seq.count('CGA')
CGC_count = cur_record.seq.count('CGC')
CTA_count = cur_record.seq.count('CTA')
CTC_count = cur_record.seq.count('CTC')
GAA_count = cur_record.seq.count('GAA')
GAC_count = cur_record.seq.count('GAC')
GCA_count = cur_record.seq.count('GCA')
GCC_count = cur_record.seq.count('GCC')
GGA_count = cur_record.seq.count('GGA')
GTA_count = cur_record.seq.count('GTA')
TAA_count = cur_record.seq.count('TAA')
TCA_count = cur_record.seq.count('TCA')
output_line = '%s\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\n' % (SequenceInput, AAA_count, AAC_count, AAG_count, AAT_count, ACA_count, ACC_count, ACG_count, ACT_count, AGA_count, AGC_count, AGG_count, ATA_count, ATC_count, ATG_count, CAA_count, CAC_count, CAG_count, CCA_count, CCC_count, CCG_count, CGA_count, CGC_count, CTA_count, CTC_count, GAA_count, GAC_count, GCA_count, GCC_count, GGA_count, GTA_count, TAA_count, TCA_count)
output_file.write(output_line)
output_file.close()


# In[ ]:


#Projektaufgabe 3: k-Mere in Genomen
#zu Aufgabe 1:
#Verwendete Spezies
#1. Chinchilla NW004955402
#2.Escheria Coli NZ_CP007393
#3. Felis Catus NC_018735
#4. Homo Sapiens NC_000021
#5. Mus Musculus NC_000085
#6. Severe Acute Respiratory Syndrome Coronavirus 2 IsolateWuhan-Hu-1 NC_045512


# In[4]:


#zu Aufgabe 2:
import pandas as pd
df = pd.read_csv('/media/steven/3e435451-bd40-4af1-844c-494c5d0eb5412/THM/Grundbionformatik/project 3/nucleotide_counts.txt',index_col = 0, delimiter='\t')
print(df)


# In[11]:


#zu Aufgabe 3
import numpy as np
import matplotlib as mlp
import matplotlib.pyplot as plt
df = pd.read_csv('/media/steven/3e435451-bd40-4af1-844c-494c5d0eb5412/THM/Grundbionformatik/project 3/dinucleotide_counts.txt', index_col = 0, delimiter='\t')
print(df)


# In[13]:


dinucleotides = ['AA', 'AC', 'AG', 'AT', 'CA', 'CC', 'CG', 'GG', 'GA', 'GC', 'TA']
height = [2802527, 2038442, 2774777, 3092310, 2921760, 1625270, 462299, 1644380, 2420557, 1705746, 2563211]
x = np.arange(len(dinucleotides))
plt.bar(x, height)
plt.xticks(x, dinucleotides)
fig, ax = plt.subplots()
plt.show()


# In[14]:


#Die zweite Fläche ist der Raum für notizen.
#Besonders häufig sind die Dinucleotide AT, CA, AG und AA vertreten
#


# In[49]:


#zu 3
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib as mlp
import matplotlib.pyplot as plt
from scipy import stats
df = pd.read_csv('/media/steven/3e435451-bd40-4af1-844c-494c5d0eb5412/THM/Grundbionformatik/project 3/trinucleotide_counts.txt', index_col = 0, delimiter='\t')
print(df)


# In[80]:


list = df.values.tolist()


# In[60]:


# NW_004955402.1 und NZ_CP007393.1
#Diese beiden Genome scheinen sich nicht sehr ähnlich, aufgrund der hohen Streuung.
res = stats.linregress(list[0], list[1])
print(f"R-squared: {res.rvalue**2:.6f}")
plt.plot(list[0], list[1], 'o', label='original data')
plt.show()


# In[61]:


# NW_004955402.1 und NC_018735.3
#Diese beiden Genome scheinen sich sehr ähnlich, aufgrund der geringen Streuung
res = stats.linregress(list[0], list[2])
print(f"R-squared: {res.rvalue**2:.6f}")
plt.plot(list[0], list[2], 'o', label='original data')
plt.show()


# In[62]:


#NW_004955402.1 und NC_000021.9
#Diese beiden Genome scheinen sich sehr ähnlich, aufgrund der geringen Streuung
res = stats.linregress(list[0], list[3])
print(f"R-squared: {res.rvalue**2:.6f}")
plt.plot(list[0], list[3], 'o', label='original data')
plt.show()


# In[63]:


#NW_004955402.1 und NC_000085.7
#Diese beiden Genome scheinen sich sehr ähnlich, aufgrund der geringen Streuung
res = stats.linregress(list[0], list[4])
print(f"R-squared: {res.rvalue**2:.6f}")
plt.plot(list[0], list[4], 'o', label='original data')
plt.show()


# In[64]:


#NW_004955402.1 und NC_045512.2
#Diese beiden Genome scheinen sich nicht sehr ähnlich, aufgrund der hohen Streuung.
res = stats.linregress(list[0], list[5])
print(f"R-squared: {res.rvalue**2:.6f}")
plt.plot(list[0], list[5], 'o', label='original data')
plt.show()


# In[66]:


#NZ_CP007393.1 und NC_018735.3
#Diese beiden Genome scheinen sich nicht sehr ähnlich, aufgrund der hohen Streuung.
res = stats.linregress(list[1], list[2])
print(f"R-squared: {res.rvalue**2:.6f}")
plt.plot(list[1], list[2], 'o', label='original data')
plt.show()


# In[67]:


#NZ_CP007393.1 und NC_000021.9
#Diese beiden Genome scheinen sich nicht sehr ähnlich, aufgrund der hohen Streuung.
res = stats.linregress(list[1], list[3])
print(f"R-squared: {res.rvalue**2:.6f}")
plt.plot(list[1], list[3], 'o', label='original data')
plt.show()


# In[68]:


#NZ_CP007393.1 und NC_000085.7
#Diese beiden Genome scheinen sich nicht sehr ähnlich, aufgrund der hohen Streuung.
res = stats.linregress(list[1], list[4])
print(f"R-squared: {res.rvalue**2:.6f}")
plt.plot(list[1], list[4], 'o', label='original data')
plt.show()


# In[69]:


#NZ_CP007393.1 und NC_045512.2
#Diese beiden Genome scheinen sich nicht sehr ähnlich, aufgrund der hohen Streuung.
res = stats.linregress(list[1], list[5])
print(f"R-squared: {res.rvalue**2:.6f}")
plt.plot(list[1], list[5], 'o', label='original data')
plt.show()


# In[70]:


#NC_018735.3 und NC_000021.9
#Diese beiden Genome scheinen sich sehr ähnlich, aufgrund der geringen Streuung
res = stats.linregress(list[2], list[3])
print(f"R-squared: {res.rvalue**2:.6f}")
plt.plot(list[2], list[3], 'o', label='original data')
plt.show()


# In[71]:


#NC_018735.3 und NC_000085.7
#Diese beiden Genome scheinen sich sehr ähnlich, aufgrund der geringen Streuung
res = stats.linregress(list[2], list[4])
print(f"R-squared: {res.rvalue**2:.6f}")
plt.plot(list[2], list[4], 'o', label='original data')
plt.show()


# In[75]:


#NC_018735.3 und NC_045512.2
#Diese beiden Genome scheinen sich nicht sehr ähnlich, aufgrund der hohen Streuung.
res = stats.linregress(list[2], list[5])
print(f"R-squared: {res.rvalue**2:.6f}")
plt.plot(list[3], list[5], 'o', label='original data')
plt.show()


# In[76]:


#NC_000021.9 und NC_000085.7
#Diese beiden Genome scheinen sich, aufgrund der geringen Streung sehr ähnlich
res = stats.linregress(list[3], list[4])
print(f"R-squared: {res.rvalue**2:.6f}")
plt.plot(list[3], list[4], 'o', label='original data')
plt.show()


# In[77]:


#NC_000021.9 und NC_045512.2
#Diese beiden Genome scheinen geine großen Gemeinsamkeiten zu haben aufgrund der hohen Streuung
es = stats.linregress(list[3], list[5])
print(f"R-squared: {res.rvalue**2:.6f}")
plt.plot(list[3], list[5], 'o', label='original data')
plt.show()


# In[78]:


#NC_000085.7 und NC_045512.2
#Diese beiden genome scheinen sich im späteren Verlauf anzunähern.
#Insgesamt scheinen sie einander nicht sehr ähnlich aufgrund der hohen Streuung.
es = stats.linregress(list[4], list[5])
print(f"R-squared: {res.rvalue**2:.6f}")
plt.plot(list[4], list[5], 'o', label='original data')
plt.show()


# In[ ]:




