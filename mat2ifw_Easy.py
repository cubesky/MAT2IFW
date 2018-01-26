# coding: utf-8
from functools import reduce
def addComp(prefix,str): return "<"+prefix+" block=\"true\" log=\"false\">\n" + str + "\n</" + prefix + ">"
mat = []
for line in open("mat.txt"):
   mat.append("    <component-filter name=\"" + line.replace("\n","") + "\" />")
matR = reduce(lambda s1,s2:s1+"\n"+s2,mat)
result = "<rules>\n" + addComp("service",matR) + "\n" + addComp("broadcast",matR) + "\n" + addComp("activity",matR) + "\n</rules>"
fo = open("ifw.xml", "w")
fo.write(result)
fo.close()
