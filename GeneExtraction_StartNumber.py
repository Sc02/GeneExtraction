import pandas as pd
from math import ceil
import os

file1 = open("Genome.txt", "r")
text = file1.read()
temp = ""
print("Size of text is ",len(text))

dataframe1 = pd.read_excel('GeneList.xlsx')
print(dataframe1)

print(dataframe1["Start"])
startingList = dataframe1["Start"]
endingList = dataframe1["End"]
name = dataframe1["Gene_Tag/Name"]

listt=[]
diff=0
startno=0
z=''
temp = ''
newLines = 0
for i in range(len(startingList)):
  diff=int(endingList[i])-int(startingList[i])
  y=int(len(str(startingList[i])))+int(len(str(endingList[i])))+15
  startno=text.find(str(startingList[i]))
  newLines = ceil(diff/70) + 3
  z=text[startno+y:startno+y+diff+newLines]
  temp = '> ' + z
  fileName = "filepath/folder_name" + str(name[i]) + ".fasta" #can be .txt
  if os.path.exists(fileName):
    continue
  else:
    f = open (fileName, "x")
    f.write(temp)
    f.close()