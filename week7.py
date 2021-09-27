import re
inFile = open('Alice.txt', 'r')
outFile = open('output.txt', 'w')
myList = []
for line in inFile:
    opt = re.sub(r'[^\w\s]', '', line)
    myList += ((opt.strip()).lower()).split()
countword = {}
for w in myList:
    countword[w] = countword.get(w, 0) + 1
newList = []
for i in countword:
    newList.append((-countword[i], i))
newList.sort()
for k in range(len(newList)):
    print((newList[k][1]), '-', -1*(newList[k][0]), file=outFile)
