import pandas as pd
from math import ceil
import os

#file1 will open your genome of concern
#to make sure that your whole genome has been copied check if the printed length of thefile is correct
file1 = open("<genome.txt>", "r")
text = file1.read()
print("Size of text is ",len(text))

#to open ur excel sheet containing the genes
dataframe1 = pd.read_excel("<genetargets.xlsx>")
print(dataframe1)

#<gene names> : refers to the name of the coloumn contaning gene names
gene_name = dataframe1["<gene names>"]

for i in range(len(gene_name)):
  temp=''
  startno=text.find(str(gene_name[i]))
  x=0
  j=0
  y=0
  while:
    if text[startno+x]=="[gbkey=Gene]":
      x=y
      break
    x=x+1

  x=0
  while(x==0):
    if text[startno+j+y+12]==">":
      temp=temp+"\n"
      x=x+1
    elif text[startno+j+y+12]=="\n":
      print("")
    else:
      temp = temp+text[startno+j+y+12]
    j=j+1

  fileName = "<file_path>" + str(gene_name[i]) + ".txt" #can be .fasta based on ur needs
  if os.path.exists(fileName):
    continue #make sure that the file which u are trying to creaate doesnt already exist
  else:
    f = open (fileName, "x")
    f.write(temp)
    f.close()
  
