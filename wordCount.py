#Oscar Castro

import re 
import sys

# set the input and output files
inputFname = sys.argv[1]
outputFname = sys.argv[2]

#Read the input file
with open(inputFname, 'r') as i:
    lines = i.read()
    i.close()
    
# Create a list of all the words in the file
list = re.findall("\S+", lines)
list = [item.strip(",.:;'-").lower() for item in list]

print(list)

# Dic for storing the words and the times it repeats
wordList = {}

# Traverse list and add to dic if is not there 
# otherwise, increment the value to denote repetition
for word in list:
    if word not in wordList:
        wordList[word.lower()] = 0
    wordList[word.lower()] += 1
    

# Write data to the output file
with open(outputFname,'w') as o:
    for word, times in sorted(wordList.items()):
        o.write(word + " " + str(times) + "\n")
    o.close()
