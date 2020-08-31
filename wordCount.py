#Oscar Castro

import re 
import sys

# set the input and output files
inputFname = sys.argv[1]
outputFname = sys.argv[2]

with open(inputFname, 'r') as i:
    lines = i.read()
    
list = re.findall("\S+", lines)

wordList = {}

for word in list:
    if word not in wordList:
        wordList[word] = 0
    wordList[word] =+ 1

with open(outputFname,'w') as o:
    for word, times in sorted(wordList.items()):
        o.write(word + " " + str(times) + "\n")
