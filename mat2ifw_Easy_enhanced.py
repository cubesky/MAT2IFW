# coding: utf-8
# about IFW: https://cn.apkjam.com/blog/ifw.html
# source: https://github.com/apkjam/MAT2IFW
# author: https://cn.apkjam.com

from functools import reduce
import re
import os

try:
    os.mkdir('ifw')
except:
    pass

def addComp(prefix,str): return "<"+prefix+" block=\"true\" log=\"false\">\n" + str + "\n</" + prefix + ">"
mat = []
appName = []

for i in open("mat.txt"):
   appName.append(re.sub(r"/.*", "", i))

newAppName = list(set(appName))

for line in open("mat.txt"):
   mat.append("<component-filter name=\"" + line.replace("\n","") + "\" />")

for i in newAppName:
   ii = i.replace("\n","/")
   i = i.replace("\n","")
   newMat = []
   for j in mat:
      if str(ii) in str(j):
         newMat.append(j)
      else:
         continue

   matR = reduce(lambda s1,s2:s1+"\n"+s2,newMat)

   result = "<rules>\n" + addComp("service",matR) + "\n" + addComp("broadcast",matR) + "\n" + addComp("activity",matR) + "\n</rules>"

   outputPath = os.path.join("./ifw", i+".xml")
   fo = open(outputPath, "w")
   fo.write(result)
   fo.close()
