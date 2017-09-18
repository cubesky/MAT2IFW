# coding: utf-8

from functools import reduce
def comb(s1,s2): return s1 + "\n" + s2
matService = []
matReciever = []
matActivity = []
matUnknown = []

for line in open("mat.txt"):
    if "service" in line.lower():
        matService.append("    <component-filter name=\"" + line.replace("\n","") + "\" />")
    elif "receiver" in line.lower():
        matReciever.append("    <component-filter name=\"" + line.replace("\n","") + "\" />")
    elif "activity" in line.lower():
        matActivity.append("    <component-filter name=\"" + line.replace("\n","") + "\" />")
    else:
        matUnknown.append("    <component-filter name=\"" + line.replace("\n","") + "\" />")

if len(matService) > 0:
    ifwServiceText = "<service block=\"true\" log=\"false\">\n" + reduce(comb,matService) + "\n</service>"
else:
    ifwServiceText = ""

if len(matReciever) > 0:
    ifwRecieverText = "<broadcast block=\"true\" log=\"false\">\n" + reduce(comb,matReciever) + "\n</broadcast>"
else:
    ifwRecieverText = ""

if len(matActivity) > 0:
    ifwActivityText = "<activity block=\"true\" log=\"false\">\n" + reduce(comb,matActivity) + "\n</activity>"
else:
    ifwActivityText = ""

if len(matUnknown) > 0:
    ifwUnknownText = "<!-- Unrecognized --\n" + reduce(comb,matUnknown) + "\n-->"
else:
    ifwUnknownText = ""

result = "<rules>\n" + ifwServiceText + "\n" + ifwRecieverText + "\n" + ifwActivityText + "\n\n" + ifwUnknownText
print(result)
fo = open("ifw.xml", "w")
fo.write(result)
fo.close()

