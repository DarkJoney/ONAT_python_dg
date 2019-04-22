##file reader
import os
import math
import sys
dataList = []
marketList = []
groupList = []
inputControl = True

try:
    fh = open('dataGroup.txt', 'r')
    print("File opened.")
except FileNotFoundError:
    print("File is not found")

data = fh.readline()

groupcounter = 0;
fh.seek(0)
for x in fh:
    #print(x)
    if "$" in x:
        groupcounter = groupcounter + 1


print("There are a " + str(groupcounter-1) + " groups in a file.")
fh.seek(0)
data = [line.strip() for line in fh]
#print(data)
cindex = 0
for x in data:
    if x is not "$":
        print(x)
    if '$' in x:
        marketList.append(cindex+1)
    cindex = cindex + 1


#print(marketList)
print("There are a few groups in file. Which would you like to export?")
cindex = 0
for x in marketList:
    if data[x] is not '':
        print(str(cindex) + " " + data[x])
        cindex = cindex +1

while inputControl:

    print("Input number:")

    target = input()

    try:
        target = int(target)
    except (TypeError, ValueError):
        print("Wrong input!")
    else:
        if target > int(cindex - 1) or target < 0:
            print("Wrong value! Let's try again.")
        else:
            inputControl = False


#target = int(target)



fh.close()
print("Enter filename for export:")
filename = input()
filename = str(filename)+".txt"
print(filename)

f = open(filename, "w+")
for i in range(marketList[int(target)], marketList[int(target)+1]):
    if data[i] is not "$":
        print(data[i])
        f.write("%s\n" % data[i])

f.close()
print("Finish. Group is exported")
os.startfile(filename)