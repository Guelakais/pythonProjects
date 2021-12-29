#!/bin/sh
esearch -db nuccore -query "Sclerotinia sclerotiorum 1980 [TITLE]"  | efilter -molecule mrna | efetch -format fasta > s_sclerot.fa