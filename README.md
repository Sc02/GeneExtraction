# GeneExtraction
This is a simple code written to extract genes from a genome downloaded from the ncbi database

File labelled "GeneExtraction_GeneName" extracts genes if the names/tags of all the targets are known

File labelled "GeneExtraction_GeneNumber" extracts genes if the start numbers of all the targets are known

In both files the Genome.txt will be the txt file of genome of interest while GeneTargets will refer to the excel sheet containing target genes,
for GeneName code:
One coloumn with the names labelled "Name"

for GeneNumber code":
One Coloumn with the "GeneTag"/"name" i.e. whatever u wish to label the induvidual txt files
One coloumn with the gene starting numbers called "Start"
One coloumn with the gene ending numbers called "End"

At the end of both codes remember to add the filepath u wish to save the final outputs in,
file format of output can be both ".txt" and ".fasta"
