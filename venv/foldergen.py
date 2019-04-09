import os
import re
try:
    fh = open('directory_structure.txt', 'r')
    print("File opened.")
except FileNotFoundError:
    print("File is not found")

folders = []

data = fh.readline()
depth = []
path = "C:/student/"
pathtemp = ""
fh.seek(0)
prevtab = 0;
currtab = 0;
lastadd = ""
for x in fh:
    currtab = x.count('\t')
    if currtab is not 0:
        depth.append(currtab)
    #print(x)
    #print(currtab)
    if "|---" in x:
            output = x.replace("-", "")
            output = output.replace("|", "")
            output = output.replace("\n", "")
            output = re.sub(r'(^[ \t]+|[ \t]+(?=:))', '', output, flags=re.M)
            folders.append(output)

print(folders)
print(depth)
fh.seek(0)
print("creating folders")


counter = 0;
pathtemp = path
#for x in range(len(folders)):
    #print(x)
    #if depth[counter + 1] > depth[counter]:
        #if '.' not in folders[x]:
        #    pathtemp= pathtemp + folders[x] + '/'
        #else:
     #       pathtemp = pathtemp + folders[x]
    #    counter = counter + 1
     #   print(pathtemp)
  #  if depth[counter + 1] < depth[counter]:
    #    pathtemp = pathtemp.replace(folders[int(x)-1], "")
    #    pathtemp = pathtemp + folders[x]
    #    counter = counter + 1
    ##if depth[counter + 1] == depth[counter]:
     #   print("azaza")
     #   print(folders[x])
     #   pathtemp = pathtemp.replace(folders[x], "")
      #  pathtemp = path + folders[x+1]
      #  print(pathtemp)
for x in range(len(depth)):
    if depth[x] == depth[x-1]:
        pathtemp = pathtemp.replace(folders[int(x)-1], "")
        pathtemp = pathtemp + folders[x]
    if depth[x] == depth[x-1]:
        pathtemp = pathtemp.replace(folders[int(x)-1], "")
        pathtemp = pathtemp + folders[x]
    print(pathtemp)